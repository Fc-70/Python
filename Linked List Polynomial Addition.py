class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def insert(self, coeff, power):
        if coeff == 0:
            return
        new_node = Node(coeff, power)
        if not self.head or power > self.head.power:
            new_node.next = self.head
            self.head = new_node
            return
        curr = self.head
        while curr.next and curr.next.power > power:
            curr = curr.next
        if curr.next and curr.next.power == power:
            curr.next.coeff += coeff
            if curr.next.coeff == 0:
                curr.next = curr.next.next
        else:
            new_node.next = curr.next
            curr.next = new_node

    def add(self, other):
        result = Polynomial()
        p1, p2 = self.head, other.head
        while p1 and p2:
            if p1.power > p2.power:
                result.insert(p1.coeff, p1.power)
                p1 = p1.next
            elif p1.power < p2.power:
                result.insert(p2.coeff, p2.power)
                p2 = p2.next
            else:
                s = p1.coeff + p2.coeff
                if s != 0:
                    result.insert(s, p1.power)
                p1, p2 = p1.next, p2.next
        while p1:
            result.insert(p1.coeff, p1.power)
            p1 = p1.next
        while p2:
            result.insert(p2.coeff, p2.power)
            p2 = p2.next
        return result

    def __str__(self):
        if not self.head:
            return "0"
        terms = []
        curr = self.head
        while curr:
            c, p = curr.coeff, curr.power
            if p == 0:
                terms.append(str(c))
            elif p == 1:
                terms.append(f"{c}x" if c != 1 else "x")
            else:
                terms.append(f"{c}x^{p}" if c != 1 else f"x^{p}")
            curr = curr.next
        return " + ".join(terms).replace("+ -", "- ")

def build_poly():
    poly = Polynomial()
    n = int(input("Number of terms: "))
    for _ in range(n):
        c = int(input("Coefficient: "))
        p = int(input("Power: "))
        poly.insert(c, p)
    return poly

# Main program
print("Enter first polynomial:")
poly1 = build_poly()
print("Enter second polynomial:")
poly2 = build_poly()

print("\nSum of polynomials:")
print(poly1.add(poly2))

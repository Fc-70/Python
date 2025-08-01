class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None

class MusicPlaylist:
    def __init__(self):
        self.head = None

    def create_playlist(self, songs):
        for song in songs:
            self.insert_song(song)

    def insert_song(self, title):
        new_song = SongNode(title)
        if not self.head:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song
        print(f"'{title}' added to the playlist.")

    def delete_song(self, title):
        current = self.head
        prev = None
        while current:
            if current.title == title:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"'{title}' has been removed from the playlist.")
                return
            prev = current
            current = current.next
        print(f"'{title}' not found in the playlist.")

    def display_playlist(self):
        if not self.head:
            print("The playlist is empty.")
            return
        current = self.head
        print("\nCurrent Playlist:")
        while current:
            print(f"🎵 {current.title}")
            current = current.next
        print()

# Example Usage
def main():
    playlist = MusicPlaylist()

    while True:
        print("\n🎶 Music Playlist Menu 🎶")
        print("1. Create Playlist")
        print("2. Insert Song")
        print("3. Delete Song")
        print("4. Display Playlist")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            songs = input("Enter song titles separated by commas: ").split(',')
            playlist.create_playlist([s.strip() for s in songs])
        elif choice == '2':
            title = input("Enter the song title to insert: ")
            playlist.insert_song(title.strip())
        elif choice == '3':
            title = input("Enter the song title to delete: ")
            playlist.delete_song(title.strip())
        elif choice == '4':
            playlist.display_playlist()
        elif choice == '5':
            print("Exiting playlist. Goodbye! 🎧")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

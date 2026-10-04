class Node:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None
class Playlist:
    def __init__(self):
        self.head = None
        self.current = None
    def add_song(self, song):
        new_node = Node(song)
        if self.head is None:
            self.head = new_node
            self.current = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last
        print("Song added!")
    def delete_song(self, song):
        current = self.head
        while current:
            if current.song.lower() == song.lower():
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                if self.current == current:
                    self.current = current.next or current.prev
                print("Song deleted!")
                return
            current = current.next
        print("Song not found!")
    def show_playlist(self):
        if self.head is None:
            print("Playlist is empty.") #1.
            return
        current = self.head #2.
        number = 1
        print("\n--- Playlist ---") 
        while current:
            print(f"{number}. {current.song}")
            current = current.next
            number += 1
    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print("Now playing:", self.current.song)
        else:
            print("There is no next song.")
    def previous_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print("Now playing:", self.current.song)
        else:
            print("There is no previous song.")
playlist = Playlist()
playlist.add_song("No One Noticed - The Marías")
playlist.add_song("505 - Arctic Monkeys")
playlist.add_song("After Dark - Mr.Kitty")
playlist.add_song("Sweater Weather - The Neighbourhood")
playlist.add_song("Apocalypse - Cigarettes After Sex")
playlist.add_song("The Night We Met - Lord Huron")
playlist.add_song("Space Song - Beach House")
playlist.add_song("Glimpse of Us - Joji")
playlist.add_song("I Wanna Be Yours - Arctic Monkeys")
playlist.add_song("Another Love - Tom Odell")
while True:
    print("\n===== MUSIC PLAYLIST =====")
    print("1. Add Song")
    print("2. Delete Song")
    print("3. Show Playlist")
    print("4. Next Song")
    print("5. Previous Song")
    print("6. Exit")
    choice = input("Choose: ")
    if choice == "1":
        song = input("Enter song name: ")
        playlist.add_song(song)
    elif choice == "2":
        song = input("Enter song to delete: ")
        playlist.delete_song(song)
    elif choice == "3":
        playlist.show_playlist()
    elif choice == "4":
        playlist.next_song()
    elif choice == "5":
        playlist.previous_song()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
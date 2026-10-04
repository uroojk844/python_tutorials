# class Car:
#     type = "SUV"

#     def __init__(self, brand: str, name: str) -> None:
#         self.brand = brand
#         self.name = name

#     def __str__(self):
#         return f"""Car type is {self.type}
# Brand: {self.brand}
# Name: {self.name}"""


# car1 = Car("bmw", "m4")
# print(car1)


class Playlist:
    songs = []

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self):
        return f"""
======={self.name}=======
{self.songs}
    """

    def details(self):
        print(f"\n======={self.name}({len(self.songs)})=======")
        for idx, song in enumerate(self.songs, start=1):
            print(f"{idx}. {song}")

    def add_song(self, name):
        self.songs.append(name)

    def remove_song(self, name):
        self.songs.remove(name)


p1 = Playlist("Favorites")
p1.add_song("Ishq")
p1.add_song("Toh phir aao")
# p1.remove_song("Toh phir aao")
p1.details()
# print(p1)

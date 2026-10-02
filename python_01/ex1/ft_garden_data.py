class Plant:
    name : str
    height : int
    day : int
    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.day} days old")
        


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.day = 30

    sunflower = Plant()
    sunflower.name = "Sunflower"
    sunflower.height = 80
    sunflower.day = 45

    cactus = Plant()
    cactus.name = "Cactus"
    cactus.height = 15
    cactus.day = 120

    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()


class Plant:
    def __init__(self, name: str, height : float, day: int) -> None:
        self.name = name
        self.height = height
        self.day = day

    def grow(self, growth: float) -> None:
        self.height = round(self.height + growth, 2)
    def age(self) -> None:
        self.day += 1
    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.day} days old")
   

if __name__ == "__main__":
    rose = Plant("Rose", float(25), 30)
    oak = Plant("Oak", float(200), 365)
    cactus = Plant("Cactus", float(5), 90)
    sunflower = Plant("Sunflower", float(80), 45)
    fern = Plant("Fern", float(15),120)

    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    rose.show()
    print("Created: ", end="")
    oak.show()
    print("Created: ", end="")
    cactus.show()
    print("Created: ", end="")
    sunflower.show()
    print("Created: ", end="")
    fern.show()


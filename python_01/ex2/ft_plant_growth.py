class Plant:
    name : str
    height : int
    days : int
    def grow(self) -> None:
        self.height = round(self.height + 0.8, 2)
    def age(self) -> None:
        self.days += 1
        
    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.days = 30
    rose.height = 25
    init_height = rose.height
    for i in range(1, 8):
        print(f"===Day {i}===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.height - init_height, 1)}cm")
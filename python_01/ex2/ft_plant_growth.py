class Plant:
    def __init__(self, name:str, height:float, day:int):
        self.name = name
        self.height = height
        self.day = day
    def grow(self) -> None:
        self.height = round(self.height + 0.8, 2)
    def age(self) -> None:
        self.day += 1
    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.day} days old")


if __name__ == "__main__":
    rose = Plant("Rose", float(25), 30)
    init_height = rose.height
    print("=== Garden Plant Growth === ")
    rose.show()
    for i in range(1, 8):
        print(f"===Day {i}===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.height - init_height, 2)}cm")
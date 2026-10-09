class Plant:
    def __init__(self, name: str, height : float, day: int) -> None:
        self.name = name
        self._height = 0.0
        self._day = 0
        self.set_age(day)
        self.set_height(height)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int: 
        return self._day

    def set_height(self, value: float) -> bool:
        if value < 0:
            print(f"{self.name}: Error height can't be negative")
            return False
        self._height = float(value)
        return True
    def set_age(self, value: int) -> bool:
            if value < 0:
                print(f"{self.name}: Error age can't be negative")
                return False
            self._day= value
            return True
    def grow(self, growth: float) -> None:
        self.set_height(round(self._height + growth, 2))
    def age(self) -> None:
        self.set_age(self._day + 1)
    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._day} days old")

class Flower(Plant):
    def __init__(self, name:str, height:float, day:int, color):
        super().__init__(name, height, day)
        self.color = color
        self._bloomed = False
    def bloom(self) -> None:
        self._bloomed = True
    def show(self) -> None:
        super().show()
        print(f"Color:{self.color}")
        if self._bloomed:
            print(f"{self.name}: is blooming beautifully!")
        else:
            print(f"{self.name}: has not bloomed yet")

class Tree(Plant):
    def __init__(self, name:str, height:float, day:int, width:float):
        super().__init__(name, height, day)
        self.width = width
    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self._height} and {self.width}cm wide")
    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.width}")

class Vegetable(Plant):
    def __init__(self, name:str, height:float, day:int, harvest_season:str):
        super().__init__(name, height, day)
        self.harvest_season = harvest_season
        self.nutricional_value = 0
    def grow(self, growth) -> None:
        super().grow(growth)
    def age(self) ->None:
        super().age()
        self.nutricional_value += 1
    def show(self) -> None:
        super().show()
        print(f"Harvest Season: {self.harvest_season}")
        print(f"Nutricional Value: {self.nutricional_value}")
if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow(2.1)
        tomato.age()
    tomato.show()
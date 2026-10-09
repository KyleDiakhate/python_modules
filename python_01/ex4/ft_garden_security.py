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
        self.set_age(self.set_day + 1)
    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._day} days old")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 80.0, 15)
    print("Plant created: ", end="")
    rose.show()
    print()

    new_height = 90.2
    new_age = 19
    if rose.set_height(new_height):
        print(f"Height updated: {new_height}cm")
    if rose.set_age(new_age):
        print(f"Age updated: {new_age} days")
    print()

    if not rose.set_height(-5):
        print("Height update rejected")
    if not rose.set_age(-5):
        print("Age update rejected")
    print()

    print("Current state: ", end="")
    rose.show()
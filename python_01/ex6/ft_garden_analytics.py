class Plant:
    # 1. Nested Class para o Sistema de Estatísticas
    class Stats:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def display(self, plant_name: str) -> None:
            print(f"[statistics for {plant_name}]")
            print(f"grow() called: {self._grow_calls} times")
            print(f"age() called: {self._age_calls} times")
            print(f"show() called: {self._show_calls} times")

    def __init__(self, name: str, height: float, day: int) -> None:
        self.name = name
        self._height = 0.0
        self._day = 0
        self._stats = self.Stats() # Inicialização do sistema interno
        self.set_age(day)
        self.set_height(height)

    # 2. Static Method (não recebe self nem cls, funciona de forma independente)
    @staticmethod
    def check_year_old(age: int) -> bool:
        return age >= 365

    # 3. Class Method (recebe cls, serve para criar instâncias "anónimas")
    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

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
        self._day = value
        return True

    def grow(self, growth: float) -> None:
        self._stats._grow_calls += 1 # Regista a chamada
        self.set_height(round(self._height + growth, 2))

    def age(self) -> None:
        self._stats._age_calls += 1 # Regista a chamada
        self.set_age(self._day + 1)

    def show(self) -> None:
        self._stats._show_calls += 1 # Regista a chamada
        print(f"{self.name}: {self._height}cm, {self._day} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, day: int, color: str):
        super().__init__(name, height, day)
        self.color = color
        self._bloomed = False
        
    def bloom(self) -> None:
        self._bloomed = True
        
    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self.name}: is blooming beautifully!")
        else:
            print(f"{self.name}: has not bloomed yet")


# 4. Nova Classe Seed que herda de Flower
class Seed(Flower):
    def __init__(self, name: str, height: float, day: int, color: str, seed_count: int = 0):
        super().__init__(name, height, day, color)
        self.seed_count = seed_count

    # Override do show para adicionar a informação das sementes
    def show(self) -> None:
        super().show()
        print(f"Seeds amount: {self.seed_count}")


class Tree(Plant):
    # A Tree precisa de uma nested class própria para rastrear o produce_shade()
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._produce_shade_calls = 0
            
        def display(self, plant_name: str) -> None:
            super().display(plant_name)
            print(f"produce_shade() called: {self._produce_shade_calls} times")

    def __init__(self, name: str, height: float, day: int, width: float):
        super().__init__(name, height, day)
        # Substituímos as estatísticas genéricas pela versão específica da árvore
        self._stats = self.Stats()
        self.width = width
        
    def produce_shade(self) -> None:
        self._stats._produce_shade_calls += 1 # Regista a chamada exclusiva
        print(f"Tree {self.name} now produces a shade of {self._height} and {self.width}cm wide")
        
    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.width}")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, day: int, harvest_season: str):
        super().__init__(name, height, day)
        self.harvest_season = harvest_season
        self.nutricional_value = 0
        
    def grow(self, growth) -> None:
        super().grow(growth)
        
    def age(self) -> None:
        super().age()
        self.nutricional_value += 1
        
    def show(self) -> None:
        super().show()
        print(f"Harvest Season: {self.harvest_season}")
        print(f"Nutricional Value: {self.nutricional_value}")


# 5. Função exterior e única para processar as estatísticas
def display_plant_stats(plant: Plant) -> None:
    print("\nGarden statistics ===")
    plant._stats.display(plant.name)


if __name__ == "__main__":
    print("=== Testing Garden Analytics ===")

    # Testar planta anónima e classmethod
    anon = Plant.create_anonymous()
    anon.show()
    
    # Testar verificação estática
    print(f"Is anonymous plant 1 year old? {Plant.check_year_old(anon.get_age())}")

    # Testar Seed
    print("\n=== Seed")
    sunflower_seed = Seed("Sunflower", 10.0, 5, "Yellow", 50)
    sunflower_seed.grow(2.5)
    sunflower_seed.show()
    
    # Testar Tree e as estatísticas específicas
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.produce_shade()
    oak.produce_shade()
    
    # Imprimir as estatísticas usando a função exterior
    display_plant_stats(sunflower_seed)
    display_plant_stats(oak)
class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant Error: ") -> None:
        super().__init__(message)
def water_plant(plant_name:str) -> None:
    if plant_name != plant_name.capitalize():
        print(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")

def test_watering_system() -> None:
    # Cenário válido
    print("Testing valid plants...")
    try:
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")
        
    # Cenário inválido
    print("Testing invalid plants...")
    try:
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("lettuce") # Letra minúscula, vai disparar o erro aqui!
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
test_watering_system()

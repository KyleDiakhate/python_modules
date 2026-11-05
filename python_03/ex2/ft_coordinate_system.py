import math
def get_player_pos(): 
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z':")
        part = text.split(",")
        try:
            x_str, y_str, z_str = part
        except ValueError:
            print("Invalid Sintax.")
            continue
        x_str = x_str.strip()
        y_str = y_str.strip()
        z_str = z_str.strip()
        try: 
            x = float(x_str)
        except ValueError as e:
            print(f"Error on parameter '{x_str}': {e}")
            continue
        try: 
            y = float(y_str)
        except ValueError as e:
            print(f"Error on parameter '{y_str}': {e}")
            continue
        try: 
            z = float(z_str)
        except ValueError as e:
            print(f"Error on parameter '{z_str}': {e}")
            continue
        return (x, y, z)

if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    
    x1, y1, z1 = pos1
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    dist_center = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distance to center: {round(dist_center, 4)}")

    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()
    x2, y2, z2 = pos2

    dist_points = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between the 2 sets of coordinates: {round(dist_points, 4)}")
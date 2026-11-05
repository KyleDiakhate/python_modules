import sys
if __name__ == "__main__":
    print("=== Inventory System Analytics ===")
    inventory = {}

    i = 1

    while i < len(sys.argv):
        arg = sys.argv[i]

        if ":" not in arg:
           print(f"Error - invalid parameter '{arg}'")
        else:
            parts = arg.split(":")
            if len(parts) == 2:
                key = parts[0]
                val_str = parts[1]

                if key in inventory:
                    print(f"Redundant item '{key}' - discarding")
                else:
                    try:
                        val = int(val_str)
                        inventory[key] = val
                    except ValueError as e:
                        print(f"Quantity error for '{key}':{e}")
            else:
                print(f"Error - invalid parameter '{arg}'")
        i += 1

    if len(inventory) > 0:
        print(f"Got inventory: {inventory}")

        items_list = list(inventory.keys())
        print(f"Items List: {items_list}")

        qty = sum(inventory.values())
        print(f"Total quantaty of the {len(inventory)} items: {qty}")

        for key in inventory:
            pct = (inventory[key] / qty) * 100
            print(f"Item {key} represents: {pct:.1f}")

        most_item = None
        most_qty = -1
        least_item = None
        least_qty = float("inf")

        for key in inventory:
            qty = inventory[key]

            if qty > most_qty:
                most_qty = qty
                most_item = key
            if qty < least_qty:
                least_qty = qty
                least_item = key

        print(f"Item most abundant: {most_item} with quantity {most_qty}")
        print(f"Item least abundant: {least_item} with quantity {least_qty}")

        inventory.update({"magic":12})
        print(f"Updated inventory: {inventory}")





    
        

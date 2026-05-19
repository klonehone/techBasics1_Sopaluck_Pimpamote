# --- Game State ---

inventory = []
items_in_room = [
    {"name": "Lockpick", "type": "tool", "description": "A small metal pick. Could be useful for something that needs opening."},
    {"name": "Keycard", "type": "tool", "description": "A security keycard. There must be a panel somewhere that accepts this."},
    {"name": "Gloves", "type": "tool", "description": "Thin leather gloves. A smart thief leaves no trace."},
    {"name": "Torch", "type": "tool", "description": "A small flashlight. Useful if you end up somewhere dark."},
    {"name": "Crowbar", "type": "tool", "description": "Heavy and sturdy. Could force something open... if you don't mind the noise."},
    {"name": "Map", "type": "tool", "description": "A map of the museum. There seems to be a maintenance corridor near the back."}
]
MAX_INVENTORY_SIZE = 5

# Scenario: steal the Golden Crown and escape!
# Step 1 - put on Gloves, then use Lockpick to crack the display case and grab the Crown
# Step 2 - use Keycard to disarm the alarm
# Step 3 - use Map to find the maintenance corridor, then use Torch to light the way... and escape

crown_stolen = False
alarm_disabled = False
map_checked = False
game_won = False

# --- Helper ---

def find_item(item_name, item_list):
    # searches for an item by name in a list of item dictionaries
    for item in item_list:
        if item["name"].lower() == item_name.lower():
            return item
    return None

# --- Functions ---

def show_inventory():
    if len(inventory) == 0:
        print("Your bag is empty.")
    else:
        print(f"Bag ({len(inventory)}/{MAX_INVENTORY_SIZE}):")
        for item in inventory:
            print(f"  - {item['name']} ({item['type']})")

def show_room_items():
    if len(items_in_room) == 0:
        print("There is nothing left here.")
    else:
        print("You look around and see:")
        for item in items_in_room:
            print(f"  - {item['name']}")

def pick_up(item_name):
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your bag is full! Drop something first.")
        return

    item = find_item(item_name, items_in_room)

    if item is None:
        print(f"There is no '{item_name}' here.")
    else:
        items_in_room.remove(item)
        inventory.append(item)
        print(f"You slip the {item['name']} into your bag.")

def drop(item_name):
    item = find_item(item_name, inventory)

    if item is None:
        print(f"You don't have '{item_name}' in your bag.")
    else:
        inventory.remove(item)
        items_in_room.append(item)
        print(f"You put the {item['name']} down.")

def use(item_name):
    global crown_stolen, alarm_disabled, map_checked, game_won

    item = find_item(item_name, inventory)

    if item is None:
        print(f"You don't have '{item_name}' in your bag.")
        return

    # Gloves: wear before touching anything
    if item["name"].lower() == "gloves":
        print("You pull on the leather gloves. No fingerprints left behind.")

    # Lockpick: step 1 - crack the display case
    elif item["name"].lower() == "lockpick":
        if find_item("gloves", inventory) is None:
            print("You stop yourself. You should put on the gloves first - no fingerprints!")
        elif not crown_stolen:
            print("You carefully pick the lock on the display case...")
            print("Click. It opens. You grab the Golden Crown!")
            crown_stolen = True
            inventory.append({"name": "Golden Crown", "type": "treasure", "description": "The Golden Crown. Priceless."})
        else:
            print("The display case is already open.")

    # Keycard: step 2 - disarm the alarm
    elif item["name"].lower() == "keycard":
        if not crown_stolen:
            print("You swipe the keycard but nothing happens. This doesn't feel like the right moment.")
        elif not alarm_disabled:
            print("You swipe the keycard on the alarm panel.")
            print("The blinking red light turns green. The alarm is disarmed.")
            alarm_disabled = True
        else:
            print("The alarm is already disarmed.")

    # Map: step 3 part 1 - find the corridor
    elif item["name"].lower() == "map":
        if not alarm_disabled:
            print("You study the map. There is a maintenance corridor near the back exit.")
            print("It could be a way out - but you are not ready to leave yet.")
        else:
            print("You unfold the map and locate the narrow maintenance corridor.")
            print("That is your way out. But it looks pitch black in there.")
            map_checked = True

    # Torch: step 3 part 2 - light the corridor and escape
    elif item["name"].lower() == "torch":
        if not alarm_disabled:
            print("You click on the torch. The beam sweeps across the room.")
            print("The Golden Crown glints behind the display case. Focus.")
        elif not map_checked:
            print("You switch on the torch but you are not sure where to go.")
            print("You should check the Map first to find the way out.")
        else:
            print("You click on the torch and step into the maintenance corridor.")
            print("The beam of light guides you through the narrow passage.")
            print("A door at the end swings open and you slip out into the cool night air.")
            print("\nBehind you, the museum stands silent. Nobody saw a thing.")
            game_won = True

    # Crowbar: tempting but too noisy
    elif item["name"].lower() == "crowbar":
        print("You raise the crowbar toward the display case... then stop.")
        print("Too noisy. The guard would hear you instantly. Better find another way.")

    else:
        print(f"You fiddle with the {item['name']} but nothing happens right now.")

def examine(item_name):
    # check inventory first, then the room
    item = find_item(item_name, inventory)

    if item is None:
        item = find_item(item_name, items_in_room)

    if item is None:
        print(f"You don't see any '{item_name}' here or in your bag.")
    else:
        print(f"{item['name']}: {item['description']}")

def hint():
    if not crown_stolen:
        print("Hint: The Golden Crown is locked away. Examine the items around you - something here can open it. And be careful not to leave any trace.")
    elif not alarm_disabled:
        print("Hint: You have the Crown but the alarm is still active. There must be a way to disarm it.")
    else:
        print("Hint: The alarm is down. Find your way out - you'll need to know the route and have some light.")

# --- Game Loop ---

def game_loop():
    print("==============================================")
    print("           THE MUSEUM HEIST                  ")
    print("==============================================")
    print("It's 2am. You've snuck into the city museum.")
    print("The Golden Crown is somewhere in this room.")
    print("Getting out won't be easy.")
    print()
    print("--- HOW TO PLAY ---")
    print("  look              — see what is in the room")
    print("  examine [item]    — inspect something closely")
    print("  pickup [item]     — pick up an item")
    print("  drop [item]       — drop an item from your bag")
    print("  use [item]        — use an item")
    print("  inventory         — check what you are carrying")
    print("  hint              — get a bit of help if you are stuck")
    print("  quit              — give up and leave")
    print()
    print("Start by typing 'look'.")
    print("==============================================")

    while True:
        if game_won:
            print("\nYou escaped with the Golden Crown. The perfect heist!")
            print("Thanks for playing!")
            print("\nType 'restart' to play again or press Enter to exit.")
            again = input("\n> ").strip().lower()
            if again == "restart":
                restart()
            else:
                print("Goodbye!")
            return

        command = input("\n> ").strip().lower()

        match command.split():
            case ["help"]:
                print("Commands: look, examine [item], pickup [item], drop [item], use [item], inventory, hint, quit")
            case ["hint"]:
                hint()
            case ["inventory"]:
                show_inventory()
            case ["look"]:
                show_room_items()
            case ["pickup", item_name]:
                pick_up(item_name)
            case ["drop", item_name]:
                drop(item_name)
            case ["use", item_name]:
                use(item_name)
            case ["examine", item_name]:
                examine(item_name)
            case ["quit"]:
                print("You lose your nerve and sneak back out empty-handed.")
                print("Thanks for playing!")
                print("\nType 'restart' to try again or press Enter to exit.")
                again = input("\n> ").strip().lower()
                if again == "restart":
                    restart()
                else:
                    print("Goodbye!")
def restart():
    # reset all game state and start over
    global inventory, items_in_room, crown_stolen, alarm_disabled, map_checked, game_won

    inventory = []
    items_in_room = [
        {"name": "Lockpick", "type": "tool", "description": "A small metal pick. Could be useful for something that needs opening."},
        {"name": "Keycard", "type": "tool", "description": "A security keycard. There must be a panel somewhere that accepts this."},
        {"name": "Gloves", "type": "tool", "description": "Thin leather gloves. A smart thief leaves no trace."},
        {"name": "Torch", "type": "tool", "description": "A small flashlight. Useful if you end up somewhere dark."},
        {"name": "Crowbar", "type": "tool", "description": "Heavy and sturdy. Could force something open... if you don't mind the noise."},
        {"name": "Map", "type": "tool", "description": "A map of the museum. There seems to be a maintenance corridor near the back."}
    ]
    crown_stolen = False
    alarm_disabled = False
    map_checked = False
    game_won = False

    print("\n--- Restarting... ---\n")
    game_loop()

if __name__ == "__main__":
    game_loop()
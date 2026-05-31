# Assignment 7 additions:

# At the top
# - imported csv and import datetime (libraries)
# - added DEBUG = True flag that skips the game, asks for name, and saves placeholder score
# - added RECORDS_FILE = "inventory_game_leaderboard.csv" - filename used for saving

# New functions (Claude AI was used to help figure out what new functions was needed to run, and where to put them)
# count_moves(command_log) - counts the amount of commands that was typed as your "score"
# count_moves(command_log) - counts how many commands you typed as your "score" (fewer = better)
# save_record(name, moves) - saves name, timestamp, and moves to the CSV
#                          - Uses try/except FileNotFoundError to handle the first run (creates the file)
#                          - plus a general except Exception for anything unexpected
# show_leaderboard() -  reads the CSV and prints a ranked table, also wrapped in try/except

# In game_loop ()
# - added leaderboard functions before game_loop()
# - now the code should accept player_name as a parameter
# - added command_log = [] to track number of moves (every command typed)
# - each input gets appended to command_log. on winnings, it calculates moves, saves record and shows leaderboard

# At the bottom
# - added DEBUG entry point at the bottom of game code

# ________________

# import necessary libraries
import csv
import datetime

# debug flag - setting DEBUG = True to skip the game for testing purposes
DEBUG = True

RECORDS_FILE = "inventory_game_leaderboard.csv"

# Game State

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

crown_stolen = False
alarm_disabled = False
map_checked = False
game_won = False

# Helper

def find_item(item_name, item_list):
    for item in item_list:
        if item["name"].lower() == item_name.lower():
            return item
    return None

# Functions

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

    name = item["name"].lower()

    if name == "gloves":
        print("You pull on the leather gloves. No fingerprints left behind.")

    elif name == "lockpick":
        if find_item("gloves", inventory) is None:
            print("You stop yourself. Put on the gloves first - no fingerprints!")
        elif not crown_stolen:
            print("You carefully pick the lock on the display case...")
            print("Click. It opens. You grab the Golden Crown!")
            crown_stolen = True
            inventory.append({"name": "Golden Crown", "type": "treasure", "description": "The Golden Crown. Priceless."})
        else:
            print("The display case is already open.")

    elif name == "keycard":
        if not crown_stolen:
            print("You swipe the keycard but nothing happens. This doesn't feel like the right moment.")
        elif not alarm_disabled:
            print("You swipe the keycard on the alarm panel.")
            print("The blinking red light turns green. The alarm is disarmed.")
            alarm_disabled = True
        else:
            print("The alarm is already disarmed.")

    elif name == "map":
        if not alarm_disabled:
            print("You study the map. There is a maintenance corridor near the back exit.")
            print("It could be a way out - but you are not ready to leave yet.")
        else:
            print("You unfold the map and locate the narrow maintenance corridor.")
            print("That is your way out. But it looks pitch black in there.")
            map_checked = True

    elif name == "torch":
        if not alarm_disabled:
            print("You click on the torch. The beam sweeps across the room.")
            print("The Golden Crown glints behind the display case. Focus.")
        elif not map_checked:
            print("You switch on the torch but you are not sure where to go.")
            print("Check the Map first to find the way out.")
        else:
            print("You click on the torch and step into the maintenance corridor.")
            print("The beam of light guides you through the narrow passage.")
            print("A door at the end swings open and you slip out into the cool night air.")
            print("\nBehind you, the museum stands silent. Nobody saw a thing.")
            game_won = True

    elif name == "crowbar":
        print("You raise the crowbar toward the display case... then stop.")
        print("Too noisy. The guard would hear you instantly. Better find another way.")

    else:
        print(f"You fiddle with the {item['name']} but nothing happens.")

def examine(item_name):
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

def restart():
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
    name = input("Enter your name: ").strip()
    game_loop(name)

# ==============================================
#   Assignment 7: Record Saving & Leaderboard
# ==============================================
# Claude AI assisted with def save_record

def count_moves(command_log):
    # count how many commands the player used as their "score"
    return len(command_log)

def save_record(name, moves):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    new_row = [name, timestamp, moves]

    try:
        # try to open the existing file and read it first
        existing_rows = []
        with open(RECORDS_FILE) as f:
            reader = csv.reader(f)
            next(reader)  # skip the header row
            for row in reader:
                existing_rows.append(row)

        # add the new result
        existing_rows.append(new_row)

        # sort by moves (fewer moves = better score), column index 2
        existing_rows.sort(key=lambda row: int(row[2]))

        # write everything back
        with open(RECORDS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Timestamp", "Moves"])
            writer.writerows(existing_rows)

        print("Your result has been saved!")

    except FileNotFoundError:
        # no record file yet - create a new one
        with open(RECORDS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Timestamp", "Moves"])
            writer.writerow(new_row)
        print("No record file found. A new one has been created!")

    except Exception as e:
        print(f"Something went wrong while saving: {e}")

def show_leaderboard():
    print("\n--- LEADERBOARD (fewest moves wins) ---")
    try:
        with open(RECORDS_FILE) as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            rows = list(reader)

        if len(rows) == 0:
            print("No records yet.")
            return

        print(f"{'Rank':<6} {'Name':<15} {'Moves':<8} {'Date'}")
        print("-" * 45)
        for i, row in enumerate(rows):
            print(f"{i + 1:<6} {row[0]:<15} {row[2]:<8} {row[1]}")

    except FileNotFoundError:
        print("No records file found yet.")
    except Exception as e:
        print(f"Something went wrong while reading the leaderboard: {e}")

# Game Loop

def game_loop(player_name):
    # Assignment 7: Track number of moves
    command_log = []

    print("==============================================")
    print("           THE MUSEUM HEIST                  ")
    print("==============================================")
    print("It's 2am. You've snuck into the city museum.")
    print("The Golden Crown is somewhere in this room.")
    print("Getting out won't be easy.")
    print()
    print("--- HOW TO PLAY ---")
    print("  look              - see what is in the room")
    print("  examine [item]    - inspect something closely")
    print("  pickup [item]     - pick up an item")
    print("  drop [item]       - drop an item from your bag")
    print("  use [item]        - use an item")
    print("  inventory         - check what you are carrying")
    print("  hint              - get a nudge if you are stuck")
    print("  quit              - give up and leave")
    print()
    print("Start by typing 'look'.")
    print("==============================================")

    while True:
        if game_won:
            moves = count_moves(command_log)
            print("\nYou escaped with the Golden Crown. The perfect heist!")
            print(f"You completed it in {moves} moves.")
            save_record(player_name, moves)
            show_leaderboard()
            print("\nType 'restart' to play again or press Enter to exit.")
            again = input("\n> ").strip().lower()
            if again == "restart":
                restart()
            else:
                print("Goodbye!")
            return

        command = input("\n> ").strip().lower()
        command_log.append(command)  # Assignment 7: Log every command

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
                return
            case _:
                print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    # DEBUG mode. when DEBUG = True, skip the game and save a placeholder score just for testing
    if DEBUG:
        print("--- DEBUG MODE ---")
        name = input("Enter your name: ").strip()
        placeholder_moves = 99  # placeholder score for testing
        save_record(name, placeholder_moves)
        show_leaderboard()
    else:
        name = input("Enter your name: ").strip()
        game_loop(name)
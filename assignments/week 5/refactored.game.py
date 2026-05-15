"""
I chose to refactor my Week 2 text-based adventure game.
Here are the visible changes made:

1. I wrapped the entire gameplay loop inside a proper
   'main()' function to avoid running code loosely.

2. I pulled the core game numbers/constant factors (CLOUT_GOAL, STARTING_CLOUT,
   STARTING_MONEY) out of the logic and defined them clearly at the top as constants.

3. In the original code, I repeated a 'while True'
   loop 5 different times to validate player input for choices 1 and 2.
   I consolidated this into 'get_valid_choice(prompt)', which takes the question
   as an argument and returns the verified choice, reducing repetitive code.

4. I created 'display_stats()' to handle the repetitive
   printing of player stats between chapters.

"""

import time

# constants
CLOUT_GOAL = 100
STARTING_CLOUT = 10
STARTING_MONEY = 100

# functions

def get_valid_choice(prompt):
    """Forces the user to enter a valid option ('1' or '2') and returns it."""
    while True:
        choice = input(prompt)
        if choice == "1" or choice == "2":
            return choice
        print("❌ That is not a valid answer, try again.")

def display_stats(clout, money):
    """Displays the player's current status."""
    print(f"\n[Stats: {clout} Clout Points | ${money} Cash]")

# main_game

def main():
    while True:
        print("\n" + "✨" * 15)
        print(" STARSTRUCK: THE ROAD TO GLORY")
        print("✨" * 15)

        # setup variables using constants
        name = input("\n👤 Enter your character name: ")
        clout_points = STARTING_CLOUT
        money = STARTING_MONEY

        print(f"\nWelcome, {name.upper()}!")
        print(f"Your goal is to earn a total of {CLOUT_GOAL} Clout Points!")
        print("You've just arrived in the city with a suitcase and a dream.")
        display_stats(clout_points, money)
        time.sleep(1)

        # chapter_1
        print("\n--- CHAPTER 1: THE GILDED LILY ---")
        print("The bass is thumping inside the most exclusive club in town.")
        print("A man in a suit stops you. 'Who do you think you are?'")
        print("1) 'I'm the next big thing.'")
        print("2) 'I'm just a fan of the music.'")

        choice1 = get_valid_choice("Choose 1 or 2: ")

        if choice1 == "1":
            print("\nHe raises an eyebrow. 'The next big thing, huh? Prove it.'")
            print("1) Sing a line of your new song right now")
            print("2) Hand him a $20 bill to let you in")

            sub_choice = get_valid_choice("Choose 1 or 2: ")

            if sub_choice == "1":
                print("\n🎤 You hit a perfect high note! The crowd nearby cheers.")
                clout_points += 30
            else:
                print("\n💵 He takes the money and winks. 'Welcome to the party.'")
                money -= 20
                clout_points += 10
        else:
            print("\n'At least you're honest,' he says. He lets you in through the side door.")
            clout_points += 5

        # chapter_2
        display_stats(clout_points, money)
        print("\n--- CHAPTER 2: THE BIG BREAK ---")
        print("Inside, a famous producer notices your style.")
        print("He offers you a recording session, but it costs $50.")
        print("1) Pay for the session to record a hit")
        print("2) Try to freestyle for him for free")

        choice2 = get_valid_choice("Choose 1 or 2: ")

        if choice2 == "1":
            print("\n🎧 The song sounds amazing! It's playing in every coffee shop.")
            money -= 50
            clout_points += 40
        else:
            print("\n😬 You got nervous and stumbled over the words. Awkward.")
            clout_points -= 5

        # chapter_3
        display_stats(clout_points, money)
        print("\n--- CHAPTER 3: THE SCANDAL ---")
        print("A tabloid magazine wants to write a fake story about you for 'hype.'")
        print("1) Agree to the drama for the Clout Points")
        print("2) Keep your reputation clean and refuse")

        choice3 = get_valid_choice("Choose 1 or 2: ")

        if choice3 == "1":
            print("\n🔥 You are trending #1 on Twitter! But your old friends are disappointed.")
            clout_points += 30
        else:
            print("\n💖 Your fans respect your honesty. You gain a 'Diamond' reputation.")
            clout_points += 15

        # chapter_4
        display_stats(clout_points, money)
        print("\n--- CHAPTER 4: THE ARENA SHOW ---")
        print("The lights are blinding. 50,000 people are screaming your name.")
        print("1) Do a stage dive into the crowd!")
        print("2) Bring a fan up on stage to sing with you")

        choice4 = get_valid_choice("Choose 1 or 2: ")

        if choice4 == "1":
            print("\n🎸 EPIC! The video of your jump goes worldwide.")
            clout_points += 20
        else:
            print("\n🥺 That was so sweet! The internet is calling you a 'Wholesome Icon.'")
            clout_points += 25

        # final_score
        print("\n" + "=" * 45)
        print(f"FINAL TOTAL: {clout_points} CLOUT POINTS")

        if clout_points >= CLOUT_GOAL:
            print(f"🏆 MEGASTAR: {name.upper()}, the world is your oyster!")
        else:
            print(f"😐 RISING STAR: You've got potential, but the journey continues.")
        print("=" * 45)

        # restart_option
        print("\nDo you want to play again?")
        print("1) Yes")
        print("2) No (Exit)")

        restart = get_valid_choice("Select 1 or 2: ")

        if restart == "2":
            print(f"\nGoodbye, {name}! Your star will always shine. ✨")
            break

if __name__ == "__main__":
    main()
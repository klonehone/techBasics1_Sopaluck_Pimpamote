import time  #

# Main game loop for restarting
while True:
    print("\n" + "✨" * 15)
    print(" STARSTRUCK: THE ROAD TO GLORY")
    print("✨" * 15)

    # Setup variables
    name = input("\n👤 Enter your character name: ")
    clout_points = 10
    money = 100

    print(f"\nWelcome, {name.upper()}!")  # [cite: 4]
    print("Your goal is to earn a total of 100 Clout Points!")
    print("You've just arrived in the city with a suitcase and a dream.")
    print(f"Stats: {clout_points} Clout Points | ${money} Cash")
    time.sleep(1)  # [cite: 4]

    # --- CHAPTER 1: THE CLUB ENTRANCE ---
    print("\n--- CHAPTER 1: THE GILDED LILY ---")
    print("The bass is thumping inside the most exclusive club in town.")
    print("A man in a suit stops you. 'Who do you think you are?'")
    print("1) 'I'm the next big thing.'")
    print("2) 'I'm just a fan of the music.'")

    while True:
        choice1 = input("Choose 1 or 2: ")
        if choice1 == "1" or choice1 == "2":
            break
        print("❌ That is not a valid answer, try again.")

    if choice1 == "1":
        # NESTED CONDITIONAL (The choice within a choice)[cite: 4]
        print("\nHe raises an eyebrow. 'The next big thing, huh? Prove it.'")
        print("1) Sing a line of your new song right now")
        print("2) Hand him a $20 bill to let you in")

        while True:
            sub_choice = input("Choose 1 or 2: ")
            if sub_choice == "1" or sub_choice == "2":
                break
            print("❌ That is not a valid answer, try again.")

        if sub_choice == "1":
            print("\n🎤 You hit a perfect high note! The crowd nearby cheers.")
            clout_points += 30
        else:
            print("\n💵 He takes the money and winks. 'Welcome to the party.'")
            money -= 20  # [cite: 4]
            clout_points += 10
    else:
        print("\n'At least you're honest,' he says. He lets you in through the side door.")
        clout_points += 5

    # --- CHAPTER 2: THE STUDIO ---
    print(f"\n[Stats: {clout_points} Clout Points | ${money}]")
    print("\n--- CHAPTER 2: THE BIG BREAK ---")
    print("Inside, a famous producer notices your style.")
    print("He offers you a recording session, but it costs $50.")
    print("1) Pay for the session to record a hit")
    print("2) Try to freestyle for him for free")

    while True:
        choice2 = input("Choose 1 or 2: ")
        if choice2 == "1" or choice2 == "2":
            break
        print("❌ That is not a valid answer, try again.")

    if choice2 == "1":
        print("\n🎧 The song sounds amazing! It's playing in every coffee shop.")
        money -= 50
        clout_points += 40
    else:
        print("\n😬 You got nervous and stumbled over the words. Awkward.")
        clout_points -= 5

    # --- CHAPTER 3: THE DRAMA ---
    print(f"\n[Stats: {clout_points} Clout Points | ${money}]")
    print("\n--- CHAPTER 3: THE SCANDAL ---")
    print("A tabloid magazine wants to write a fake story about you for 'hype.'")
    print("1) Agree to the drama for the Clout Points")
    print("2) Keep your reputation clean and refuse")

    while True:
        choice3 = input("Choose 1 or 2: ")
        if choice3 == "1" or choice3 == "2":
            break
        print("❌ That is not a valid answer, try again.")

    if choice3 == "1":
        print("\n🔥 You are trending #1 on Twitter! But your old friends are disappointed.")
        clout_points += 30
    else:
        print("\n💖 Your fans respect your honesty. You gain a 'Diamond' reputation.")
        clout_points += 15

    # --- CHAPTER 4: THE FINALE ---
    print(f"\n[Stats: {clout_points} Clout Points | ${money}]")
    print("\n--- CHAPTER 4: THE ARENA SHOW ---")
    print("The lights are blinding. 50,000 people are screaming your name.")
    print("1) Do a stage dive into the crowd!")
    print("2) Bring a fan up on stage to sing with you")

    while True:
        choice4 = input("Choose 1 or 2: ")
        if choice4 == "1" or choice4 == "2":
            break
        print("❌ That is not a valid answer, try again.")

    if choice4 == "1":
        print("\n🎸 EPIC! The video of your jump goes worldwide.")
        clout_points += 20
    else:
        print("\n🥺 That was so sweet! The internet is calling you a 'Wholesome Icon.'")
        clout_points += 25

    # --- FINAL SCORE ---
    print("\n" + "=" * 45)
    print(f"FINAL TOTAL: {clout_points} CLOUT POINTS")

    if clout_points >= 100:
        print(f"🏆 MEGASTAR: {name.upper()}, the world is your oyster!")
    else:
        print(f"😐 RISING STAR: You've got potential, but the journey continues.")
    print("=" * 45)

    # --- RESTART OPTION ---
    print("\nDo you want to play again?")
    print("1) Yes")
    print("2) No (Exit)")

    while True:
        restart = input("Select 1 or 2: ")
        if restart == "1" or restart == "2":
            break
        print("❌ That is not a valid answer, try again.")

    if restart == "2":
        print(f"\nGoodbye, {name}! Your star will always shine. ✨")
        break  # Exits the main loop[cite: 4]
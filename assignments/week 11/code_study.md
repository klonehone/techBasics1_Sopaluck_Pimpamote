# Code Reading Exercise - Assignment 11

---

### 1. Where did you find the code? Why did you choose it?

**Link:** https://github.com/geekcomputers/Python/blob/master/blackJackGUI.py

I found it in the `geekcomputers/Python` repository on GitHub. I chose `blackJackGUI.py` because it's a complete, self-contained game (Blackjack) written in about 180 lines. It uses classes, functions, and a GUI library called simplegui. I could recognize the Python concepts from class (like dictionaries, lists, classes) but also see new things I hadn't used before, like simplegui.

---

### 2. What does the program do?

The program is a Blackjack card game. The player can deal cards, hit, or stand. The dealer plays automatically after the player stands. The program checks who has the higher score without going over 21, and displays the result on a canvas window.

The structure of the file looks something like this:

- **Imports and global variables** at the top (score, game state, card image URL)
- **Constants** - `SUITS`, `RANKS`, and `VALUES` (a dictionary mapping card names to their point values)
- **Three classes** - `Card`, `Hand`, and `Deck`, each handling a different part of the game logic
- **Three game functions** - `deal()`, `hit()`, and `stand()`, controlling the flow of the game
- **A draw function** - `draw(canvas)`, which renders text and cards onto the GUI
- **GUI setup** at the bottom using simplegui to create the window and buttons
---

### 3. Function analysis: `get_value()` in the `Hand` class

**What does it do?**
It calculates the total point value of all cards currently in a player's hand. It also handles the special case of the Ace card, which can be worth either 1 or 11 depending on which is better for the player.

**Inputs and outputs:**
- Input: none (it reads `self.hand`, the list of cards in the hand)
- Output: an integer - the total point value of the hand

**How it works step by step (Claude AI-assisted):**

1. It creates an empty list `var` and sets `self.hand_value` to 0.
2. It loops through each card in the hand. Each card is converted to a string like `"H5"` (suit + rank), so `card[1]` gives the rank.
3. It looks up the rank in the `VALUES` dictionary and adds its point value to `self.hand_value`.
4. It also appends the rank to `var`, so we can check later if an Ace was dealt.
5. After the loop: if there's no Ace in the hand, it just returns `self.hand_value`.
6. If there is an Ace: it checks whether adding 10 (to make the Ace worth 11 instead of 1) would keep the total at 21 or under. If yes, it returns `self.hand_value + 10`. If not, it returns `self.hand_value` as-is (Ace counts as 1).

---

### 4. Takeaways

**Dictionaries for lookup tables: (Claude AI-assisted)**
The `VALUES` dictionary (`"A": 1, "2": 2, ...`) is a clean way to map card names to numbers. Instead of writing a long `if/elif` chain for every card, you just do `VALUES[card_rank]` and get the value instantly. This is something I could use in my own projects as well.

**Breaking a program into classes:**
The code separates `Card`, `Hand`, and `Deck` into three different classes. Each class only handles its own responsibility. This made the code much easier to read because each part was self-contained.

**`__str__` methods:**
Each class defines a `__str__` method, which controls what gets printed when you use `print()` or `str()` on an object. It's a neat way to make objects print in a readable way.

---

### 5. What parts were confusing at first?

**`simplegui`:**
The library `simplegui` was unfamiliar to me. It works differently from regular Python libraries - it runs in a browser environment called CodeSkulptor, which run Python programs in the browser. So this file would not actually run in a normal Python environment like PyCharm. It did take a while to understand and figure that out(and the code too). 

**`from __future__ import print_function`:*
This is at the very top of the file. I looked it up and found it's a compatibility line from older Python 2 code - it makes `print` behave like Python 3's `print()` function. It's not needed in Python 3. I have never seen it before, but I looked up and people say that you'll sometimes still see it in older code on GitHub.

**Global variables inside functions:**
The `deal()` and `hit()` functions use the `global` keyword to modify variables defined outside the function. We saw this concept in class. I understood it technically, but seeing it used across multiple functions made it clearer why it can get messy, and why using classes to store state is often cleaner.

---

### Extra notes

- Repository: `geekcomputers/Python`
- File: `blackJackGUI.py` - 181 lines
- Language: Python 3
- Concepts recognised from class: dictionaries, lists, classes, functions, loops, global variables
- New concepts encountered: `__str__` method, `simplegui` library, `from __future__`
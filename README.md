# stacklifo
# 🃏 Card Stack Game

A simple, interactive **Card Stack Game built using Python and Tkinter**. This project demonstrates the working of the **Stack data structure** and its LIFO (Last In, First Out) principle through a graphical user interface.

Players can draw cards, remove the top card, view the top card, and reset the game while keeping track of their score.

## 📌 Project Overview

The Card Stack Game is a beginner-friendly Python project designed to demonstrate basic data structure operations in an interactive way.

The game uses a shuffled deck of 52 playing cards and implements stack operations using Python lists.

## ✨ Features

- 🃏 **Draw Card (PUSH):** Draw a card and add it to the top of the stack.
- ⬇️ **Pop Card (POP):** Remove the top card from the stack.
- 👀 **Peek Card (PEEK):** View the top card without removing it.
- 🔄 **Reset Game:** Clear the stack, shuffle the deck, and restart the score.
- 📊 **Score Tracking:** Earn points by performing stack operations.
- 🔢 **Card Counter:** View the current number of cards in the stack.
- 🎴 **Shuffled Deck:** Play with 52 cards, including all four suits.
- 🖥️ **Graphical User Interface:** Simple and interactive interface created using Tkinter.
- ⚠️ **Error Handling:** Displays messages when the stack is empty or all cards have been used.

## 🧠 Data Structure Used

**Stack — LIFO (Last In, First Out)**

A stack is a linear data structure in which the last element added is the first element removed.

This project uses Python lists to implement the stack.

| Operation | Python Method | Description |
|---|---|---|
| PUSH | `append()` | Adds a card to the top of the stack. |
| POP | `pop()` | Removes the top card from the stack. |
| PEEK | `stack[-1]` | Displays the top card without removing it. |
| DISPLAY | `reversed()` | Displays the stack from top to bottom. |

### Example

If the cards are added in this order:

`A♥ → K♠ → 7♦`

The top card is `7♦`.

When the POP operation is performed, `7♦` is removed first. This demonstrates the LIFO principle.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **GUI Library:** Tkinter
- **Module:** Random
- **Data Structure:** Stack
- **IDE:** Visual Studio Code or any Python-supported editor

## ⚙️ Requirements

- Python 3.x
- Tkinter (usually included with standard Python installations)

No external Python packages are required for the basic version.



1. **Start playing!**

   Use the Draw Card, Pop, Peek, and Reset buttons to explore the stack operations.

## 🎮 How to Play

1. Click **DRAW CARD** to add a card to the stack and earn 5 points.
2. Click **POP** to remove the top card and earn 2 points.
3. Click **PEEK** to view the top card without removing it.
4. Check the number of cards and your score.
5. Click **RESET** to restart the game with a newly shuffled deck.

## 📂 Project Structure

```text
card-stack-game/
│
├── card_stack_game.py   # Main Python application
├── README.md            # Project documentation
└── LICENSE              # Optional license file
```

## 🎯 Learning Objectives

This project helps beginners understand:

- The Stack data structure.
- The LIFO principle.
- PUSH, POP, and PEEK operations.
- Python lists and functions.
- Randomization and list manipulation.
- GUI development using Tkinter.
- Event handling through buttons.
- Basic error handling and score management.

## 🔮 Future Improvements

- Add card images and animations.
- Improve the interface with colors and custom themes.
- Add sound effects.
- Introduce different game modes.
- Save high scores.
- Add a game timer and leaderboard.

**Built with Python 🐍 and Tkinter 🖥️**


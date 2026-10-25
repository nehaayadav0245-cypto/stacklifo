import tkinter as tk
import random

# -----------------------------
# CARD STACK GAME
# Data Structure: STACK
# Principle: LIFO
# -----------------------------

# Create the main window
root = tk.Tk()
root.title("🃏 Card Stack Game")
root.geometry("500x650")
root.resizable(False, False)

# -----------------------------
# VARIABLES
# -----------------------------

# Stack
stack = []

# Create deck
deck = [
    "A", "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "J", "Q", "K"
]

# Add suits
suits = ["♥", "♦", "♣", "♠"]

# Create complete deck
cards = [rank + suit for rank in deck for suit in suits]

# Shuffle cards
random.shuffle(cards)

score = 0


# -----------------------------
# FUNCTIONS
# -----------------------------

def update_display():
    """Update the stack display."""

    stack_list.delete(0, tk.END)

    # Display cards from top to bottom
    for card in reversed(stack):
        stack_list.insert(tk.END, card)

    # Update number of cards
    count_label.config(
        text="Cards in Stack: " + str(len(stack))
    )

    # Update score
    score_label.config(
        text="Score: " + str(score)
    )

    # Show top card
    if len(stack) > 0:
        top_label.config(
            text="TOP CARD: " + stack[-1]
        )
    else:
        top_label.config(
            text="TOP CARD: None"
        )


def draw_card():
    """Push a card into the stack."""

    global score

    if len(cards) == 0:
        message_label.config(
            text="🎉 All cards have been used!"
        )
        return

    # Take a card from deck
    card = cards.pop()

    # PUSH operation
    stack.append(card)

    # Increase score
    score += 5

    message_label.config(
        text="🃏 Card " + card + " pushed into stack!"
    )

    update_display()


def pop_card():
    """Remove the top card from stack."""

    global score

    if len(stack) == 0:
        message_label.config(
            text="⚠️ Stack Underflow! Stack is empty."
        )
        return

    # POP operation
    card = stack.pop()

    score += 2

    message_label.config(
        text="⬇️ Card " + card + " popped from stack!"
    )

    update_display()


def peek_card():
    """Show the top card without removing it."""

    if len(stack) == 0:
        message_label.config(
            text="⚠️ Stack is empty!"
        )
        return

    # PEEK operation
    card = stack[-1]

    message_label.config(
        text="👀 Peek: Top card is " + card
    )


def reset_game():
    """Reset the game."""

    global stack, cards, score

    stack = []

    cards = [
        rank + suit
        for rank in deck
        for suit in suits
    ]

    random.shuffle(cards)

    score = 0

    message_label.config(
        text="🔄 Game has been reset!"
    )

    update_display()


# -----------------------------
# TITLE
# -----------------------------

title_label = tk.Label(
    root,
    text="🃏 CARD STACK GAME",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=15)


# -----------------------------
# DATA STRUCTURE INFORMATION
# -----------------------------

info_label = tk.Label(
    root,
    text="STACK  →  LIFO (Last In, First Out)",
    font=("Arial", 13, "bold")
)

info_label.pack(pady=5)


# -----------------------------
# TOP CARD
# -----------------------------

top_label = tk.Label(
    root,
    text="TOP CARD: None",
    font=("Arial", 18, "bold")
)

top_label.pack(pady=15)


# -----------------------------
# STACK DISPLAY
# -----------------------------

stack_list = tk.Listbox(
    root,
    width=20,
    height=10,
    font=("Arial", 16),
    justify="center"
)

stack_list.pack(pady=10)


# -----------------------------
# STATUS
# -----------------------------

count_label = tk.Label(
    root,
    text="Cards in Stack: 0",
    font=("Arial", 12)
)

count_label.pack(pady=3)


score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 12, "bold")
)

score_label.pack(pady=3)


message_label = tk.Label(
    root,
    text="Click DRAW CARD to start!",
    font=("Arial", 11)
)

message_label.pack(pady=10)


# -----------------------------
# BUTTONS
# -----------------------------

button_frame = tk.Frame(root)
button_frame.pack(pady=10)


draw_button = tk.Button(
    button_frame,
    text="🃏 DRAW CARD",
    font=("Arial", 12, "bold"),
    width=15,
    command=draw_card
)

draw_button.grid(row=0, column=0, padx=5, pady=5)


pop_button = tk.Button(
    button_frame,
    text="⬇️ POP",
    font=("Arial", 12, "bold"),
    width=15,
    command=pop_card
)

pop_button.grid(row=0, column=1, padx=5, pady=5)


peek_button = tk.Button(
    button_frame,
    text="👀 PEEK",
    font=("Arial", 12, "bold"),
    width=15,
    command=peek_card
)

peek_button.grid(row=1, column=0, padx=5, pady=5)


reset_button = tk.Button(
    button_frame,
    text="🔄 RESET",
    font=("Arial", 12, "bold"),
    width=15,
    command=reset_game
)

reset_button.grid(row=1, column=1, padx=5, pady=5)


# -----------------------------
# START GAME
# -----------------------------

update_display()

root.mainloop()
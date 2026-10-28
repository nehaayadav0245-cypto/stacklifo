
import tkinter as tk
from tkinter import ttk
import random

# -------------------- COLORS --------------------
BG = "#101827"
PANEL = "#1B263B"
CARD_BG = "#F8FAFC"
ACCENT = "#7C5CFC"
GREEN = "#22C55E"
RED = "#F87171"
WHITE = "#F1F5F9"
MUTED = "#94A3B8"

# -------------------- MAIN WINDOW --------------------
root = tk.Tk()
root.title("Card Stack Pro | Data Structures Project")
root.geometry("760x790")
root.resizable(False, False)
root.configure(bg=BG)

# -------------------- GAME DATA --------------------
ranks = ["A", "2", "3", "4", "5", "6", "7",
         "8", "9", "10", "J", "Q", "K"]
suits = ["♥", "♦", "♣", "♠"]

stack = []
cards = []
score = 0
moves = 0

# -------------------- DECK FUNCTIONS --------------------
def create_deck():
    return [rank + suit for rank in ranks for suit in suits]


def reset_game():
    global stack, cards, score, moves

    stack = []
    cards = create_deck()
    random.shuffle(cards)
    score = 0
    moves = 0

    message_label.config(
        text="Welcome! Click DRAW CARD to begin.",
        fg=WHITE
    )
    update_display()


# -------------------- DISPLAY FUNCTIONS --------------------
def update_display():
    stack_list.delete(0, tk.END)

    # Show the most recent card first
    for card in reversed(stack):
        stack_list.insert(tk.END, "     " + card)

    score_label.config(text=str(score))
    moves_label.config(text=str(moves))
    remaining_label.config(text=str(len(cards)))
    stack_count_label.config(text=str(len(stack)))

    if stack:
        card = stack[-1]
        rank = card[:-1]
        suit = card[-1]
        color = RED if suit in ["♥", "♦"] else BG

        card_canvas.delete("all")

        # Draw a playing card
        card_canvas.create_rectangle(
            55, 12, 205, 205,
            fill=CARD_BG, outline="#CBD5E1", width=2
        )
        card_canvas.create_text(
            75, 35, text=rank,
            fill=color, font=("Arial", 20, "bold")
        )
        card_canvas.create_text(
            75, 58, text=suit,
            fill=color, font=("Arial", 18, "bold")
        )
        card_canvas.create_text(
            130, 110, text=suit,
            fill=color, font=("Arial", 65, "bold")
        )
        card_canvas.create_text(
            185, 182, text=rank,
            fill=color, font=("Arial", 20, "bold")
        )

        top_card_label.config(text="TOP CARD")
    else:
        card_canvas.delete("all")
        card_canvas.create_rectangle(
            55, 12, 205, 205,
            fill=PANEL, outline=ACCENT, width=3
        )
        card_canvas.create_text(
            130, 85, text="?",
            fill=WHITE, font=("Arial", 65, "bold")
        )
        card_canvas.create_text(
            130, 145, text="NO CARD",
            fill=MUTED, font=("Arial", 13, "bold")
        )
        top_card_label.config(text="TOP CARD: EMPTY")

    # Update progress bar
    progress["value"] = (52 - len(cards)) / 52 * 100


# -------------------- STACK OPERATIONS --------------------
def draw_card():
    global score, moves

    if not cards:
        message_label.config(
            text="All 52 cards have been drawn!",
            fg=GREEN
        )
        return

    card = cards.pop()
    stack.append(card)       # PUSH operation
    score += 5
    moves += 1

    message_label.config(
        text=f"Card {card} pushed into the stack!  +5 points",
        fg=GREEN
    )
    update_display()


def pop_card():
    global score, moves

    if not stack:
        message_label.config(
            text="Stack Underflow! There are no cards to remove.",
            fg=RED
        )
        return

    card = stack.pop()       # POP operation
    score += 2
    moves += 1

    message_label.config(
        text=f"Card {card} popped from the stack!  +2 points",
        fg=GREEN
    )
    update_display()


def peek_card():
    if not stack:
        message_label.config(
            text="Stack is empty! Draw a card first.",
            fg=RED
        )
        return

    card = stack[-1]         # PEEK operation

    message_label.config(
        text=f"Top card is {card}. The stack is unchanged.",
        fg=ACCENT
    )


# -------------------- HEADER --------------------
header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=25, pady=(22, 12))

tk.Label(
    header,
    text="♠  CARD STACK PRO",
    font=("Arial", 25, "bold"),
    bg=BG, fg=WHITE
).pack(anchor="w")

tk.Label(
    header,
    text="DATA STRUCTURES  |  STACK VISUALIZER",
    font=("Arial", 10, "bold"),
    bg=BG, fg=ACCENT
).pack(anchor="w", pady=(5, 0))


# -------------------- STATISTICS --------------------
stats = tk.Frame(root, bg=BG)
stats.pack(fill="x", padx=25, pady=8)

def create_stat(parent, title, value, color):
    frame = tk.Frame(parent, bg=PANEL, padx=12, pady=12)
    frame.pack(side="left", expand=True, fill="both", padx=5)

    tk.Label(
        frame, text=title, font=("Arial", 10),
        bg=PANEL, fg=MUTED
    ).pack()

    label = tk.Label(
        frame, text=value, font=("Arial", 23, "bold"),
        bg=PANEL, fg=color
    )
    label.pack(pady=(4, 0))
    return label


score_label = create_stat(stats, "SCORE", "0", GREEN)
moves_label = create_stat(stats, "MOVES", "0", WHITE)
remaining_label = create_stat(stats, "DECK LEFT", "52", ACCENT)
stack_count_label = create_stat(stats, "STACK SIZE", "0", WHITE)


# -------------------- GAME AREA --------------------
game_area = tk.Frame(root, bg=BG)
game_area.pack(fill="both", expand=True, padx=30, pady=15)

# Left: playing card
left_panel = tk.Frame(game_area, bg=PANEL, padx=15, pady=15)
left_panel.pack(side="left", fill="both", expand=True, padx=(0, 10))

tk.Label(
    left_panel, text="CURRENT CARD",
    font=("Arial", 11, "bold"), bg=PANEL, fg=MUTED
).pack(pady=(0, 10))

card_canvas = tk.Canvas(
    left_panel, width=260, height=220,
    bg=PANEL, highlightthickness=0
)
card_canvas.pack(pady=5)

top_card_label = tk.Label(
    left_panel, text="TOP CARD: EMPTY",
    font=("Arial", 12, "bold"), bg=PANEL, fg=WHITE
)
top_card_label.pack(pady=12)

tk.Label(
    left_panel, text="LIFO: Last In, First Out",
    font=("Arial", 10, "bold"), bg=PANEL, fg=ACCENT
).pack(pady=5)

# Right: stack list
right_panel = tk.Frame(game_area, bg=PANEL, padx=12, pady=15)
right_panel.pack(side="right", fill="both", expand=True, padx=(10, 0))

tk.Label(
    right_panel, text="STACK CONTENTS",
    font=("Arial", 11, "bold"), bg=PANEL, fg=WHITE
).pack(pady=(0, 10))

stack_list = tk.Listbox(
    right_panel,
    height=12,
    width=16,
    font=("Consolas", 13, "bold"),
    bg="#0B1220",
    fg=WHITE,
    selectbackground=ACCENT,
    relief="flat",
    borderwidth=0,
    highlightthickness=0
)
stack_list.pack(fill="both", expand=True)

tk.Label(
    right_panel, text="Newest card appears first",
    font=("Arial", 9), bg=PANEL, fg=MUTED
).pack(pady=(8, 0))


# -------------------- DECK PROGRESS --------------------
progress_frame = tk.Frame(root, bg=BG)
progress_frame.pack(fill="x", padx=35, pady=(0, 10))

tk.Label(
    progress_frame, text="DECK PROGRESS",
    font=("Arial", 9, "bold"), bg=BG, fg=MUTED
).pack(anchor="w")

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Game.Horizontal.TProgressbar",
    troughcolor=PANEL,
    background=ACCENT,
    thickness=9,
    bordercolor=BG
)

progress = ttk.Progressbar(
    progress_frame,
    maximum=100,
    value=0,
    style="Game.Horizontal.TProgressbar"
)
progress.pack(fill="x", pady=5)


# -------------------- MESSAGE --------------------
message_label = tk.Label(
    root,
    text="Welcome! Click DRAW CARD to begin.",
    font=("Arial", 10, "bold"),
    bg=BG, fg=WHITE,
    wraplength=690
)
message_label.pack(pady=8)


# -------------------- BUTTONS --------------------
button_frame = tk.Frame(root, bg=BG)
button_frame.pack(pady=12)

def make_button(text, command, color):
    return tk.Button(
        button_frame,
        text=text,
        command=command,
        font=("Arial", 11, "bold"),
        bg=color,
        fg="white",
        activebackground=color,
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=15,
        pady=10
    )

make_button("♠ DRAW CARD", draw_card, ACCENT).grid(
    row=0, column=0, padx=6, pady=5
)
make_button("▼ POP", pop_card, "#DC4545").grid(
    row=0, column=1, padx=6, pady=5
)
make_button("◉ PEEK", peek_card, "#2878C8").grid(
    row=0, column=2, padx=6, pady=5
)
make_button("↻ RESET", reset_game, "#475569").grid(
    row=0, column=3, padx=6, pady=5
)


# -------------------- FOOTER --------------------
tk.Label(
    root,
    text="PYTHON • TKINTER • STACK DATA STRUCTURE • LIFO",
    font=("Arial", 9),
    bg=BG, fg=MUTED
).pack(pady=(5, 15))


# Start the game
reset_game()
root.mainloop()

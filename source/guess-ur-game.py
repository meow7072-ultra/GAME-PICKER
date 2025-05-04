import tkinter as tk
from tkinter import messagebox, scrolledtext, Toplevel
import random

# --- Font Setup ---
USE_FONT = "Monocraft Nerd Font"
fallback_font = "Courier New"

try:
    test = tk.Tk()
    test_font = (USE_FONT, 10)
    tk.Label(test, text=".", font=test_font).pack()
    test.destroy()
except:
    USE_FONT = fallback_font

# --- Default Game List ---
game_list = [
    "Danganronpa", "Bloodborne", "Devil May Cry", "Ultrakill",
    "Sally Face", "The Binding of Isaac", "Persona", "Omori",
    "Resident Evil", "Silent Hill", "Hollow Knight", "Pokemon"
]

# --- Assign Games to Teams ---
def assign_games():
    input_text = team_input.get("1.0", tk.END).strip()
    names = [line.strip() for line in input_text.splitlines() if line.strip()]

    if not names:
        result_label.config(text="⚠️ Please enter at least one name.")
        return
    if not game_list:
        result_label.config(text="⚠️ Game list is empty.")
        return

    assignments = []
    for name in names:
        game = random.choice(game_list)
        assignments.append(f"{name}: {game}")

    result_label.config(text="\n".join(assignments))

# --- Edit Game List Window ---
def open_game_editor():
    def save_games():
        global game_list  # Declare it as global here, before using it

        updated = text.get("1.0", tk.END).strip().splitlines()
        new_game_list = [g.strip() for g in updated if g.strip()]
        
        # Confirm before saving the changes
        if new_game_list != game_list:
            confirm = messagebox.askyesno("Confirm Changes", "Are you sure you want to save the changes?")
            if confirm:
                game_list = new_game_list
                messagebox.showinfo("Success", "Game list updated successfully!")
                game_editor.destroy()
        else:
            messagebox.showinfo("No Changes", "No changes detected in the game list.")


    game_editor = Toplevel(root)
    game_editor.title("Edit Game List")
    game_editor.geometry("600x600")
    game_editor.configure(bg="#1e1e1e")

    game_editor.rowconfigure(1, weight=1)
    game_editor.columnconfigure(0, weight=1)

    label = tk.Label(game_editor, text="📝 Edit Game List (one per line)", font=(USE_FONT, 12), fg="white", bg="#1e1e1e")
    label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    text = scrolledtext.ScrolledText(game_editor, font=(USE_FONT, 12), bg="#2b2b2b", fg="white", insertbackground="white")
    text.grid(row=1, column=0, padx=10, pady=(0,10), sticky="nsew")

    text.insert(tk.END, "\n".join(game_list))

    save_btn = tk.Button(game_editor, text="💾 Save & Close", font=(USE_FONT, 12), bg="#4CAF50", fg="white", command=save_games)
    save_btn.grid(row=2, column=0, pady=10)

# --- UI Setup ---
root = tk.Tk()
root.title("Game Picker")
root.geometry("600x600")
root.configure(bg="#1e1e1e")

# Fonts
TITLE_FONT = (USE_FONT, 18, "bold")
LABEL_FONT = (USE_FONT, 12)
ENTRY_FONT = (USE_FONT, 12)
RESULT_FONT = (USE_FONT, 12)
BUTTON_FONT = (USE_FONT, 14)

# --- Title ---
title = tk.Label(root, text="Game Picker", font=TITLE_FONT, fg="white", bg="#1e1e1e")
title.pack(pady=15)

# --- Team Entry Area (Scrollable) ---
entry_label = tk.Label(root, text="Enter players:", font=LABEL_FONT, fg="white", bg="#1e1e1e")
entry_label.pack()

entry_frame = tk.Frame(root)
entry_frame.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

team_input = scrolledtext.ScrolledText(entry_frame, height=1, font=ENTRY_FONT, bg="#2b2b2b", fg="white", insertbackground="white")
team_input.pack(fill=tk.BOTH, expand=True)

team_input.insert(tk.END, "vladem\nhuman")

# --- Buttons ---
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)

assign_button = tk.Button(button_frame, text="🎲 Assign Games", font=BUTTON_FONT, bg="#4CAF50", fg="white", command=assign_games)
assign_button.pack(side=tk.LEFT, padx=10)

edit_games_button = tk.Button(button_frame, text="📝 Edit Game List", font=BUTTON_FONT, bg="#2196F3", fg="white", command=open_game_editor)
edit_games_button.pack(side=tk.LEFT, padx=10)

# --- Result Label ---
result_label = tk.Label(root, text="", font=RESULT_FONT, fg="#FFD700", bg="#1e1e1e", wraplength=650, justify="left")
result_label.pack(pady=20)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe - Themed")
root.configure(bg="#222831")  # Dark background

# Global variables
turn = "X"
buttons = []

# Turn label
turn_label = tk.Label(root, text="X's Turn", font=('Arial', 20, 'bold'), fg="#00FFF5", bg="#222831")
turn_label.grid(row=0, column=0, columnspan=3, pady=10)

# Check winner function
def check_winner():
    for i in range(3):
        if all(buttons[i][j]['text'] == buttons[i][0]['text'] != "" for j in range(3)):
            winner(buttons[i][0]['text'])
        if all(buttons[j][i]['text'] == buttons[0][i]['text'] != "" for j in range(3)):
            winner(buttons[0][i]['text'])

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        winner(buttons[0][0]['text'])
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        winner(buttons[0][2]['text'])

def winner(player):
    messagebox.showinfo("Game Over", f"{player} wins!")
    root.quit()

# On click event
def on_click(r, c):
    global turn
    if buttons[r][c]['text'] == "":
        buttons[r][c]['text'] = turn
        buttons[r][c].config(fg="#00FFF5" if turn == "X" else "#FF0080")
        turn = "O" if turn == "X" else "X"
        turn_label.config(text=f"{turn}'s Turn", fg="#00FFF5" if turn == "X" else "#FF0080")
        check_winner()

# Create 3x3 grid of buttons
for r in range(3):
    row = []
    for c in range(3):
        btn = tk.Button(root, text="", font=('Arial', 32, 'bold'), width=5, height=2,
                        bg="#393E46", activebackground="#00ADB5",
                        command=lambda r=r, c=c: on_click(r, c))
        btn.grid(row=r+1, column=c, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

root.mainloop()

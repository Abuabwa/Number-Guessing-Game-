import random
import tkinter as tk
from tkinter import messagebox

attempts = 6  # Number of attempts allowed

def check_guess():
    global attempts
    guess = int(entry.get())
    
    if guess == secret_number:
        messagebox.showinfo("Congratulations", "You guessed the number!")
        root.quit()
    elif guess < secret_number:
        messagebox.showinfo("Try Again", "Try a higher number.")
    else:
        messagebox.showinfo("Try Again", "Try a lower number.")
    
    attempts -= 1
    if attempts == 0:
        messagebox.showinfo("Game Over", f"Sorry, you've run out of attempts. The secret number was {secret_number}.")
        root.quit()
    
    entry.delete(0, 'end')

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Create labels and entry for user input
label = tk.Label(root, text="Guess the number (between 1 and 100):")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create a button to submit the guess
button = tk.Button(root, text="Submit Guess", command=check_guess)
button.pack()

# Run the GUI
root.mainloop()

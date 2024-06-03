import random
import tkinter as tk

def guess_number():
  number = random.randint(1, 100)
  attempts = 0

  def check_guess(event=None):
    nonlocal attempts
    guess = int(entry.get())
    entry.delete(0, tk.END)
    attempts += 1

    if guess < number:
      result_label.config(text="Too low!")
    elif guess > number:
      result_label.config(text="Too high!")
    else:
      result_label.config(text=f"Congratulations! You guessed the number in {attempts} attempts.")
      window.destroy()

  window = tk.Tk()
  window.title("Guess the Number")
  label = tk.Label(window, text="Guess a number between 1 and 100:")
  label.pack()
  entry = tk.Entry(window)
  entry.pack()
  button = tk.Button(window, text="Guess", command=check_guess)
  button.pack()
  result_label = tk.Label(window, text="")
  result_label.pack()

  # Bind the Enter key to the check_guess function
  window.bind('<Return>', check_guess)

  window.mainloop()

guess_number()

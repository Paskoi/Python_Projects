import tkinter as tk
from PIL import Image, ImageTk
import random


class DiceSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Simulator")

        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack()

        self.roll_button = tk.Button(root, text="Roll", command=self.start_rolling)
        self.roll_button.pack()

        # Load dice face images
        self.dice_images = [ImageTk.PhotoImage(Image.open(f"dice-six-faces-{i}.png").resize((100, 100))) for i in range(1, 7)]

        # Initialize the label to display dice
        self.dice_label = tk.Label(self.canvas, image=self.dice_images[0])
        self.dice_label.place(x=100, y=100)

        self.animation_steps = 20  # Number of steps in the rolling animation
        self.current_step = 0

    def start_rolling(self):
        self.current_step = 0
        self.roll_button.config(state=tk.DISABLED)
        self.roll_dice()

    def roll_dice(self):
        if self.current_step < self.animation_steps:
            self.dice_value = random.randint(1, 6)
            self.dice_label.config(image=self.dice_images[self.dice_value - 1])
            self.current_step += 1
            self.root.after(50, self.roll_dice)
        else:
            self.dice_value = random.randint(1, 6)
            self.dice_label.config(image=self.dice_images[self.dice_value - 1])
            self.roll_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    app = DiceSimulator(root)
    root.mainloop()

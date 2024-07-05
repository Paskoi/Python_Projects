import tkinter as tk
from PIL import Image, ImageTk
import random

class DiceSimulator:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Dice Simulator")

        # Create a canvas to display the image
        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack()

        # Create a button to roll the dice
        self.roll_button = tk.Button(root, text="Roll", command=self.start_rolling)
        self.roll_button.pack()

        # Load dice face images (images are named dice-six-faces-1.png, dice-six-faces-2.png, ...)
        self.dice_images = [ImageTk.PhotoImage(Image.open(f"dice-six-faces-{i}.png").resize((100, 100))) for i in range(1, 7)]

        # Initialize the label to display dice, initially showing the first image
        self.dice_label = tk.Label(self.canvas, image=self.dice_images[0])
        self.dice_label.place(x=100, y=100)

        # Settings for dice rolling animation
        self.animation_steps = 20  # Number of steps in the rolling animation
        self.current_step = 0

    def start_rolling(self):
        # Start the dice rolling animation
        self.current_step = 0
        self.roll_button.config(state=tk.DISABLED)  # Disable the button during the animation
        self.roll_dice()

    def roll_dice(self):
        # Simulate the dice rolling animation
        if self.current_step < self.animation_steps:
            # Randomize the dice value and update the image
            self.dice_value = random.randint(1, 6)
            self.dice_label.config(image=self.dice_images[self.dice_value - 1])
            self.current_step += 1
            self.root.after(50, self.roll_dice)  # Delay 50 ms before the next animation step
        else:
            # Finalize the dice value after animation
            self.dice_value = random.randint(1, 6)
            self.dice_label.config(image=self.dice_images[self.dice_value - 1])
            self.roll_button.config(state=tk.NORMAL)  # Re-enable the button

if __name__ == "__main__":
    # Create the main window and run the application
    root = tk.Tk()
    app = DiceSimulator(root)
    root.mainloop()

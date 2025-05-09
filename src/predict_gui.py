import tkinter as tk
import numpy as np
import tensorflow as tf

# Load pre-trained model
model = tf.keras.models.load_model('digit_model.h5')

# Constants
GRID_SIZE = 28
PIXEL_SIZE = 10  # Each grid cell will be 10x10 pixels
WIDTH, HEIGHT = GRID_SIZE * PIXEL_SIZE, GRID_SIZE * PIXEL_SIZE

class App:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()

        # 28x28 pixel array (float32 between 0 and 1)
        self.pixels = np.zeros((GRID_SIZE, GRID_SIZE), dtype=np.float32)

        # Draw the initial grid
        self.draw_grid()

        # Bind mouse movement to drawing
        self.canvas.bind("<B1-Motion>", self.draw_pixel)

        # Buttons
        btn_clear = tk.Button(master, text="Clear", command=self.clear)
        btn_clear.pack()

        btn_predict = tk.Button(master, text="Predict", command=self.predict)
        btn_predict.pack()

        # Label for result
        self.label = tk.Label(master, text="", font=("Helvetica", 24))
        self.label.pack()

    def draw_grid(self):
        # Draw gray grid lines for 28x28 layout
        for i in range(GRID_SIZE + 1):
            pos = i * PIXEL_SIZE
            self.canvas.create_line(pos, 0, pos, HEIGHT, fill="lightgray")
            self.canvas.create_line(0, pos, WIDTH, pos, fill="lightgray")

    def draw_pixel(self, event):
        x, y = event.x // PIXEL_SIZE, event.y // PIXEL_SIZE
        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
            self.pixels[y, x] = 1.0  # Set pixel as black
            x1, y1 = x * PIXEL_SIZE, y * PIXEL_SIZE
            self.canvas.create_rectangle(
                x1, y1, x1 + PIXEL_SIZE, y1 + PIXEL_SIZE,
                fill="black", outline="gray"
            )

    def clear(self):
        self.pixels.fill(0)
        self.canvas.delete("all")
        self.draw_grid()
        self.label.config(text="")

    def predict(self):
        img = self.pixels.reshape(1, 28, 28, 1)
        pred = model.predict(img, verbose=0)
        self.label.config(text=f"Prediction: {np.argmax(pred)}")

# Launch the app
root = tk.Tk()
root.title("Digit Drawer (28x28 Pixel Grid)")
app = App(root)
root.mainloop()

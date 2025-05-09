from tensorflow.keras.datasets import mnist
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import TensorBoard
import datetime
import os

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize to [0, 1]
x_train = x_train / 255.0
x_test = x_test / 255.0

# Expand dimensions to match CNN input: (batch, 28, 28, 1)
x_train = x_train[..., None]
x_test = x_test[..., None]

# Build the CNN model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')  # 10 digits (0–9)
])

model.summary()

# Compile the model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Create log directory for TensorBoard
log_dir = "../logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

# Train the model with TensorBoard callback
model.fit(
    x_train, y_train,
    epochs=5,
    validation_split=0.1,
    callbacks=[tensorboard_callback]
)

# Evaluate model on test data
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {test_acc:.2f}")

model.save("digit_model.h5")
# Save the trained model
os.makedirs("../model", exist_ok=True)
model.save('../model/digit_model.h5')

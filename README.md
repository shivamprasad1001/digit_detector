# 🧠 Digit Detector - Handwritten Digit Recognition with CNN & GUI

![demo](https://user-images.githubusercontent.com/yourusername/demo.gif)

Digit Detector is a full-stack machine learning project that trains a Convolutional Neural Network (CNN) on the MNIST dataset to recognize handwritten digits. It also includes a real-time digit drawing interface built with Tkinter, bringing ML from model to user interaction.

---

## 🚀 Features

- ✅ Train a CNN model on MNIST digits
- ✅ Save and reuse the trained model (`.h5`)
- ✅ Predict digits from hand-drawn images in a GUI
- ✅ Clean project structure for reproducibility
- ✅ Real-world application demo using Python’s Tkinter

---

## 🏗️ Project Structure

```

digit-detector/
├── model/                   # Saved model goes here
│   └── digit\_model.h5
├── src/
│   ├── train.py             # Model training script
│   └── predict\_gui.py       # GUI prediction app
├── .gitignore
├── README.md
└── requirements.txt

````

---

## 🧠 Technologies Used

- TensorFlow / Keras
- NumPy
- PIL (Pillow)
- Tkinter (Python GUI)
- MNIST Dataset

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/digit-detector.git
````
```
cd digit-detector
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Train the Model

```bash
cd src
python train.py
```

Model will be saved to `model/digit_model.h5`.

### 4. Run the GUI Application

```bash
python predict_gui.py
```

---

## 📈 Model Summary

```text
Conv2D → MaxPool → Conv2D → MaxPool → Flatten → Dense(64) → Dense(10)
```

* Optimizer: `Adam`
* Loss: `Sparse Categorical Crossentropy`
* Accuracy: \~98% on test set

---

## 📂 Requirements

```
tensorflow
numpy
pillow
tk
```

---

## 🔍 Future Improvements

* Add web version using Streamlit or Flask
* Use a custom digit dataset for robustness
* Export predictions to CSV or Excel
* Upload model to Hugging Face or ONNX

---

## 🤝 Contributing

Pull requests are welcome! If you have suggestions or improvements, feel free to fork and open a PR.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgments

* [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)
* TensorFlow and Keras documentation

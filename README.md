# Digit Detector

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-brightgreen)
![TensorFlow](https://img.shields.io/badge/tensorflow-2.x-orange)

<p align="center">
  <img src="https://user-images.githubusercontent.com/yourusername/demo.gif" alt="Digit Detector Demo" width="550">
</p>

## Overview

Digit Detector is a comprehensive machine learning solution that leverages Convolutional Neural Networks (CNN) to recognize handwritten digits with high accuracy. Built on the MNIST dataset, this project combines advanced deep learning techniques with an intuitive GUI interface, providing a complete end-to-end implementation from model training to real-time user interaction.

## Key Features

- **Advanced CNN Architecture**: Multi-layer convolutional network optimized for digit recognition
- **Interactive GUI**: Real-time handwritten digit recognition via Tkinter drawing interface
- **Model Persistence**: Save and load trained models for immediate deployment
- **High Accuracy**: ~98% accuracy on the MNIST test dataset
- **Modular Design**: Clean separation between training and inference components

## Architecture

The project utilizes a sequential CNN architecture:

```
Input → Conv2D → MaxPooling2D → Conv2D → MaxPooling2D → Flatten → Dense(64) → Dense(10) → Output
```

### Model Parameters
- **Optimizer**: Adam
- **Loss Function**: Sparse Categorical Crossentropy
- **Performance**: ~98% accuracy on test set

## Project Structure

```
digit-detector/
├── model/                # Trained model storage
│   └── digit_model.h5
├── src/
│   ├── train.py          # CNN training implementation
│   └── predict_gui.py    # GUI application for inference
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/digit-detector.git
   cd digit-detector
   ```

2. **Create and activate a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training the Model

```bash
cd src
python train.py
```

The trained model will be automatically saved to `model/digit_model.h5`.

### Running the GUI Application

```bash
python predict_gui.py
```

This launches an interactive drawing canvas where you can:
- Draw digits using your mouse
- Submit for real-time recognition
- Clear the canvas to try new digits

## Dependencies

- TensorFlow 2.x
- NumPy
- Pillow (PIL)
- Tkinter

## Future Development Roadmap

- [ ] Web-based interface using Flask or Streamlit
- [ ] Support for extended character recognition (letters, symbols)
- [ ] Augmented training data for improved robustness
- [ ] Batch processing capabilities for image files
- [ ] Export functionality for prediction results

## Contributing

Contributions are welcome and appreciated. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code follows the project's style guidelines and includes appropriate tests.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- [MNIST Dataset](http://yann.lecun.com/exdb/mnist/) - The foundation for training data
- [TensorFlow Documentation](https://www.tensorflow.org/guide) - Deep learning framework
- [Keras Documentation](https://keras.io/documentation/) - High-level neural networks API

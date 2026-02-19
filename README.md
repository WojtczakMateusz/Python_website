# Project: MNIST Image Classification
# 1. Task Type

The objective of this project is the classification of handwritten digit images (0–9) using two neural networks with different levels of complexity.

# 2. Dataset

The MNIST dataset was used, containing 70,000 grayscale images with a resolution of 28×28 pixels.

Training set: 60,000 images

Test set: 10,000 images

The data was divided into training, validation, and test sets.

# 3. Architectures and Training Process
Model	Architecture	Epochs	Accuracy
Simple CNN	Conv2D + Dense	5	~98%
Advanced CNN	Conv2D + Data Augmentation	10	~99%

The Adam optimizer and the sparse_categorical_crossentropy loss function were used.

# 4. Conclusions

The advanced model achieved higher accuracy at the cost of longer training time.
Data augmentation improved the network’s robustness to image distortions.

#How to run:

Check your Python version: 
python --version 

Clone the repository 
git clone https://github.com/WojtczakMateusz/Python_website.git

Navigate to the project folder: 
cd YOUR_REPOSITORY

Run the application: 
python3 main.py





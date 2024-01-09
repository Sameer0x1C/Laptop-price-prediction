# Laptop Price Prediction Project

This project aims to predict the price of laptops based on various features. It utilizes a RandomForest machine learning model and is deployed using Streamlit.


## Output Screenshots
1. **Home Page**
    ![Home Page](outputs/index.png)

2. **Insert Data**
    ![Registration Form](outputs/insert.png)

3. **Update Data**
    ![Update Form](outputs/update.png)


## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Laptop Price Prediction Project is built to help users estimate the price of a laptop by providing specific details about the laptop, such as brand, type, RAM, weight, and other relevant features. The machine learning model, based on RandomForest, has been trained to make predictions.

## Installation
To run the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd laptop_price_prediction_project
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage
1. Select the brand, type, RAM, weight, and other features of the laptop.
2. Click the "Predict Price" button to get the predicted price.
3. The result will be displayed along with a celebratory balloon animation.

## Features
- Interactive user interface with Streamlit.
- Predict laptop price based on RandomForest machine learning model.
- Features include brand, type, RAM, weight, touchscreen, IPS display, screen size, screen resolution, processor, hard drive, SSD size, GPU, and operating system.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License
This project is licensed under the [MIT License](LICENSE).

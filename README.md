# 🌱 SmartCrop – AI-Based Crop Recommendation System

An intelligent web application that recommends the most suitable crop based on soil nutrients and environmental conditions using Machine Learning.

## 📌 Project Overview

SmartCrop is a machine learning-based crop recommendation system developed using Python and Flask. It analyzes soil and environmental parameters to predict the most suitable crop for cultivation.

The system uses a trained Machine Learning model to generate predictions and provides a visual representation of input parameters through interactive graphs.

## 🎯 Objectives

* Recommend suitable crops based on soil conditions.
* Analyze essential soil nutrients such as Nitrogen, Phosphorus, and Potassium.
* Evaluate environmental factors such as temperature, humidity, rainfall, and soil pH.
* Provide quick and accurate crop predictions.
* Present input data through a user-friendly web interface.

## 🛠️ Technologies Used

| Technology               | Purpose                                    |
| ------------------------ | ------------------------------------------ |
| Python                   | Backend programming                        |
| Flask                    | Web application framework                  |
| Machine Learning         | Crop prediction                            |
| Random Forest Classifier | Prediction model (if used during training) |
| HTML                     | Webpage structure                          |
| CSS                      | User interface design                      |
| JavaScript               | Interactive features                       |
| Joblib                   | Loading the trained ML model               |

## ⚙️ Input Parameters

The system accepts seven input parameters:

1. Nitrogen (N)
2. Phosphorus (P)
3. Potassium (K)
4. Temperature
5. Humidity
6. Soil pH
7. Rainfall

Based on these values, the trained model predicts a suitable crop.

## ✨ Features

* User-friendly web interface.
* Machine Learning-based crop prediction.
* Instant prediction results.
* Input parameter visualization.
* Model accuracy display.
* Responsive design.
* Real-time form submission using Flask.

## 📊 Model Performance

**Model Accuracy: 99.55%**

The application displays the model accuracy in its interface. This value should be interpreted as the measured accuracy on the evaluation dataset used during model development.

## 📁 Project Structure

```text
Crop_Recommendation_System/
│
├── app.py
├── crop_model.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
│── homepage.png
│── prediction.png
│
└── README.md
```

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AkhilBethamcharla-Lang/Crop_Recommendation_System.git
```

### 2. Navigate to the Project Directory

```bash
cd Crop_Recommendation_System
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

Visit:

```text
http://127.0.0.1:5000
```

Enter the soil and environmental parameters and click the Recommend button to view the predicted crop.

## 📸 Project Screenshots

### Homepage

![SmartCrop Homepage](screenshots/homepage.png)

### Crop Prediction Result

![Crop Prediction Result](screenshots/prediction.png)

## 🔮 Future Enhancements

* Integration of real-time weather data.
* Crop yield prediction.
* Fertilizer recommendation.
* Multilingual support.
* Deployment on a cloud hosting platform.
* Integration of additional machine learning algorithms.

## 👨‍💻 Developer

**Akhil Bethamcharla**

B.Tech – Computer Science and Engineering (AI & ML)

## 📜 License

This project is developed for educational and academic purposes.

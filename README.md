# Soil Nutrient Analysis with Automated Recommendation System

## 🌱 Project Overview

The Soil Nutrient Analysis with Automated Recommendation System is an IoT and Machine Learning based smart agriculture solution designed to monitor soil health and provide intelligent recommendations to farmers.

The system uses an ESP32 microcontroller connected to an NPK Soil Sensor to measure soil parameters such as Nitrogen (N), Phosphorus (P), Potassium (K), pH, temperature, moisture, and electrical conductivity (EC). The collected data is transmitted to a Flask-based web application where it is analyzed and displayed on a real-time dashboard.

The project also integrates an XGBoost Machine Learning model for crop recommendation and provides fertilizer suggestions based on soil nutrient deficiencies. Weather data can be obtained using the OpenWeatherMap API for rainfall-based analysis.

---

## 🚀 Features

* Real-time soil monitoring using ESP32.
* NPK, pH, moisture, temperature, and EC measurement.
* Flask-based web dashboard.
* Crop recommendation using XGBoost Machine Learning.
* Fertilizer recommendation system.
* Weather API integration for rainfall analysis.
* Live sensor data visualization.
* User-friendly web interface.

---

## 🛠 Hardware Components

* ESP32 Development Board
* NPK Soil Sensor (RS485 Modbus)
* MAX485 RS485 to TTL Converter
* Jumper Wires
* USB Cable
* Wi-Fi Network

---

## 💻 Software Technologies

* Python
* Flask
* HTML
* CSS
* JavaScript
* XGBoost
* NumPy
* OpenWeatherMap API
* Arduino IDE
* Git & GitHub

---

## 📂 Project Structure

```text
Project_Folder/
│
├── app.py
├── xgboost_soil_model.pkl
├── label_encoder.pkl
├── crop_ideal_values.json
│
└── templates/
    ├── index.html
    ├── mode1.html
    └── mode2.html
```

---

## 📄 File Description

### app.py

Main Flask application that:

* Receives data from ESP32.
* Stores sensor values.
* Provides API endpoints.
* Runs crop recommendation.
* Generates fertilizer recommendations.
* Integrates weather API.

### xgboost_soil_model.pkl

Trained XGBoost machine learning model used for crop prediction.

### label_encoder.pkl

Converts model prediction IDs into crop names.

### crop_ideal_values.json

Contains ideal NPK values used for fertilizer recommendation.

### templates/index.html

Main dashboard page showing real-time soil parameters.

### templates/mode1.html

Fertilizer recommendation page.

### templates/mode2.html

Crop recommendation page.

---

## ⚙️ Working Principle

1. NPK sensor measures soil parameters.
2. ESP32 reads sensor values using RS485 Modbus communication.
3. Data is converted into JSON format.
4. ESP32 sends data to the Flask server through Wi-Fi.
5. Flask stores the latest sensor readings.
6. Dashboard displays live soil information.
7. XGBoost model predicts the most suitable crop.
8. Fertilizer recommendation is generated using nutrient analysis.
9. Weather API provides rainfall information for improved recommendations.

---

## 🔄 System Workflow

```text
NPK Sensor
     │
     ▼
   ESP32
     │
     ▼
 Flask Server
     │
 ┌───┴───────────┐
 ▼               ▼
Mode 1       Mode 2
(Fertilizer) (Crop Recommendation)
     │               │
     ▼               ▼
 Recommendation   XGBoost Model
     │               │
     └───────┬───────┘
             ▼
       Web Dashboard
```

---

## 🤖 Machine Learning Model

### Algorithm Used

* XGBoost Classifier

### Input Features

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH
* Rainfall

### Output

* Recommended Crop

---

## 🌾 Applications

* Smart Agriculture
* Precision Farming
* Soil Health Monitoring
* Crop Recommendation Systems
* Fertilizer Optimization
* Agricultural Research

---

## 🔮 Future Enhancements

* Mobile Application
* Cloud Database Integration
* Historical Data Storage
* SMS Alerts
* AI-based Disease Detection
* Multi-Sensor Support

---

## 👥 Team Members

This project was developed as a Bachelor of Engineering group project.

* Dewang Korgaonkar
* Suyash Morye
* Sarthak Parab
* Aryan Gaonkar

---

## 👨‍💻 My Contributions

* ESP32 and NPK Sensor Integration
* Flask Backend Development
* API Development
* Real-Time Dashboard Integration
* GitHub Repository Management
* Machine Learning Model Integration

---

## 📚 Academic Information

**Project Title:** Soil Nutrient Analysis with Automated Recommendation System

**College:** Finolex Academy of Management and Technology

**Degree:** Bachelor of Engineering (Electronics & Telecommunication)

---

## 📜 License

This project is intended for educational and research purposes.

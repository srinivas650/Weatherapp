<<<<<<< HEAD
🌦️ Django Weather App
A simple Django web application that allows users to enter a city name and get real-time weather information using the OpenWeatherMap API.

🔧 Features
🌍 Get current weather by city name
🌡️ Displays:
City & Country
Temperature
Weather Condition
Humidity
Timezone
❗ Shows a user-friendly error if the city is not found
🎨 Beautiful, responsive UI with inline CSS
🔐 CSRF protection built-in (via Django)
📸 Screenshot
(Optional) Add a screenshot of your weather app UI here
Example:
![Weather App Screenshot](screenshot.png)

🚀 How to Run the Project
1. Clone the Repository
=======
# 🌦️ Django Weather App

A simple Django web application that allows users to enter a city name and get real-time weather information using the **OpenWeatherMap API**.

---

## 🔧 Features

- 🌍 Get **current weather** by city name  
- 🌡️ Displays:
  - City & Country  
  - Temperature  
  - Weather Condition  
  - Humidity  
  - Timezone  
- ❗ Shows a user-friendly error if the city is not found  
- 🎨 Beautiful, responsive UI with inline CSS  
- 🔐 CSRF protection built-in (via Django)

---

## 📸 Screenshot

> *(Optional)* Add a screenshot of your weather app UI here  
> Example:  
> `![Weather App Screenshot](screenshot.png)`

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
>>>>>>> 2b090b5059903fcd2df3524a00cf8aa59be77623
git clone https://github.com/your-username/weather-app.git
cd weather-app
## TO run the Project
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
pip install django requests
URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY
<<<<<<< HEAD
python manage.py runserver
=======
python manage.py runserver

>>>>>>> 2b090b5059903fcd2df3524a00cf8aa59be77623

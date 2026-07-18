# 🌦️ Weather Data App

A simple Python application that fetches real-time weather information for any city using the OpenWeather API.

---

## ✨ Features

- 🌍 Search weather by city name
- 🌡️ Current temperature (°C)
- 🤗 Feels like temperature
- 💧 Humidity
- 🌬️ Wind speed
- 🌅 Sunrise time
- 🌇 Sunset time
- ❌ Handles invalid city names
- 🌐 Handles internet connection errors
- 🔒 API key stored securely using `.env`

---

## 🛠️ Technologies Used

- Python 3
- Requests
- Python-dotenv
- OpenWeather API

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/jiya2k07-cyber/weather-data-app.git
```

Move into the project folder:

```bash
cd weather-data-app
```

Install the required libraries:

```bash
pip install requests
pip install python-dotenv
```

---

## ⚙️ Setup

Create a `.env` file in the project folder.

```env
API_KEY=your_openweather_api_key
```

You can get your free API key from:

https://openweathermap.org/api

---

## ▶️ Run the Project

```bash
python weather.py
```

---

## 📂 Project Structure

```
weather-data-app/
│
├── weather.py
├── README.md
├── sample_output.txt
├── .gitignore
└── .env (not uploaded)
```

---

## 📸 Sample Output

```
----------- WEATHER REPORT -----------

🌍 City: Delhi
🌡️ Temperature: 34°C
🤗 Feels Like: 37°C
💧 Humidity: 62%
🌬️ Wind Speed: 4.2 m/s
🌅 Sunrise: 05:32 AM
🌇 Sunset: 07:18 PM
☁️ Weather: Clear Sky
```

---

## 📚 Concepts Learned

- APIs
- JSON Parsing
- Requests Library
- Environment Variables
- Error Handling
- Exception Handling
- Python Modules
- Git & GitHub

---

## 👩‍💻 Author

**Jiya Gupta**

GitHub:
https://github.com/jiya2k07-cyber

---
⭐ If you like this project, feel free to star the repository!

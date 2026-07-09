# 🌦️ Weather AI Assistant

An AI-powered weather application built with **Python, Streamlit, OpenWeather API, and OpenAI API**.
This application provides real-time weather information and generates an AI-based weather summary to help users understand current conditions.

## 🚀 Features

* 🌡️ Real-time temperature information
* 💧 Humidity percentage
* 🌬️ Wind speed details
* ☁️ Current weather condition
* 🤖 AI-generated weather summary
* 🖥️ Interactive Streamlit web interface
* 🔐 Secure API key management using environment variables

## 🛠️ Tech Stack

* **Python**
* **Streamlit** - Web application framework
* **OpenWeather API** - Real-time weather data
* **OpenAI API** - AI weather analysis
* **python-dotenv** - Environment variable management

## 📂 Project Structure

```text
Weather-App-Streamlit-OpenAi/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Project dependencies
├── .gitignore              # Ignored files
├── .env                    # API keys (not uploaded)
└── README.md               # Documentation
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/GavinBedi/Weather-App-Streamlit-OpenAi.git
```

### 2. Navigate to project folder

```bash
cd Weather-App-Streamlit-OpenAi
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file in the project directory:

```env
OPENWEATHER_API_KEY=your_openweather_api_key
OPENAI_API_KEY=your_openai_api_key
```

Replace the values with your own API keys.

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

## 🔒 Security

* API keys are stored securely using environment variables.
* `.env` file is excluded from GitHub using `.gitignore`.
* Never upload API keys publicly.

## 📸 Screenshots





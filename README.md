# Coursera_Building-Gen-AI-Powered-Applications

🧠 This repository is my personal workspace for following the course **"Building Generative AI Powered Applications"** on Coursera.  
[Course link](https://www.coursera.org/learn/building-gen-ai-powered-applications)

---

## Prerequisites

- Python 3.8 or higher installed  
- Git (optional, to clone the repo)  
- (Recommended) Use a virtual environment to manage dependencies  

---

## Setup Instructions

### 1. Clone the repository 

```bash
git clone https://github.com/YourUsername/Coursera_Building-Gen-AI-Powered-Applications.git
```

### 2. Create and activate a virtual environment

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

---

### 3. Install dependencies

Dependencies will be listed in the `requirements.txt` file as they are added.

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file (if needed)

You may need to create a `.env` file in the root directory to configure API keys or runtime settings:

```
OPENAI_API_KEY=your-openai-key
ENV=development
```

---

### 5. Run the application

Instructions for running the app will be provided as the project evolves.

---

## Application Modules

TODO

---

### Module 2: Create Your Own CatGPT-Like Website

The most recent additions and developments for the chatbot web application are located in the
`Module2_CreateYourOwnCatGPT-LikeWebsite/` folder.

#### Overview

This module demonstrates how to integrate a Flask backend chatbot with a frontend template website.

#### Project Structure in `Module2_CreateYourOwnCatGPT-LikeWebsite`

```
Module2_CreateYourOwnCatGPT-LikeWebsite/
│
├── LLM_application_chatbot/
│   ├── app.py               # Flask backend application serving chatbot API and frontend
│   ├── static/              # Static frontend assets (JavaScript, CSS, images)
│   └── templates/           # HTML templates, including index.html for chatbot UI
│
├── requirements.txt         # Dependencies required for this module
└── ...
```

#### Setup Instructions

1. Clone the template repository for the chatbot website:

```bash
git clone https://github.com/ibm-developer-skills-network/LLM_application_chatbot
```

2. Install required Python packages:

```bash
python3.11 -m pip install -r Module2_CreateYourOwnCatGPT-LikeWebsite/LLM_application_chatbot/requirements.txt
```

3. Move your `app.py` Flask application into the `LLM_application_chatbot/` folder inside the module directory.

4. Navigate to the `LLM_application_chatbot/` folder:

```bash
cd Module2_CreateYourOwnCatGPT-LikeWebsite/LLM_application_chatbot/
```

5. Run the Flask app:

```bash
flask run
```

6. Open your browser and visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the chatbot frontend.

#### Important Notes

* The Flask app now serves the chatbot frontend (`index.html`) at `/`.
* The frontend JavaScript in `static/script.js` is configured to send user messages to the `/chatbot` endpoint on the Flask backend.
* Ensure the Flask server is running before interacting with the chatbot UI.

---


## Notes

- Always **activate your virtual environment** before working on the project.  
- Use the `.env` file for environment-specific settings.  
- To stop the app or server, use `Ctrl+C` in the terminal.  

---

## License

This project is for educational purposes, based on the Coursera course content.

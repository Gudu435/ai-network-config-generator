# 🤖 AI Network Config Generator

An AI-powered web application that converts natural language into Cisco IOS CLI configurations.

---

## 🚀 Features

- Natural Language → CLI conversion  
- Web-based interface (Flask)  
- Safety validation (blocks dangerous commands)  
- Lightweight and easy to deploy  

---

## 🏗️ Architecture Diagram

[Architecture Diagram](https://github.com/Gudu435/ai-network-config-generator/blob/main/architecture-diagram.png.png)

---

## 🧠 How It Works

1. User enters request in web UI  
2. Flask backend processes input  
3. OpenAI API generates Cisco CLI  
4. Safety filter validates commands  
5. Output displayed in browser  

---

## ⚙️ Prerequisites

- Python 3 installed
If Not installed
	```winget install Python.Python.3
	python --version
	pip --version
```
---

## 📦 Installation

### 1) Clone the repository

```bash
git clone https://github.com/Gudu435/ai-network-config-generator.git
cd ai-network-config-generator
```

### 2) Install dependencies

```pip install -r requirements.txt```

### 3) For Linux
``` export OPENAI_API_KEY="your_api_key" ```

**OR**

### 4) Windows (PowerShell)
```setx OPENAI_API_KEY "your_api_key" ```

### 5) ▶️ Run Application
```python3 app.py```

# 🤖 Simple LLM Install

**Simple LLM Install** is a Python-based tool that helps you easily run and chat with **local Large Language Models (LLMs)** using **Ollama**.
No cloud, no API keys — everything runs locally on your machine.

---

## 🚀 Features

- ✅ Check if Ollama is installed
- ✅ Automatically detect if Ollama service is running
- 📥 Download LLM models from Ollama
- 📋 List available local models
- 💬 Simple interactive chat interface
- 🔒 Fully local & privacy-friendly

---

## 🛠 Prerequisites

### 1️⃣ Python 3.8+
```bash
python --version
```

### 2️⃣ Ollama Installed
Download from: https://ollama.ai/

**Install commands**
- **Windows**: Use the installer from the website
- **macOS**:
```bash
brew install ollama
```
- **Linux**:
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

---

## ▶️ Getting Started

### Clone the repository
```bash
git clone https://github.com/pankajjjat/simple-llm-install.git
cd simple-llm-install
```

### Install dependencies
```bash
pip install requests
```

### Start Ollama
```bash
ollama serve
```

### Run the app
```bash
python main.py
```

---

## 📦 Popular Models

| Model | Use Case | Approx Size |
|------|---------|-------------|
| llama2 | General chat | ~3.8GB |
| mistral | Fast & efficient | ~4.1GB |
| codellama | Coding assistant | ~3.8GB |
| llama2:13b | Advanced reasoning | ~7.3GB |

Download example:
```bash
ollama pull llama2
```

---

## 💬 Chat Commands

- `quit` → Exit chat
- `models` → Show available models

---

## 📁 Project Structure

```text
simple-llm-install/
│
├── main.py
├── README.md
├── .gitignore
└── LICENSE
```

---

## 🔐 Privacy

- 100% local execution
- No API keys
- No data tracking

---

## 📄 License

Licensed under the **MIT License**.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

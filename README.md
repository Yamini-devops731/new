# 🚀 AI-Powered CI/CD Failure Analyzer (Jenkins + LLM)

## 📌 Overview

This project demonstrates an AI-driven approach to improving CI/CD pipelines by automatically analyzing build failures and suggesting fixes using Large Language Models (LLMs).

The system integrates Jenkins with an LLM-based log analyzer to reduce manual debugging effort and accelerate issue resolution.

---

## 🎯 Key Features

* 🔍 Automatic detection of CI/CD pipeline failures
* 🤖 AI-based log analysis using LLM
* 🧠 Root cause identification and fix suggestions
* ⚙️ Jenkins pipeline integration
* 🐳 Docker-based application build
* ☁️ Deployable on AWS EC2 (Free Tier compatible)

---

## 🧱 Architecture

Jenkins Pipeline
→ Build & Failure
→ Log Collection
→ Python Script
→ LLM API
→ Root Cause + Fix Suggestion

---

## 🛠️ Tech Stack

* Jenkins (CI/CD)
* Docker
* Python
* LLM API (OpenAI)
* Node.js (sample microservice)
* AWS EC2

---

## 📂 Project Structure

```
project/
├── app/
│   ├── app.js
│   ├── package.json
│   └── Dockerfile
├── Jenkinsfile
├── analyze_logs.py
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1️⃣ Launch EC2 Instance

* Ubuntu (Free Tier)
* Open ports: 22, 8080

---

### 2️⃣ Install Dependencies

```bash
sudo apt update
sudo apt install docker.io python3-pip -y
pip3 install -r requirements.txt
```

---

### 3️⃣ Run Jenkins (Docker)

```bash
docker run -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
```

---

### 4️⃣ Configure Jenkins

* Access: `http://<EC2-IP>:8080`
* Install plugins
* Add credential:

  * Type: Secret Text
  * ID: `openai-key`
  * Value: Your API Key

---

### 5️⃣ Create Pipeline Job

* Connect GitHub repository
* Use Jenkinsfile from repo

---

### 6️⃣ Run Pipeline

* Build will fail intentionally
* AI analyzer will trigger automatically

---

## 🤖 AI Log Analysis

The system:

1. Captures failure logs
2. Sends logs to LLM
3. Returns:

   * Root cause
   * Suggested fix

---

## 💡 Example Output

```
Root Cause:
Missing dependency in Dockerfile

Suggested Fix:
Add required package installation step in Dockerfile
```

---

## 🚀 Future Enhancements

* 🔔 Slack/Teams notifications
* 🔄 Auto-remediation (restart jobs/pods)
* 📊 Integration with monitoring tools
* 🧠 Advanced LLM workflows using LangChain

---

## 🎯 Use Case

This project demonstrates how AI can transform DevOps by:

* Reducing manual debugging
* Improving CI/CD efficiency
* Enabling intelligent automation

---

## 👨‍💻 Author

DevOps Engineer with hands-on experience in CI/CD, Kubernetes, AWS, and Infrastructure Automation.

---

## ⭐ Key Takeaway

"Moving from reactive DevOps to proactive AI-driven DevOps using LLMs."


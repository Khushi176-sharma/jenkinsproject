# jenkinsproject
🚀 Flask App with Jenkins CI/CD & Docker
Hi there! 👋

This is a simple Python Flask application, set up with Jenkins CI/CD pipeline and Docker support. If you're exploring how to automate your development-to-deployment workflow, this project is a great place to start!

📁 What’s Inside
flask-ci-cd-demo/
├── app.py             # Flask app code
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker image setup
├── Jenkinsfile        # CI/CD pipeline config
└── README.md          # You’re reading it!
💡 Features
Simple & clean Flask app
Docker container ready
Jenkins pipeline for automated:
Code checkout
Unit testing with pytest
Docker image build + tag
Push to container registry
Deployment with health-check
🧪 How to Run Locally
Make sure you have Python installed, then:

C:\Users\khushi> pip install -r requirements.txt

Now visit: (['http://localhost:8080/'])

🐳 Want to Use Docker?
No problem! Just run:

docker build -t flask-app:dev .
docker run -d -p 8000:8000 --name flask flask-app:dev
⚙️ Jenkins Pipeline in Action
Your Jenkinsfile automates the full workflow:

Pulls the latest code
Installs dependencies
Runs tests
Builds Docker image with version tag
Pushes image to Docker Hub or GHCR
Replaces any existing container
Runs a simple health check on No more manual deployments! 🚀
🔐 Image Registry Setup
You can push to:

Docker Hub (docker.io/)
GitHub Container Registry (ghcr.io/Khushi176-sharma/)
🧠 Health Check Route
Use this route to confirm the app is running:

GET /health
Response:

{"status": "ok"}
👨‍💻 Made By
Developed by Khushi Sharma

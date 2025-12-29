# 🔭 DevOps Kubernetes Observability Platform

This repository contains a **complete DevOps workflow** for a Flask application deployed on Kubernetes, with **CI/CD, monitoring, logging, and alerting** built in.

The goal of this project is to demonstrate how a real-world application is:
- Built and containerized
- Deployed to Kubernetes
- Observed using metrics and logs
- Monitored with alerts
- Automated using CI/CD

---

## 🧱 What’s Inside This Repository
.
├── app/ # Flask application source code
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── k8s/ # Kubernetes manifests
│ ├── deployment.yaml
│ ├── service.yaml
│ └── flask-alerts.yaml
│
├── logging/ # Logging stack (EFK)
│ ├── fluent-bit.yaml
│ ├── fluentbit-config.yaml
│ ├── elasticsearch.yaml
│ ├── elasticsearch-service.yaml
│ ├── kibana.yaml
│ └── kibana-service.yaml
│
├── ci/
│ └── concourse/ # Concourse CI/CD setup
│ ├── pipeline.yml
│ └── docker-compose.yaml
│
├── .gitignore
└── README.md


---


- Flask app exposes:
  - `/health` for health checks
  - `/metrics` for Prometheus
- CI pipeline builds and pushes Docker images
- Kubernetes runs the application
- Prometheus scrapes metrics
- Alertmanager triggers alerts
- Fluent Bit ships logs to Elasticsearch
- Kibana visualizes logs

---

##  Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/devops-k8s-observability.git
cd devops-k8s-observability

2️⃣ Run the Flask App Locally (Optional)
cd app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py


Test locally:

curl http://localhost:5000/health
curl http://localhost:5000/metrics

3️⃣ Build and Run with Docker (Local Test)
cd app
docker build -t flask-login-app:local .
docker run -p 5000:5000 flask-login-app:local

 Kubernetes Deployment
4️⃣ Deploy the Application

Make sure your Kubernetes cluster is running and kubectl is configured.

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml


Verify:

kubectl get pods
kubectl get svc

5️⃣ Deploy Monitoring (Prometheus & Grafana)

Assumes Prometheus stack is already installed (e.g., via Helm)

The Flask app exposes /metrics, which Prometheus scrapes automatically.

Verify metrics:

kubectl port-forward svc/flask-login 5000:5000
curl http://localhost:5000/metrics

6️⃣ Apply Alert Rules
kubectl apply -f k8s/flask-alerts.yaml


Example alerts include:

Application down

High request error rate

Latency issues

 Logging (EFK Stack)
7️⃣ Deploy Logging Stack
kubectl apply -f logging/elasticsearch.yaml
kubectl apply -f logging/elasticsearch-service.yaml

kubectl apply -f logging/kibana.yaml
kubectl apply -f logging/kibana-service.yaml

kubectl apply -f logging/fluent-bit.yaml
kubectl apply -f logging/fluentbit-config.yaml


What happens:

Fluent Bit reads container logs

Logs are sent to Elasticsearch

Kibana visualizes logs

Access Kibana:

kubectl port-forward svc/kibana 5601:5601

 What Logs You Can See

The Flask app logs structured events like:

{
  "event": "login_failure",
  "username": "test"
}


These fields are searchable and visualizable in Kibana.

🔁 CI/CD Pipeline (Concourse)
8️⃣ Start Concourse
cd ci/concourse
docker compose up -d


Access UI:

http://localhost:8080

9️⃣ Set the Pipeline
fly -t local login -c http://localhost:8080
fly -t local set-pipeline -p flask-login-ci -c pipeline.yml
fly -t local unpause-pipeline -p flask-login-ci


Pipeline stages:

Fetch code from GitHub

Build Docker image

Push image to registry

Deploy to Kubernetes

Apply alerts

Verify observability endpoints

 Verification Checklist

After everything is up, you should be able to:

 Access Flask /health

 View /metrics in Prometheus

 See alerts in Alertmanager

 View logs in Kibana

 See pipeline runs in Concourse

 What This Project Demonstrates

Real-world CI/CD workflow

Kubernetes-native deployment

Metrics-based monitoring

Log aggregation and analysis

Alerting on application behavior

Debugging using observability data

 Possible Improvements

Helm charts for all components

Canary or blue-green deployments

Tracing with OpenTelemetry

Secrets management with Vault

GitOps using Argo CD

 Author

Built as a hands-on DevOps learning project focused on practical, production-relevant skills.

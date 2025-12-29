# 🔭 DevOps Kubernetes Observability Platform

This repository contains a **complete DevOps workflow** for a Flask application deployed on Kubernetes, with **CI/CD, monitoring, logging, and alerting** built in.

The goal of this project is to demonstrate how a real-world application is:
- Built and containerized
- Deployed to Kubernetes
- Observed using metrics and logs
- Monitored with alerts
- Automated using CI/CD

---

## 🧱 Repository Structure

```text
.
├── app/                     # Flask application source code
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── k8s/                     # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   └── flask-alerts.yaml
│
├── logging/                 # Logging stack (EFK)
│   ├── fluent-bit.yaml
│   ├── fluentbit-config.yaml
│   ├── elasticsearch.yaml
│   ├── elasticsearch-service.yaml
│   ├── kibana.yaml
│   └── kibana-service.yaml
│
├── ci/
│   └── concourse/           # Concourse CI/CD setup
│       ├── pipeline.yml
│       └── docker-compose.yaml
│
├── .gitignore
└── README.md

# ♾️ DevOps Engineer Roadmap (15 Months)

This detailed roadmap transforms you from a novice to a production-ready DevOps Engineer over 15 months. It covers the full lifecycle of software development and operations.

---

## Phase 1: Foundation (Month 1-2)

**Focus:** Mastering the Operating System and Networking.

### 📋 Prerequisites

* Basic understanding of how computers work (CPU, RAM, Disk).
* Ability to use a computer terminal.

### 🛠️ Tools to Master

* **Linux:** Ubuntu/CentOS (File system, Permissions, Package Management).
* **Shell:** Bash scripting.
* **Git:** Branching, Merging, Rebasing, Pull Requests.
* **Networking:** SSH, cURL, ping, telnet, netstat.

### 📖 Concepts

* **OS Fundamentals:** Process management, Threads, Concurrency, Virtualization.
* **Networking:** OSI Model, TCP/IP, DNS, HTTP/HTTPS, Firewalls, Subnetting.
* **Version Control:** Git Flow vs. Trunk Based Development.

### 🧪 Hands-On Labs

1. **Linux Server Setup:** Install Ubuntu Server (or use a VM), set up SSH keys, configure a firewall (UFW), and create users with specific sudo permissions.
2. **Bash Automation:** Write a script that checks disk space usage every hour and logs it to a file.
3. **Git Conflict Resolver:** Create a repository, create a branch, modify the same line in both branches, and successfully merge/resolve the conflict.

### 📚 Resources

* **Official Docs:** [Linux Command Line](https://linuxcommand.org/), [Git SCM](https://git-scm.com/doc)
* **Courses:** [Udacity - Linux Command Line Basics](https://www.udacity.com/course/linux-command-line-basics--ud595)
* **Practice:** [OverTheWire (Bandit)](https://overthewire.org/wargames/bandit/)

### 🏆 Certifications to Consider (Optional)

* CompTIA Linux+ / LPIC-1

### ✅ By End of This Phase

You should be comfortable navigating Linux servers via SSH and troubleshooting network connectivity issues.

---

## Phase 2: Programming & Scripting (Month 3-4)

**Focus:** Automating usage tasks and interacting with APIs.

### 📋 Prerequisites

* Phase 1 completion.

### 🛠️ Tools to Master

* **Language:** Python 3 (Boto3 library).
* **Formats:** YAML, JSON.
* **Tools:** jq (JSON processor), Postman.

### 📖 Concepts

* **Automation:** "If you do it twice, automate it."
* **Data Structures:** Lists, Dictionaries (crucial for JSON).
* **APIs:** RESTful architecture, Authentication (Keys, Tokens).
* **Regex:** Pattern matching for log parsing.

### 🧪 Hands-On Labs

1. **Log Parser:** Write a Python script to parse an Apache/Nginx access log and count 404 errors.
2. **API Interactor:** Write a script that fetches the weather from an API and saves a YAML summary.
3. **Config Generator:** Create a script that reads a JSON input and generates a configuration file.

### 📚 Resources

* **Official Docs:** [Python 3 Docs](https://docs.python.org/3/)
* **Courses:** [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

### ✅ By End of This Phase

You should be able to write scripts that interact with the OS and external web services.

---

## Phase 3: Infrastructure as Code (Month 5-6)

**Focus:** Treating infrastructure like software.

### 📋 Prerequisites

* Basic programming knowledge (variables, loops).
* Cloud account (AWS Free Tier).

### 🛠️ Tools to Master

* **Terraform:** HCL syntax, State files, Backends.
* **AWS CloudFormation:** Templates (optional but good to know).

### 📖 Concepts

* **IaC:** Declarative vs. Imperative.
* **Immutability:** Immutable infrastructure paradigm.
* **State Management:** Handling `terraform.tfstate` securely.
* **Modules:** DRY (Don't Repeat Yourself) infrastructure.

### 🧪 Hands-On Labs

1. **3-Tier Arch:** Use Terraform to provision a VPC, Public/Private Subnets, an EC2 instance, and an RDS database.
2. **State Locking:** Configure S3 backend with DynamoDB locking for Terraform.
3. **Module Creation:** Create a reusable module for an S3 bucket with specific encryption policies.

### 📚 Resources

* **Official Docs:** [Terraform Documentation](https://developer.hashicorp.com/terraform/docs)
* **Courses:** [HashiCorp Learn](https://developer.hashicorp.com/terraform/tutorials)

### 🏆 Certifications to Consider

* HashiCorp Certified: Terraform Associate

### ✅ By End of This Phase

You should be able to spin up and destroy a complete environment with a single command (`terraform apply`).

---

## Phase 4: Containerization (Month 7-8)

**Focus:** Packaging applications for consistency.

### 📋 Prerequisites

* Linux fundamentals (cgroups, namespaces).

### 🛠️ Tools to Master

* **Docker:** Dockerfile, CLI, Compose.
* **Registry:** Docker Hub / AWS ECR.
* **Scanning:** Trivy (security).

### 📖 Concepts

* **Virtualization vs. Containerization.**
* **Layers:** Image layering and caching strategy.
* **Networking:** Bridge, Host, Overlay networks.
* **Multi-stage Builds:** optimizing image size.

### 🧪 Hands-On Labs

1. **Dockerize App:** Take a Python/Node.js app and write an optimized Dockerfile (multistage).
2. **Compose Stack:** Run a web app + Redis + Database using `docker-compose.yml`.
3. **Security Scan:** Integrate Trivy to scan your image for vulnerabilities.

### 📚 Resources

* **Official Docs:** [Docker Docs](https://docs.docker.com/)
* **Courses:** [Docker Mastery (Udemy/YouTube)](https://www.youtube.com/watch?v=fqMOX6JJhGo)

### ✅ By End of This Phase

You should strictly avoid installing runtimes (Node, Python) directly on your host machine—containerize everything!

---

## Phase 5: Orchestration (Month 9-10)

**Focus:** Managing containers at scale.

### 📋 Prerequisites

* Docker mastery.

### 🛠️ Tools to Master

* **Kubernetes (K8s):** Kubectl, Minikube/Kind.
* **Helm:** Package manager for K8s.

### 📖 Concepts

* **Architecture:** Control Plane vs. Worker Nodes.
* **Resources:** Pods, Deployments, Services (ClusterIP, NodePort, LoadBalancer), Ingress.
* **Config:** ConfigMaps & Secrets.
* **Self-Healing:** Liveness and Readiness probes.

### 🧪 Hands-On Labs

1. **Local Cluster:** Set up Minikube and deploy the app from Phase 4.
2. **Rolling Update:** Perform a zero-downtime update of your application image.
3. **Helm Chart:** Create a simple Helm chart for your application.

### 📚 Resources

* **Official Docs:** [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
* **Courses:** [KubeAcademy by VMware](https://ubeacademy.vmware.com/)

### 🏆 Certifications to Consider

* CKAD (Certified Kubernetes Application Developer)

### ✅ By End of This Phase

You should be able to deploy complex microservices architectures on a Kubernetes cluster.

---

## Phase 6: CI/CD Pipelines (Month 11-12)

**Focus:** Automating the delivery pipeline.

### 📋 Prerequisites

* Git, Shell Scripting, Docker.

### 🛠️ Tools to Master

* **CI Tools:** Jenkins (Classic), GitHub Actions (Modern), GitLab CI.
* **Pipeline as Code:** Jenkinsfile, .gitlab-ci.yml.

### 📖 Concepts

* **CI vs CD:** Continuous Integration vs. Continuous Delivery vs. Deployment.
* **Strategies:** Blue/Green, Canary, Rolling updates.
* **Artifacts:** Storing build outputs.

### 🧪 Hands-On Labs

1. **Simple CI:** Create a GitHub Action that runs linting and unit tests on every Push.
2. **Docker Build & Push:** Pipeline that builds a docker image and pushes to Docker Hub with the commit SHA tag.
3. **CD to K8s:** Pipeline that updates a K8s deployment manifest when a new image is pushed.

### 📚 Resources

* **Official Docs:** [GitHub Actions Docs](https://docs.github.com/en/actions)
* **Practice:** [Jenkins X](https://jenkins-x.io/)

### ✅ By End of This Phase

You should be able to commit code and watch it automatically deploy to a staging environment.

---

## Phase 7: Cloud Platforms (Month 13-14)

**Focus:** Managing production-grade infrastructure.

### 📋 Prerequisites

* Networking, IaC.

### 🛠️ Tools to Master

* **AWS:** EC2, S3, VPC, RDS, IAM, Route53, EKS.
* *(Alternative: Azure or GCP).*

### 📖 Concepts

* **Shared Responsibility Model.**
* **IAM:** Least Privilege Principle.
* **Well-Architected Framework:** Security, Reliability, Performance, Cost, Operations.
* **Serverless:** Lambda functions.

### 🧪 Hands-On Labs

1. **Secure VPC:** Build a VPC with public/private subnets and a NAT Gateway.
2. **S3 Hosting:** Host a static website on S3 with CloudFront CDN.
3. **IAM Policy:** Create a user that can *only* read from a specific S3 bucket.

### 📚 Resources

* **Official Docs:** [AWS Documentation](https://docs.aws.amazon.com/)
* **Courses:** [AWS Skill Builder](https://explore.skillbuilder.aws/)

### 🏆 Certifications to Consider

* AWS Certified Solutions Architect – Associate

### ✅ By End of This Phase

You should understand how to design scalable and secure cloud architectures.

---

## Phase 8: Monitoring & Observability (Month 15)

**Focus:** Knowing when something is wrong before the customer does.

### 📋 Prerequisites

* Systems running in K8s/Cloud.

### 🛠️ Tools to Master

* **Metrics:** Prometheus & Grafana.
* **Logging:** ELK Stack (Elasticsearch, Logstash, Kibana) or Loki.
* **Tracing:** Jaeger.

### 📖 Concepts

* **Observability:** Logs vs. Metrics vs. Traces.
* **SLIs, SLOs, SLAs.**
* **Alerting:** PagerDuty integration, avoiding alert fatigue.
* **RED Method:** Rate, Errors, Duration.

### 🧪 Hands-On Labs

1. **Dashboarding:** Install Prometheus/Grafana on K8s and import a dashboard to monitor node resources.
2. **Logging:** Set up Fluentd to collect container logs and send them to Elasticsearch.
3. **Alerts:** Configure an alert to fire if CPU usage > 80% for 5 minutes.

### 📚 Resources

* **Official Docs:** [Prometheus Docs](https://prometheus.io/docs/introduction/overview/)
* **Book:** Site Reliability Engineering (Google).

### ✅ By End of This Phase

You should have visibility into the health and performance of your applications.

---

## 🧭 DevOps Culture & Career

### 🤝 DevOps Culture

* **Collaboration:** Breaking down silos between Dev and Ops.
* **Feedback Loops:** Faster failures, faster fixes.
* **Continuous Improvement:** Kaizen.

### 🏠 Building a Home Lab

* **Hardware:** Raspberry Pi cluster or old laptop.
* **Software:** Proxmox, Portainer, Pi-hole.
* **Goal:** Break things safely.

### 🎤 Interview Preparation

* **Scenario Questions:** "The site is down 5 minutes before Black Friday sale. What do you do?"
* **Whiteboarding:** Draw a CI/CD pipeline or a 3-tier architecture.
* **Troubleshooting:** "I can't SSH into this server. Walk me through your debugging process."

### 🌐 Open Source

* Contribute documentation fixes to projects like Terraform, Kubernetes, or smaller tools you use.

---

*Last Updated: 2026-03-29*

![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat&logo=terraform&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat&logo=githubactions&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazonaws&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white)

## 💰 Salary & Job Market

* **Median Salary (US):** $100,000–$150,000/year (Junior to Mid-level)
* **Senior DevOps / Platform Engineer:** $150,000–$220,000+
* **Top Hiring Companies:** Amazon, Google, Microsoft, Netflix, Cloudflare, HashiCorp, and any company running significant cloud infrastructure
* **In-Demand Skills:** Kubernetes, Terraform, AWS/GCP/Azure, CI/CD pipelines, Docker, Python scripting, observability (Prometheus/Grafana), security (DevSecOps)
* **Job Market Note:** DevOps and Platform Engineering are among the highest-paying engineering roles. The shift toward "Platform Engineering" means strong Kubernetes and IaC skills command premium salaries.

## ⚠️ Common Mistakes

1. **Treating DevOps as just tooling** — DevOps is a culture and set of practices, not just a collection of tools. Engineers who focus only on learning Kubernetes without understanding CI/CD philosophy, feedback loops, and collaboration principles miss the point and struggle in interviews.
2. **Skipping Linux fundamentals** — Many DevOps learners jump straight to Kubernetes without solid Linux and networking foundations. When a pod fails to start or a network policy blocks traffic, you need to be able to debug at the OS level.
3. **Neglecting security** — DevSecOps is not optional. Misconfigured IAM roles, exposed secrets in environment variables, and unscanned container images are the most common causes of cloud security incidents. Build security practices into every pipeline from the start.

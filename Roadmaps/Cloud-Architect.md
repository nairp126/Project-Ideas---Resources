# ☁️ Cloud Architect Roadmap (18 Months)

This roadmap guides you from IT basics to a strategic Cloud/Solutions Architect role over 18 months, with a primary focus on **AWS** (while referencing Azure/GCP).

---

## Phase 1 (Month 1-2): Cloud Fundamentals

### 🎯 Phase Objective

Understand the "What" and "Why" of the cloud.

### ✅ Prerequisites

* Basic understanding of how servers work (CPU, RAM).
* CLI basics (Bash/PowerShell).

### ☁️ Cloud Services (AWS | Azure | GCP)

* **Compute:** EC2 | VMs | Compute Engine
* **Storage:** S3 | Blob Storage | Cloud Storage
* **Database:** RDS | SQL Database | Cloud SQL
* **Global:** AWS Global Infrastructure (Regions, AZs, Edge Locations).

### 🏗️ Architectural Concepts

* **Cloud Models:** IaaS vs PaaS vs SaaS.
* **Deployment:** Public vs Private vs Hybrid.
* **Virtualization:** Hypervisors, VMs.
* **Networking 101:** IP CIDR blocks, Subnets, DNS resolution.

### 🔍 Design Patterns

* **Stateless Web App:** Storing session state in DB/Cache, not on the server.
* **Vertical Scaling:** Increasing instance size (t2.micro -> t2.large).

### 🧪 Hands-On Labs

1. **First Deployment:** Launch an EC2 Linux instance, SSH into it, install Apache, and host a "Hello World" HTML page.
2. **S3 Hosting:** Host a static website using an S3 bucket with public read access.

### 📚 Learning Resources

* **Whitepaper:** [Overview of Amazon Web Services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html)
* **Course:** AWS Cloud Practitioner Essentials (Free on AWS Skill Builder).

### 🏆 Certification Milestone

* **AWS Certified Cloud Practitioner (CLF-C02)**

### 📊 Real-World Scenario

**Problem:** A startup wants to launch a marketing landing page quickly and cheaply.
**Solution:** Use S3 Static Website Hosting instead of running a dedicated server.

### ✅ Phase Completion Criteria

You can explain "Why Cloud?" to a non-technical person and launch basic resources.

---

## Phase 2 (Month 3-4): Compute & Storage

### 🎯 Phase Objective

Mastering the building blocks of infrastructure.

### ✅ Prerequisites

* Phase 1 completion.
* Basic Linux administration.

### ☁️ Cloud Services (AWS | Azure | GCP)

* **Scaling:** Auto Scaling Groups (ASG) | VM Scale Sets | Instance Groups
* **Load Balancing:** ELB (ALB/NLB) | Azure LB | Cloud Load Balancing
* **Serverless:** Lambda | Functions | Cloud Functions
* **Storage:** EBS vs EFS vs S3 | Disk vs Files vs Blob | Persistent Disk vs Filestore vs GCS

### 🏗️ Architectural Concepts

* **High Availability (HA):** Deploying across multiple Availability Zones (AZs).
* **Horizontal Scaling:** Adding more instances vs making instances bigger (Scale Out vs Scale Up).
* **Loose Coupling:** Decoupling components.

### 🔍 Design Patterns

* **N-Tier Architecture:** Web Tier -> App Tier -> DB Tier.
* **Load Balancing Pattern:** Distributing traffic to healthy instances only.

### 🧪 Hands-On Labs

1. **Auto-Healing App:** Create an ASG with min=1, max=1. Terminate the instance manually and watch AWS recreate it.
2. **Serverless API:** Create a Lambda function triggered by API Gateway to return a JSON response.

### 📚 Learning Resources

* **Docs:** [EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)
* **Lab:** [AWS Well-Architected Labs](https://www.wellarchitectedlabs.com/)

### 📊 Real-World Scenario

**Problem:** An e-commerce site crashes on Black Friday due to traffic spikes.
**Solution:** Implement Auto Scaling Groups triggered by CPU utilization > 60%.

### ✅ Phase Completion Criteria

You can architect a web application that automatically creates new servers when traffic increases.

---

## Phase 3 (Month 5-6): Networking & Security

### 🎯 Phase Objective

Building the secure backbone of your infrastructure.

### ✅ Prerequisites

* TCP/IP, Subnetting, Firewalls.

### ☁️ Cloud Services (AWS | Azure | GCP)

* **Network:** VPC, Route53, Direct Connect | VNet, DNS, ExpressRoute | VPC, Cloud DNS, Interconnect
* **Security:** IAM, Security Groups, WAF, Shield | Entra ID, NSG, Firewall | IAM, Firewall Rules, Cloud Armor

### 🏗️ Architectural Concepts

* **Defense in Depth:** Multi-layered security (Edge -> Network -> Host -> App).
* **Least Privilege:** Giving users only permissions they need.
* **Encryption:** At Rest (KMS) and In Transit (SSL/TLS).

### 🔍 Design Patterns

* **Bastion Host (Jump Box):** Secure access to private instances.
* **Hub and Spoke:** Centralized network management.

### 🧪 Hands-On Labs

1. **Custom VPC:** Build a VPC from scratch with 2 Public and 2 Private subnets across 2 AZs.
2. **Three-Tier Net:** Deploy a Web Server (Public), App Server (Private), and DB (Private) with correct Security Group rules.

### 📚 Learning Resources

* **Whitepaper:** [AWS Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
* **Tool:** [CIDR.xyz](https://cidr.xyz/) visualizer.

### 📊 Real-World Scenario

**Problem:** Developers need access to a database implementation in a private subnet.
**Solution:** Deploy a Bastion Host in the public subnet and allow SSH only from the corporate IP range.

### ✅ Phase Completion Criteria

You can draw a VPC diagram showing public/private subnets, NAT Gateways, and route tables.

---

## Phase 4 (Month 7-9): Databases & Data Services

### 🎯 Phase Objective

Designing the data layer for performance and durability.

### ✅ Prerequisites

* SQL vs NoSQL basics.

### ☁️ Cloud Services (AWS | Azure | GCP)

* **Relational:** RDS, Aurora | SQL Database | Cloud SQL
* **NoSQL:** DynamoDB | Cosmos DB | Firestore/Bigtable
* **Caching:** ElastiCache (Redis) | Azure Cache for Redis | Memorystore
* **Warehousing:** Redshift | Synapse | BigQuery

### 🏗️ Architectural Concepts

* **ACID vs BASE:** Consistency models.
* **Read Replicas:** Offloading read traffic.
* **Multi-AZ:** Synchronous replication for failover.

### 🔍 Design Patterns

* **Cache-Aside:** Application checks cache before DB.
* **Database Migration:** Strategies for moving data with minimal downtime.

### 🧪 Hands-On Labs

1. **RDS Multi-AZ:** Launch an RDS instance with a standby. Simulate a failover and observe endpoint DNS changes.
2. **DynamoDB API:** Create a table and use Python (Boto3) to put/get items.

### 📚 Learning Resources

* **Whitepaper:** [AWS Database Services](https://aws.amazon.com/products/databases/)
* **Course:** Data Engineering on AWS (Coursera).

### 📊 Real-World Scenario

**Problem:** A reporting dashboard is slowing down the primary transactional database.
**Solution:** Create a Read Replica and point the dashboard to the replica endpoint.

### ✅ Phase Completion Criteria

You can choose the right database engine (SQL vs NoSQL vs Graph) based on business requirements.

---

## Phase 5 (Month 10-12): Advanced Architecture Patterns

### 🎯 Phase Objective

Decoupling systems for scale and agility.

### ✅ Prerequisites

* Basic coding (Python/Node).

### ☁️ Cloud Services (AWS | Azure | GCP)

* **Messaging:** SQS, SNS | Service Bus, Event Grid | Pub/Sub
* **API:** API Gateway | API Management | Apigee
* **Orchestration:** Step Functions | Logic Apps | Workflows

### 🏗️ Architectural Concepts

* **Microservices:** Breaking monoliths into small services.
* **Event-Driven:** Systems reacting to state changes.
* **Asynchronous Processing:** Fire and forget.

### 🔍 Design Patterns

* **Fan-Out:** Sending one message to multiple queues/subscribers via SNS.
* **Strangler Fig:** Gradually replacing a monolith with microservices.

### 🧪 Hands-On Labs

1. **Decoupled Image Processor:** User uploads to S3 -> S3 Event -> Lambda Function -> Resize Image.
2. **Fan-Out:** SNS Topic triggers 2 SQS queues (one for Email, one for Analytics).

### 📚 Learning Resources

* **Book:** Serverless Architectures on AWS.
* **Site:** [ServerlessLand](https://serverlessland.com/)

### 📊 Real-World Scenario

**Problem:** Users experience timeouts when uploading large files that need processing.
**Solution:** Upload to S3, which triggers an async background job (Lambda) via SQS, notifying user later.

### ✅ Phase Completion Criteria

You can explain when to use SQS (Queue) vs SNS (Pub/Sub) vs Kinesis (Streams).

---

## Phase 6 (Month 13-15): HA & Disaster Recovery

### 🎯 Phase Objective

Keeping the lights on when things break.

### ✅ Prerequisites

* Multi-region concepts.

### ☁️ Cloud Services (AWS | Azure | GCP)

* **Route53:** DNS Failover protocols.
* **Backup:** AWS Backup | Azure Backup.
* **Global:** CloudFront (CDN), Global Accelerator.

### 🏗️ Architectural Concepts

* **RTO (Recovery Time Objective):** How fast must we recover?
* **RPO (Recovery Point Objective):** How much data can we lose?
* **Active-Active vs Active-Passive.**

### 🔍 Design Patterns

* **Pilot Light:** Minimal resources running in DR region.
* **Warm Standby:** Scaled-down version running in DR region.

### 🧪 Hands-On Labs

1. **Cross-Region Replication:** Set up S3 CRR to automatically copy files from us-east-1 to eu-west-1.
2. **DNS Failover:** Configure Route53 to switch traffic to a static S3 page if the Load Balancer fails health checks.

### 📚 Learning Resources

* **Whitepaper:** [Disaster Recovery of Workloads on AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/introduction.html)

### 🏆 Certification Milestone

* **AWS Certified Solutions Architect – Associate (SAA-C03)**

### 📊 Real-World Scenario

**Problem:** A hurricane destroys the primary data center (Region).
**Solution:** Initiate DR plan: Promote Read Replicas in the secondary region to Primary, update DNS weights.

### ✅ Phase Completion Criteria

You can design a solution that survives a complete regional outage.

---

## Phase 7 (Month 16-18): Enterprise & Advanced

### 🎯 Phase Objective

Designing for the enterprise at massive scale.

### ✅ Prerequisites

* Comprehensive knowledge of all prior phases.

### ☁️ Cloud Services (AWS | Azure | GCP)

* **Governance:** Organizations, Control Tower | Management Groups | Resource Hierarchy
* **Hybrid:** Outposts, Storage Gateway.
* **Containers:** EKS (Kubernetes).
* **IaC:** Terraform / CloudFormation.

### 🏗️ Architectural Concepts

* **Well-Architected Framework:** Operation Excellence, Security, Reliability, Performance, Cost, Sustainability.
* **Landing Zones:** Multi-account setups with guardrails.

### 🔍 Design Patterns

* **Sidecar Pattern (Kubernetes):** Helper container.
* **Transit Gateway:** Connecting hundreds of VPCs.

### 🧪 Hands-On Labs

1. **Terraform Multi-Cloud:** Write a script that Deploys a VM in AWS and Azure simultaneously.
2. **EKS Cluster:** Deploy a Kubernetes cluster and run a microservices demo app.

### 📚 Learning Resources

* **Whitepaper:** [AWS Well-Architected Framework](https://wa.aws.amazon.com/)

### 🏆 Certification Milestone

* **AWS Certified Solutions Architect – Professional (SAP-C02)**

### 📊 Real-World Scenario

**Problem:** A global enterprise has 500 AWS accounts and needs centralized billing and security auditing.
**Solution:** Implement AWS Organizations with SCPs (Service Control Policies) and centralized CloudTrail logging.

### ✅ Phase Completion Criteria

You can lead a whiteboard session designing a complete cloud migration strategy for a legacy enterprise.

---

## 🎨 Portfolio & Career Strategy

### 📁 Building a Portfolio

* **Diagrams:** Use **Lucidchart** or **Draw.io**. An architect's main deliverable is often a diagram.
* **Writeups:** "How I built X using Y services to solve Z problem."
* **GitHub:** Store your Terraform/CloudFormation code here.

### 🎤 Interview Prep (System Design)

* **Requirement Gathering:** Always ask "How many users?", "Read vs Write heavy?", "Budget?".
* **Trade-offs:** There is no "perfect" solution. Explain why you chose DynamoDB over RDS (Scaling vs Complex Queries).

### 🤝 Community

* **Hero/Builder Programs:** AWS Community Builders, Azure Heroes.
* **Meetups:** Attend local Cloud meetups.

Good luck on your journey to the clouds! ☁️

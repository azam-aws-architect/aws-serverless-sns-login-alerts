# Project #29: AWS Serverless Notification System (SNS + Lambda)

## 🏢 Business Scenario & Customer Demand
An international banking institution required a highly scalable, serverless security alert system. The requirement was to instantly broadcast "Login Alert Notifications" to security monitoring services and user endpoints whenever a dynamic banking session is initialized, without managing heavy standard mail servers.

**The Solution:** Developed a fully decoupled, real-time alerting layer leveraging managed pub/sub messaging and serverless execution units to trigger notification broadcasts instantaneously.

## 🛠️ Tech Stack & Services Used
* **Amazon SNS (Simple Notification Service):** Public/Subscribe platform configured with standard topic topologies to ingest real-time payloads.
* **AWS Lambda (Python 3.x):** Embedded event handler integrated with SNS topic triggers to process incoming records instantly.
* **Amazon CloudWatch:** System health monitoring and log metric visualization.

## 📊 Architecture Flow
[User Login Session] ➔ [Amazon SNS Topic] ➔ [AWS Lambda Processor] & [Email Subscription Node] ➔ [CloudWatch Event Logs]

## 🧪 Verification Results
Simulated a live transaction payload from a corporate IP space. Real-time testing confirmed that notification alerts were distributed via email subscribers within milliseconds, and synchronous event tracking prints were successfully cataloged inside CloudWatch streams.

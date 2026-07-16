<div align="center">

# 🚀 CodeMentorAI
### Always-On AI Coding Interview Coach

**An autonomous AWS agent that wakes up every day, invents a brand-new coding interview question, and delivers it straight to your inbox — with zero human interaction.**

[![AWS](https://img.shields.io/badge/AWS-Serverless-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)
[![Bedrock](https://img.shields.io/badge/Amazon%20Bedrock-Nova%20Lite-8A3FFC?style=for-the-badge&logo=amazon&logoColor=white)](https://aws.amazon.com/bedrock/)
[![Lambda](https://img.shields.io/badge/AWS%20Lambda-Serverless-FF9900?style=for-the-badge&logo=awslambda&logoColor=white)](https://aws.amazon.com/lambda/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge)](#-license)

*Built for the **AWS "Build an Always-On Agent" Weekend Challenge*** 🏆

<br>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=3000&pause=1000&color=FF9900&center=true&vCenter=true&width=600&lines=One+question.+Every+day.+No+clicks.;Powered+by+Amazon+Bedrock+Nova+Lite;100%25+Serverless+%7C+100%25+Automated" alt="Typing SVG" />

</div>

<br>

## 📌 Overview

**CodeMentorAI** is an *always-on* AI agent that removes the friction from interview prep. There's no app to open and no button to press — the agent runs itself.

Every day, on a fixed schedule, it:

1. **Wakes up** automatically via Amazon EventBridge
2. **Generates** a fresh coding interview question using Amazon Bedrock (Nova Lite)
3. **Archives** the question permanently in Amazon S3
4. **Emails** it directly to you through Amazon SES

No dashboards. No manual triggers. Just a quiet, reliable AI coach that shows up in your inbox — rain or shine.

<br>

## ✨ Features

<table>
<tr>
<td width="50%">

**🤖 AI-Generated Questions**
Fresh, unique coding interview questions generated on-demand by Amazon Bedrock — never the same static question bank.

**📅 Fully Autonomous Scheduling**
Runs every single day without any human intervention, powered by EventBridge cron scheduling.

**⚡ Powered by Bedrock Nova Lite**
Fast, cost-efficient foundation model generation tuned for concise, high-quality prompts.

</td>
<td width="50%">

**☁️ 100% Serverless**
Built entirely on AWS Lambda — no servers to patch, scale, or babysit.

**🗂 Persistent Archive**
Every question is stored in Amazon S3, building a growing personal question bank over time.

**📧 Inbox Delivery**
Daily notifications land straight in your Gmail via Amazon SES — no app-switching required.

</td>
</tr>
</table>

<br>

## 🏗 Architecture

<div align="center">

```mermaid
flowchart TD
    A["⏰ Amazon EventBridge<br/><sub>Daily Cron Trigger</sub>"] -->|invokes| B["⚡ AWS Lambda<br/><sub>lambda_function.py</sub>"]
    B -->|prompts| C["🤖 Amazon Bedrock<br/><sub>Nova Lite Model</sub>"]
    C -->|generated question| B
    B -->|archives| D["🗂 Amazon S3<br/><sub>Question Store</sub>"]
    B -->|sends via| E["📧 Amazon SES<br/><sub>Email Delivery</sub>"]
    E -->|delivers to| F["📬 Gmail Inbox"]

    style A fill:#FF9900,stroke:#232F3E,color:#fff
    style B fill:#FF9900,stroke:#232F3E,color:#fff
    style C fill:#8A3FFC,stroke:#232F3E,color:#fff
    style D fill:#569A31,stroke:#232F3E,color:#fff
    style E fill:#D13212,stroke:#232F3E,color:#fff
    style F fill:#4285F4,stroke:#232F3E,color:#fff
```

</div>

The entire pipeline runs **without a single manual step** — from trigger to inbox, it's agentic end-to-end.

<br>

## 🛠 Tech Stack & AWS Services

| Service | Role |
|---|---|
| ![EventBridge](https://img.shields.io/badge/-Amazon%20EventBridge-FF4F8B?style=flat-square&logo=amazoneventbridge&logoColor=white) | Daily cron-based trigger — the agent's "alarm clock" |
| ![Lambda](https://img.shields.io/badge/-AWS%20Lambda-FF9900?style=flat-square&logo=awslambda&logoColor=white) | Core compute — orchestrates the entire workflow |
| ![Bedrock](https://img.shields.io/badge/-Amazon%20Bedrock-8A3FFC?style=flat-square&logo=amazon&logoColor=white) | Generates the interview question via Nova Lite |
| ![S3](https://img.shields.io/badge/-Amazon%20S3-569A31?style=flat-square&logo=amazons3&logoColor=white) | Durable storage for all generated questions |
| ![SES](https://img.shields.io/badge/-Amazon%20SES-D13212?style=flat-square&logo=amazon&logoColor=white) | Sends the daily email notification |
| ![IAM](https://img.shields.io/badge/-AWS%20IAM-DD344C?style=flat-square&logo=amazonaws&logoColor=white) | Secures least-privilege access between services |

<br>

## 📂 Project Structure

```
CodeMentorAI/
│
├── 📄 lambda_function.py     # Core agent logic (generate → store → email)
├── 📘 README.md              # You are here
├── 🏛 architecture/          # Architecture diagrams
├── 🖼 screenshots/           # Console proof-of-work screenshots
└── 📜 LICENSE                # MIT License
```

<br>

## ⚙️ How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│  1. EventBridge fires the Lambda on a daily schedule             │
│  2. Lambda sends a prompt to Amazon Bedrock (Nova Lite)          │
│  3. Bedrock returns a freshly generated coding question          │
│  4. Lambda writes the question as an object into Amazon S3       │
│  5. Lambda formats and sends an email through Amazon SES         │
│  6. The question lands in your Gmail inbox — no clicks needed    │
└─────────────────────────────────────────────────────────────────┘
```

<br>

## 📸 Screenshots

<div align="center">

| | |
|---|---|
| 🔧 **Lambda Function** | ✅ **Lambda Test Success** |
| ⏰ **EventBridge Scheduler** | 🤖 **Amazon Bedrock Console** |
| 🗂 **Amazon S3 Bucket** | 📧 **Amazon SES Setup** |
| 📬 **Gmail Output** | |

*See the [`/screenshots`](./screenshots) folder for full-resolution proof-of-work images.*

</div>

<br>

## 🚀 Future Improvements

- [ ] 🗺️ Weekly DSA Roadmap generation
- [ ] 🗃️ SQL Interview Mode
- [ ] 🏛️ System Design question track
- [ ] 📚 Topic-wise adaptive learning
- [ ] 💬 Slack & Microsoft Teams notifications
- [ ] 📱 Companion mobile application

<br>

## 🧠 Why This Project Matters

This isn't just a script that runs on a timer — it's a demonstration of a true **agentic pattern** on AWS: an autonomous system that perceives (schedule trigger), reasons (Bedrock generation), acts (S3 + SES), and delivers value **without waiting to be asked**. It's a small, focused example of how generative AI can be wired directly into everyday infrastructure to create a genuinely "always-on" experience.

<br>

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

<br>

## 👨‍💻 Author

<div align="center">

**Deepak Raj JS**

[![GitHub](https://img.shields.io/badge/GitHub-deepakrajjs--29-181717?style=for-the-badge&logo=github)](https://github.com/deepakrajjs-29)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-deepak--raj--js-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/deepak-raj-js)

<br>

⭐ **If you found this project interesting, consider giving it a star!** ⭐

</div>

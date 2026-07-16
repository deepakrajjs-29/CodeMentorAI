# 🚀 CodeMentorAI – Always-On AI Coding Interview Coach

CodeMentorAI is an AI-powered serverless application built on AWS that automatically generates a coding interview question every day without any user interaction.

The application is triggered automatically by Amazon EventBridge, invokes AWS Lambda, uses Amazon Bedrock Nova Lite to generate interview questions, stores the generated content in Amazon S3, and finally emails the result using Amazon SES.

---

## ✨ Features

- Automatically runs every day
- AI-generated coding interview questions
- Difficulty level included
- Helpful interview hints
- Interview preparation tips
- Saves results to Amazon S3
- Sends the generated question via email
- Fully serverless

---

## 🏗 AWS Services Used

- Amazon EventBridge
- AWS Lambda
- Amazon Bedrock (Nova Lite)
- Amazon S3
- Amazon SES
- IAM

---

## Architecture

EventBridge
↓

Lambda
↓

Amazon Bedrock

↓

Amazon S3

↓

Amazon SES

↓

Gmail Inbox

---

## Technologies

- Python
- boto3
- Amazon Bedrock Nova Lite

---

## Sample Output

Question:
Reverse a singly linked list.

Difficulty:
Medium

Hint:
Use three pointers.

Interview Tip:
Visualize pointers on paper before coding.

---

## Future Improvements

- Weekly interview roadmap
- SQL interview mode
- System Design mode
- DSA topic rotation
- Slack / Discord notifications
- Mobile App

---

## Author

Deepak Raj JS

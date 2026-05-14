# Serverless CI/CD Automation using AWS Lambda and CodePipeline

This project demonstrates a serverless CI/CD pipeline using AWS services. Whenever code is pushed to GitHub, AWS Lambda triggers AWS CodePipeline, which automatically deploys the application to Amazon S3.

---

## Architecture Flow

GitHub → AWS Lambda → AWS CodePipeline → Amazon S3 → Live Application

---

## Tech Stack

- Python (Flask)
- Git & GitHub
- AWS Lambda
- AWS CodePipeline
- Amazon S3
- IAM

---

## Features

- Automatic deployment on every GitHub push  
- Fully serverless CI/CD pipeline  
- No manual deployment required  
- End-to-end automation using AWS services  

---

## Working Process

1. Code pushed to GitHub repository  
2. AWS Lambda is triggered automatically  
3. Lambda starts AWS CodePipeline  
4. Pipeline pulls latest code from GitHub  
5. Application is deployed to Amazon S3  
6. Changes reflect on live website  

---

## Screenshots

### 1. Flask Application Output
<img src="https://github.com/user-attachments/assets/d5f23e38-56a5-4d96-a93b-853711b23c55" />

---

### 2. Git Commit History (Development Activity)
<img src="https://github.com/user-attachments/assets/436f7a11-cf81-4e2a-97c5-87f55cb06ef8" />

---

### 3. AWS CodePipeline Execution (Build & Deploy Stages)
<img src="https://github.com/user-attachments/assets/891e0cf3-2bba-4f19-b3ba-f3a9801a2499" />

---

### 4. AWS Lambda Trigger Execution
<img src="https://github.com/user-attachments/assets/d9e529ae-2acc-436a-a6a6-31c15f252394" />

---

## IAM Roles Used

- Lambda execution role to trigger CodePipeline  
- CodePipeline service role for deployment  
- S3 access role for hosting files  
- IAM ensures secure AWS service communication  

---

## Result

The application is successfully deployed using a fully automated CI/CD pipeline. Every GitHub push automatically updates the live application hosted on Amazon S3.

---

## Key Highlight

This project demonstrates real-world DevOps automation using AWS serverless services with zero manual deployment effort.

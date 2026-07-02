# AWS Serverless Personal To-Do List Application

A cloud-native To-Do List application developed using **AWS Serverless Services**. This project demonstrates how to build and deploy a serverless web application using **AWS Lambda**, **Amazon API Gateway**, **Amazon DynamoDB**, and **Amazon S3** without managing any servers.

---

##  Project Overview

The application allows users to add and view tasks through a simple web interface. The frontend is hosted separately, while the backend uses AWS Lambda functions connected through API Gateway. Task data is stored in Amazon DynamoDB.

This project demonstrates the practical implementation of serverless architecture on AWS.

---

##  Features

- Add new tasks
- View existing tasks
- Serverless backend
- REST API integration
- Cloud-based data storage
- Simple and responsive user interface

---

##  Technologies Used

- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon S3
- Python
- HTML
- CSS
- JavaScript

---

## Architecture

```
User
   │
   ▼
Frontend (HTML, CSS, JavaScript)
   │
   ▼
Amazon API Gateway
   │
   ▼
AWS Lambda (Python)
   │
   ▼
Amazon DynamoDB
```

---

##  Project Structure

```
aws-serverless-todo-app/

├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── lambda/
│   └── lambda_function.py
│
├── Project_1___Serverless_Personal_To_Do_List_Application.pdf
│
├── README.md
└── LICENSE
```

---

##  Working

1. User enters a task in the web application.
2. The frontend sends a POST request to Amazon API Gateway.
3. API Gateway invokes the AWS Lambda function.
4. Lambda stores the task in Amazon DynamoDB.
5. When the application loads, it sends a GET request to retrieve all stored tasks.
6. DynamoDB returns the task list, which is displayed on the webpage.

---

##  Documentation

The complete project report, implementation details, architecture, methodology, and screenshots are included in the PDF available in this repository.

---

##  Learning Outcomes

- Understanding of Serverless Computing
- AWS Lambda Function Development
- API Gateway Integration
- Amazon DynamoDB Operations
- REST API Development
- Cloud-Based Application Deployment

---

##  Future Enhancements

- User Authentication using AWS Cognito
- Task Categories
- Task Priorities
- Edit and Delete Tasks
- Responsive UI Improvements
- Notifications and Reminders

---

## 👩‍💻 Author

**Bhavani M Ghorpade**

Electronics and Communication Engineering  
Cloud Computing Project – 2026

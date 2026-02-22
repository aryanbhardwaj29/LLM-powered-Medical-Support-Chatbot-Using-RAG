# 🩺 Medical Support Chatbot  
AI-Powered Medical Assistance System using MySQL, Flask, and RAG Architecture  

---

## 📌 Overview

The Medical Support Chatbot is a backend-driven AI application designed to assist users with queries related to symptoms, diseases, and medications. The system integrates a structured MySQL relational database with a Flask-based REST API and a Retrieval-Augmented Generation (RAG) pipeline to provide accurate and context-aware responses.

This project demonstrates practical implementation of SQL, relational database design, and backend integration in a real-world use case.

---

## 🗄 Database Design (MySQL Implementation)

A relational database schema was designed to store structured medical data, including:

- Disease Information  
- Symptoms  
- Medications  
- Descriptions and Metadata  

### Key Database Features:

- Designed normalized relational tables  
- Implemented Primary Keys and Foreign Keys  
- Used SQL queries (SELECT, INSERT, JOIN) for data retrieval  
- Applied indexing for faster query execution  
- Ensured data consistency and integrity  

The database was integrated with the backend using secure MySQL connectors and structured query execution.

---

## ⚙️ System Architecture

User Query  
⬇  
Flask REST API  
⬇  
MySQL Database (Structured Retrieval)  
⬇  
RAG Pipeline (Embedding + Context Matching)  
⬇  
Generated Response  

The chatbot processes user input, retrieves relevant structured records from the database, and enhances responses using embedding-based similarity search.

---

## 🚀 Key Features

- AI-powered medical query handling  
- Relational database integration using MySQL  
- REST API backend using Flask  
- Metadata filtering and chunking for optimized retrieval  
- Modular and scalable system design  

---

## 🛠 Tech Stack

- Python  
- Flask  
- MySQL  
- SQL  
- LangChain  
- SentenceTransformers  
- REST API  

---

## 📂 Project Structure

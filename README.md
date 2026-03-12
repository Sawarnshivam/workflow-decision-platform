# Configurable Workflow Decision Platform

## Overview
The Configurable Workflow Decision Platform is a modular system that processes requests and automatically makes decisions based on business rules and configurable workflows.

The system exposes an API endpoint that receives a request, evaluates rules, interacts with an external service, and determines the final decision using a configurable workflow.

This type of system is commonly used in domains such as loan approvals, insurance claims, fraud detection, and vendor onboarding.

---

## Architecture

Client Request  
↓  
FastAPI API Layer  
↓  
Decision Engine  
↓  
Rule Engine  
• Income Rule  
• Duplicate Rule  
• Credit Rule  
↓  
External Credit Service (Simulated)  
↓  
Workflow Engine (JSON Configurable)  
↓  
State Manager  
↓  
Audit Logs  

---

## Features

- API-based request processing using FastAPI
- Modular rule engine
- Configurable workflow using JSON
- External dependency simulation
- Retry logic for external service failures
- Audit logging
- Request state tracking
- Test scenarios for different cases

---

## Project Structure

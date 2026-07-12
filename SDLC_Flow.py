#===================
# SDLC FLOW 
#===================

"""Requirement Gathering
        ↓
Planning
        ↓
System Design
        ↓
Development (Coding)
        ↓
Testing
        ↓
Deployment
        ↓
Maintenance"""



"""=========Phase 1: Requirement Gathering
Goal===========

Understand what the client wants.

Who Works Here?
Client
Business Analyst (BA)
Product Owner
Project Manager
Business Analyst (BA)

The BA talks to the client.

Example questions:

What software do you need?
Who will use it?
What problem are you trying to solve?
Which features are required?
What's your budget?
When do you need it?

The BA converts the client's ideas into clear requirements.

Example

Client says:


"I want an online shopping website."

BA asks:

User login?
Google login?
Add to cart?
Online payment?
COD?
Order tracking?
Wishlist?
Coupons?
Admin panel?

Everything is documented.



Output

========SRS Document (Software Requirement Specification)==========

This document includes:

Features
Requirements
Rules
Timeline
User roles
Business goals



=========Phase 2: Planning===========
Goal

Plan the project before coding starts.

Who Works Here?
Project Manager (PM)
Team Lead
Software Architect
Business Analyst

They decide:

Team size
Cost
Deadline
Technologies
Risks
Budget

Example:

Project Duration:
6 Months

Budget:
₹40 Lakhs

Team:

5 Developers
2 Testers
1 UI Designer
1 BA
1 DevOps Engineer
Project Manager (PM)

The PM manages the entire project.

Responsibilities:

Team management
Client meetings
Deadlines
Budget
Resource allocation
Progress tracking
Risk management

The PM usually does not write code.



===================Phase 3: System Design=================
Goal

Plan how the software will work.

Who Works Here?
Software Architect
UI/UX Designer
Database Designer
Team Lead

They decide:

Database structure
Screens
APIs
Security
Backend architecture
Cloud setup
UI Designer

Creates the application's appearance.

Designs:

Login page
Home page
Buttons
Colors
Icons

Uses tools like:

Figma
Adobe XD
UX Designer

Improves the user experience.

Example:
Instead of making payment in 8 steps, they reduce it to 3 steps.

Software Architect

The architect decides:

Which programming language?
Which database?
Which framework?
Microservices or Monolith?
Security design?
Server architecture?

This is one of the most experienced technical roles.



====================Phase 4: Development==================
Goal

Write the code.

Who Works Here?

Frontend Developers

Backend Developers

Full Stack Developers

Database Developers

Frontend Developer

Creates what users see.

Works with:

HTML
CSS
JavaScript
React
Angular
Vue

Builds:

Buttons
Forms
Pages
Menus
Backend Developer

Creates the application's logic.

Works with:

Python
Java
C#
Node.js
PHP

Handles:

Login
Payment
Authentication
Business logic
APIs
Database Developer

Creates and manages databases.

Uses:

MySQL
PostgreSQL
Oracle
MongoDB

Responsibilities:

Store data
Optimize queries
Backups
Security
Full Stack Developer

Works on both:

Frontend
Backend

Can build complete applications.



==========================Phase 5: Testing=======================
Goal

Find bugs before users do.

Who Works Here?
QA Engineer
Software Tester
Automation Tester
Manual Tester

Checks software manually.

Example:

Login works?
Payment works?
Search works?
Logout works?
Automation Tester

Writes scripts that automatically test the software.

Common tools:

Selenium
Cypress
Playwright
Types of Testing
Unit Testing

Developers test individual functions or methods.

Integration Testing

Checks whether different modules work together.

System Testing

Tests the complete application.

Regression Testing

Ensures new changes haven't broken existing features.

Performance Testing

Checks how the application performs under heavy traffic.

Security Testing

Finds security vulnerabilities.

User Acceptance Testing (UAT)

The client tests the software to ensure it meets business needs.



==================Phase 6: Deployment============
Goal

Make the application available to users.

Who Works Here?
DevOps Engineer
Cloud Engineer
System Administrator
DevOps Engineer

Responsibilities:

Deploy applications
Configure servers
Set up CI/CD pipelines
Monitor systems
Roll back if deployment fails

Common tools:

Docker
Kubernetes
Jenkins
GitHub Actions
GitLab CI/CD
Cloud Engineer

Manages cloud infrastructure.

Platforms:

AWS
Microsoft Azure
Google Cloud

Responsibilities:

Servers
Storage
Networking
Scalability
Security


====================Phase 7: Maintenance==================
Goal

Keep the software working after release.

Who Works Here?
Developers
Testers
DevOps
Support Team

Responsibilities:

Fix bugs
Add new features
Improve performance
Security updates
Customer support

Example:
Users report that the app crashes during payment. The team investigates, fixes the bug, tests it, and deploys the update.

==================Complete Team Structure========================

::::Role:::	                             :::Main Responsibility:::

Client	                        Gives project requirements and feedback
Business Analyst (BA)	        Understands business needs and writes requirements
Product Owner	                Decides feature priorities based on business value
Project Manager (PM)	        Plans, coordinates, and tracks the project
Software Architect   	        Designs the overall technical architecture
UI Designer	                    Creates the visual interface
UX Designer	                    Improves usability and user experience
Frontend Developer	            Builds the user interface
Backend Developer	            Develops business logic and APIs
Full Stack Developer	        Handles both frontend and backend
Database Administrator (DBA)    Designs and maintains databases
QA/Test Engineer	            Tests software and reports defects
Automation Tester	            Automates repetitive testing
DevOps Engineer	                Deploys and maintains delivery pipelines
Cloud Engineer	                Manages cloud infrastructure
Support Engineer	            Helps users and resolves production issues
                ::::How Everyone Works Together:::




 Client
   │
   ▼
Business Analyst
   │
   ▼
Project Manager
   │
   ▼
Software Architect
   │
   ▼
UI/UX Designers
   │
   ▼
Developers
   │
   ▼
QA/Testers
   │
   ▼
DevOps
   │
   ▼
Users
   │
   ▼
Support & Maintenance"""
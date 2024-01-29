## CAR PRICE PREDICTION


# Table of Content
1. [About](#about)
2. [Features](#features)
3. [Pre-Requisites](#pre-requisites)
4. [Code-File](#code-file)
5. [Dataset](#dataset)
6. [Git](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/README.md#1-git)
7. [UML](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/README.md#2-uml)
8. [Requirement Engineering](https://github.com/shreyaa98/Car-Price-Prediction?tab=readme-ov-file#3-requirement-engineering)
9. [Analysis](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/README.md#4-analysis)
10. [DDD](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/README.md#5-ddd)
11. [Metrics](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/README.md#6-metrics)
12. [Clean Code](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/README.md#7-clean-code)
13. [Build](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/README.md#8-build)
14. [Unit Tests](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/README.md#9-unit-tests)
15. [IDE](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/README.md#10-ide)
16. [Funcational programming](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/README.md#11-functional-programming)
17. [Conclusion](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/README.md#conclusion)
18. [License](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/README.md#license)


# About 
This repository contains the Selenium web scraper for extracting data from cars24.com, a popular online platform for buying and selling used cars.
The scraper retrieves information about different types of used cars, including sedans, SUVs, hatchbacks, luxury SUVs, and luxury sedans.


# Features
1. Car Name: The name or model of the car.
2. Distance: The distance already traveled by the car.
3. Year Bought: The year when the car was purchased.
4. Previous Owners: The number of previous owners of the car.
5. RTO Location: The location of the Regional Transport Office.
6. Transmission: The type of transmission (automatic or manual).
7. Car Type: The type of car (sedan, SUV, hatchback, luxury SUV, luxury sedan).
8. Fuel: The fuel used (petrol, diesel, CNG, etc.).
9. Price: The price of the car.


# Pre-requisites
To run the scraper, ensure you have the following dependencies installed:

- Python 
- Selenium WebDriver
- Chrome or Firefox web browser
- Pandas library

You can download the Chrome driver from the following [link](https://chromedriver.storage.googleapis.com/index.html). Please download the version that matches your browser version. For python, the download link is here [python link](https://www.python.org/)

# Code File 
To access the code and check how I created this project the link is given Below [Python file](https://github.com/shreyaa98/Car-Price-Prediction/tree/600276a9a063c71938b8e5b349e28bf5ecaec432/code)

# DataSet
The scraped data consists of approximately 8015 rows and 9 columns, including the following information:

[Link for the dataset](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/cars_24_combined.csv)

# 1. Git
Usage of GitHub for the whole Project [Git](https://github.com/shreyaa98/Car-Price-Prediction/commits/main/)

 # 2. UML 
 UML diagrams provide a clear visual representation of the  structure, user interactions, and workflow of an online shopping system.
 These diagrams help developers, designers, and stakeholders understand the system's architecture, functionality, and behavior and promote effective communication and collaboration throughout the  software 
 development process. Here is my UML for my project [UML](https://github.com/shreyaa98/Car-Price-Prediction/tree/0c3c362f74f5e037aa522de9eda28fac0f9d8fe9/UML)
 
---
# 3. Requirement Engineering
Requirement engineering for my project involves gathering, analyzing, documenting, and managing the needs and constraints of the system's users and stakeholders. It's a crucial phase where clear and complete specifications are defined to guide the software development process. This includes understanding user expectations, functional and non-functional requirements, and potential risks. Effective requirement engineering ensures that the final software product meets user expectations and operates smoothly within the specified constraints, leading to a successful and satisfying outcome for both developers and users.
[Screenshots of Jira and Trello](https://github.com/shreyaa98/Car-Price-Prediction/tree/a45153ba40e3db74640551b07b9ec976a752a1ee/Requirements%20Engineering%20(Trello%20and%20Jira))

---
# 4. Analysis
Setting the foundation for a strong Car Price Prediction requires thorough analysis that includes defining the scope of the car price, identifying stakeholders, minimizing risks, guaranteeing compliance, integrating seamlessly, and assessing technical feasibility, budget, scalability, and market distinctiveness.

[Link to Analysis](https://github.com/shreyaa98/Car-Price-Prediction/blob/a2855d67773818245dbec3bcb982388bc462dd1d/Analysis%20Report.pdf)

---

# 5. DDD
 Imagine if everyone at the dealership, from salespeople to managers, used the same language to explain things. For example, when we talk about "customers" or "cars" they all mean the same thing.
 This helps avoid confusion.
 
 Different areas with clear rules: Imagine a car dealership with different departments, such as sales and finance.
 Each division has its own  rules and focuses on certain things. For example, the sales team is responsible for selling cars, and the finance team is responsible for financial matters.
 
 Important Things and Collections: Imagine something important  at the dealership, such as a particular car or  customer. These are like the main characters. Additionally, there are groups  such as "Car Sales" 
 that involve customers, cars, and prices.
 
 Prices and Details: Consider the price of a car. This is an important detail, but it does not exist in and of itself. It is part of a larger whole, such as the entire transaction when a customer buys a car.DDD 
 thinks this way about pricing and other details.
 
 Storing and Retrieving Information: Think of the "car repository" as a big file cabinet where car dealers store all the information about the cars they own. Similarly, the Customer Repository stores details 
 about  customers. This makes it easier to find and manage information.
 
 Special Tasks: Sometimes some tasks don't  fit  the essence or details. At a car dealership, a "pricing service" can be a special helper that determines the final price of a car based on a variety of factors.
 In other words, DDD is about speaking the same language, dividing the dealer into clear areas, focusing on what's important  and its details, keeping information organized, and having dedicated helpers for 
 specific tasks. It's like creating a well-written storybook of how a car dealership works.


**Domains**
1. Product
2. Customer
3. Order
4. Payment
5.  Inventory
6. Service
7. Location
8. Time
9. Event

**Here is my DDD for my project**
[DDD](https://github.com/shreyaa98/Car-Price-Prediction/tree/76b2e555b1c1112e1e11847f3fa33c9968cb7ea9/DDD)

---
# 6. Metrics

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=shreyaa98_Car-Price-Prediction&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=shreyaa98_Car-Price-Prediction)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=shreyaa98_Car-Price-Prediction&metric=bugs)](https://sonarcloud.io/summary/new_code?id=shreyaa98_Car-Price-Prediction)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=shreyaa98_Car-Price-Prediction&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=shreyaa98_Car-Price-Prediction)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=shreyaa98_Car-Price-Prediction&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=shreyaa98_Car-Price-Prediction)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=shreyaa98_Car-Price-Prediction&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=shreyaa98_Car-Price-Prediction)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=shreyaa98_Car-Price-Prediction&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=shreyaa98_Car-Price-Prediction)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=shreyaa98_Car-Price-Prediction&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=shreyaa98_Car-Price-Prediction)

**Screenshot**
Reference for Badge if the above link expires 
![Screenshot 2024-01-19 161342](https://github.com/shreyaa98/Car-Price-Prediction/assets/33647234/04827c5e-b7c3-4976-a94b-238e49ed05c0)



---
# 7. Clean Code
Writing code that is simple to read, comprehend and update is known as "clean code development." It entails eliminating needless complexity, utilizing meaningful names, and maintaining consistency in formatting. Clean code is simpler and adheres to concepts like single responsibility, which improves collaboration and long-term software development. Here is my clean Code for my project [Clean Code](https://github.com/shreyaa98/Car-Price-Prediction/blob/7837a61b1b2750c93f52ea3640cd02e571e95c7d/Clean%20Code%20Development.pdf)

---
# 8. Build
Utilizes Python with a custom build system for predicting car price data and is designed for seamless integration as a reusable package. 

[Link to build](https://github.com/shreyaa98/Car-Price-Prediction/blob/4c95da31eb53956948c3f0681eab9e618f030749/Build.md)

[Link to yml](https://github.com/shreyaa98/Car-Price-Prediction/blob/4c95da31eb53956948c3f0681eab9e618f030749/Build.yml)

---
# 9. Unit Tests
The project's unit tests ensure robust functionality and adherence to specifications, promoting code reliability. 

[![Test](https://github.com/shreyaa98/Car-Price-Prediction/actions/workflows/main.yml/badge.svg)](https://github.com/shreyaa98/Car-Price-Prediction/actions/workflows/main.yml)

---
# 10. IDE
Adding most favorite shortcuts here and create own to allow faster developemnt without lifting hands from the keyboard

### Pycharm 
&rarr; *own Shortcut*: 
- ```option + r``` (run) 
  
&rarr; *build-in*:
- ```cmd + f``` (find)
- ```cmd + r``` (replace) 
- ```option + c/v/x``` (copy/paste/cut)
- ```cmd + /``` (comment (out))  
- ``` shift + ctrl + d``` (start debugger)

---
# 11. Functional Programming
A coding approach known as functional programming views computation as the assessment of mathematical functions. Immutability—the idea that data remains unchanged after creation—is emphasized. Functions can be assigned to variables, supplied as arguments, and returned as results since they are first-class citizens. This method makes it easier to reason about code and promotes programs that are clear, modular, and predictable.

[Data Structure](https://github.com/shreyaa98/Car-Price-Prediction/blob/d65e9e1d457009454be2071d87ee52eb8f85103f/Functional%20engineering.py#L1)

[Side effect-free functions](https://github.com/shreyaa98/Car-Price-Prediction/blob/d65e9e1d457009454be2071d87ee52eb8f85103f/Functional%20engineering.py#L9)

[Higher Order functions](https://github.com/shreyaa98/Car-Price-Prediction/blob/d65e9e1d457009454be2071d87ee52eb8f85103f/Functional%20engineering.py#L17)

[Functions as parameters and return values](https://github.com/shreyaa98/Car-Price-Prediction/blob/d65e9e1d457009454be2071d87ee52eb8f85103f/Functional%20engineering.py#L25)

[Use of closures/anonymous functions](https://github.com/shreyaa98/Car-Price-Prediction/blob/d65e9e1d457009454be2071d87ee52eb8f85103f/Functional%20engineering.py#L29)

---
# Conclusion

This is a sneak peek of my project, which is a car price prediction model. I'm still working on the details, so feel free to point out any errors or bugs. Right now, I only have the Python code for this project, but I plan to add more to it. Here is a rough sketch of how the car price predictions work in Python code.

---
# License

This project is privately owned by Shreyaasri Prakash, a student at SRH Berlin University of Applied Sciences pursuing an MSc in Computer Science, Focused on Big Data and Artificial Intelligence.

Contact Information:

Name: Shreyaasri Prakash

Email: shreyaa.prakash2015@gmail.com


 



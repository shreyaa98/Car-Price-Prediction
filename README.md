## CAR PRICE PREDICTION


# Table of Content
1. [About](#about)
2. [Features](#features)
3. [Pre-Requisites](#pre-requisites)
4. [Code-File](#code-file)
5. [Dataset](#dataset)
6. [Git](#https://github.com/shreyaa98/Car-Price-Prediction?tab=readme-ov-file#git)
7. [UML](#uml)
8. [Requirement Engineering](https://github.com/shreyaa98/Car-Price-Prediction?tab=readme-ov-file#3-requirement-engineering)
9. [Analysis](#analysis)
10. [DDD](#ddd)
11. [Metrics](#metrics)
12. [Clean Code](#clean_code)
13. [Build](#build)
14. [Unit Tests](unit_tests)
15. [IDE](#ide)
16. [Funcational programming](functional_programming)
17. [Conclusion](#conclusion)
18. [License](#license)


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
To access the code and check how I created this project the link is given Below [python_file](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/cars24.py)

# DataSet
The scraped data consists of approximately 8015 rows and 9 columns, including the following information:

The link for the dataset (https://github.com/shreyaa98/Car-Price-Prediction/blob/main/cars_24_combined.csv)

# 1. Git
Usage of GitHub for the whole Project [Git](https://github.com/shreyaa98/Car-Price-Prediction/commits/main/)

 # 2. UML 
 UML diagrams provide a clear visual representation of the  structure, user interactions, and workflow of an online shopping system.
 These diagrams help developers, designers, and stakeholders understand the system's architecture, functionality, and behavior and promote effective communication and collaboration throughout the  software 
 development process. Here is my UML for my project  
 [uml](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/UML_diagram.png)

 UML for my ML Model 
 1. [Linear Regression](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/Linear_Regression.png)



 2. [Random Forest Classifier](https://github.com/shreyaa98/Car-Price-Prediction/blob/main/Random%20Forest.png)

---
# 3. Requirement Engineering
[Screenshots of Jira and Trello](https://github.com/shreyaa98/Car-Price-Prediction/tree/a45153ba40e3db74640551b07b9ec976a752a1ee/Requirements%20Engineering%20(Trello%20and%20Jira))

---
# 4. Analysis

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

**Relational Diagram**
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

---
# 8. Build

---
# 9. Unit Tests

---
# 10. IDE

---
# 11. Functional Programming

---
# Conclusion

This is a sneak peek of my project, which is a car price prediction model. I'm still working on the details, so feel free to point out any errors or bugs. Right now, I only have the Python code for this project, but I plan to add more to it. Here is a rough sketch of how the car price predictions work in Python code.

---
# License

This project is privately owned by Shreyaasri Prakash, a student at SRH Berlin University of Applied Sciences pursuing an MSc in Computer Science, Focused on Big Data and Artificial Intelligence.

Contact Information:

Name: Shreyaasri Prakash

Email: shreyaa.prakash2015@gmail.com


 



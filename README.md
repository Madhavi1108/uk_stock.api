Stock and News Alert System

Overview
This project is a Python-based stock and news alert system that monitors the closing price of Tesla Inc. (TSLA) stock. If the price fluctuates by more than 5% in a day, it fetches the latest news articles related to Tesla Inc. and sends alerts via Twilio SMS.

Features
Fetches daily closing stock prices using the Alpha Vantage API.
Calculates the percentage change in stock price over two consecutive days.
If the percentage change exceeds 5%, it fetches news articles related to Tesla Inc. from the News API.
Sends SMS alerts with news headlines and descriptions using Twilio.

Technologies Used
Python
Requests (for API calls)
Twilio (for sending SMS)

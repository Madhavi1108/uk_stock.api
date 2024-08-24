import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

my_api = ""
my_news_api = ""
TWILIO_SID = ""
TWILIO_AUTH_TOKEN =""

# TODO 1. - Get yesterday's closing stock price.
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": my_api
}
response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)

# TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_price)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

# TODO 4. - Work out the percentage difference in price
percentage = round(difference/float(day_before_yesterday_closing_price) * 100, 2)
print(percentage)

# TODO 5. - If TODO4 percentage is greater than 5 then use the News API to get articles related to the COMPANY_NAME.
if difference > 5:
    news_params = {
        "apiKey": my_news_api,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

# TODO 6. - Use Python slice operator to create a list that contains the first 3 articles.
three_articles = articles[:3]
print(three_articles)

# TODO 7. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

# TODO 8. - Send each article as a separate message via Twilio.
client = Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="",
        to=""
    )

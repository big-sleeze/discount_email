from email.message import EmailMessage
import ssl
import smtplib
import os
import requests
from bs4 import BeautifulSoup
import lxml


head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.7",
}

response = requests.get('https://www.amazon.com/Officially-RAMBO-II-MC-RB2-15-38-Inch/dp/B001TMW78G/ref=sr_1_1?crid=2P1KTDSWVKVBQ&keywords=rambo+knife&qid=1662237296&sprefix=rambo+knife%2Caps%2C170&sr=8-1', headers=head)
page = response.text

soup = BeautifulSoup(page, 'lxml')
price = soup.find(name='span', class_="a-price-whole")
decimal_after_price = soup.find(name='span', class_='a-price-fraction')
full_price = f"{price.text}{decimal_after_price.text}"
real_full_price = float(full_price)


EMAIL_SENDER = "networksleezy@gmail.com"
EMAIL_PASSWORD = os.environ.get('NETWORK_SLEEZY_EMAIL_KEY')
EMAIL_RECEIVER = 'endritlleshi1337@gmail.com'

subject = "Amazon Price Alert!"
body = f"Officially Licensed RAMBO II MC-RB2 Officially Licensed First" \
       f" Blood Part II Survival Knife 15.38-Inch Overall is now {full_price}. " \
       f"https://www.amazon.com/Officially-RAMBO-II-MC-RB2-15-38-Inch/dp/B001TMW78G/ref=sr_1_1?crid=2P1KTDSWVKVBQ&keywords=rambo+knife&qid=1662237296&sprefix=rambo+knife%2Caps%2C170&sr=8-1"

em = EmailMessage()
em['From'] = EMAIL_SENDER
em['To'] = EMAIL_RECEIVER
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

if real_full_price < 90:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, em.as_string())




import requests
import smtplib
from bs4 import BeautifulSoup


def get_price():
    # URL for the product
    URL_flipkart = "https://www.flipkart.com/boat-rockerz-255f-pro-fast-charging-bluetooth-headset/p/itmaf6afd84aaae3?pid=ACCFMZ5GEGCVGUHA&lid=LSTACCFMZ5GEGCVGUHATN5GQE&marketplace=FLIPKART"
    # Your User-Agent
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0"
    }

    # Connecting to the Page
    page = requests.get(URL_flipkart, headers=header)
    soup = BeautifulSoup(page.content, "html.parser")

    # Getting the Title and Price of the Product
    title = soup.find("span", class_="_35KyD6").get_text().strip()
    print(title)
    price = soup.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    print(price)

    # Converting the Price and Checking It
    converted_price = float(price[1] + price[3:6])
    print(converted_price)
    if converted_price < 1299:
        send_email(title, URL_flipkart)


def send_email(title, url):
    # Connecting to the GMail Service
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Mail to be sent From
    mail_1 = "mail-1"
    # Mail to be Sent to
    mail_2 = "mail-2"

    # Logging with Gmail Account
    # Change the Password for your App Accordingly
    server.login(mail_1, "passwd")

    # Composing the Message
    subject = "Price Fell Down!!"
    body = f"The Price For {title} has fallen\n\
            Check the Link:\
            {url}"
    msg = f"Subject: {subject} \n\n {body}"

    # Sending the Mail
    server.sendmail(mail_1, mail_2, msg.encode("utf-8"))
    print("Email has been Sent")
    server.quit()


get_price()


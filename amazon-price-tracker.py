import requests
import smtplib
from bs4 import BeautifulSoup


def get_price():
    # URL for the product
    URL_amazon = "https://www.amazon.in/gp/product/B071KNKBQ1/ref=ox_sc_act_title_1?smid=ARBEPCMT3FADX&psc=1"
    # Your User-Agent
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0"
    }

    # Connecting to the Page
    page = requests.get(URL_amazon, headers=header)
    soup = BeautifulSoup(page.content, "html.parser")

    # Getting the Title and Price of the Product
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text()

    # Converting the Price and Checking It
    converted_price = float(price[2] + price[4:7])
    if converted_price < 2700:
        send_email(title, URL_amazon)


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


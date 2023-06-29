import requests
from bs4 import BeautifulSoup
import smtplib
expected_pot_price = float(100)
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "PHPSESSID=6nc0nht9prs37ok50g68jnmvn4; _ga=GA1.2.788938616.1667210500; _gid=GA1.2.1582162059.1667210500",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 "
                  "Safari/537.36 "
}
response = requests.get(url="https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463",
                        headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "lxml")
price = float(soup.find(name="span", class_="a-offscreen").text.replace("$", ""))

if price < expected_pot_price:
    my_email = "udemy.testing.day32@gmail.com"
    receiver_addr = "udemy_testing_day32@yahoo.com"
    pw = "aefjqwdzfzndffwl"
    message = "Subject: Amazon Price Alert!\n\n The price of Instant pot is lower than $300!".encode('UTF-8')
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver_addr,
                            msg=message)


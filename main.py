import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os


load_dotenv()

user = os.getenv("user")
password = os.getenv("password")
receiver = os.getenv("receiver")


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}
response = requests.get("https://www.amazon.in/DECOR-COMPANY-Metal-Wall-Clock/dp/B0CWLPD8VP/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.70c123a1-6488-46e5-8a35-eda9437e9b7a&crid=2B2E4ELPDP0FZ&dib=eyJ2IjoiMSJ9.Sg1-ymARnlhUcVjQ8cHyhFYhhyCPkgxw5y7ElKT5G9ZxJZMvPdcLQ5iqrA53_bJ9JEXajXkKvKOfRCgYV7T-KPKGPjhyikPg3AGLowBR2pq4p2SMCPm8m_qernZxdv_px5YlKZG9_FBydHIY1DiWz7LxKD2ugEprQ-OvAGWBowYU67PfAge3Ak88b-Qa6Ltv9ddKiuitL1U6NuXhTrcs6n2ZK92DCQbTmgilHduxKdQ.dBG56uQR4LohWY8ITN1dLSdod9iSf0VS2xXB1ydDpxw&dib_tag=se&pd_rd_r=0c02dcc5-4ef2-4914-9a8e-f02e2b5cb8de&pd_rd_w=HywqQ&pd_rd_wg=GVDOg&pf_rd_p=70c123a1-6488-46e5-8a35-eda9437e9b7a&pf_rd_r=YC000P9QRFXCJ6PEC8BY&qid=1733579118&sprefix=wall+arts%2C+paintings%2C+decor%2C+clock%2Cspecialty-aps%2C194&sr=8-1&srs=26129819031", headers=headers)

data = response.text

soup = BeautifulSoup(data, "html.parser")

price = float(soup.select_one(".a-price span").string[1:])
target_price = 1000

if price <= target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = user, password = password)
        connection.sendmail(
            from_addr = user,
            to_addrs = receiver,
            msg = f"Subject:Price Drop Alert!!\n\nYour Wishlist item is currently available at {price} which is less than you target price of {target_price}."
        )
    


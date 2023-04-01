from bs4 import BeautifulSoup
import requests
import smtplib
import os
import lxml

# scraping camel camel camel website
response = requests.get(
    url="https://camelcamelcamel.com/product/B0B9YSHFJR",
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
             })
amazon_product = response.text

# preparing the soup
soup = BeautifulSoup(amazon_product, "lxml")

# getting hold of the price
price_tag = soup.select_one(selector="#histories > div:nth-child(1) > div > div:nth-child(2) > div > div > table > "
                                     "tbody > tr:nth-child(1) > td:nth-child(2)")
price = float(price_tag.string.removeprefix("$"))

# this block is commented out due to anti-scraping techniques difficulties ⬇️

# # getting hold of the product product_name
# name_tag = soup.select_one(selector="#content > div:nth-child(5) > div.column.small-12.medium-7 > "
#                                     "div.row.column.show-for-medium > h2:nth-child(2) > a")
# product_name = name_tag.get_text().split(" – ")[0]
#
# # getting hold of the product amazon URL
# url_tag = soup.select_one(selector="#content > div:nth-child(5) > div.column.column-block.small-12.medium-3.medium"
#                                    "-text-right > div:nth-child(2) > div > a")
# product_url = url_tag.get("href")

# this block is commented out due to anti-scraping techniques difficulties ⬆️


# checking the price
good_offer = False
if price <= 130:
    good_offer = True

if good_offer:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.environ.get("MY_EMAIL"), password=os.environ.get("MY_PASSWORD"))
        connection.sendmail(
            from_addr=os.environ.get("MY_EMAIL"),
            to_addrs="omarmobarak53@gmail.com",
            msg=f"Subject: LOW PRICE ALERT! (amazon version)\n\n"
                f"only ${price} to buy your long desired 'product_name'!\n"
                f"DON'T HESITATE!\n"
                f"Amazon URL: 'product_url'"
        )

    # print(f"Subject: LOW PRICE ALERT! (amazon version)\n\n"
    #       f"only ${price} to buy your long desired kindle!\n"
    #       f"DON'T HESITATE!\n"
    #       f"Amazon URL: URL")

import requests
import sqlite3
from bs4 import BeautifulSoup


# conn.execute('''CREATE TABLE FOODS
#          (FOOD           TEXT    NOT NULL,
#          RESTAURANT     TEXT     NOT NULL);''')


# url_to_scrape = 'https://www.yelp.com/menu/tanuki-san-diego'
# url_to_scrape = 'https://www.yelp.com/menu/bleu-boh%C3%A8me-san-diego-6'
# url_to_scrape = 'https://www.yelp.com/menu/kensington-cafe-san-diego'
#https://www.yelp.com/menu/pachamama-san-diego-2



def add_foods(url_to_scrape):
    conn = sqlite3.connect('foods.db')
    print("Database connected successfully")

    plain_html_text = requests.get(url_to_scrape)
    soup = BeautifulSoup(plain_html_text.text, "html.parser")

    restaurant = soup.find('h1').text.strip()[9:]
    print("RESTAURANT NAME:", restaurant)

    food_cells = soup.find_all('h4')
    for i in food_cells:
        food = i.text.strip()
        conn.execute("INSERT INTO FOODS (FOOD, RESTAURANT) VALUES (?, ?)", (food, restaurant));

    conn.commit()
    conn.close()

add_foods('')
conn = sqlite3.connect('foods.db')
print(conn.execute("SELECT food FROM FOODS WHERE RESTAURANT='Pachamama'").fetchall())
from bs4 import BeautifulSoup

from selenium import webdriver
from getpass import getpass
from login_info import username, password 
from time import sleep

usr = username
pwd = password

input ("link 1")

opions = webdriver.ChromeOptions()
opions.add_argument('--disable-notifications')
driver = webdriver.Chrome(options=opions)

driver.get('https://www.facebook.com')

username_box = driver.find_element_by_id('email')
username_box.send_keys(username)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)

login_btn = driver.find_element_by_id('u_0_b')
login_btn.submit()

sleep(3)

driver.get("https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit=150&total_count=141&ft_ent_identifier=170515301123900")

page = driver.page_source
soup = BeautifulSoup(page, "html.parser")
names = soup.find_all(class_='bj')
sleep(2)

people_who_liked_post_1 = []

for name in names:
    people_who_liked_post_1.append(name.text)
print(people_who_liked_post_1)

from bs4 import BeautifulSoup as bsib
import urllib as url
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.maximize_window()
driver.get("https://www.travelkhana.com/rail-infoindian-railway-station-list-with-station-code/")
file_name = "train_codes.csv"
excel = open(file_name,"w")
object_write = csv.writer(excel)
table = driver.find_element_by_css_selector(".entry-content table tbody")
for i in table.find_elements_by_css_selector("tr"):
	row_data = []
	for j in i.find_elements_by_css_selector("td"):
		row_data.append(j.text)		
	object_write.writerow(row_data)

import urllib as url
import time
from yattag import Doc,indent
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import os
import datetime
import csv
import tkinter as GUI
from tkinter import *
def get_availability(from_station,to_station,get_date):
	seat_list = []
	train_names = []
	train_time =[]
	#Inputting Data and Getting Train List Page
	driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
	driver.maximize_window()
	#driver.minimize_window()
	driver.get("https://www.irctc.co.in/nget/train-search")
	driver.find_element_by_css_selector("#origin input").send_keys(from_station)
	driver.find_element_by_css_selector("#destination input").send_keys(to_station)
	driver.find_element_by_css_selector("p-calendar input").clear()
	driver.find_element_by_css_selector("p-calendar input").send_keys(Keys.CONTROL + "a")
	driver.find_element_by_css_selector("p-calendar input").send_keys(Keys.DELETE)
	driver.find_element_by_css_selector("p-calendar input").send_keys(get_date)
	driver.find_element_by_css_selector("button.search_btn").click()
	wait(driver,30).until(EC.url_changes("https://www.irctc.co.in/nget/train-list"))
	#End of Inputting Data and Getting Train List Page
	#Disable Chat Bot
	try:
		chatbot = driver.find_element_by_css_selector("#chatbot-service")
		driver.execute_script("arguments[0].style.display = 'none';",chatbot)
	except:
		pass
	#End of Disable Chat Bot
	time.sleep(1)
	#Filtering Trains
	class_ele = driver.find_elements_by_css_selector(".left_div ul li")
	for i in class_ele:
		if i.text.startswith("AC"):
			i.click()
	time.sleep(1)
	#End of filtering Trains
	#Check Train Availability
	avail_ele = driver.find_elements_by_css_selector("#check-availability")
	for i in avail_ele:
		print("click")
		time.sleep(6)
		i.click()
	try:
		for i in driver.find_elements_by_css_selector(".train_avl_enq_box"):
			seat_list.append(i.find_element_by_css_selector(".table tbody tr td div.span3 .updatesDiv span").text)
			train_names.append(i.find_element_by_css_selector("a .trainName").text)
			train_time.append(i.find_element_by_css_selector("h5").text)
	except:
		print("Error Occured")
	driver.close()
	return (seat_list,train_names,train_time)
	#End of Check Train Availability
#Get Input from User
def get_data():
	
	from_inp = from_station.get() 
	to_inp = to_station.get()
	date_inp = date_get.get()
	from_station_name = ""
	to_station_name = ""
	file_obj = open("train_codes.csv")
	csv_reader = csv.reader(file_obj)
	for row in csv_reader:
		if from_inp.upper() == row[2]:
			from_station_name = row[1].upper()
		if to_inp.upper() == row[2]:
			to_station_name = row[1].upper()
	print(from_station_name,to_station_name)
	from_send = from_station_name + " - "+from_inp.upper()
	to_send = to_station_name + " - "+to_inp.upper() 
	if from_inp != "" and to_inp!= "" and date_inp!= "":
		(seat_list,train_names,train_time)  = get_availability(from_send,to_send,date_inp)
	for i in range(0,len(seat_list)):
		print(train_names[i],train_time[i],seat_list[i])
	output(train_names,train_time,seat_list)
#End of Get Input from User
#Create HTML File and Open it
def output(train_names,train_time,seat_list):
	file_obj = open("Sample.html","w")
	doc, tag, text = Doc().tagtext()
	fields = ['Train Name','Departure Time','Availability']
	with tag('table'):
		with tag('tr'):
			for i in range(len(fields)):
				with tag('th',("colspan","2")):
					text(fields[i])
		for i in range(len(seat_list)):
			with tag('tr'):
				for j in range(len(fields)):
					with tag('td',("colspan","2")):
						if(j==0):
							text(train_names[i])
						if(j==1):
							text(train_time[i])
						if(j==2):
							text(seat_list[i])
	code = indent(doc.getvalue())
	file_obj.write(code)
	webbrowser.open('file://' + os.path.realpath("Sample.html"))
#End of Create HTML File and Open it
#Create Window
window_obj = GUI.Tk()
window_obj.title("Train Searcher")
wid,hei = window_obj.winfo_screenwidth(), window_obj.winfo_screenheight()
window_obj.geometry("%dx%d+0+0"%(wid,hei))
for i in range(0,11):
	window_obj.rowconfigure(i,weight = 1)
for i in range(0,5):
	window_obj.columnconfigure(i,weight = 1)
window_obj.configure(background = "coral")
#Adding Widgets
heading_label = Label(window_obj,text ="AVAILABILITY OF SEATS IN TRAIN",font =("Arial",18),fg = "White",bg ="coral")
heading_label.grid(row =0, column =0,columnspan = 4)
from_label = Label(window_obj,text = "From Station",font=("Arial",14),fg = "White",bg ="coral")
from_label.grid(row = 1,column = 1)
from_station = Entry(window_obj,font =("Arial",18),fg = "White",highlightcolor= "white",bg ="coral")
from_station.grid(row =1, column =2)
to_label = Label(window_obj,text = "To Station",font=("Arial",14),fg = "White",bg ="coral")
to_label.grid(row = 2,column = 1)
to_station = Entry(window_obj,font =("Arial",18),highlightcolor= "white",fg = "White",bg ="coral")
to_station.grid(row =2, column =2)
date_get_label = Label(window_obj,text = "Date(dd-mm-yyyy)",font=("Arial",14),fg = "White",bg ="coral")
date_get_label.grid(row = 3,column = 1)
date_get = Entry(window_obj,font =("Arial",18),highlightcolor= "white",fg = "White",bg ="coral")
date_get.grid(row =3, column =2)
go_btn = Button(window_obj,font =("Arial",18),text="Find Availability",activeforeground="white",highlightcolor= "white",fg = "White",bg ="green",activebackground = "green",relief =FLAT, command = get_data)
go_btn.grid(row =4, column =2)
#End of Adding Widgets
window_obj.mainloop()
#End of Create Window

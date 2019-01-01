# IRCTC-Train-ticket-Aavailability-Checking

**This is used for Educational Purpose**

This is a script that is used to check the availability of seats in various trains automatically at a single time by taking inputs from station code, to station code and jouney date.

There are two Python Scripts in this repository. They are:
* train_coder.py
* train_search.py

**train_coder.py:**

train_coder.py is used to fetch data regarding station names and their respective codes. It builds a csv file train_codes.csv that contains the station names and their codes

**train_search.py:**

train_search will build a GUI that has three text fields to enter from station code, to station code, and date in the format of dd-mm-yyyy. Then there is a button to check the availability of seats in various trains **(Sleeper and Sitting only)** available on the given date between given stations.

The GUI built by the train_search.py looks like **GUI Train Search.png**. The output of the script is a html file that is opened automatically and looks like **Result.png**. The output code will be similar to **Sample.html**.

**Pre-requisites needed to run the scripts:**
The following things are needed to run the scripts:

* Python compiler for the operating system
* Chrome Browser
* Chrome driver
* Python Tkinter module
* Python urllib module
* Python selenium module
* Python yattag module

**Excecution of Scripts:**

First execute the **train_coder.py** and built the database of station names and codes. Then execute the **train_search.py** that uses train_codes.csv which generates the output.

## This folder contains Homework 3 for 2018PUI class

1. In the first part of the HW, we are responsible to perform the deletion of data and its history from a GitHub repo.
To do that,  I created a test.csv file in the repo, and then deleted the file and its history through command bash.
The pictures in the **screenshots** folder are prooves that such a history of the test.csv file existed before but not anymore.


2. In the second part of the HW, we are required to choose a file in CSV format from NYC Open Data and use pandas to read the
file and mangle the data within it. 
I chose the Traffic Volume Counts CSV file from NYC Open Data, read the file and plot the data based on requirement. 
For details please see the **HW3_2_XH1163**. ipynb. An extra credit part is also included in the document.


3. In the third part of the HW, I wrote a python script to stream real-time bus data from MTA through the MTA Bus Time interface.
using the API key and URL requested from MTA.
**show_bus_locations_xh1163.py** is the document that takes 2 arguments: the API KEY and the Bus Name (in the following format:
python show_bus_locations_xh1163..py <MTA_KEY> <BUS_LINE>) 
The program will output the following to the console: the bus name, the number of vehicles and their current positions.


4. In the fourth part of the HW, I wrote a Python script that writes information on the next stop location of all busses 
of a given line into a CSV file.
**get_bus_info_xh1163.py** is the document that takes 2 arguments: the API KEY and the Bus Name (in the following format:
python get_bus_info_xh1163.py <MTA_KEY> <BUS_LINE1> <BUS_LINE2>...) 
The program will output the buses information into secreted CSV files, the file will be named as the bus name.


Homework partnership: none.

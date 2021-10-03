# NasaHackBackend

### Getting data
1. install python3 and dependencies
- sudo apt-get install python3.6
- sudo apt-get install python3-pip
- pip install urllib3 <insertMissingDependecies>
2. run the python files from *src* folder with stable connection
- python3 Get_CelesTrak_Data.py # will create new data based on http://celestrak.com/
- python3 Get_Clean_Data.py 	 # will clean data from different source e.g. https://www.space-track.org/auth/login 

### This project is correlated to https://github.com/Renji3/NasaHack
- NasaHack is supposed to be the front end, wheras this project is supposed to be the data generator

### It is advised to add Get_CelesTrak_Data.py to the cron jobs to execute twice a day

### For hosting a static file to the front end use tools like nginx

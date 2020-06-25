import requests
from bs4 import BeautifulSoup
from csv import writer
import re
from datetime import date
import gspread

today = date.today().strftime('%m/%d/%Y')

codyurl = 'https://cod.tracker.gg/warzone/profile/xbl/Alazyturtle7/overview'
nickurl = 'https://cod.tracker.gg/warzone/profile/xbl/shippedmypants1/overview'
justinurl = 'https://cod.tracker.gg/warzone/profile/xbl/sockz%20n%20sandalz/overview'
bondourl = 'https://cod.tracker.gg/warzone/profile/xbl/BoNDo%20Is%20KLuTCH/overview'
loganurl = 'https://cod.tracker.gg/warzone/profile/xbl/CRAZY%20x2BIGx/overview'
ckurl = 'https://cod.tracker.gg/warzone/profile/atvi/koobie2727%239788810/overview'
everetturl = 'https://cod.tracker.gg/warzone/profile/xbl/Prodigychild11/overview'
erichurl = 'https://cod.tracker.gg/warzone/profile/xbl/captn%20ugly/overview'
zachurl = 'https://cod.tracker.gg/warzone/profile/xbl/Beastlyxone/overview'
samurl = 'https://cod.tracker.gg/warzone/profile/xbl/SKILLMASTERX109/overview'
maxurl = 'https://cod.tracker.gg/warzone/profile/xbl/big%20mackie%20xl/overview'
jonurl = 'https://cod.tracker.gg/warzone/profile/atvi/i-love-my-cub%235807885/overview'

# Start of gathering user data

# Get Cody's Data
response = requests.get(codyurl)

soup = BeautifulSoup(response.text,'html.parser')

matches = soup.find_all(class_='matches')[1].get_text() # Get number of matches played

values = []
for value in soup.select('.value'): # Get all other data
    values += [value.get_text()]

codydata = []
codydata += [today, 'Cody']
codydata += [float(re.sub('[^0-9]','',matches))] # Number of matches played with words removed
codydata += [int(values[16])] # Number of wins
codydata += [round(int(values[16])/int(codydata[2]),4)] # Win percentage
codydata += [int(values[17])] # Number of top 5s
codydata += [round(int(values[17])/int(codydata[2]),4)] # Top 5 percentage
codydata += [int(values[18])] # Number of top 10s
codydata += [round(int(values[18])/int(codydata[2]),4)] # Top 10 percentage
codydata += [int(values[19])] # Number of top 25s
codydata += [round(int(values[19])/int(codydata[2]),4)] # Top 25 percentage
codydata += [float(values[22])] # Kill to Death Ratio
codydata += [float(re.sub(',','',values[3]))] # Damage per Game
codydata += [values[24].replace("m ",":").replace("s","")] # Average life length
codydata += [float(re.sub(',','',values[26]))] # Average Score per Minute
codydata += [float(re.sub(',','',values[27]))] # Average Score per Game

# Get nick's Data
response = requests.get(nickurl)

soup = BeautifulSoup(response.text,'html.parser')

matches = soup.find_all(class_='matches')[1].get_text() # Get number of matches

values = []
for value in soup.select('.value'): # Get all other data
    values += [value.get_text()]

nickdata = []
nickdata += [today, 'Nick']
nickdata += [float(re.sub('[^0-9]','',matches))] # Number of matches played with words removed
nickdata += [int(values[16])] # Number of wins
nickdata += [round(int(values[16])/int(nickdata[2]),4)] # Win percentage
nickdata += [int(values[17])] # Number of top 5s
nickdata += [round(int(values[17])/int(nickdata[2]),4)] # Top 5 percentage
nickdata += [int(values[18])] # Number of top 10s
nickdata += [round(int(values[18])/int(nickdata[2]),4)] # Top 10 percentage
nickdata += [int(values[19])] # Number of top 25s
nickdata += [round(int(values[19])/int(nickdata[2]),4)] # Top 25 percentage
nickdata += [float(values[22])] # Kill to Death Ratio
nickdata += [float(re.sub(',','',values[3]))] # Damage per Game
nickdata += [values[24].replace("m ",":").replace("s","")] # Average life length
nickdata += [float(re.sub(',','',values[26]))] # Average Score per Minute
nickdata += [float(re.sub(',','',values[27]))] # Average Score per Game

# Get justin's Data
response = requests.get(justinurl)

soup = BeautifulSoup(response.text,'html.parser')

matches = soup.find_all(class_='matches')[1].get_text() # Get number of matches 

values = []
for value in soup.select('.value'): # Get all other data
    values += [value.get_text()]

justindata = []
justindata += [today, 'Justin']
justindata += [float(re.sub('[^0-9]','',matches))] # Number of matches played with words removed
justindata += [int(values[16])] # Number of wins
justindata += [round(int(values[16])/int(justindata[2]),4)] # Win percentage
justindata += [int(values[17])] # Number of top 5s
justindata += [round(int(values[17])/int(justindata[2]),4)] # Top 5 percentage
justindata += [int(values[18])] # Number of top 10s
justindata += [round(int(values[18])/int(justindata[2]),4)] # Top 10 percentage
justindata += [int(values[19])] # Number of top 25s
justindata += [round(int(values[19])/int(justindata[2]),4)] # Top 25 percentage
justindata += [float(values[22])] # Kill to Death Ratio
justindata += [float(re.sub(',','',values[3]))] # Damage per Game
justindata += [values[24].replace("m ",":").replace("s","")] # Average life length
justindata += [float(re.sub(',','',values[26]))] # Average Score per Minute
justindata += [float(re.sub(',','',values[27]))] # Average Score per Game

# Get bondo's Data
response = requests.get(bondourl)

soup = BeautifulSoup(response.text,'html.parser')

matches = soup.find_all(class_='matches')[1].get_text() # Get number of matches

values = []
for value in soup.select('.value'): # Get all other data
    values += [value.get_text()]

bondodata = []
bondodata += [today, 'Bondo']
bondodata += [float(re.sub('[^0-9]','',matches))] # Number of matches played with words removed
bondodata += [int(values[16])] # Number of wins
bondodata += [round(int(values[16])/int(bondodata[2]),4)] # Win percentage
bondodata += [int(values[17])] # Number of top 5s
bondodata += [round(int(values[17])/int(bondodata[2]),4)] # Top 5 percentage
bondodata += [int(values[18])] # Number of top 10s
bondodata += [round(int(values[18])/int(bondodata[2]),4)] # Top 10 percentage
bondodata += [int(values[19])] # Number of top 25s
bondodata += [round(int(values[19])/int(bondodata[2]),4)] # Top 25 percentage
bondodata += [float(values[22])] # Kill to Death Ratio
bondodata += [float(re.sub(',','',values[3]))] # Damage per Game
bondodata += [values[24].replace("m ",":").replace("s","")] # Average life length
bondodata += [float(re.sub(',','',values[26]))] # Average Score per Minute
bondodata += [float(re.sub(',','',values[27]))] # Average Score per Game

# Get logan's Data
response = requests.get(loganurl)

soup = BeautifulSoup(response.text,'html.parser')

matches = soup.find_all(class_='matches')[1].get_text() # Get number of matches 

values = []
for value in soup.select('.value'): # Get all other data
    values += [value.get_text()]

logandata = []
logandata += [today, 'Logan']
logandata += [float(re.sub('[^0-9]','',matches))] # Number of matches played with words removed
logandata += [int(values[16])] # Number of wins
logandata += [round(int(values[16])/int(logandata[2]),4)] # Win percentage
logandata += [int(values[17])] # Number of top 5s
logandata += [round(int(values[17])/int(logandata[2]),4)] # Top 5 percentage
logandata += [int(values[18])] # Number of top 10s
logandata += [round(int(values[18])/int(logandata[2]),4)] # Top 10 percentage
logandata += [int(values[19])] # Number of top 25s
logandata += [round(int(values[19])/int(logandata[2]),4)] # Top 25 percentage
logandata += [float(values[22])] # Kill to Death Ratio
logandata += [float(re.sub(',','',values[3]))] # Damage per Game
logandata += [values[24].replace("m ",":").replace("s","")] # Average life length
logandata += [float(re.sub(',','',values[26]))] # Average Score per Minute
logandata += [float(re.sub(',','',values[27]))] # Average Score per Game

# Get ck's Data
response = requests.get(ckurl)

soup = BeautifulSoup(response.text,'html.parser')

matches = soup.find_all(class_='matches')[1].get_text() # Get number of matches 

values = []
for value in soup.select('.value'): # Get all other data
    values += [value.get_text()]

ckdata = []
ckdata += [today, 'CK']
ckdata += [float(re.sub('[^0-9]','',matches))] # Number of matches played with words removed
ckdata += [int(values[16])] # Number of wins
ckdata += [round(int(values[16])/int(ckdata[2]),4)] # Win percentage
ckdata += [int(values[17])] # Number of top 5s
ckdata += [round(int(values[17])/int(ckdata[2]),4)] # Top 5 percentage
ckdata += [int(values[18])] # Number of top 10s
ckdata += [round(int(values[18])/int(ckdata[2]),4)] # Top 10 percentage
ckdata += [int(values[19])] # Number of top 25s
ckdata += [round(int(values[19])/int(ckdata[2]),4)] # Top 25 percentage
ckdata += [float(values[22])] # Kill to Death Ratio
ckdata += [float(re.sub(',','',values[3]))] # Damage per Game
ckdata += [values[24].replace("m ",":").replace("s","")] # Average life length
ckdata += [float(re.sub(',','',values[26]))] # Average Score per Minute
ckdata += [float(re.sub(',','',values[27]))] # Average Score per Game

# Get everett's Data
response = requests.get(everetturl)

soup = BeautifulSoup(response.text,'html.parser')

matches = soup.find_all(class_='matches')[1].get_text() # Get number of matches 

values = []
for value in soup.select('.value'): # Get all other data
    values += [value.get_text()]

everettdata = []
everettdata += [today, 'Everett']
everettdata += [float(re.sub('[^0-9]','',matches))] # Number of matches played with words removed
everettdata += [int(values[16])] # Number of wins
everettdata += [round(int(values[16])/int(everettdata[2]),4)] # Win percentage
everettdata += [int(values[17])] # Number of top 5s
everettdata += [round(int(values[17])/int(everettdata[2]),4)] # Top 5 percentage
everettdata += [int(values[18])] # Number of top 10s
everettdata += [round(int(values[18])/int(everettdata[2]),4)] # Top 10 percentage
everettdata += [int(values[19])] # Number of top 25s
everettdata += [round(int(values[19])/int(everettdata[2]),4)] # Top 25 percentage
everettdata += [float(values[22])] # Kill to Death Ratio
everettdata += [float(re.sub(',','',values[3]))] # Damage per Game
everettdata += [values[24].replace("m ",":").replace("s","")] # Average life length
everettdata += [float(re.sub(',','',values[26]))] # Average Score per Minute
everettdata += [float(re.sub(',','',values[27]))] # Average Score per Game

# Get erich's Data
response = requests.get(erichurl)

soup = BeautifulSoup(response.text,'html.parser')

matches = soup.find_all(class_='matches')[1].get_text() # Get number of matches 

values = []
for value in soup.select('.value'): # Get all other data
    values += [value.get_text()]

erichdata = []
erichdata += [today, 'Erich']
erichdata += [float(re.sub('[^0-9]','',matches))] # Number of matches played with words removed
erichdata += [int(values[16])] # Number of wins
erichdata += [round(int(values[16])/int(erichdata[2]),4)] # Win percentage
erichdata += [int(values[17])] # Number of top 5s
erichdata += [round(int(values[17])/int(erichdata[2]),4)] # Top 5 percentage
erichdata += [int(values[18])] # Number of top 10s
erichdata += [round(int(values[18])/int(erichdata[2]),4)] # Top 10 percentage
erichdata += [int(values[19])] # Number of top 25s
erichdata += [round(int(values[19])/int(erichdata[2]),4)] # Top 25 percentage
erichdata += [float(values[22])] # Kill to Death Ratio
erichdata += [float(re.sub(',','',values[3]))] # Damage per Game
erichdata += [values[24].replace("m ",":").replace("s","")] # Average life length
erichdata += [float(re.sub(',','',values[26]))] # Average Score per Minute
erichdata += [float(re.sub(',','',values[27]))] # Average Score per Game

# Get zach's Data
response = requests.get(zachurl)

soup = BeautifulSoup(response.text,'html.parser')

matches = soup.find_all(class_='matches')[1].get_text() # Get number of matches 

values = []
for value in soup.select('.value'): # Get all other data
    values += [value.get_text()]

zachdata = []
zachdata += [today, 'Zach']
zachdata += [float(re.sub('[^0-9]','',matches))] # Number of matches played with words removed
zachdata += [int(values[16])] # Number of wins
zachdata += [round(int(values[16])/int(zachdata[2]),4)] # Win percentage
zachdata += [int(values[17])] # Number of top 5s
zachdata += [round(int(values[17])/int(zachdata[2]),4)] # Top 5 percentage
zachdata += [int(values[18])] # Number of top 10s
zachdata += [round(int(values[18])/int(zachdata[2]),4)] # Top 10 percentage
zachdata += [int(values[19])] # Number of top 25s
zachdata += [round(int(values[19])/int(zachdata[2]),4)] # Top 25 percentage
zachdata += [float(values[22])] # Kill to Death Ratio
zachdata += [float(re.sub(',','',values[3]))] # Damage per Game
zachdata += [values[24].replace("m ",":").replace("s","")] # Average life length
zachdata += [float(re.sub(',','',values[26]))] # Average Score per Minute
zachdata += [float(re.sub(',','',values[27]))] # Average Score per Game

# Get sam's Data
response = requests.get(samurl)

soup = BeautifulSoup(response.text,'html.parser')

matches = soup.find_all(class_='matches')[1].get_text() # Get number of matches 

values = []
for value in soup.select('.value'): # Get all other data
    values += [value.get_text()]

samdata = []
samdata += [today, 'Sam']
samdata += [float(re.sub('[^0-9]','',matches))] # Number of matches played with words removed
samdata += [int(values[16])] # Number of wins
samdata += [round(int(values[16])/int(samdata[2]),4)] # Win percentage
samdata += [int(values[17])] # Number of top 5s
samdata += [round(int(values[17])/int(samdata[2]),4)] # Top 5 percentage
samdata += [int(values[18])] # Number of top 10s
samdata += [round(int(values[18])/int(samdata[2]),4)] # Top 10 percentage
samdata += [int(values[19])] # Number of top 25s
samdata += [round(int(values[19])/int(samdata[2]),4)] # Top 25 percentage
samdata += [float(values[22])] # Kill to Death Ratio
samdata += [float(re.sub(',','',values[3]))] # Damage per Game
samdata += [values[24].replace("m ",":").replace("s","")] # Average life length
samdata += [float(re.sub(',','',values[26]))] # Average Score per Minute
samdata += [float(re.sub(',','',values[27]))] # Average Score per Game

# Get max's Data
response = requests.get(maxurl)

soup = BeautifulSoup(response.text,'html.parser')

matches = soup.find_all(class_='matches')[1].get_text() # Get number of matches 

values = []
for value in soup.select('.value'): # Get all other data
    values += [value.get_text()]

maxdata = []
maxdata += [today, 'Max']
maxdata += [float(re.sub('[^0-9]','',matches))] # Number of matches played with words removed
maxdata += [int(values[16])] # Number of wins
maxdata += [round(int(values[16])/int(maxdata[2]),4)] # Win percentage
maxdata += [int(values[17])] # Number of top 5s
maxdata += [round(int(values[17])/int(maxdata[2]),4)] # Top 5 percentage
maxdata += [int(values[18])] # Number of top 10s
maxdata += [round(int(values[18])/int(maxdata[2]),4)] # Top 10 percentage
maxdata += [int(values[19])] # Number of top 25s
maxdata += [round(int(values[19])/int(maxdata[2]),4)] # Top 25 percentage
maxdata += [float(values[22])] # Kill to Death Ratio
maxdata += [float(re.sub(',','',values[3]))] # Damage per Game
maxdata += [values[24].replace("m ",":").replace("s","")] # Average life length
maxdata += [float(re.sub(',','',values[26]))] # Average Score per Minute
maxdata += [float(re.sub(',','',values[27]))] # Average Score per Game

# Get jon's Data
response = requests.get(jonurl)

soup = BeautifulSoup(response.text,'html.parser')

matches = soup.find_all(class_='matches')[1].get_text() # Get number of matches 

values = []
for value in soup.select('.value'): # Get all other data
    values += [value.get_text()]

jondata = []
jondata += [today, 'Jon']
jondata += [float(re.sub('[^0-9]','',matches))] # Number of matches played with words removed
jondata += [int(values[16])] # Number of wins
jondata += [round(int(values[16])/int(jondata[2]),4)] # Win percentage
jondata += [int(values[17])] # Number of top 5s
jondata += [round(int(values[17])/int(jondata[2]),4)] # Top 5 percentage
jondata += [int(values[18])] # Number of top 10s
jondata += [round(int(values[18])/int(jondata[2]),4)] # Top 10 percentage
jondata += [int(values[19])] # Number of top 25s
jondata += [round(int(values[19])/int(jondata[2]),4)] # Top 25 percentage
jondata += [float(values[22])] # Kill to Death Ratio
jondata += [float(re.sub(',','',values[3]))] # Damage per Game
jondata += [values[24].replace("m ",":").replace("s","")] # Average life length
jondata += [float(re.sub(',','',values[26]))] # Average Score per Minute
jondata += [float(re.sub(',','',values[27]))] # Average Score per Game

# End of gathering user data


# Write data to csv file

csvname = str(date.today().strftime('%Y_%m_%d')) + "_warzone_data.csv"
with open(csvname, 'w', newline='') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(codydata)
    csv_writer.writerow(nickdata)    
    csv_writer.writerow(justindata)
    csv_writer.writerow(bondodata)
    csv_writer.writerow(logandata)
    csv_writer.writerow(ckdata)
    csv_writer.writerow(everettdata)
    csv_writer.writerow(erichdata)
    csv_writer.writerow(zachdata)
    csv_writer.writerow(samdata)
    csv_writer.writerow(maxdata)
    csv_writer.writerow(jondata)

# Write data to google sheets

gc = gspread.service_account(filename='G:\python\COD_Warzone_Data\client_secret.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Q7pArMUHR_dGr3Bjk-FvogxhG3hHbouUIZ7ElAv8YwI/edit#gid=1520860220').worksheet("Raw Data")
sh.append_row(codydata, value_input_option='USER_ENTERED')
sh.append_row(nickdata, value_input_option='USER_ENTERED')
sh.append_row(justindata, value_input_option='USER_ENTERED')
sh.append_row(bondodata, value_input_option='USER_ENTERED')
sh.append_row(logandata, value_input_option='USER_ENTERED')
sh.append_row(ckdata, value_input_option='USER_ENTERED')
sh.append_row(everettdata, value_input_option='USER_ENTERED')
sh.append_row(erichdata, value_input_option='USER_ENTERED')
sh.append_row(zachdata, value_input_option='USER_ENTERED')
sh.append_row(samdata, value_input_option='USER_ENTERED')
sh.append_row(maxdata, value_input_option='USER_ENTERED')
sh.append_row(jondata, value_input_option='USER_ENTERED')

sh.format('A62:A', {
    "numberFormat": {
      "type": "DATE"
    }})

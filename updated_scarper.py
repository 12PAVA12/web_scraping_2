from bs4 import BeautifulSoup
import requests
import pandas as pd

star_names = []
distance = []
mass = []
radius = []
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

webpage = requests.get(START_URL, verify = False)
headers = ["Star_Name", "Distance", "Mass", "Radius"]
soup = BeautifulSoup(webpage.content, "html.parser")
tables = soup.find_all('table', attrs = {"class" : "wikitable sortable"})
table = tables[2]
tables_rows = table.find_all('tr')

star_list = []
for rows in tables_rows:
    table_data = rows.find_all('td')
    row = [data.text.strip() for data in table_data]
    star_list.append(row)

for table_data in range(1, len(star_list)):
    data = star_list[table_data]
    star_names.append(data[0])
    distance.append(data[5])
    mass.append(data[7])
    radius.append(data[8])

star_data = zip(star_names, distance, mass, radius)
star_data_list = pd.DataFrame(star_data, columns = headers)
star_data_list.to_csv("dwarfs_planet.csv", index = False)
print("page scraped")
from bs4 import BeautifulSoup
import requests
import pandas as pd

name = []
distance = []
mass = []
radius = []

START_URL = ("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")
wiki = requests.get(START_URL)
soup = BeautifulSoup(wiki.text, "html.parser")
temp_list = []

for tr in soup.find("table").find_all("tr"):
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

for i in range(1, len(temp_list)):
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    name.append(temp_list[i][1])
    distance.append(temp_list[i][3])

data = pd.DataFrame(
    list(zip(name, distance, mass, radius)),
    columns=["Star_name", "Distance", "Mass", "Radius"],
)
print("page scraped")
data.to_csv("srcaper.csv")
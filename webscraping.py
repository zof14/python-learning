import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
db2_name = "Ranking.db"
table_name = "Top"
table2_name = "Highest Rotten Tomatoes' Ranking"

csv_path = r"C:\Users\User\Desktop\python-learning\top_50_films.csv"
csv2_path = r"C:\Users\User\Desktop\python-learning\worst_50_films.csv"

df = pd.DataFrame(columns=["Average Rank","Film","Year"])
df_rt = pd.DataFrame(columns=["Rotten Tomatoes' Ranking","Film","Year"])
count = 0

html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

for row in rows:
    if count<50:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {"Average Rank": col[0].contents[0],
                         "Film": col[1].contents[0],
                         "Year": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break




for row in rows:
    cols = row.find_all('td')
    if len(cols) !=0 and cols[3].contents[0]!= "unranked":
        data_dict = {
            "Rotten Tomatoes' Ranking": cols[3].contents[0],
            "Film": cols[1].contents[0],
            "Year": cols[2].contents[0]
        }
        df_row = pd.DataFrame(data_dict, index=[0])
        df_rt = pd.concat([df_rt, df_row], ignore_index=True)

df_rt["Rotten Tomatoes' Ranking"] = pd.to_numeric(df_rt["Rotten Tomatoes' Ranking"], errors='coerce')
df_rt = df_rt.sort_values(by="Rotten Tomatoes' Ranking",ascending=False).head(50)


df.to_csv(csv_path)
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()

df_rt.to_csv(csv2_path)
conn = sqlite3.connect(db2_name)
df_rt.to_sql(table2_name, conn, if_exists='replace', index=False)
conn.close()
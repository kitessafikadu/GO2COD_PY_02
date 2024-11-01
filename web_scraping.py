import pandas as pd
import requests
from bs4 import BeautifulSoup

link = "https://ceoworld.biz/2024/01/12/richest-billionaires-2024/"
link_text = requests.get(link).text

soup = BeautifulSoup(link_text, 'html.parser')

table = soup.find('table', id='tablepress-738') 

if table is None:
    print("The specific table was not found. Please verify the ID.")
else:
    columns = ["Rank", "Company", "Executive Name", "Net Worth", "Country"]
    df = pd.DataFrame(columns=columns)

    rows = table.find_all('tr')[1:]  
    for row in rows:
        rank = row.find('td', class_='column-1').text.strip()
        company = row.find('td', class_='column-2').text.strip()
        executive_name = row.find('td', class_='column-3').text.strip()
        net_worth = row.find('td', class_='column-4').text.strip()
        country = row.find('td', class_='column-5').text.strip()

        df.loc[len(df)] = [rank, company, executive_name, net_worth, country]

    df['Net Worth'] = (
        df['Net Worth']
        .str.replace('[\$, B]', '', regex=True) 
        .astype(float)
    )

    top_ten_richest = df.sort_values(by='Net Worth', ascending=False).head(10)
    print(top_ten_richest[['Rank', 'Company', 'Executive Name', 'Net Worth', 'Country']])
    top_ten_richest.to_csv(r'D:/Projects/PYTHON/GO2COD/top_ten_richest.csv', index=False)

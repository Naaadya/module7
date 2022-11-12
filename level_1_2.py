import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import datetime

page = requests.get('https://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
rows =  soup.find("table", {'class':'mfd-table mfd-currency-table'}).find_all("tr")
print("--------- START-----------")
data = []
dates = []
for ind, row in enumerate(rows):
    if ind == 0:#пропускаем первую строчку таблицы с заголовком
        continue
    cells = row.find_all("td")
    print(f"{cells[0].text} {cells[1].text} {cells[2].text}")
    dateStr = cells[0].text.replace("с ","")#убираем букву с
    date = datetime.datetime.strptime(dateStr,'%d.%m.%Y').date()#выводим на конслоь для отладки
    dates.append(date)
    data.append(float(cells[1].text))

print("--------FINISH------------")


data.reverse()
dates.reverse()
plt.plot(dates, data)
plt.show()

        
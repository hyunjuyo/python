import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

def get_country_list():
    r = requests.get(url)
    if r.status_code != 200:
        print("Check url!")
        exit()
    soup = BeautifulSoup(r.text, "html.parser")
    table_total = soup.find(name="table", attrs={"class":"table table-bordered downloads tablesorter"})
    tables = table_total.find_all("tr")

    country = []
    for table in tables[1:]:
        infos = table.find_all("td")
        if infos[1].string == "No universal currency":
            continue
        sub_list = []
        for v in infos[::2]:
            sub_list.append(v.string)
        country.append(sub_list)
    
    for str in country:
        str[0] = str[0].capitalize()
    
    return country

def main():
    print("Hello! Please choose select a country by number:")
    country = get_country_list()

    max_index = 0
    for i, infos in enumerate(country):
        print(f"# {i} {infos[0]}")
        max_index = i

    while(1):
        input_num = input("#: ")
        
        try:
            i = int(input_num)
        except ValueError:
            print("That wasn't a number.")
            continue
        else:
            if i >= 0 and i <= max_index:
                print(f"You chose {country[i][0]}")
                print(f"The currency code is {country[i][1]}")
                break
            else:
                print("Choose a numer from the list.")
                continue

main()
from bs4 import BeautifulSoup
from requests import get
import json


class JsonSave:
    def save_to_json(self, brand: str, model: str):

        response = get(f'https://www.olx.pl/motoryzacja/samochody/'
                       f'{brand}/?search%5Bfilter_enum_model%5D%5B0%5D={model}')

        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all(class_='css-u2ayx9')

        json_dict = {}
        path = input('podaj sciezke do zapisania pliku json: ')
        with open(f'{path}/olx_input.json', 'w', encoding='utf-8') as file:
            for item in data:
                # title
                json_dict['name'] = item.select_one('h6').text
                # price
                json_dict['price'] = item.select_one('p').text

                # ensure_ascii - wyswietla polskie znaki w pliku
                file.write(json.dumps(json_dict, ensure_ascii=False))
                file.write('\n')

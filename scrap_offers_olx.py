from bs4 import BeautifulSoup
from requests import get


class Offers:
    def get_offers(self, brand: str, model: str):
        # if brand name has more than 1 word -> it must be 1 word in the link below
        brand_olx = brand.replace(' ', '')
        response = get(f'https://www.olx.pl/motoryzacja/samochody/'
                       f'{brand_olx}/?search%5Bfilter_enum_model%5D%5B0%5D={model}')

        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all(class_='css-u2ayx9')

        for item in data:
            # offers title
            name = item.select_one('h6').text
            # offers price
            price = item.select_one('p').text
            if \
                    brand.capitalize() in list(name.split()) \
                    or brand in list(name.split())\
                    or model in list(name.split()) \
                    or model.capitalize() in list(name.split())\
                    or brand.upper() in list(name.split()) \
                    or brand.title() in name:
                print(name)
                print(price.replace('złdo', 'zł do'))
            else:
                print('We do not have offers for chosen model!')
                break

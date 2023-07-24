from bs4 import BeautifulSoup
from requests import get


class Offers:
    def get_offers(self, brand: str, model: str):
        brand_olx = brand.replace(' ', '')
        response = get(f'https://www.olx.pl/motoryzacja/samochody/'
                       f'{brand_olx}/?search%5Bfilter_enum_model%5D%5B0%5D={model}')

        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all(class_='css-u2ayx9')

        for item in data:
            # title
            name = item.select_one('h6').text
            if \
                    brand.capitalize() in list(name.split()) \
                    or brand in list(name.split())\
                    or model in list(name.split()) \
                    or model.capitalize() in list(name.split())\
                    or brand.upper() in list(name.split()) \
                    or brand.title() in name:
                print(name)
            else:
                # print('error')
                print('Niestety nie mamy ofert dla wybranego pojazdu!')
                break


# scrap = Offers()
# scrap.get_offers('aixam', 'a721')
# scrap.get_offers('audi', 'a1')
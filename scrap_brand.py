from requests import get
from bs4 import BeautifulSoup


class Brand:
    def scrap_brand_olx(self):
        response = get('https://www.olx.pl/motoryzacja/samochody/')
        soup = BeautifulSoup(response.text, 'html.parser')

        data = soup.find_all('li', class_='css-szrfjb')

        car_brand = []
        for brands in data:
            if brands.select('a') is not None:
                for brand in brands.select('a'):
                    # The .contents attribute is a list with all its children elements
                    # If the current element does not contain nested HTML elements,
                    # then .contents[0] will be just the text inside it
                    car_brand.append(brand.contents[0].lower())

        return car_brand

    def check(self, brand: str):
        if brand not in self.scrap_brand_olx():
            print('Cannot find chosen brand! Try again!')
            return False
        else:
            print('Choose model from the list!')
            return True

    def question(self):
        for item in self.scrap_brand_olx():
            print(item, end=', ')
        print('\n')

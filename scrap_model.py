from requests import get
from bs4 import BeautifulSoup


class Model:
    def scrap_model_autocentrum(self, brand: str):
        brand = brand.replace(' ', '-')
        response_at = get(f'https://www.autocentrum.pl/dane-techniczne/{brand}/')
        soup = BeautifulSoup(response_at.text, 'html.parser')

        car_models = []
        models = soup.find_all(class_='name-of-the-car')
        for model in models:
            car_models.append(model.text.strip().lower())

        return car_models

    def question(self, brand: str):
        for item in self.scrap_model_autocentrum(brand):
            print(item, end=', ')
        print('\n')

    def check(self, brand: str, model: str):
        if model not in self.scrap_model_autocentrum(brand):
            print('nie odnaleziono modelu!')
            return False
        else:
            return True


# car_model = Model()
# car_model.scrap_model_autocentrum('opel')

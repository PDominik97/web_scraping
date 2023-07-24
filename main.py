from scrap_brand import Brand
from scrap_model import Model
from scrap_offers_olx import Offers

brands = Brand()
models = Model()
offers = Offers()

if __name__ == '__main__':
    print('Wybierz marke pojazdu z listy!')
    brands.question()
    brand = input('podaj marke z listy: ')
    if brands.check(brand) is True:
        models.question(brand)
        model = input('Model: ')
        if models.check(brand, model) is True:
            if len(model) > 3:
                model = model.replace(' ', '')
            offers.get_offers(brand, model)


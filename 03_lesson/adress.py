class Adress():
    def __init__(self, index, city, street, house, appartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.appartment = appartment

    def __str__(self):
        return f"индекс{self.index}, город{self.city}, улица{self.street}, дом{self.house} - квартира{self.appartment}"
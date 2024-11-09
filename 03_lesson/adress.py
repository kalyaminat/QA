class Adress():
    def __init__(self, post_code, city, street, building, appartment):
        self.post_code = post_code
        self.city = city
        self.street = street
        self.building = building
        self.appartment = appartment

    def __str__(self):
        return f"{self.index}, {self.city}, {self.street}, {self.house} - {self.apartment}"
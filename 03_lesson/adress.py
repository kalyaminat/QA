class Adress():
    def __init__(self, индекс, город, улица, дом, квартира):
        self.индекс = индекс
        self.город = город
        self.улица = улица
        self.дом = дом
        self.квартира = квартира

    def __str__(self):
        return f"{self.индекс}, {self.город}, {self.улица}, {self.дом} - {self.квартира}"
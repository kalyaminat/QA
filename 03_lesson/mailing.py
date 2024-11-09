from adress import Adress
class Mailing():
    def __init__(self, to_adress: Adress, from_adress: Adress, cost: int, track: str ):
        self.to_adress = to_adress
        self.from_adress = from_adress
        self.cost = cost
        self.track = track

    def getMailing(self):
        print(f'Отправление {self.track} из {self.from_adress} в {self.to_adress}. Стоимость {self.cost} рублей')
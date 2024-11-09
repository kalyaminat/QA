from smartphone import Smartphone
smartphone1 = Smartphone('Apple', 'IPhone 11 Pro', '+79991111111')
smartphone2 = Smartphone('Samsung', 'Galaxy A52', '+79992222222')
smartphone3 = Smartphone('Honor', '200 Lite', '+79993333333')
smartphone4 = Smartphone('Huawei', 'Nova 11I', '+79994444444')
smartphone5 = Smartphone('Tecno', 'Camon 20Pro', '+79995555555')

catalog = [smartphone1, smartphone2, smartphone3, smartphone4, smartphone5]

for elem in catalog:
    print(elem.getSmartphone())
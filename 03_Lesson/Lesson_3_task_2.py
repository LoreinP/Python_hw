from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Sumsung", "Galaxy A32", "+79147154848")
phone2 = Smartphone("Xiaomi", "POCO C65", "+79187133535")
phone3 = Smartphone("Tecno", "POVA 4 pro", "+79147565838")
phone4 = Smartphone("Apple", "G900", "+79156881213")
phone5 = Smartphone("Apple", "iPhone SS", "+79177171111")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)


for Smartphone in catalog:
    print(f"{Smartphone.brand} - {Smartphone.model} - {Smartphone.phone_number}")

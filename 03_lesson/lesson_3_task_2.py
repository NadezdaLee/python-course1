from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79111111111"),
    Smartphone("Samsung", "Galaxy S23", "+79222222222"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79333333333"),
    Smartphone("Google", "Pixel 7", "+79444444444"),
    Smartphone("Huawei", "P60", "+79555555555"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")

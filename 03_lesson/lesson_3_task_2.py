from smartphone import Smartphone

catalog = [
    Smartphone('Samsung', 'A-35', '+79236667853'),
    Smartphone('Xiaomi', 'M6', '+79237897853'),
    Smartphone('Honor', '200', '+79236467823'),
    Smartphone('Motorola', 'Razr 50', '+79226477853'),
    Smartphone('Google', 'Pixel 8', '+79235667899')
]

for tel in catalog:
    print(f'{tel.brand} - {tel.model}. {tel.number}.')

import random

def generate_email():
    
    #Генерирует уникальный email в формате:
    #имя_фамилия_когорта_3цифры@домен

    random_digits = random.randint(100, 999)
    return f"viktor_lata_39_{random_digits}@yandex.ru"

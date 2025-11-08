import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

def exchange(rate, currencycode):
    print("Валюта:", currencycode, "\nКурс на даний момент:", rate) 
    result = float(rate) * float(input("Введіть суму для обміну: "))
    print("Обмін успішний! Результат:", round(result, 2), "UAH")

while True:

    choice = input("Введіть 'show' для показу курсу валют, код валюти(cc) для обміну на UAH або exit для виходу: ")

    match choice:
        case "show":
            for elem in response.json():
                if (elem["cc"] == "EUR" or elem["cc"] == "USD" or elem["cc"] == "PLN"):
                    print(elem)

        case "EUR" | "eur":
            for elem in response.json():
                if (elem["cc"] == "EUR"):
                    exchange(elem["rate"], elem["cc"])
                    
        case "USD" | "usd":
            for elem in response.json():
                if (elem["cc"] == "USD"):
                    exchange(elem["rate"], elem["cc"])

        case "PLN" | "pln":
            for elem in response.json():
                if (elem["cc"] == "PLN"):
                    exchange(elem["rate"], elem["cc"])

        case "exit":
            break
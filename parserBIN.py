import requests
from bs4 import BeautifulSoup

def fetch_bin_details(bin_number):
    url = f"https://bincheck.io/ru/details/{bin_number}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем успешность запроса
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Находим все элементы с классом 'hover:text-blue-500'
        elements = soup.find_all('a', {'class': 'hover:text-blue-500'})  # Измените на реальный класс элемента

        if len(elements) >= 2:
            # Предполагаем, что первый элемент - это банк, а второй - страна
            bank_name = elements[0].text.strip()
            country_name = elements[1].text.strip()
            return bank_name, country_name
        else:
            return None, None

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"Error occurred: {err}")
    
    return None, None

def Bin(bin_number):
    try:
        bank_name, country_name = fetch_bin_details(bin_number)
        return [bank_name , country_name]
    except:
        return [None, None]

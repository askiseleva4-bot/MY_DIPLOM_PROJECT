# Импорт настроек из модуля configuration
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Определение функции создания нового заказа POST запрос
def create_order(order_body):
# Выполнение POST запроса
    return requests.post (configuration.URL_MAIN + configuration.URL_NEW_ORDER, json = order_body)

# Определение функции получение информации о треке заказа
def get_order_info (track_number):
    return requests.get (configuration.URL_MAIN + configuration.URL_INFO_ORDER + str(track_number))
     
    
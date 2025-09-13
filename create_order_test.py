# Импортируем модуль sender_stand_request
import sender_stand_request

# Импорт данных запроса из модуля data
import data

# Функция получения данных о заказе по треку
def test_get_order_info():
    track = sender_stand_request.create_order(data.order_body).json()['track']
    response = sender_stand_request.get_order_info(track)
    assert response.status_code == 200
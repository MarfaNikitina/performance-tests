import time

import httpx  # Импортируем библиотеку HTTPX

# Данные для создания пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Выполняем запрос на создание пользователя
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Данные для создания кредитного счета
open_credit_card_account_payload = {
    "userId": create_user_response_data['user']['id']
}

# Выполняем запрос на создание крдитного счета
open_credit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account", json=open_credit_card_account_payload)
open_credit_card_account_data = open_credit_card_account_response.json()

# Данные для выполнения операции покупки
make_purchase_operation_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "cardId": open_credit_card_account_data['account']['cards'][0]['id'],
    "accountId": open_credit_card_account_data['account']['id'],
    "category": "taxi"
}

# Выполнение операции покупки
make_purchase_operation_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation", json=make_purchase_operation_payload)
make_purchase_operation_data = make_purchase_operation_response.json()

# выполняем запрос получения чека по операции покупки
get_operation_receipt_response = httpx.get(
    f"http://localhost:8003/api/v1/operations/operation-receipt/"
    f"{make_purchase_operation_data['operation']['id']}"
)

get_operation_receipt_response_data = get_operation_receipt_response.json()

# Выводим полученные данные
print("Get operation receipt response:", get_operation_receipt_response_data)
print("Status Code:", get_operation_receipt_response.status_code)

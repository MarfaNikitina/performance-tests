from typing import TypedDict
import random
from clients.http.gateway.client import build_gateway_http_client

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from enum import Enum

class StatusEnum(str, Enum):
    """
    Enum для выбора статуса.
    """
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"

class OperationDict(TypedDict):
    """
    Описание структуры операции.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str

class OperationReceiptDict(TypedDict):
    """
    Описание структуры чека.
    """
    url: str
    document: str

class GetOperationResponseDict(TypedDict):
    """
    Описание структуры ответа для получения данных по операции.
    """
    operation: OperationDict

class GetOperationsResponseDict(TypedDict):
    """
    Описание структуры ответа для получения списка операций по счету.
    """
    operations: list[OperationDict]

class GetOperationReceiptResponseDict(TypedDict):
    """
    Описание структуры ответа  для получения чека по операции.
    """
    receipt: OperationReceiptDict

class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    accountId: str

class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """
    accountId: str

class OperationsSummaryDict(TypedDict):
    """
    Описание структуры статистики по операциям для определенного счета.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float

class GetOperationSummaryResponseDict(TypedDict):
    """
    Описание структуры ответа для получения статистики по операциям для определенного счета.
    """
    summary: OperationsSummaryDict

class MakeFeeOperationRequestDict(TypedDict):
    """
    Структура данных для создание операции комиссии.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeFeeOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции комиссии.
    """
    operation: OperationDict

class MakeTopUpOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции пополнения.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTopUpOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции пополнения.
    """
    operation: OperationDict

class MakeCashbackOperationRequestDict(TypedDict):
    """
    Структура данных для создание операции кэшбэка.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashbackOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции кэшбэка.
    """
    operation: OperationDict


class MakeTransferOperationRequestDict(TypedDict):
    """
    Структура данных для создание операции перевода.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTransferOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции перевода.
    """
    operation: OperationDict

class MakePurchaseOperationRequestDict(TypedDict):
    """
    Структура данных для создание операции покупки.
    """
    status: str
    amount: float
    cardId: str
    accountId: str
    category: str

class MakePurchaseOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции покупки.
    """
    operation: OperationDict


class MakeBillPaymentOperationRequestDict(TypedDict):
    """
    Структура данных для создание операции оплаты по счету.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции оплаты по счету.
    """
    operation: OperationDict

class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """
    Структура данных для создание операции снятия наличных денег.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции снятия наличных денег.
    """
    operation: OperationDict


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение списка операций для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Получение статистики по операциям для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))


    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь с параметрами для создания операции комиссий.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Словарь с параметрами для создания операции пополнения.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с параметрами для создания операции кэшбэка.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с параметрами для создания операции перевода.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с параметрами для создания операции покупки.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param request: Словарь с параметрами для создания операции оплаты по счету.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных денег.

        :param request: Словарь с параметрами для создания операции снятия наличных денег.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)


    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(self, account_id: str, card_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status=random.choice(list(StatusEnum)),
            amount=round(random.uniform(1, 100), 2),
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, account_id: str, card_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status=random.choice(list(StatusEnum)),
            amount=round(random.uniform(1, 100), 2),
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, account_id: str, card_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status=random.choice(list(StatusEnum)),
            amount=round(random.uniform(1, 100), 2),
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, account_id: str, card_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status=random.choice(list(StatusEnum)),
            amount=round(random.uniform(1, 100), 2),
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, account_id: str, card_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status=random.choice(list(StatusEnum)),
            amount=round(random.uniform(1, 100), 2),
            cardId=card_id,
            accountId=account_id,
            category="string"
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, account_id: str, card_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status=random.choice(list(StatusEnum)),
            amount=round(random.uniform(1, 100), 2),
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, account_id: str, card_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status=random.choice(list(StatusEnum)),
            amount=round(random.uniform(1, 100), 2),
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()

def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())

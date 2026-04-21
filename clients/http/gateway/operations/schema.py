from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from enum import StrEnum
from datetime import datetime

class StatusEnum(StrEnum):
    """
    Enum для выбора статуса.
    """
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"

class OperationTypeEnum(StrEnum):
    """
    Enum для выбора типа операции.
    """
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationSchema(BaseModel):
    """
    Описание структуры операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationTypeEnum
    status: StatusEnum
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class OperationReceiptSchema(BaseModel):
    """
    Описание структуры чека.
    """
    url: HttpUrl
    document: str

class GetOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа для получения данных по операции.
    """
    operation: OperationSchema

class GetOperationsResponseSchema(BaseModel):
    """
    Описание структуры ответа для получения списка операций по счету.
    """
    operations: list[OperationSchema]

class GetOperationReceiptResponseSchema(BaseModel):
    """
    Описание структуры ответа  для получения чека по операции.
    """
    receipt: OperationReceiptSchema

class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")

class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")

class OperationsSummarySchema(BaseModel):
    """
    Описание структуры статистики по операциям для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")

class GetOperationSummaryResponseSchema(BaseModel):
    """
    Описание структуры ответа для получения статистики по операциям для определенного счета.
    """
    summary: OperationsSummarySchema

class MakeFeeOperationRequestSchema(BaseModel):
    """
    Структура данных для создание операции комиссии.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: StatusEnum
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeFeeOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции комиссии.
    """
    operation: OperationSchema

class MakeTopUpOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции пополнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: StatusEnum
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции пополнения.
    """
    operation: OperationSchema

class MakeCashbackOperationRequestSchema(BaseModel):
    """
    Структура данных для создание операции кэшбэка.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: StatusEnum
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции кэшбэка.
    """
    operation: OperationSchema


class MakeTransferOperationRequestSchema(BaseModel):
    """
    Структура данных для создание операции перевода.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: StatusEnum
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeTransferOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции перевода.
    """
    operation: OperationSchema

class MakePurchaseOperationRequestSchema(BaseModel):
    """
    Структура данных для создание операции покупки.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: StatusEnum
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    category: str

class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции покупки.
    """
    operation: OperationSchema


class MakeBillPaymentOperationRequestSchema(BaseModel):
    """
    Структура данных для создание операции оплаты по счету.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: StatusEnum
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции оплаты по счету.
    """
    operation: OperationSchema

class MakeCashWithdrawalOperationRequestSchema(BaseModel):
    """
    Структура данных для создание операции снятия наличных денег.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: StatusEnum
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции снятия наличных денег.
    """
    operation: OperationSchema

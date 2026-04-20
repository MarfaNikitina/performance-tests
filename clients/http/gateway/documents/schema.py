from pydantic import BaseModel, HttpUrl


class DocumentSchema(BaseModel):
    """
    Описание структуры документа.
    """
    url: HttpUrl
    document: str

# Добавили описание структуры ответа получения документа тарифа
class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения документа тарифа.
    """
    tariff: DocumentSchema

# Добавили описание структуры ответа получения документа контракта
class GetContactDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения документа контракта.
    """
    contract: DocumentSchema
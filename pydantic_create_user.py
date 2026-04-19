import uuid
import random
import string
from pydantic import BaseModel, Field, HttpUrl, EmailStr


# модель UserSchema
class UserSchema(BaseModel):
    id:  str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr  # Используем EmailStr вместо str
    last_name: str = Field(alias="lastName")
    firstName: str = Field(alias="firstName")
    phone_number: str = Field(alias="phoneNumber")

# модель создания пользователя
class CreateUserRequestSchema(BaseModel):
    email: EmailStr = Field(default_factory=lambda: ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(8, 15))) + '@mail.ru') # Используем EmailStr вместо str, генерируем рандомное уникальное значение
    last_name: str = Field(alias="lastName", default="Ivanova")
    firstName: str = Field(alias="firstName", default="Anna")
    middle_name: str = Field(alias="middleName", default="Ivanovna")
    phone_number: str = Field(alias="phoneNumber", default_factory=lambda: ''.join(random.choices(string.digits, k=10))) # генерируем рандомный номер телефона

# модель ответа создания пользователя
class CreateUserResponseSchema(BaseModel):
    user: UserSchema

from pydantic import BaseModel


# Создать класс нужного объекта
class ObjBase(BaseModel):
    pass


# class UserBase(BaseModel):
#     username: str
#     foo: int
#     bar: int
#
# class UserCreate(UserBase):
#     pass
#
# class UserRead(UserBase):
#     id: int

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserCreate(UserBase):
    pass


class UserResponsePublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class UserResponsePrivate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    email: str

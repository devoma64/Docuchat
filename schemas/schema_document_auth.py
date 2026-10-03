from pydantic import BaseModel, ConfigDict


class DocumentBase(BaseModel):
    id: int
    filename: str


class DocumetCreate(DocumentBase):
    pass


class DocumentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    filename: str
    user_id: str

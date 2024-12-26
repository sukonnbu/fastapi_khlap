from pydantic import BaseModel, Field


class UsedItemSchema(BaseModel):
    title: str = Field(...)
    username: str = Field(...)
    content: str = Field(...)
    image: str = Field(...)
    updated_at: str = Field(...)
    comments: list[dict[str, str]] = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                {
                    "title":"망이쿠션 팔아요",
                 "username":"망밑흥은과학이다",
                 "updated_at":"12/24 09:32",
                 "itemname":"망이쿠션",
                 "sold":false,
                 "price":10000,
                 "else":"",
                 "comments":
                     [{"username":"행이복상사","content":"나 살래 저거","updated_at":"12/24 09:33"}],
                 "image":""
                 }
            }
        }


class UpdateUsedItemModel(BaseModel):
    title: str
    content: str
    image: str
    updated_at: str
    comments: list[dict[str, str]]

    class Config:
        json_schema_extra = {
            "example": {
                {
                    "title":"망이쿠션 팔아요",
                 "username":"망밑흥은과학이다",
                 "updated_at":"12/24 09:32",
                 "itemname":"망이쿠션",
                 "sold":false,
                 "price":10000,
                 "else":"",
                 "comments":
                     [{"username":"행이복상사","content":"나 살래 저거","updated_at":"12/24 09:33"}],
                 "image":""
                 }
            }
        }

from pydantic import BaseModel

#1. 공통 속성(상품 만들때나 조회할때나 똑같은 것)
class ItemBase(BaseModel):
    name: str
    price: int

#2. 상품 생성 할때 필요한 스키마
class ItemCreate(ItemBase):
    pass

#3. 상품 조회 할때 보여줄 스키마
class Item(ItemBase):
    id: int
    is_offer:bool

    class Config:
        from_attributes = True      

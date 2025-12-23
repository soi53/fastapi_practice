from sqlalchemy import Column, Integer, String, Boolean
from database import Base # 위에서 만든 database.py의 Base를 가져옴

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    is_offer = Column(Boolean, default=True)




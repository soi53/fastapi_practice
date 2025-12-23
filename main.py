from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
from database import SessionLocal, engine

#DB 생성
models.Base.metadata.create_all(bind=engine)

app=FastAPI()

#DB 세션관리

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

#[CREATE] 상품 등록

@app.post("/items", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db:Session=Depends(get_db)):
    #스키마로 받은 데이터를 DB 모델로 변환
    db_item = models.Item(name=item.name, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

#[READ] 상품 조회
# 응답형태를 List로 정의
@app.get("/items/", response_model=List[schemas.Item])
def read_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items


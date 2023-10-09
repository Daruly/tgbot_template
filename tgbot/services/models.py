import sqlalchemy.sql
from sqlalchemy import (Column, Integer, String, Sequence)
from sqlalchemy import sql
from tgbot.services.database import db


class Item(db.Model):
    __tablename__ = "items"
    query: sqlalchemy.sql.Select

    # Уникальный идентификатор товара
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)

    # Код категории (для отображения в колбек дате)
    category_code = Column(String(20))

    # Название категории (для отображения в кнопке)
    category_name = Column(String(50))

    # Код подкатегории (для отображения в колбек дате)
    subcategory_code = Column(String(50))

    # Название подкатегории (для отображения в кнопке)
    subcategory_name = Column(String(20))

    # Название, фото и цена товара
    name = Column(String(50))
    photo = Column(String(250))
    price = Column(Integer)


    def __repr__ (self):
        return f"""
        Товар #{self.id} - {self.name} 
        Цена : {self.price}
        """

from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,Enum
from sqlalchemy.ext.declarative import declarative_base

engine = create_enging('sqlite:///nobel_prize.db', echo = True) #echo 有否顯示讀入資料庫的訊息
Base   = declarative_base()

class Winner(Base):
    __tablename__='winners'
    id  = Column(Integer, primary_key=True)
    name= Column(String)
    category = Column(String)
    year= Column(Integer)
    nationality = Column(String)
    sex = Column(Enum('male','female'))
    
    def __repr__(self):
        return '<Winner(name={0!s},category={0!s},year={0!s})>'.format(self.name,self.category,self.year)
       
Base.metadata.create_all(engine)
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///nobel_prize.db', echo = True) #engine 處理下方的 insert to ; echo 有否顯示讀入資料庫的轉換訊息、狀況
Base   = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()                                             #maker餵資料給session,會自動建立連線      

class Winner(Base):
    __tablename__='winners'
    id  = Column(Integer, primary_key=True)
    name= Column(String)
    category = Column(String)
    year= Column(Integer)
    nationality = Column(String)
    sex = Column(Enum('male','female'))
    
    def __repr__(self):
        return '<Winner(name=%s,category=%s,year=%s)>'%(self.name,self.category,self.year)
        
#Base.metadata.create_all(engine)                                #create會檢查是否已存在

print(session.query(Winner).count())                             #找印筆數
print(session.query(Winner).all())
#print(session.query(Winner).order_by('year').all())      
#print(session.query(Winner).filter_by(year=1911).all()) 
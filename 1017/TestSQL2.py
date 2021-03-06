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
        return '<Winner(name=%s,category=%s,year=%s)>'.format(self.name,self.category,self.year)

nobel_winners = [
{'category': 'Physics',
'name': 'Albert Einstein',
'nationality': 'Swiss',
'sex': 'male',
'year': 1921},
{'category': 'Physics',
'name': 'Paul Dirac',
'nationality': 'British',
'sex': 'male',
'year': 1933},
{'category': 'Chemistry',
'name': 'Marie Curie',
'nationality': 'Polish',
'sex': 'female',
'year': 1911}
]        
        
Base.metadata.create_all(engine)
#版1
#Albert = Winner(**nobel_winners[0])
#session.add(Albert)

#版2
session.add(Winner(**nobel_winners[0])) 
session.add(Winner(**nobel_winners[1]))
session.add(Winner(**nobel_winners[2]))

#版3
#winner_rows = [Winner(**w) for w in nobel_winners]
#session.add_all(winner_rows)

print(session.new)
session.commit()
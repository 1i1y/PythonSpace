from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#sessionmaker 生成sqlite 的基礎

engine = create_engine('sqlite:///nobel_prize.db', echo=True)
Base = declarative_base()

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
#Base.metadata.create_all(engine) #創table

Session = sessionmaker(bind=engine)
session = Session()

#----------------這兩行自動匯入資料---------------
winner_rows = [Winner(**w) for w in nobel_winners]
session.add_all(winner_rows)
#-------------------------------------------------

print(session.query(Winner).all())
#query 詢問
session.commit()


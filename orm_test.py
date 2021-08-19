import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import Integer, String, Float
from sqlalchemy import Column

print(sqlalchemy.__version__)

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:postgres@postgresdb.cqh8zx545xp6.eu-central-1.rds.amazonaws.com:5432/academicDB')
connection = engine.connect()

results = connection.execute("SELECT * FROM superheroes")

# for row in results:
#     print ('title:', row['hero_name'])

# results.close()

# trans = connection.begin()

# try:
#     connection.execute("INSERT INTO superheroes(hero_name, strength) VALUES('Spiderman','100')")
#     trans.commit()
# except:
#     trans.rollback()
#     raise

# with connection.begin() as trans:
#     connection.execute("INSERT INTO superheroes(hero_name, strength) VALUES('Test','90')")



Base = declarative_base()

class Users(Base):
    __tablename__ = 'superheroes' 

    hero_id = Column(Integer, primary_key = true)
    hero_name =Column(String(25))
    strength = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user = Users(hero_id=26,hero_name='Serhii', strength=12)
session.add(user)
session.commit()

for item in session.query(Users).order_by(Users.strength):
    print(item.hero_name, ' ', item.strength)

for item in session.query(Users).filter(Users.strength > 4.5):
    print(item.hero_name, ' ', item.strength)

connection.close()

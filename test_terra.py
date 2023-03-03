import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
import sqlalchemy
from sqlalchemy.orm import sessionmaker

Base = declarative_base()




class Course(Base):
     __tablename__ = "result_4"

     id = sq.Column(sq.Integer, primary_key=True)
     name = sq.Column(sq.String)
     gender = sq.Column(sq.String)

     def __str__(self):
          return f'{self.id},{self.name} ,{self.gender}'

with open("password_base.txt", "r") as file_object:
    password = file_object.read().strip()

list_base = password.split(",")

login= list_base[0]
password = list_base[1]
database = list_base[2]

def create_tables(login,password,database):
     DSN = f"postgresql://{login}:{password}@localhost:5432/{database}"
     engine = sqlalchemy.create_engine(DSN)
     Base.metadata.create_all(engine)
     # Base.metadata.drop_all(engine)
     # Base.metadata.drop_all(engine)



create_tables(login,password,database)
def session(login,password,database):
    DSN = f"postgresql://{login}:{password}@localhost:5432/{database}"
    engine = sqlalchemy.create_engine(DSN)
    Session = sessionmaker(bind=engine)
    session = Session()

    database_line =[]
    for id in session.query(Course).all():
        number = id
        number_1 = str(number)
        data_ingridient = number_1.split(',')
        database_line.append(data_ingridient)
    database = []
    for list in database_line:
        data_user = dict.fromkeys(['id', 'name', 'gender'])
        data_user['id'] = list[0]
        data_user['name'] = list[1]
        data_user['gender'] = list[2]
        database.append(data_user)
    print(database)
    return database

# def session_add():
#     course1 = Course(id_people=id, id_user=user_id)
#     session.add(course1)
#     session.commit()
#     session.close()

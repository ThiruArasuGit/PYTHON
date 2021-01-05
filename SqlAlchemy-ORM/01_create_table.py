from sqlalchemy import create_engine, Column, Integer, String
import cx_Oracle
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker


dburl = 'oracle+cx_oracle://hr:hr@localhost/orcl'
print('dburl: '+ dburl)

engine = create_engine(dburl)
Session = sessionmaker(bind=engine)
session = Session()
try:
    conn = engine.connect()
    print('Oracle DB connection established successfully! \n {}'.format(conn))

    query = 'select * from DEPARTMENTS'
    rs = conn.execute(query)
    for i in rs:
        print("{} is department id of '{}'".format(i[0], i[1]))

# Create a table in Oracle data base

    Base = declarative_base()

    class Student(Base):
        __tablename__ = 'student'
        id = Column(Integer, primary_key=True)
        name = Column(String(50))

    Base.metadata.create_all(engine)
    print('Table got created!')

# Insert data into Student table
    student1 = Student(id=100, name='Thiru')
    session.add(student1)

    student2 = Student(id=101, name="Anitha")
    student3 = Student(id=102, name='Sweta')
    session.add_all([student2, student3])
    session.commit()

except Exception as err:
    print('DB connection failed. \n error: {}'.format(err))
finally:
    conn.close()
    print('Connection closed!')


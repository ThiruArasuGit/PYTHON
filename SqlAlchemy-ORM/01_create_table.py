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

# Create a table in Oracle data base [C]

    Base = declarative_base()
    dt = conn.execute('drop table student')
    print('Table student dropped!')

    class Student(Base):
        __tablename__ = 'student'
        id = Column(Integer, primary_key=True)
        name = Column(String(50))

    Base.metadata.create_all(engine)
    print('Table student created!')

# Insert data into Student table [I]
    insert_student1 = Student(id=100, name='Thiru')
    session.add(insert_student1)

    insert_student2 = Student(id=101, name="Anitha")
    insert_student3 = Student(id=102, name='Sweta')
    insert_student4 = Student(id=103, name='Roshan')
    insert_student5 = Student(id=104, name='Gaurab')

    session.add_all([insert_student2, insert_student3, insert_student4, insert_student5])

    insert_student_cnt = session.query(Student).count()

    print('{} students are inserted into student table.'.format(insert_student_cnt))

# Update the student name from 'Gaurab' to 'Gaurav' [U]
    update_student = session.query(Student).filter(Student.name=='Gaurab').first()
    print(update_student.name)
    update_student.name = 'Gaurav'
    print('Corrected the name to {} !'.format(update_student.name))


# Fetch all data from student table order by student name AFTER insertion
    all_students = session.query(Student).order_by(Student.name)

    for student in all_students:
        print(student.id, student.name)

# Delete a student from student table.
    del_student = session.query(Student).filter(Student.name == 'Thiru').first()
    print('Student opted for deletion: {}'.format(del_student.name))
    session.delete(del_student)

# Fetch all data from student table order by student name AFTER deletion
    all_students = session.query(Student).order_by(Student.id)

    for student in all_students:
        print(student.id, student.name)

except Exception as err:
    print('DB connection failed. \n error: {}'.format(err))
finally:
    session.commit()
    conn.close()
    print('Connection closed!')


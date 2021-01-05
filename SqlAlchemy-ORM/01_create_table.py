from sqlalchemy import create_engine
import cx_Oracle

dburl = 'oracle+cx_oracle://hr:hr@localhost/orcl'
print('dburl: '+ dburl)

engine = create_engine(dburl)
try:
    conn = engine.connect()
    print('Oracle DB connection established successfully! \n {}'.format(conn))

    query = 'select * from DEPARTMENTS'
    rs = conn.execute(query)
    for i in rs:
        print("{} is department id of '{}'".format(i[0], i[1]))

except Exception as err:
    print('DB connection failed. \n error: {}'.format(err))
finally:
    conn.close()
    print('Connection closed!')


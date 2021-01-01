import cx_Oracle

try:
    conn = cx_Oracle.connect("hr/hr")
except Exception as err:
    print("Error while connecting to Oracle database: ", err)
else:
    print('Connected to oracle db version: ' + conn.version)
    try:
        # Create table in oracle database
        create_table_str = """CREATE TABLE EMP(ENAME VARCHAR2(50),EMPNO NUMBER, POSITION VARCHAR2(50))"""
        cur = conn.cursor()
        cur.execute(create_table_str)

        # Check if table created successfully or not.
        chk_table_str = """ SELECT COUNT(1) FROM USER_OBJECTS WHERE OBJECT_NAME = 'EMP'"""
        cur.execute(chk_table_str)
        cnt = cur.fetchone()  # returns a tuple
        if cnt[0] > 0:
            print(str(cnt[0]) + ' Table created successfully!')
        else:
            print('Table creation failed!')

        # Insert the table
        insert_table_str = """INSERT INTO EMP (ENAME,EMPNO,POSITION) SELECT ENAME,EMPNO,POSITION FROM (SELECT FIRST_NAME|| ' '|| LAST_NAME ENAME, EMPLOYEE_ID EMPNO,J.JOB_TITLE POSITION FROM EMPLOYEES E,JOBS J WHERE E.JOB_ID = J.JOB_ID)"""
        cur.execute(insert_table_str)

    except Exception as err:
        print('Table creation and insertion failed: ', err)
    else:
        print('Table is successfully created and populated with the data!')
        conn.commit()
finally:
    cur.close()
    conn.close()
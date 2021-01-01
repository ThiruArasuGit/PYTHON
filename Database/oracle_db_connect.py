import cx_Oracle

# Create connection
conn = cx_Oracle.connect("hr/hr")
print('Connected to oracle db version: ' + conn.version)

# Create table in oracle database
create_table_str = """
CREATE TABLE EMP(
ENAME VARCHAR2(50),
EMPNO NUMBER,
POSITION VARCHAR2(30)
)
"""
cur = conn.cursor()
cur.execute(create_table_str)

chk_table_str = """ SELECT COUNT(1) FROM USER_OBJECTS WHERE OBJECT_NAME = 'EMP'"""
cur.execute(chk_table_str)
cnt = cur.fetchone()  # returns a tuple
print(str(cnt[0]) + ' Table created')
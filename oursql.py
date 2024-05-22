from mysql import connector
from mysql.connector import errorcode

try:
    conn = connector.connect(
        host="localhost",
        user="root",
        password="rahul12345",
        database="Student",
        port=3306,
    )
    # cursor_obj = conn.cursor(buffered=True)
    # cursor_obj = conn.cursor(prepared=True)
    cursor_obj = conn.cursor()

    # studentrecord = """ create table Student(
    #                 NAME  VARCHAR(20) NOT NULL,
    #                BRANCH VARCHAR(50),
    #                ROLL INT NOT NULL,
    #                SECTION VARCHAR(5),
    #                AGE INT
    #             ) """
    insertstudent = """ insert into Student(NAME,BRANCH,ROLL,SECTION,AGE) values(%s,%s,%s,%s,%s)"""
    # val = ("rahul", "IT", 1, "A", 21)
    # val = ["rahul", "IT", 1, "A", 21]
    val = [("Nikhil", "CSE", "98", "A", "18"),
       ("Nisha", "CSE", "99", "A", "18"),
       ("Rohan", "MAE", "43", "B", "20"),
       ("Amit", "ECE", "24", "A", "21"),
       ("Anil", "MAE", "45", "B", "20"), 
       ("Megha", "ECE", "55", "A", "22"), 
       ("Sita", "CSE", "95", "A", "19")]
    # val = [("rahul", "IT", 1, "A", 21), ("rahul", "IT", 1, "A", 21), ("rahul", "IT", 1, "A", 21)]
    # cursor_obj.execute(insertstudent, val)
    # cursor_obj.executemany(insertstudent, val)
    # cursor_obj.execute("select * from Student")
    cursor_obj.execute("delete from Student  where Name = 'Nikhil'")
    conn.commit()
    for i in cursor_obj.fetchall():
        print(i)
    cursor_obj.close()
except connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(f"Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
        conn.close()
# studenrecord = """ create table Stuents(
#     id int auto_increment primary key,
#     name varchar(255),
#     marks int
# ) """
# result =cursor_obj.execute("use ourdb")
# cursor_obj.execute(studenrecord)
# print(result)

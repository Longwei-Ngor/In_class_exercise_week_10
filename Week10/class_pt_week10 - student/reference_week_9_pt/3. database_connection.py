import mysql.connector
from prettytable import PrettyTable

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="week_9_pts",
    port=3306
)

# there are .. components that we need in order to execute sql transaction
# more info for mysql python https://www.w3schools.com/python/python_mysql_getstarted.asp
# 1. handle: cursor is a handler that we get use to our database server, .cursor()
# 2. execute: this where we tell the instruction of what to run on the database, .execute()
# 3. fetch: one executed, result is expected as return, using fetch to get all of that, .fetchall() or .fetchone()

cursor = mydb.cursor()


def get_all_customer():
    sql = "SELECT * from customer"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_one_customer(name):
    sql = f"SELECT * from customer where name = '{name}'"
    cursor.execute(sql)
    result = cursor.fetchone()

    # print table
    # more info for PrettyTable https://pypi.org/project/prettytable/
    # display table, prettytable library help us format the display of our data retrieve from database nicely,
    # 1. you need to instanciate the PrettyTable class using table = PrettyTable()
    table = PrettyTable()
    # 2. add fields name for your table, please noted: field number need to match number of item in return
    table.field_names = ["ID", "Customer Name", "Phone Numer", "Birth Date"]
    # 3. add data to table as a row, this add_row can be prural add_rows if there are more than 1 record.
    table.add_row(result)
    # 4. finally, return the table as string format in order to print it out.
    return table.get_string()


print(get_one_customer('joe'))

# print(get_all_customer()[0][1])

from atexit import register
import mysql.connector
from prettytable import PrettyTable

'''
State your group member name and id here:
ex: 1. 2022279 Longwei Ngor
    2. 2022226 Vicheda Narith
    3. 2022278 Kunthea Mak

'''


# TODO:
# host can be 'localhost' or '127.0.0.1'
# if you are using mamp, password is root
# and port is 8889
# use cat_db as database.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cat_db",
    port="3306"
)

#print(mydb)
cursor = mydb.cursor()


def register_cat(cat_info):
    '''
    TODO:
    cat_info is in a form of list ex: ["rose", "f", "Siberian", "2020-03-08", "smart one"], that register_cat function will insert the provided
    list to cats table as an insert record.
    '''
    cursor.execute("INSERT INTO cats (Name, Gender, Breed, DoB, Description) VALUES (%s, %s, %s, %s, %s)", cat_info)
    mydb.commit()
    print("\n Registration Complete!")
    pass
# test = ["rose", "f", "Siberian", "2020-03-08", "smart one"]
# register_cat(test)

def get_cats():
    '''
    TODO:
    this function will get all cat from cats table 
    '''
    cursor.execute("SELECT * FROM cats")
    b_all = cursor.fetchall()
    return(b_all)
    pass
#get_cats()
def get_cat(id):
    '''
    TODO:
    this function will get a single cat data from cat table base on the id parameter
    '''
    x = f"SELECT * FROM cats WHERE id = '{id}'"
    cursor.execute(x)
    r_id = cursor.fetchone()
    table = PrettyTable()
    table.field_names = ['ID', 'Name', 'Gender', 'Breed', 'DoB', 'Description']
    table.add_row(r_id)
    print(table.get_string())
    return r_id
    pass
#print(get_cat(6))

def update_cat(cat_info):
    '''
    TODO:
    cat_info is in a form of list ex: [1,"rose", "f", "Siberian", "2020-03-08", "smart one"], that update_cat function will use as 
    an update record for specific cat information where equal to cat_info[0]
    '''
    id, name, gender, breed, dob, description = cat_info
    cursor.execute(f"UPDATE cats SET name = '{name}', gender = '{gender}', breed = '{breed}', dob = '{dob}', description = '{description}' WHERE id = '{id}'")
    mydb.commit()
    pass


def remove_cat(id):
    '''
    TODO:
    this function will remove record from cat table base on id parameter.
    '''
    cursor.execute(f"DELETE FROM cats WHERE id = {id}")
    mydb.commit()
    pass

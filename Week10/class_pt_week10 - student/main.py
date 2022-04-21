from db import *
from getname import random_name
from prettytable import PrettyTable


breeds = ["Ragdoll", "Scottish Fold", "Himalayan", "Siberian"]


def display_breed():
    print('''\nCat available breed''')
    for index, breed in enumerate(breeds):
        print(f"{index+1}. {breed}")


print("Welcome to Stray Cat Registration APP")
print("-------------------------------------\n")


menu_1 = '''Menu
1. Register Cat 😻
2. Listed Cat 🐈
3. Update Cat 😼
4. Remove Cat 🙀
5. Exit 🚪
'''

menu_2 = '''\nCat Name
1. Generate name
2. Enter name
'''
while True:
    print(menu_1)

    menu_one_input = input("enter menu number 1 -> 5: ")

    if menu_one_input == "1":

        print(menu_2)

        register_name = input("enter menu number 1 -> 2: ")

        if register_name == "1":
            # TODO:
            # generate random cat name using getname library\
            cat = random_name('cat')
            print(f"Your generated name is: {cat}")
            pass

        elif register_name == "2":
            cat_name = input("\nEnter cat name: ")

        cat_gender = input("\nCat gender (m/f): ")

        display_breed()

        register_breed = int(
            input(f"\nenter menu number 1 -> {len(breeds)}: "))
        #cat_breed = ''
        cat_breed = breeds[register_breed - 1]

        cat_dob = input(
            f"\nEnter {'her' if cat_gender == 'f' else 'his'} date of birth (yyyy-mm-dd): ")

        cat_description = input("\nAnything to note for this cat: ")

        cat_info = (cat_name, cat_gender, cat_breed, cat_dob, cat_description)

        register_cat(cat_info)

    elif menu_one_input == "2":
        all_cat = get_cats()
        print(all_cat)
        # TODO:
        # display all cat information in a table format using PrettyTable library
        #listcat = PrettyTable(['ID', 'Name', 'Gender', 'Breed', 'DoB', 'Description'])
        table = PrettyTable()
        table.field_names = ['ID', 'Name', 'Gender', 'Breed', 'DoB', 'Description']
        table.add_rows(all_cat)
        print(table.get_string())

    elif menu_one_input == "3":

        update_cat_id = int(input("\nEnter cat ID for update: "))
        id, name, gender, breed, dob, description = get_cat(update_cat_id)

        update_name = input(f"Update Name ({name}): ")
        if update_name == '':
            update_name = name

        update_gender = input(f"Update Gender ({gender}): ")
        if update_gender == '':
            update_gender = gender

        display_breed()
        update_breed = int(
            input(f"\nenter menu number 1 -> {len(breeds)} ({breed}): "))
        if update_breed == '':
            update_breed = breed
        else:
            update_breed = breeds[update_breed - 1]

        update_dob = input(f"Update DOB ({dob}): ")
        if update_dob == '':
            update_dob = dob

        update_description = input(f"Update Description ({description}): ")
        if update_description == '':
            update_description = description

        cat_update_data = (update_cat_id, update_name, update_gender,
                           update_breed, update_dob, update_description)

        update_cat(cat_update_data)

    elif menu_one_input == "4":
        remove_cat_id = int(input("\nCat ID to be remove: "))
        remove_cat(remove_cat_id)

    else:
        break

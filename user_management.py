import csv


def main():

    user_dict = {}
    user_dict = get_users(user_dict)
    print("Welcome to the user management system!")
    menu(user_dict)

def menu(user_dict):
    is_menu_running = True
    while is_menu_running:
        print(
            "Please select what you would like to do now:\nADD user, LIST users, LOGIN")
        while 1:
            choice = str(input("")).upper()
            if choice == "ADD" or choice == "LIST" or choice == "LOGIN":
                break
        if choice == "ADD":
            add_user(get_input_for_users(user_dict), user_dict)

        elif choice == "LIST":
            print_users(user_dict)
        elif choice == "LOGIN":
            login(user_dict)


def print_users(user_dict):
    for key, value in user_dict.items():
        print(f"{value[0]} {value[1]}, User Id:{value[3]}, Email: {key}")


def login(user_dict):
    logging_in = True
    current_user = None
    while logging_in:
        print("Welcome to the login screen!")

        key = input("Please enter your email:")
        if key in user_dict:
            user_password = input("Password:")

            if user_password == user_dict[key][2]:
                print(user_dict[key])
                current_user = user_dict[key]
        elif key not in user_dict:
            add_user(get_input_for_users(user_dict), user_dict)
        if current_user != None:
            logging_in = False

    return current_user


def get_users(dict):
    with open('users.csv') as users:
        reader = csv.reader(users)
        next(reader)
        for l in reader:
            dict[l[0]] = [l[1], l[2], l[3], l[4], ]
    return dict


def get_input_for_users(users_dict):
    while True:
        first_name = input("First name: ")
        if first_name.isalpha():
            break
        elif first_name.strip().isalpha():
            first_name = first_name.strip()
            break
    while True:
        last_name = input("Last name: ")
        if last_name.isalpha():
            break
        elif last_name.strip().isalpha():
            last_name = last_name.strip()
            break
    while True:
        email = input("Email: ")
        if "@" in email and "." in email:
            break
    while True:
        password = input("Choose a password (8-12 characters):")
        if len(password) >= 8 and len(password) <= 12 and password.isalnum():
            break
        elif len(password) < 8:
            print("Password must be more than 8 characters!")
        elif len(password) > 12:
            print("Password must be less than 12 characters!")
        if password.isalnum() == False:
            print("Password can only contain letters and numbers!")
    return [email, first_name, last_name, password, len(users_dict)+1]


def add_user(user, users_dict):
    users_dict[user[0]] = user[1:]
    with open('users.csv', 'a+', newline='\n') as csv_file:
        user_writer = csv.writer(csv_file)
        user_writer.writerow(user)
    print(f"Added user:{user[1]} {user[2]}")


if __name__ == "__main__":
    try:
        main()
    except KeyError as key_err:
        print(f"{type(key_err).__name__}: Unknown product id:{key_err}")
    except FileNotFoundError as not_found_err:
        print(not_found_err)
    except PermissionError as perm_err:
        print(perm_err)

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Сheck the validity of the entered data"
        except IndexError:
            return "Enter user name"
    return inner


@input_error
def add_contact(args, contacts):
        name, phone = args
        if name not in contacts:
            contacts[name] = phone 
            return "Contact added."
        else:
            return "Перевірте вірність введених даних"
      

@input_error
def change_contact(args, contacts):
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated." 
        else:
            return "Перевірте вірність введених даних"
     

@input_error
def show_phone(args,contacts):
        name = args[0]
        if name in contacts:
            return (contacts[name])
        else: 
            return "Користувача з таким іменем не знайдено, перевірте вірність введених даних"
    

@input_error
def show_all(contacts):
    result = []
    if contacts:
        for name, phone in contacts.items():
            result.append(f"{name}: {phone}")
        return result
    else:
        result.append("Список контактів порожній")
        return result


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args,contacts))
        elif command == "all":
            contact_list = show_all(contacts)
            for contact in contact_list:
                 print(contact)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
    
contacts_dict = {}


def input_error(func):
    def inner(args):
        try:
            return func(args)
        except ValueError:
            return "Invalid arguments."
        except IndexError:
            return "Give me a username."
        except KeyError:
            return f"{args} doesn't exist."

    return inner


def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


def get_greeting():
    return "How can I help you?"


@input_error
def add_contact(args: list[str]):
    name, phone = args

    if name in contacts_dict.keys():
        print(f"{name} already exists. It will be overwritten.")

    contacts_dict[name] = phone

    return "Contact added."


@input_error
def change_phone(args: list[str]):
    name, phone = args
    contacts_dict[name] = phone

    return "Contact updated."


@input_error
def get_phone(args: list[str]):
    name = args[0]
    phone = contacts_dict[name]

    return phone


def get_all_contacts():
    if len(contacts_dict) == 0:
        return "Contacts list is empty."

    return contacts_dict


def get_good_bye():
    return "Good bye!"


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        cmd, *args = parse_input(user_input)

        if cmd == "hello":
            print(get_greeting())
        elif cmd == "add":
            print(add_contact(args))
        elif cmd == "change":
            print(change_phone(args))
        elif cmd == "phone":
            print(get_phone(args))
        elif cmd == "all":
            print(get_all_contacts())
        elif cmd == "close" or cmd == "exit":
            print(get_good_bye())
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

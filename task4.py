from typing import Callable


def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid command format. Use: [command] [name] [phone]"
        except IndexError:
            return "Invalid command format. Use: phone [name]"
        except KeyError:
            return "That user is not found"

    return inner


def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: list, contacts: dict) -> str:

    name, phone = args
    if name in contacts:
        return f"Name {name} already exists in contacts!"

    contacts[name] = phone
    return "Contact added."


def show_all(contacts: dict) -> str:
    if not contacts:
        return "Contact list is empty"

    result = [f"{name}: {phone}" for name, phone in contacts.items()]

    return "\n".join(result)


@input_error
def change_contact(args: list, contacts: dict) -> str:

    name, phone = args

    # To trigger KeyError if contact is not present in contacts
    existing_phone = contacts[name]
    contacts[name] = phone
    return f"Contact {name} changed from {existing_phone} to {phone}."


@input_error
def phone_user(args: list, contacts: dict) -> str:

    name = args[0]

    return contacts[name]


def main():
    contacts = {}
    # contacts = {'Vi': 345,
    #             'Dsa': 45346}
    # contacts = {'Vi': 4535,}
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
            print(phone_user(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

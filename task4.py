from typing import Callable, Dict


# Function for handling errors during processing input commands (decorator)
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


# Function for handling input commands from a terminal
def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
# Add new contact to contacts dictionary
def add_contact(args: list, contacts: Dict[str, str]) -> str:
    name, phone = args
    if name in contacts:
        return f"Name {name} already exists in contacts!"

    contacts[name] = phone
    return "Contact added."


# Show all existing contacts in dictionary
def show_all(contacts: Dict[str, str]) -> str:
    if not contacts:
        return "Contact list is empty"

    result = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(result)


@input_error
# Change existing contact in contacts dictionary
def change_contact(args: list, contacts: Dict[str, str]) -> str:
    name, phone = args
    # To trigger KeyError if contact is not present in contacts
    existing_phone = contacts[name]
    contacts[name] = phone
    return f"Contact {name} changed from {existing_phone} to {phone}."


@input_error
# Show phone number fpr selected user
def phone_user(args: list, contacts: Dict[str, str]) -> str:
    name = args[0]
    return contacts[name]


# Main function for handling input commands
def main():
    contacts = {}
    # examples for testing purposes
    # contacts = {'Vi': 345,
    #             'Dsa': 45346}
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

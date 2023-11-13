val = input("Please enter a value: ")
if val == "exit":
    print("Goodbye!")
    exit()


def convert_to_type(val):
    if val.lower() in ["true", "false"]:
        print("Returning bool")
        return bool(val.lower() == "true")
    try:
        # let's try int first (more efficient data structure)
        return int(val)
    except ValueError:
        try:
            # it might be a float!
            print("Not int")
            return float(val)
        except ValueError:
            # invalid data type. it must be a string.
            print("Not float")
            return str(val)


def type_to_pretty(val):
    val_type = type(val)
    print(val_type)
    match str(val_type):
        case "<class 'int'>":
            return "integer"
        case "<class 'float'>":
            return "float"
        case "<class 'str'>":
            return "string"
        case "<class 'bool'>":
            return "boolean"


print("The value's type is", type_to_pretty(convert_to_type(val)))

def list_check(list_values):
    # Add item to list of string if it is a string
    int_list = [item for item in list_values if isinstance(item, int)]
    # Add item to list of ints if it is an int
    str_list = [item for item in list_values if isinstance(item, str)]
    if len(list_values) == len(int_list):
        return int_list[::-1]
    elif len(list_values) == len(str_list):
        return [str_item.upper() for str_item in str_list]
    else:
        return list_values

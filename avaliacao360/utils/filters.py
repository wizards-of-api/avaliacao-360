def filter_by_key(list, key_name, key_value):
    return [dict for dict in list if dict[key_name] == key_value][0]
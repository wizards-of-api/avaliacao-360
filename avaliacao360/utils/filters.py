def filter_by_key(list, key_name, key_value):
    return [dict for dict in list if dict[key_name] == key_value][0]

def replace_on_list(list, filter_key, new_value):
    index = [index for index, dict in enumerate(list) if dict[filter_key] == new_value[filter_key]][0]
    list[index] = new_value
    
    return list
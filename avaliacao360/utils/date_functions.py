from datetime import date

def convert_date_str(str_date: str):
    str_num_list = str_date.split('/')
    int_date_list = [int(str_num) for str_num in str_num_list]
    day = int_date_list[0]
    month = int_date_list[1]
    year = int_date_list[2]
    return date(year, month, day)
import json
from os.path import abspath, exists

mock_path = abspath('./mock_db.json')

def create_db():
    if not exists(mock_path):
        mock_db_file = open(mock_path, 'w')
        mock_db_file.write('')
        mock_db_file.close()
        clear_db()

def clear_db():
    base_db = {
        'class-room-list': [],
        'group-list': [],
        'student-list': []
    }
    mock_db_file = open(mock_path, 'w')
    mock_db_file.write(json.dumps(base_db, indent=2))
    mock_db_file.close()

def get_data():
    mock_db_file = open(mock_path)
    mock_db_str = mock_db_file.read()
    mock_db_file.close()
    return json.loads(mock_db_str)

def get_last_id(key):
    mock_db = get_data()
    mock_table = mock_db[key]

    if len(mock_table) == 0:
        return 0

    mock_table_sorted = sorted(mock_table, key=lambda dict: dict['id'])
    return mock_table_sorted[-1]['id']

def overwrite_data(key, new_data):
    mock_db = get_data()
    mock_db[key] = new_data
    mock_db_file = open(mock_path, 'w')
    mock_db_file.write(json.dumps(mock_db, indent=2))
    mock_db_file.close()
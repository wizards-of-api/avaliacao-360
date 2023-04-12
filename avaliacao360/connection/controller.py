import json
from os.path import abspath, exists

mock_path = abspath('./mock_db.json')

def create_db():
    """
    Verifica se o arquivo do banco de dados mockado (fictício) existe. Se não existir, cria e inicializa o banco de dados
    com a função clear_db.
    """
    if not exists(mock_path):
        with open(mock_path, 'w') as mock_db_file:
            mock_db_file.write('')
        clear_db()

def clear_db():
    """
    Inicializa o banco de dados mockado (fictício) com um dicionário vazio.
    """
    base_db = {
        'class-room-list': [],
        'group-list': [],
        'student-list': [],
        'evaluation-list': []
    }
    with open(mock_path, 'w') as mock_db_file:
        json.dump(base_db, mock_db_file, indent=2)

def get_data():
    """
    Lê o conteúdo do arquivo do banco de dados mockado (fictício), analisa como JSON e retorna o dicionário resultante.
    """
    with open(mock_path, 'r') as mock_db_file:
        mock_db_str = mock_db_file.read()
        return json.loads(mock_db_str)

def get_last_id(key):
    """
    Retorna o último valor id usado em uma lista de dicionários armazenados sob uma determinada chave no banco de dados mockado (fictício).
    """
    mock_db = get_data()
    mock_table = mock_db[key]
    if len(mock_table) == 0:
        return 0
    mock_table_sorted = sorted(mock_table, key=lambda dict: dict['id'])
    return mock_table_sorted[-1]['id']

def overwrite_data(key: str, new_data: dict) -> None:
    """
    Atualiza o banco de dados mockado (fictício) existente sobrescrevendo os dados de uma chave particular
    com novos dados. O banco de dados mockado atualizado é gravado no disco.

    :parâmetro key: Uma string representando a chave dos dados a serem atualizados no banco de dados mockado .
    :parâmetro new_data: Um dicionário representando os novos dados a serem atualizados no banco de dados mockado .
    :return: None
    """
    mock_db = get_data()
    mock_db[key] = new_data
    
    with open(mock_path, 'w') as mock_db_file:
        json.dump(mock_db, mock_db_file, indent=2)

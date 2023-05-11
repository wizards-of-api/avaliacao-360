import json
from os.path import abspath

mock_path = abspath('./mock_db.json')

def evaluation_result():
    """Essa função  irá retorna a lista de avaliação no geral"""
    with open(mock_path, 'r') as mock_db_file:
      mock_db_str = mock_db_file.read()
      read_json = json.loads(mock_db_str)
      for evaluation_list in read_json['evaluation-list']:
        return evaluation_list
    
def evaluation_result_student(name):
    """Essa função irá retornar a avaliação do aluno e avaliação dos colegas"""
    with open(mock_path, 'r') as mock_db_file:
      mock_db_str = mock_db_file.read()
      read_json = json.loads(mock_db_str)
      for student in read_json['student-list']:
        if student['name'] == name:
          student_id = str(student['id'])
          group_id = student['group-id']
          for evaluation_result_group in read_json["evaluation-list"]:
            if evaluation_result_group['group-id'] == group_id:
              dict_evaluation_group = evaluation_result_group['answer-dict']
              list_result = []
              for id, key in dict_evaluation_group.items():
                list_result.append({'id': id , 'evaluation': key})
              return list_result  
                

          
          

       

  
  

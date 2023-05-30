import json
from os.path import abspath, exists

mock_path = abspath('./mock_db.json')

def evaluation_score(name, sprint, group):
  with open(mock_path, 'r') as mock_db_file:
    mock_db_str = mock_db_file.read()
    json_db = json.loads(mock_db_str)
    name_student = name
    sprint_student = sprint
    id_student = ''
    group_id_student = group
    for student in json_db['student-list']:
      if student['name'] == name_student:
        id_student = str(student['id'])
    for evaluation in json_db['evaluation-list']:
      if evaluation['group-id'] == group_id_student and evaluation['sprint'] == sprint_student:
        dict_evaluation = evaluation['answer-dict']
        student_own_evluation = ''
        group_evaluation = ''
        list_avaluation_value = []
        list_avaluation_group = []
        list_avaluation_full = []
        list_evaluation_feedback = []
        global  list_avaluation_average
        list_avaluation_average = []
        for evaluator in dict_evaluation:
          if evaluator == id_student:
            student_own_evluation = dict_evaluation[id_student][id_student]
            list_student = []
            for index in student_own_evluation:
               list_student.append(index['value'])
            list_avaluation_value.append( list_student)
          else:
            group_evaluation = dict_evaluation[evaluator][id_student]
            list_student = []
            list_feedback = []
            for index in group_evaluation:
              list_student.append(index['value'])
              if index['feedback'] != None :
                list_feedback.append(index['feedback'])
            list_avaluation_group.append(list_student)
            list_evaluation_feedback.append(list_feedback)
        list_avaluation_full =  list_avaluation_group + list_avaluation_value
        list_avaluation_average = media_list(list_avaluation_full)
        evaluation_dict_student = {
          name :student_own_evluation,
          'values': list_avaluation_value,
          'average': list_avaluation_average, 
          'feedback': list_evaluation_feedback
        }
        return evaluation_dict_student
      
def general_dash(id_student, group_id):
  with open(mock_path, 'r') as mock_db_file:
    mock_db_str = mock_db_file.read()
    json_db = json.loads(mock_db_str)
    id_student_data = id_student 
    name_student = ''
    group_id_data = group_id
    name_group = []
    sprint = 0
    for student in json_db['student-list']:
      if student['id'] == id_student_data:
        name_student = student['name']
        print(name_student)
        group_id_list = student['group-id-list']
        for group in group_id_list:
          if group_id_data == group:
            for names in json_db['group-list']:
              if group_id_data == names['id']:
                name_group = names['name']
    for sprints in json_db['evaluation-list']:
      if sprints['group-id'] == group_id_data:
        sprint = sprints['sprint']
    avarage = evaluation_score(name_student, sprint ,group_id)
    generate_dict_student = {
      'average': avarage['average'],
      'group': name_group,
      'sprint': sprint,
    }
    return generate_dict_student



    
              


        

          
def media_list(list):
  nota1 = 0
  nota2 = 0
  nota3 = 0
  nota4 = 0
  nota5 = 0
  nota6 = 0
  for score in list:
    nota1 += score[0]
    nota2 += score[1]
    nota3 += score[2]
    nota4 += score[3]
    nota5 += score[4]
    nota6 += score[5]
  if len(list) > 0 :    
    list_avaluation_average =[ nota1/len(list),
    nota2/len(list), nota3/len(list), nota4/len(list),
    nota5/len(list), nota6/len(list)]
  else:
    list_avaluation_average = [0]
    
  return list_avaluation_average
  


  
   
    
  


          
      
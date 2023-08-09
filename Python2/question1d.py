'''
Create a function create_student_report that takes the student's
name as the first argument, the student's age as the second argument, and an
arbitrary number of keyword arguments for the subjects and their respective
scores. The function should return a dictionary with the student's information and a
list of subjects along with their scores.

'''



def create_student_report(name , age , **kwargs): 
    """Creates a student report 

    Args:
        name (str): name of the student 
        age (int): age of the student 

    Returns:
        dict: student's information
    """
    result_dict = {} 
    result_dict['name'] = name 
    result_dict['age'] = age 
    subjects_list = [] 
    for key , value in kwargs.items(): 
        subjects_list.append({key: value})
    result_dict['subjects'] = subjects_list
    
    return result_dict 

print(create_student_report("Elon Musk", 18, math=95, science=88, history=78))
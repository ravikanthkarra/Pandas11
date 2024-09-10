import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    group1 = examinations.groupby(['student_id','subject_name']).size().reset_index(name='attended_exams')
    df1 = pd.merge(students, subjects, how = 'cross').sort_values(['student_id','subject_name'])
    result = df1.merge(group1, on = ['student_id','subject_name'], how = 'left')
    result['attended_exams'].fillna(0, inplace = True)
    # print(result)
    return result
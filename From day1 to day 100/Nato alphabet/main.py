import pandas

student_dict = {
    'student': ['Daniel', 'Dariq', 'Vesi'],
    'score': [56, 65, 76]
}
student_data_frame = pandas.DataFrame(student_dict)

for(index, row) in student_data_frame.iterrows():
    print(row)
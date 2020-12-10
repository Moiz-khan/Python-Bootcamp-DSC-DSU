record = int(input("Enter the No. of record: "))

student_info = {}
marks = []

for i in range(record):
    student_info_values = []
    
    std_roll_num = str(input('Enter roll num: '))
    std_name = str(input('Enter name: '))
    std_age = int(input('Enter age: '))
    std_mark = int(input('Enter marks(out of 100): '))
    
    student_info_values.append(std_name)
    student_info_values.append(std_age)
    student_info_values.append(std_mark)
    
    marks.append(std_mark) 
    
    student_info.update({std_roll_num:student_info_values})
 
mini_mark = min(marks)
max_mark = max(marks)
average = sum(marks)/len(marks)
print("Minimum Marks:", mini_mark, "Maximum marks: ",max_mark, "Avg marks: ",average)

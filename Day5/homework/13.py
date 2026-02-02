"""给定一个嵌套列表，表示学生的成绩数据，数据结构如下：
scores = [[85, 90, 78], [76, 82, 88], [90, 92, 86], [68, 72, 80], [92, 88, 90]]
请编写程序完成一下操作：
    · 计算每个学生的平均分
    · 计算每科的平均分"""

scores = [[85, 90, 78], [76, 82, 88], [90, 92, 86], [68, 72, 80], [92, 88, 90]]
num_students = len(scores)
num_subjects = len(scores[0])

student_averages = [sum(student_scores) / num_subjects for student_scores in scores]
print("每个学生的平均分:", student_averages) 

subject_averages = []

for subject_index in range(num_subjects):
    subject_total = sum(scores[student_index][subject_index] for student_index in range(num_students))
    subject_average = subject_total / num_students
    subject_averages.append(subject_average)
print("每科的平均分:", subject_averages)

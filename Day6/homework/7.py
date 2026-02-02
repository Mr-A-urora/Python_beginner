""" 假设有一个班级的学生成绩数据，数据结构如下：
	students = [
		{'name': 'Alice', 'score': 85},
		{'name': 'Bob', 'score': 76},
		{'name': 'Charlie', 'score': 90},
		{'name': 'David', 'score': 68}.
		{'name': 'Evas', 'score': 92}
	]
请编写程序完成以下操作：
～ 计算学生人数
～ 计算班级总分和平均分
～ 找出成绩最高和最低的学生"""

students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 76},
    {'name': 'Charlie', 'score': 90},
    {'name': 'David', 'score': 68},
    {'name': 'Evas', 'score': 92}
]

student_num = len(students )
class_sum_scores = sum(student['score'] for student in students)
class_average_score = class_sum_scores / student_num
highest_score_student = max(students, key=lambda x: x['score'])
lowest_score_student = min(students, key=lambda x: x['score'])
average_score = class_sum_scores / student_num

print(f"学生人数: {student_num}")
print(f"班级总分: {class_sum_scores}")
print(f"班级平均分: {class_average_score:.2f}")
print(f"成绩最高的学生: {highest_score_student['name']}，分数: {highest_score_student['score']}")
print(f"成绩最低的学生: {lowest_score_student['name']}，分数: {lowest_score_student['score']}")

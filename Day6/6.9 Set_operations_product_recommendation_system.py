peiQi_hobby = {"螺蛳粉", "臭豆腐", "榴莲", "apple"}
alex_hobby = {"螺蛳粉", "臭豆腐", "榴莲", "便便"}
yuan_hobby = {"pizza", "salad", "icecream", "臭豆腐", "榴莲"}
hobbies = [peiQi_hobby, yuan_hobby, alex_hobby]

# 给peiQi推荐商品
hobbies.remove(peiQi_hobby)
peiQi_recommend_set = set()

for hobby in hobbies:
	if len(peiQi_hobby.intersection(hobby)) >= 2:
		peiQi_recommend_set.update(hobby - peiQi_hobby)
		
print(peiQi_recommend_set)

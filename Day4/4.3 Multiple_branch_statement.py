# BMI测试
height = float(input("请输入您的身高（单位：米）："))
weight = float(input("请输入您的体重（单位：千克）："))

BMI = weight / (height ** 2)

if BMI < 18.5:
    advice = f"您的BMI的值为{BMI:.3}，您的体重过轻，建议多吃少动！"
elif BMI >= 18.5 and BMI < 24:
    advice = f"您的BMI的值为{BMI:.3}，您的体重正常，建议保持！"
elif BMI >= 24 and BMI < 28:
    advice = f"您的BMI的值{BMI:.3}，您的体重稍胖，建议多动少吃！"
else:
    advice = f"您的BMI的值为{BMI:.3}，太肥胖！建议绝食！"

print("我们的建议：", advice, sep = "")

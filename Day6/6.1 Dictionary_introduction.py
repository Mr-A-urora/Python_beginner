# 字典格式：{键：值}
info = {"username":"yuan", "age":23, "height":189, "weight":75}
print(info, type(info))
print(info["age"])

info["height"] = 190
print(info["height"])

del info["height"]
print(info)

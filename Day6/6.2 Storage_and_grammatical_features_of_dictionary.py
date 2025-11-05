info_dict = {"apple":"yuan", "age":18, "height":185, "weight":70}
a = hash("apple")
b = hash("age")
c = hash("height")
d = hash("weight")

print(a)
print(b)
print(c)
print(d)

# 十进制转换二进制（了解存储方式）
print(bin(a))
print(bin(b))
print(bin(c))
print(bin(d))

# 补充：Python3.7+ 的版本默认有序字典
print(info_dict) 

""" 将 Unix/Linux 系统下的路径字符串“/Users/yuan/npm/index.js”转换为
    Windows 系统下的路径字符串“\Users\yuan\npm\index.js”。
    请使用两种方式来实现路径转换"""

path = "/Users/yuan/npm/index.js"

# 方法一：使用 str.replace() 方法
windows_path1 = path.replace("/", "\\")
print("方法一转换结果：", windows_path1)

# 方法二：使用 pathlib 模块
from pathlib import PureWindowsPath, PurePosixPath
posix_path = PurePosixPath(path)
windows_path2 = PureWindowsPath(posix_path)
print("方法二转换结果：", windows_path2)

# 方法三：使用字符串拼接
parts = path.split("/")
windows_path3 = ""
for part in parts:
    windows_path3 += part + "\\"
windows_path3 = windows_path3.rstrip("\\")
print("方法三转换结果：", windows_path3)

# 方法四：使用 map 函数
windows_path4 = "\\".join(map(str, path.split("/")))
print("方法四转换结果：", windows_path4)

# 方法五：使用列表的 extend 方法
parts = path.split("/")
windows_path_extend = []
windows_path_extend.extend(parts)
windows_path_extend_str = "\\".join(windows_path_extend)
print("方法五转换结果：", windows_path_extend_str)

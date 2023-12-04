path_info = input().split(".")
file_ext = path_info[-1]
path_info.pop()

for i in path_info:
    file_n = i.split("\\")
    file_name = file_n[-1]

print(f"File name: {file_name}")
print(f"File extension: {file_ext}")
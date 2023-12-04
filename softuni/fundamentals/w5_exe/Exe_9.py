text = input().split()
cmd = input().split()

while cmd[0] != "3:1":
    if cmd[0] == "merge":
        start_index = int(cmd[1])
        end_index = int(cmd[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(text) - 1:
            end_index = len(text) - 1
        merged_elements = " ".join(text[start_index: end_index+1])
        text[start_index:end_index+1] = [merged_elements]
    elif cmd[0] == "divide":
        index = int(cmd[1])
        partitions = int(cmd[2])
        element = text[index]
        divided = []
        part_length = len(element) // partitions
        for i in range(partitions):
            if i != partitions - 1:
                divided.append(element[i*part_length: (i+1)*part_length])
            else:
                divided.append((element[i*part_length:]))
        text[index:index+1] = divided

    cmd = input().split()
print(" ".join(text))
#https://judge.softuni.org/Contests/Practice/Index/2525#0
def decipher_msg(msg, instr):
    for i in instr:
        partitions = i.split("|")
        type = partitions[0]

        if type == "Move":
            moves = int(partitions[1])
            msg = msg[moves:] + msg[:moves]
        elif type == "Insert":
            index = int(partitions[1])
            value = partitions[2]
            msg = msg[:index] + value + msg[index:]
        elif type == "ChangeAll":
            old_char = partitions[1]
            new_char = partitions[2]
            msg = msg.replace(old_char, new_char)
        elif type == "Decode":
            print(f"The decrypted message is: {msg}")


encrypted_message = input()
cmd_list = []

while True:
    cmd = input()
    cmd_list.append(cmd)
    if cmd == "Decode":
        break

decipher_msg(encrypted_message, cmd_list)
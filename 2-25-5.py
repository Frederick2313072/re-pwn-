text = '棿棢棢棲棥棷棊棐棁棚棨棨棵棢棌'
key = 987654321
flag = ''

for i in text:
    # 将结果限制在有效的 Unicode 范围内，限制在0-255范围内
    flag += chr((ord(i) ^ key) % 256)

print(flag)
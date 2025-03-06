#爆破脚本，菜狗不会逆向
result = 'v0b9n1nkajz@j0c4jjo3oi1h1i937b395i5y5e0e$i'
s = 'wesyvbniazxchjko1973652048@$+-&*<>'
flag = ''
l=range(len(result)//2)
#先找到s中的索引值
for i in l:
    indx1 = s.index(result[2*i])
    indx2 = s.index(result[2*i+1])
    for num in range(32,127):
        s1 = num //17
        s2 = num % 17
        ds1 = (s1+i)%34
        ds2 = -(s2+i+1)%34
        if indx1 == ds1 and indx2 == ds2:
            flag += chr(num)
            break
print(flag)

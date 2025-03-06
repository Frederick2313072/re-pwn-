import libnum
s="u#k4ggia61egegzjuqz12jhfspfkay"[::-1]
s_box = 'qwertyuiopasdfghjkzxcvb123456#$'
print(s)
for i in range(5):
    key = i
    for j in range((len(s))):
        key = key *31 + s_box.index(s[j])
        print(libnum.n2s(int(key)))
s=[0x44,0x59,0x59,0x49,0x5E,0x4C,0x71,0x7E,0x62,0x63,0x79,0x55,0x63,0x79,0x55,0x44,0x43,0x59,0x4B,0x55,0x78,0x6F,0x55,0x79,0x63,0x6D,0x64,0x77,0x14]
for letter in s:
    print(chr(letter^0xA),end="")


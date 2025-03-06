start = 0x1144
end = 0x3100

for i in range(start, end):
    if get_wide_byte(i) == 0xEB and get_wide_byte(i + 1) == 0xFF and get_wide_byte(i + 2) == 0xC0:
        patch_byte(i, 0x90)

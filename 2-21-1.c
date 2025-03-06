#include <stdio.h>
#include <stdlib.h>

void ReverseDecryption(const char *encrypted)
{
    unsigned long data;
    sscanf(encrypted, "CW-%lu-CRACKED", &data);

    // 逆向操作
    data /= 2;
    data /= 0x29;

    char original_char = (char)data;
    printf("Original character: %c\n", original_char);
}

int main()
{
    const char *encrypted = "CW-123456-CRACKED"; // 示例加密字符串
    ReverseDecryption(encrypted);
    return 0;
}
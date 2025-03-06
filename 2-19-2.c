#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    char flag[] = "c~scvdzKCEoDEZ[^roDICUMC";
    char v5;

    for (int i = 0; i < strlen(flag) / 2; ++i)
    {
        v5 = flag[2 * i];
        flag[2 * i] = flag[2 * i + 1];
        flag[2 * i + 1] = v5;
    }

    for (int j = 0; j < strlen(flag); j++)
    {
        flag[j] ^= 0x30;
    }

    printf("%s", flag);

    return 0;
}
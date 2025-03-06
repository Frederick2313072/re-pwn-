#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    char flag[] = "c~scvdzKCEoDEZ[^roDICUMC";
    char v5;
    for (int i = 0; i < strlen(flag); i++)
    {
        v5 = flag[2 * i];
        flag[2 * i] = flag[2 * i + 1];
        flag[2 * i + 1] = v5;
    }
    for (int j = 0; j < strlen(flag); j++)
    {
        flag[j] = flag[j] ^ 0x30u;
    }
    printf("%s\n", flag);
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char const *argv[])
{
    char flag[] = "LQQAVDyWRZ]3q]zmpf]uc{]vm]glap{rv]dnce";
    for (int i = 0; i < strlen(flag); i++)
    {
        flag[i] ^= 2;
    }
    printf("%s\n", flag);
    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    char str[] = "LQQAVDyZMP]3q]emmf]uc{]vm]glap{rv]dnce";
    char flag[39];
    for (int i = 0; i <= 38; i++)
    {
        flag[i] = str[i] ^ 2;
    }
    printf("%s", flag);
}

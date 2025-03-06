#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    char flag1[] = "E`}J]OrQF[V8zV:hzpV}fVF[t";
    char flag[] = "";
    for (int i = 0; i < strlen(flag1); i++)
    {
        flag1[i] ^= 3 * 3;
        printf("%s\n", flag1);
    }
}
#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    char flag[] = "DYYI ^ Lq ~bcyUcyUDCYKUxoUycmdw";
    for (int i = 0; i < strlen(flag); i++)
    {
        flag[i] ^= 0xA;
    }
    printf(“% s”, flag);

    return 0;
}
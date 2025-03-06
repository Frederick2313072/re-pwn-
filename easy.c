#include <stdio.h>
#include <string.h>

int main()
{
    char b[] = "d`vxbQd";
    for (int i = 0; i < 7; i++)
    {
        b[i] = b[i] ^ 2;
        b[i]--;
    }
    printf("%s\n", b);
}
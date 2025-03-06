#include <stdio.h>
int main(int argc, char *argv[])
{
    float f = (float)argc;
    printf("%f\n", f);
    argc = (int)f;
    printf("%d\n", argc);
    return 0;
}
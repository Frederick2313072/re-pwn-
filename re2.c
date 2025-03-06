#include <stdio.h>
#include <string.h>
int main()
{
    char Str[] = "ylqq]aycqyp{";
    int length = strlen(Str);
    for (int i = 0; i < length; ++i)
    {
        if ((Str[i] <= 96 || Str[i] > 98) && (Str[i] <= 64 || Str[i] > 66))
            Str[i] += 2;
        else
            Str[i] -= 24;
    }
    printf("%s\n", Str);
    return 0;
}

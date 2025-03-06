#include <stdio.h>
#include <stdint.h>
#define delta 0xF462900 // 题目中的魔改数值

int main()
{
    uint32_t key[4] = {2233, 4455, 6677, 8899};                                                                                                   // 密钥
    uint32_t Data[10] = {0x1A800BDA, 0xF7A6219B, 0x491811D8, 0xF2013328, 0x156C365B, 0x3C6EAAD8, 0x84D4BF28, 0xF11A7EE7, 0x3313B252, 0xDD9FE279}; // 密文
    unsigned int j;
    int i;
    unsigned int sum;
    for (i = 8; i >= 0; i--)
    {
        j = 33;
        sum = delta * (i + j); // 注意乘的数值
        while (j--)
        {
            sum -= delta; // 注意是减号，而且放的位置也要注意
            Data[i + 1] -= (sum + key[(sum >> 11) & 3]) ^ ((Data[i] + ((Data[i] >> 5) ^ (Data[i] << 4))));
            Data[i] -= sum ^ (Data[i + 1] + ((Data[i + 1] >> 5) ^ (Data[i + 1] << 4))) ^ (sum + key[sum & 3]);
        }
    }

    for (int i = 0; i < 10; i++)
    {
        printf("%x", Data[i]);
    }

    return 0;
}
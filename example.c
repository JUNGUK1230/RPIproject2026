#include <stdio.h>

int main() {
    int a = 0;
    scanf("%d", &a);
    if(a>90 && a<100)
    {
        printf("A");
    }
    if(a>80 && a<89)
    {
        printf("B");
    }
    if(a>70 && a<79)
    {
        printf("C");
    }
    if(a>60 && a<69)
    {
        printf("D");
    }
    else
    {
        printf("F");
    }
    return 0;
}
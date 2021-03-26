#include <stdio.h>
int main()
{
    int i,even=0,odd=0,dif=0;
    long long num;
    scanf("%lld",&num);
    if(num<=0)
    {
        printf("Invalid Input");
    }
    else
    {
        while(num>0)
        {
            if(i%2==0)
            {
                even=even+num%10;
                num=num/10;
                i++;
            }
            else
            {
                odd=odd+num%10;
                num=num/10;
                i++;
            }
        }
    }
    dif=even-odd;
    printf("Difference is:%d",dif);
}

#include <stdio.h>

int main()
{
    int a, b, i, j;
    double c, d;

    int t, ctr=0;

    scanf("%d",&t);

    while(t--)
    {
        scanf("%d %d %lf %lf",&a,&b,&c,&d);
        ctr=0;

        while( a<=b)
        {
            a+=(a*c)/100;
            b+=(b*d)/100;

            ctr++;

            if(ctr>100)
                break;
        }

        if(ctr>100)
            printf("Mais de 1 seculo.\n");

        else
            printf("%d anos.\n",ctr);
    }

    return 0;
}


#include <stdio.h>
#include<stdbool.h>

int main()
{
    int g, h;
    while(scanf("%d %d",&g,&h)!=EOF)
    {
    int f, i, x, t, ctr=0;
        for(i=g; i<=h; i++)
        {
            int a=0,o=0, b=0, c=0, d=0, e=0,k=0,l=0,m=0,n=0;
            x = i;
                bool flag = true;

            while(x>0)
            {
                t = x%10;

                if(t==0)
                    o++;
                else if(t==1)
                    a++;
                else if(t==2)
                    b++;
                else if(t==3)
                    c++;
                else if(t==4)
                    d++;
                else if(t==5)
                    e++;
                else if(t==6)
                    k++;
                else if(t==7)
                    l++;
                else if(t==8)
                    m++;
                else if(t==9)
                    n++;

                x/=10;
            }

            if(o>1 || a>1 || b>1 || c>1 || d>1 || e>1 || k>1 || l>1 || m>1 || n>1 )
                    flag = false;

            if(flag)
                ctr++;
        }

        printf("%d\n",ctr);
    }

    return 0;
}

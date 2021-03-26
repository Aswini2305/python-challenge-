int main()
{   
    int trainee[3][3];
    int i,j,sum,avg[3],max=0;
    //read the input
    for (i=0;i<3;i++)
    {
        for (j=0;j<3;j++)
        {
            scanf("%d",&trainee[i][j]);
        }
    }
    //sum the input and find the average
    for (i=0;i<3;i++)
    {
        for (j=0;j<3;j++)
        {
            sum=sum+trainee[j][i];
        }
        avg[i]=sum/3;
    }
    
    for (i=0;i<3;i++)
    {
        if(avg[i]>=max)
        {
            max=avg[i];
            
        }
    }
    for(i=0;i<3;i++)
    {
        if(avg[i]==max)
        {
            printf("Trainee No:%d",(i+1));
        }
        if(avg[i]<=70)
        {
            printf("Trainee is unfit");
        }
    }
    
    
    return 0;
}

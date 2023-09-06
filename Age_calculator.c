#include <stdio.h>
#include <time.h>
#include <stdlib.h>


int noofleap(int y,int y1)
{ 
    int co,year;
	for(year=y;year<y1;year++)
	{
         if(((year%4==0)&&(year%100!=0))||(year%400==0))
             co++;
    }
    return co;
}


int day(int d,int m,int y) 
{
 int year, month, day, i;
 if( (d > 31) || (m > 12) )
 {
 printf("INVALID INPUT");
 }
 else
 {
 year = y-1900;
 year = year/4;
 year = year+y-1900;
 
 switch(m)
 {
 case 1:
 case 10:
   month = 1;
   break;
 case 2:
 case 3:
 case 11:
 month = 4;
 break;
 case 7:
 case 4:
 month = 0;
 break;
 case 5:
 month = 2;
 break;
 case 6:
 month = 5;
 break;
 case 8:
 month = 3;
 break;
 case 9:
 case 12:
 month = 6;
 break;
 }
 year = year + month;
 year = year + d;
 if(( y > 1900 ) && ( y % 4 == 0 ) && ( m < 2 ) )
 year--;
 day = year % 7;
 
 switch(day)
 {
 case 0:
 printf("Day is SATURDAY\n");
 break;
 case 1:
 printf("Day is SUNDAY\n");
 break;
 case 2:
 printf("Day is MONDAY\n");
 break;
 case 3:
 printf("Day is TUESDAY\n");
 break;
 case 4:
 printf("Day is WEDNESDAY\n");
 break;
 case 5:
 printf("Day is THURSDAY\n");
 break;
 case 6:
 printf("Day is FRIDAY\n");
 break;
 }
 }
 
 return 0;
}
 
 
 
int isLeapYear(int year, int mon) 
{
    int flag;
    if(((year%4==0)&&(year%100!=0))||(year%400==0))
    {
        if (mon == 2 || mon==1) 
            {
                flag = 1;
            }
    } 
    
    else 
       flag=0;
    return (flag);
	
}
 
 
int main()
{
 
    int DaysInMon[] = {31, 28, 31, 30, 31, 30,
                       31, 31, 30, 31, 30, 31};
    int times,in=1,days, month, year,ad,am,ay,d,n,m,i,day1,chec,cd,cm,cy,mon,da;
    int dayOff   =   0;
    int dayOffset   = 0;
    long d1;
    char dob[100];
    time_t ts;
    struct tm *ct;
    printf("::::::::::::::::::::::::::::::::::::::::::::WELCOME::::::::::::::::::::::::::::::::::::::::::::");
    printf("\n\nHow many ages do you want to calculate?? ");
    scanf("%d",&times);
    while(in<=times){
    printf("\n****************************************AGE CALCULATOR*****************************************");
    printf("\n\nEnter your date of birth (DD/MM/YYYY): ");
    scanf("%d/%d/%d",&days,&month, &year);
    ad=days;
    am=month;
    ay=year;
    ts = time(NULL);
    ct = localtime(&ts);
    cd=ct->tm_mday;
    cm=ct->tm_mon + 1;
    cy=ct->tm_year + 1900;
    printf("\nCurrent Date: %d/%d/%d\n",ct->tm_mday, ct->tm_mon + 1, ct->tm_year + 1900);
	days = (DaysInMon[month - 1] - days) +1;
    chec=isLeapYear(year, month);
    if (chec==1) 
    {
            days = days + 1;
    }
    days = days + ct->tm_mday;
    month = (12 - month) + (ct->tm_mon);
    year = (ct->tm_year + 1900) - year - 1;
    if (isLeapYear((ct->tm_year + 1900), (ct->tm_mon + 1))==1) 
    {
            if (days >= (DaysInMon[ct->tm_mon] + 1)) 
            {
                    days = days - (DaysInMon[ct->tm_mon] + 1);
                    month = month + 1;
            }
    } 
    else if (days >= DaysInMon[ct->tm_mon]) 
    {
            days = days - (DaysInMon[ct->tm_mon]);
            month = month + 1;
    }
 
    if (month >= 12) 
    {
            year = year + 1;
            month = month - 12;
    }
    
    printf("\n_______________________________________________________________________________________________");
    printf("\n AGE : ");
    printf("\n\nYou are %d years %d months and %d days old\n", year, month, days);
    printf("\n_______________________________________________________________________________________________");
    printf("\n DAY OF BIRTH : \n\n");
    day(ad,am,ay);
    printf("\n_______________________________________________________________________________________________");
    m=isLeapYear(ay,am);
    i=isLeapYear(ct->tm_year + 1900,ct->tm_mon + 1);
    if(m==0){
        if (i==1)
          n=noofleap(ay+1,ct->tm_year + 1900);
        else
           n=noofleap(ay+1,ct->tm_year + 1900+1);
    }
    else {
      if (i==1)
        n=noofleap(ay,ct->tm_year + 1900);
      else
        n=noofleap(ay,ct->tm_year + 1900+1);
    }
    if ((cm < am) || ((cm == am) && (cd < ad))){
    while (cm < am)
    {
        if (cm == 1)
            dayOffset += 31;
        else if (cm == 2)
        {
            if ((cy / 4) * 4 == cy)
                dayOffset += 29;
            else 
			    dayOffset += 28;
        }
        else if (cm == 3)
            dayOffset += 31;
        else if (cm == 4)
            dayOffset += 30;
        else if (cm == 5)
            dayOffset += 31;
        else if (cm == 6)
            dayOffset += 30;
        else if (cm == 7)
            dayOffset += 31;
        else if (cm == 8)
            dayOffset += 31;
        else if (cm == 9)
            dayOffset += 30;
        else if (cm == 10)
            dayOffset += 31;
        else if (cm == 11)
            dayOffset += 30;
        else if (cm == 12)
        {
            dayOffset += 31;
            cm = 0;
        }

        cm ++;
    }
    dayOffset -= cd;
    dayOffset += ad;
    dayOff = 365 - dayOffset;
    }
    else if ((cm == am) && (cd == ad)){
       dayOff = 0;
    }
    else{
    while (am < cm)
    {
        if (am == 1)
            dayOffset += 31;
        else if (am==2)
        {
            if (((cy- 1) / 4) * 4 == (cy - 1))
                dayOffset += 29;
            else 
			   dayOffset += 28;
        }
        else if (am == 3)
            dayOffset += 31;
        else if (am == 4)
            dayOffset += 30;
        else if (am == 5)
            dayOffset += 31;
        else if (am == 6)
            dayOffset += 30;
        else if (am == 7)
            dayOffset += 31;
        else if (am == 8)
            dayOffset += 31;
        else if (am == 9)
            dayOffset += 30;
        else if (am == 10)
            dayOffset += 31;
        else if (am == 11)
            dayOffset += 30;
        else if (am == 12)
        {
            dayOffset += 31;
            am = 0;
        }

        am ++;
    }

    dayOffset -= ad;
    dayOffset += cd;
    dayOff = dayOffset;
    }
    d=year*365+n+dayOff;
    d1=d*24*60*60;
    printf("\n YOU ARE ALIVE FOR");
	printf("\n\n %d DAYS",d);
    printf("\nOr %d HOURS",d*24);
    printf("\nOr %d MINUTES",d*24*60);
    printf("\nOr %d SECONDS\n\n",d1);
    printf("\n_______________________________________________________________________________________________");
    printf("\n DAYS LEFT FOR NEXT BIRTHDAY");
    printf("\n\n%d\n",dayOff);
    printf("\n_______________________________________________________________________________________________");
    printf("\n\n***********************************************************************************************\n\n");
    in++;
    }
    printf("\n\n:::::::::::::::::::::::::::::::::::::::::::THANK YOU:::::::::::::::::::::::::::::::::::::::::::");
	return 0;
}

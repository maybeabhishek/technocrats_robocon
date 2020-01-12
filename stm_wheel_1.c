#include "mbed.h"
char test;
char a;
float sp;
float spe;
Serial uart(PA_9 ,PA_10,115200);
Serial pc(USBTX, USBRX);

PwmOut p1(PC_6);
PwmOut p2(PA_11);
PwmOut p3(PB_13);
PwmOut p4(PB_15);
DigitalOut d1(PA_12);
DigitalOut d2(PB_2);
DigitalOut d3(PB_14);
DigitalOut d4(PB_1);
DigitalOut pd(LED1);



//DigitalOut myled(LED1);

void diag_sped(float k1, bool t)
{
    if (t)
    {
        p1.write(k1);
        p2.write(0);
        p3.write(0);
        p4.write(k1);
    }
    else
    {
        p1.write(0);
        p2.write(k1);
        p3.write(k1);
        p4.write(0);        
    }        
}
void speed(float k)
{
    p1.write(k);
    p2.write(k);
    p3.write(k);
    p4.write(k);    
}  
void directions(int  i,int j,int k,int l)
{
    d1 = i;
    d2 = j;
    d3 = k;
    d4 = l;
} 
 
int main() {
    
    p1.period(0.001);
    p2.period(0.001);
    p3.period(0.001);
    p4.period(0.001);
    p1.write(0);
    p2.write(0);
    p3.write(0);
    p4.write(0);
    d1 = 0;
    d2 = 0;
    d3 = 0;
    d4 = 0;
    pd =0;
    spe=0.0;
    sp=0.0;
while(1)
{
if (uart.readable()) {
    a = uart.getc();
    pc.putc(a);
if (a == 'S')
{
    speed(0);
    pd =0;
}      
else if (a == '0')
    {
        pd = 1;
    directions(1,0,0,1);
    speed(spe);
    }
else if (a == '4')
{
    directions(0,1,1,0);
    speed(spe);
    pd =1;
}
else if (a == '6')
{
    pd =1;
    directions(1,1,1,1);
    speed(spe);    //perform action for RIGHT
}
else if (a == '2')
{
    pd =1;
    directions(0,0,0,0);
    speed(spe);    //perform action for RIGHT
}
else if(a == '1')
{
    pd =1;
    directions(1,1,1,1);
    diag_sped(sp,0);
}
else if (a == '3')
{
    pd =1;
    directions(0,0,0,0);
    diag_sped(sp,1);
}
else if (a == '5')
{
     pd =1;
     directions(1,1,1,1);
     diag_sped(sp,1);
}
else if (a == '7')
{
     pd =1;
     directions(0,0,0,0);
     diag_sped(sp,0);
}
else if(a == '<')
{
    sp=0.2;
    spe=0.4;
}
else if(a == '>')
{
    sp=0.4;
    spe=0.6;
}
else if(a == '(')
{
    sp=0.6;
    spe=0.8;
}
else if(a == ')')
{
    sp=0.8;
    spe=1.0;
}
}
}
}
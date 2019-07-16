#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

double *rk4_2(double Vx, double Vy, double x,double y, int len, double h);
double *euler_2(double Vx, double Vy, double x,double y, int len, double h);
double *leapfrog_2(double Vx, double Vy, double x,double y, int len, double h);

int main(){
    double h = 0.1;   
    double min_x = 0;
    double max_x = 10;
    int i;
    double x0, Vx0, y0, Vy0;
    int len = ((max_x-min_x)/h);
    x0 = 0.1163;
    Vx0 = -6.35;
    y0 = 0.9772;
    Vy0 = 0.606;

    rk4_2(Vx0,Vy0,x0,y0,len,h);
    euler_2(Vx0,Vy0,x0,y0,len,h);
    leapfrog_2(Vx0,Vy0,x0,y0,len,h);
    
    return 0;    
}

double f1(double Vx, double s, double x, double y){
    return Vx;
}    
    
double f2(double Vx, double s, double x, double y){
    double G = 6.67e-11;
    double M = 1.99e30;
    return (-G*M*s)/((x*x+y*y)*(x*x+y*y));
}    
   
double *rk4_2(double Vx, double Vy, double x,double y, int len, double h){
    int i;
    double average1;
    double average2;
    double average3;
    double average4;
    
    
    double a[len], b[len], c[len], d[len], t[len];
    a[1] = x;
    b[1] = y;
    c[1] = Vx;
    d[1] = Vy;
    
    for(i = 2; i<=len; i++){
        a[i] = 0;
        b[i] = 0;
        c[i] = 0;
        d[i] = 0;
    }    
    
    double k11x,k21x,k31x,k41x,k12x,k22x,k32x,k42x;
    double k11y,k21y,k31y,k41y,k12y,k22y,k32y,k42y;

    double y11x,y12x,y21x,y22x,y31x,y32x;
    double y11y,y12y,y21y,y22y,y31y,y32y;
    
    for(i = 2; i<=len; i++){
        k11x = f1(c[i-1],a[i-1],a[i-1],b[i-1]);
        k11y = f1(d[i-1],b[i-1],a[i-1],b[i-1]);
        
        k12x = f2(c[i-1],a[i-1],a[i-1],b[i-1]);
        k12y = f2(d[i-1],b[i-1],a[i-1],b[i-1]);
        
        y11x = a[i-1] + (h/2.0) * k11x;
        y11y = b[i-1] + (h/2.0) * k11y;
        
        y12x = c[i-1] + (h/2.0) * k12x;
        y12y = d[i-1] + (h/2.0) * k12y;
        
        k21x = f1(y12x, y11x,a[i-1],b[i-1]);
        k21y = f1(y12y, y11y,a[i-1],b[i-1]);
        
        k22x = f2(y12x, y11x,a[i-1],b[i-1]);
        k22y = f2(y12y, y11y,a[i-1],b[i-1]);
        
        y21x = a[i-1] + (h/2.0) * k21x;
        y21y = b[i-1] + (h/2.0) * k21y;
        
        y22x = c[i-1] + (h/2.0) * k22x;
        y22y = d[i-1] + (h/2.0) * k22y;
        
        k31x = f1(y22x, y21x,a[i-1],b[i-1]);
        k31y = f1(y22y, y21y,a[i-1],b[i-1]);
        
        k32x = f2(y22x, y21x,a[i-1],b[i-1]);
        k32y = f2(y12y, y21y,a[i-1],b[i-1]);
        
        y31x = a[i-1] + h * k31x;
        y31y = b[i-1] + h* k31y;
        
        y32x = c[i-1] + h* k32x;
        y32y = d[i-1] + h* k32y;
        
        k41x = f1(y32x, y31x,a[i-1],b[i-1]);
        k41y = f1(y32y, y31y,a[i-1],b[i-1]);
        
        k42x = f2(y32x, y31x,a[i-1],b[i-1]);
        k42y = f2(y32y, y31y,a[i-1],b[i-1]);
        
        average1 = (1.0/6.0)*(k11x + 2.0*k21x + 2.0*k31x + k41x);
        average2 = (1.0/6.0)*(k12x + 2.0*k22x + 2.0*k32x + k42x);
        average3 = (1.0/6.0)*(k11y + 2.0*k21y + 2.0*k31y + k41y);
        average4 = (1.0/6.0)*(k12y + 2.0*k22y + 2.0*k32y + k42y);
        
        a[i] = a[i-1] + h * average1;
        b[i] = b[i-1] + h * average3;
        c[i] = c[i-1] + h * average2;
        d[i] = d[i-1] + h * average4;
    }    

    
    t[1] = h;
    for(i = 2; i <= len; i++){
        t[i]  = t[i-1] + h;
    }  
    ofstream myfile;
    myfile.open ("datos1.dat", ios::out);
    streambuf* stream_buffer_cout1 = cout.rdbuf();
    streambuf* stream_buffer_myfile = myfile.rdbuf();
    cout.rdbuf(stream_buffer_myfile);
    for(i = 1; i<=len; i++){
            cout << t[i]<< " "  <<a[i] << " " << b[i] << " " << c[i] << " " << d[i] << endl;
    }    
    myfile.close();   

    return Vx,a;
}    

double *euler_2(double Vx, double Vy, double x,double y, int len, double h){
    int i;
    double *a1 = new double(len);
    double *a2 = new double(len);
    double *V1 = new double(len);
    double *V2 = new double(len);
    
    double a[len], b[len], c[len], d[len], t[len];
    a[1] = x;
    b[1] = y;
    c[1] = Vx;
    d[1] = Vy;
    
    for(i = 2; i<=len-1; i++){
        a[i] = 0;
        b[i] = 0;
        c[i] = 0;
        d[i] = 0;
    }    
    
    for(i = 1; i<=len; i++){
        a[i+1] = a[i] + f1(c[i], a[i],a[i],b[i])*h;
        b[i+1] = b[i] + f1(d[i], b[i],a[i],b[i])*h;
        
        c[i+1] = c[i] + f2(c[i], a[i],a[i],b[i])*h;
        d[i+1] = d[i] + f2(d[i], b[i],a[i],b[i])*h;

    }  
    
    a1 = a;
    a2 = b;
    V1 = c;
    V2 = d;
    
    t[1] = h;
    for(i = 2; i <= len; i++){
        t[i]  = t[i-1] + h;
    }  
    ofstream myfile;
    myfile.open ("datos2.dat", ios::out);
    streambuf* stream_buffer_cout1 = cout.rdbuf();
    streambuf* stream_buffer_myfile = myfile.rdbuf();
    cout.rdbuf(stream_buffer_myfile);
    for(i = 1; i<=len; i++){
            cout << t[i]<< " "  <<a[i] << " " << b[i] << " " << c[i] << " " << d[i] << endl;
    }    
    myfile.close();   
    return Vx,a;
}    

double *leapfrog_2(double Vx, double Vy, double x,double y, int len, double h){
    int i;
    double tau = 1e-2;
    
    double a[len], b[len], c[len], d[len], t[len];
    a[1] = x;
    b[1] = y;
    c[1] = Vx;
    d[1] = Vy;
    
    for(i = 2; i<=len-1; i++){
        a[i] = 0;
        b[i] = 0;
        c[i] = 0;
        d[i] = 0;
    }    
    
    for(i = 2; i<len-1; i++){
        a[i+1] = a[i-1] + 2*f1(c[i], a[i],a[i],b[i])*h;
        b[i+1] = b[i-1] + 2*f1(d[i], b[i],a[i],b[i])*h;
        c[i+1] = c[i-1] + 2*f2(c[i], a[i],a[i],b[i])*h;
        d[i+1] = d[i-1] + 2*f2(d[i], b[i],a[i],b[i])*h;
    }    
    
    
    t[1] = h;
    for(i = 2; i <= len; i++){
        t[i]  = t[i-1] + h;
    }  
    ofstream myfile;
    myfile.open ("datos3.dat", ios::out);
    streambuf* stream_buffer_cout1 = cout.rdbuf();
    streambuf* stream_buffer_myfile = myfile.rdbuf();
    cout.rdbuf(stream_buffer_myfile);
    for(i = 1; i<=len; i++){
            cout << t[i]<< " "  <<a[i] << " " << b[i] << " " << c[i] << " " << d[i] << endl;
    }    
    myfile.close();    
}    
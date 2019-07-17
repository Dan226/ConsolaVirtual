#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

double rk4_2(double Vx, double Vy, double x,double y, int len, double h);
double euler_2(double Vx, double Vy, double x,double y, int len, double h);
double leapfrog_2(double Vx, double Vy, double x,double y, int len, double h);

int main(){
    double h1 = 0.01;   
    double tmax = 20;
    int i;
    double x0, Vx0, y0, Vy0;
    int len1 = ((tmax)/h1);
    x0 = 0.1163;
    Vx0 = -6.35;
    y0 = 0.9772;
    Vy0 = 0.606;
    
    //dt = 0.01
    
    ofstream myfile1;
    myfile1.open ("datos1.dat", ios::out);
    streambuf* stream_buffer_cout1 = cout.rdbuf();
    streambuf* stream_buffer_myfile1 = myfile1.rdbuf();
    cout.rdbuf(stream_buffer_myfile1);
    rk4_2(Vx0,Vy0,x0,y0,len1,h1);
    myfile1.close();   
    
    ofstream myfile2;
    myfile2.open ("datos2.dat", ios::out);
    streambuf* stream_buffer_cout2 = cout.rdbuf();
    streambuf* stream_buffer_myfile2 = myfile2.rdbuf();
    cout.rdbuf(stream_buffer_myfile2);
    euler_2(Vx0,Vy0,x0,y0,len1,h1);
    myfile2.close(); 
    
    ofstream myfile3;
    myfile3.open ("datos3.dat", ios::out);
    streambuf* stream_buffer_cout3 = cout.rdbuf();
    streambuf* stream_buffer_myfile3 = myfile3.rdbuf();
    cout.rdbuf(stream_buffer_myfile3);
    leapfrog_2(Vx0,Vy0,x0,y0,len1,h1);
    myfile3.close();   
    
    //dt = 0.5
    
    double h2 = 0.0001;
    int len2 = ((tmax)/h2);    
    
    ofstream myfile4;
    myfile4.open ("datos4.dat", ios::out);
    streambuf* stream_buffer_cout4 = cout.rdbuf();
    streambuf* stream_buffer_myfile4 = myfile4.rdbuf();
    cout.rdbuf(stream_buffer_myfile4);
    rk4_2(Vx0,Vy0,x0,y0,len2,h2);
    myfile4.close();   
    
    ofstream myfile5;
    myfile5.open ("datos5.dat", ios::out);
    streambuf* stream_buffer_cout5 = cout.rdbuf();
    streambuf* stream_buffer_myfile5 = myfile5.rdbuf();
    cout.rdbuf(stream_buffer_myfile5);
    euler_2(Vx0,Vy0,x0,y0,len2,h2);
    myfile5.close(); 
    
    ofstream myfile6;
    myfile6.open ("datos6.dat", ios::out);
    streambuf* stream_buffer_cout6 = cout.rdbuf();
    streambuf* stream_buffer_myfile6 = myfile6.rdbuf();
    cout.rdbuf(stream_buffer_myfile6);
    leapfrog_2(Vx0,Vy0,x0,y0,len2,h2);
    myfile6.close();   
    
    // dt = 0.001

    double h3 = 0.001;
    int len3 = ((tmax)/h3);    
    
    ofstream myfile7;
    myfile7.open ("datos7.dat", ios::out);
    streambuf* stream_buffer_cout7 = cout.rdbuf();
    streambuf* stream_buffer_myfile7 = myfile7.rdbuf();
    cout.rdbuf(stream_buffer_myfile7);
    rk4_2(Vx0,Vy0,x0,y0,len3,h3);
    myfile7.close();   
    
    ofstream myfile8;
    myfile8.open ("datos8.dat", ios::out);
    streambuf* stream_buffer_cout8 = cout.rdbuf();
    streambuf* stream_buffer_myfile8 = myfile8.rdbuf();
    cout.rdbuf(stream_buffer_myfile8);
    euler_2(Vx0,Vy0,x0,y0,len3,h3);
    myfile8.close(); 
    
    ofstream myfile9;
    myfile9.open ("datos9.dat", ios::out);
    streambuf* stream_buffer_cout9 = cout.rdbuf();
    streambuf* stream_buffer_myfile9 = myfile9.rdbuf();
    cout.rdbuf(stream_buffer_myfile9);
    leapfrog_2(Vx0,Vy0,x0,y0,len3,h3);
    myfile9.close(); 
    return 0;    
}

double f1(double Vx, double s, double x, double y){
    return Vx;
}    
    
double f2(double Vx, double s, double x, double y){
    double G1 = 6.67e-11;
    double UA = 149597870700;
    double M = 1.99e30;
    double yr = 31536000;
    double G = G1*(1/(UA*UA*UA))*(M)*(yr*yr);
    return -(G*s)/pow(((x*x+y*y)),(3.0/2.0));
}    

double f3(double Vx, double Vy, double x, double y){
    double G1 = 6.67e-11;
    double UA = 149597870700;
    double M = 1.99e30;
    double yr = 31536000;
    double m = 5.972e24;
    double G = G1*(1/(UA*UA*UA))*(M)*(yr*yr);
    return 0.5*m*(Vx*Vx + Vy*Vy)- (G*M*m)/(pow(x*x+y*y,0.5));   
}    
   
double rk4_2(double Vx, double Vy, double x,double y, int len, double h){
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
        y31y = b[i-1] + h * k31y;
        
        y32x = c[i-1] + h * k32x;
        y32y = d[i-1] + h * k32y;
        
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
    
    for(i = 1; i<=len; i++){
            cout << t[i]<< " "  <<a[i] << " " << b[i] << " " << c[i] << " " << d[i] << endl;
    } 
  
    
}    

double euler_2(double Vx, double Vy, double x,double y, int len, double h){
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
    
 
    for(i = 1; i<=len-1; i++){
        a[i+1] = a[i] + f1(c[i], a[i],a[i],b[i])*h;
        b[i+1] = b[i] + f1(d[i], b[i],a[i],b[i])*h;
        
        c[i+1] = c[i] + f2(c[i], a[i],a[i],b[i])*h;
        d[i+1] = d[i] + f2(d[i], b[i],a[i],b[i])*h;
    }  
    
    t[1] = h;
    for(i = 2; i <= len; i++){
        t[i]  = t[i-1] + h;
    }  
    for(i = 1; i<=len; i++){
            cout << t[i]<< " "  <<a[i] << " " << b[i] << " " << c[i] << " " << d[i] << endl;
    }      

}    

double leapfrog_2(double Vx, double Vy, double x,double y, int len, double h){
    int i;
    double tau = h/2.0;
    
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
    
    a[0] = a[1] - 2.0*f1(c[1], a[1],a[1],b[1])*h;
    b[0] = b[1] - 2.0*f1(d[1], b[1],a[1],b[1])*h;
        
    c[0] = c[1] - 2.0*f2(c[1], a[1],a[1],b[1])*h;
    d[0] = d[1] - 2.0*f2(d[1], b[1],a[1],b[1])*h;
    
    
    
    for(i =1; i<len-2; i++){
        
        c[i+1] = c[i-1] + 2.0*f2(c[i], a[i],a[i],b[i])*h;
        d[i+1] = d[i-1] + 2.0*f2(d[i], b[i],a[i],b[i])*h;
        
        a[i+1] = a[i-1] + 2.0*f1(c[i], a[i],a[i],b[i])*h;
        b[i+1] = b[i-1] + 2.0*f1(d[i], b[i],a[i],b[i])*h;
        
        
    }    
    
    
    t[1] = h;
    for(i = 2; i <= len; i++){
        t[i]  = t[i-1] + h;
    }  

    for(i = 1; i<=len; i++){
            cout << t[i]<< " "  <<a[i] << " " << b[i] << " " << c[i] << " " << d[i] << endl;
    }    
  
}    

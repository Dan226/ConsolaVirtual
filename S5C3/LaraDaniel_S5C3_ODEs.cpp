#include <iostream>
#include <fstream>

using namespace std;

double f1(double x, double y);
double *rk4_2(double *x, double *y, int len, double h);

int main(){
    double h = 0.01;   
    double min_x = 0;
    double max_x = 10;
    int i;
    double *x, *V, *x0;
    int len = ((max_x-min_x)/h);
    double a[len], b[len], c[len];
    a[1] = 0.1;
    b[1] = 0.0;
    c[1] = h;
    for(i = 2; i <= len; i++){
        a[i] = 0;
        b[i] = 0; 
        c[i]  = c[i-1] + h;
    }  
    x = a;
    V = b;
    x0 = c;

    rk4_2(x,V,len,h);
    
    return 0;    
}



double f1(double Vx, double x){
    double k = 300.0;
    double m = 2.0;
    return Vx;
}    
    
double f2(double Vx, double x){
    double k = 300.0;
    double m = 2.0;
    double h = 0.01;
    return -(k/m)*x;
}    
    
double *rk4_2(double *x, double *V, int len, double h){
    int i;
    double average1;
    double average2;
    double k11,k21,k31,k41,k12,k22,k32,k42;
    double x1,x2,x3;
    double y11,y12,y21,y22,y31,y32;
    double *a = new double(len);
    double *Vx = new double(len);
    double t[len];
    
    for(i = 2; i<=len; i++){
        k11 = f1(V[i-1],x[i-1]);
        k12 = f2(V[i-1],x[i-1]);
        
        x1 = x[i-1]+ (h/2.0);
        y11 = x[i-1] + (h/2.0) * k11;
        y12 = V[i-1] + (h/2.0) * k12;
        k21 = f1(y12, y11);
        k22 = f2(y12, y11);
        
        x2 = x[i-1] + (h/2.0);
        y21 = x[i-1] + (h/2.0) * k21;
        y22 = V[i-1] + (h/2.0) * k22;
        k31 = f1(y22, y21);
        k32 = f2(y22, y21);
        
        x3 = x[i-1] + h;
        y31 = x[i-1] + h * k31;
        y32 = V[i-1] + h * k32;
        k41 = f1(y32, y31);
        k42 = f2(y32, y31);
        
        average1 = (1.0/6.0)*(k11 + 2.0*k21 + 2.0*k31 + k41);
        average2 = (1.0/6.0)*(k12 + 2.0*k22 + 2.0*k32 + k42);
        
        x[i] = x[i-1] + h * average1;
        V[i] = V[i-1] + h * average2;
    }    
    a = x;
    Vx = V;
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
            cout << Vx[i]<< " "  <<a[i] << " " << t[i] << endl;
    }    
    myfile.close();   
    
    return Vx,a;
}    
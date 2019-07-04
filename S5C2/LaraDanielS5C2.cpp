#include <iostream>
#include <fstream>

using namespace std;

double *euler(double *x, double *y, int len, double h);
double *rk4(double *x, double *y, int len, double h);

int main(){
    double h = 0.01;   
    double min_x = 0.0;
    double max_x = 2.0;
    int i;
    double *x, *y, *x0;
    int len = ((max_x - min_x)/h); 
    double a[len], b[len], c[len];
    a[1] = min_x;
    b[1] = 1.0;
    c[1] = h;
    for(i = 2; i <= len; i++){
        a[i] = 0;
        b[i] = 0; 
        c[i]  = c[i-1] + h;
    }   
    x = a;
    y = b;
    x0 = c;
    double *d1;
    double *d2;
    d1 = euler(x,y,len,h);
    d2 = rk4(x,y,len,h);
    ofstream myfile;
    myfile.open ("datos1.dat", ios::out);
    streambuf* stream_buffer_cout1 = cout.rdbuf();
    streambuf* stream_buffer_myfile = myfile.rdbuf();
    cout.rdbuf(stream_buffer_myfile);
    x0 ;
    for(i = 1; i<=len; i++){
            cout << x[i]<< " "  <<d1[i] << endl;
    }    
    myfile.close();   
    ofstream file;
    file.open ("datos2.dat", ios::out);
    streambuf* stream_buffer_cout2 = cout.rdbuf();
    streambuf* stream_buffer_file = file.rdbuf();
    cout.rdbuf(stream_buffer_file);
    x0 ;
    for(i = 1; i<=len; i++){
            cout << x[i]<< " "  <<d2[i] << endl;
    }    
    file.close();  
    return 0;
}    
    
double fun(double x, double y){
    return -y;
}    
    

double *euler(double *x, double *y, int len, double h){
    double *dx, *dy;
    for(int i = 2; i<= len; i++){
        x[i] = x[i-1] + h;
        y[i] = y[i-1] + h * fun(x[i-1], y[i-1]); 
    }       
    dx = x;
    dy = y;
    return dy;
}    
    

double *rk4(double *x, double *y, int len, double h){
    int i;
    double average;
    double k1,k2,k3,k4;
    double *a = new double(len);
    double *b = new double(len);
    for(i = 2; i<=len; i++){
        k1 = h*fun(x[i-1], y[i-1]);
        k2 = h*fun(x[i-1] + 0.5 * h, y[i-1] + 0.5 * k1);
        k3 = h*fun(x[i-1] + 0.5 * h, y[i-1] + 0.5 * k2);
        k4 = h*fun(x[i-1] + h      , y[i-1] + k3);
        average = (1.0/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4);
        
        x[i] = x[i-1] + h;
        y[i] = y[i-1] + average;
    }    
    a = x;
    b = y;
    return b;
}    
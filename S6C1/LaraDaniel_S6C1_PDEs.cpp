#include <iostream>
#include <fstream>
#include <math.h> 

using namespace std;

double pde(int len, double h);

int main(){
    double h = 0.01;   
    double min_x = 0;
    double max_x = 5;
    int i;
    int len = ((max_x-min_x)/h);
    pde(len,h);
    
    return 0;    
}

double pde(int len, double h){
    double a[len];
    double u_inicial[len];
    double u_future[len];
    double *u_past = new double(len);
    double *u_present = new double(len);
    double delta_a, delta_t, c, r;
    a[1] = h;
    int i;
    int iter = 350;
    for(i = 1; i <= len; i++){
        a[i]  = a[i-1] + h;
    }  
    for(i = 2; i <= len; i++){
        u_inicial[i]  = exp(-((a[i]-0.3)*(a[i]-0.3))/0.01);
    }  
    delta_a = a[1]-a[0];  
    delta_t = 0.0005;
    c = 1.0;
    r = c*delta_t/delta_a;
    u_inicial[0] = 0.0;
    u_inicial[len-1] = 0.0;
    for(i = 1; i <= len; i++){
        u_future[i]  = 0.0;
    }  
    for(i = 1; i <= len; i++){
        u_future[i] = u_inicial[i] + (pow(r,2.0)/2.0) * (u_inicial[i+1] - 2.0 * u_inicial[i] + u_inicial[i-1]);
    }     
    u_past = u_inicial;
    u_present = u_future;
    
    for(int j = 1; j <= iter; j++){
        for(i = 2; i <= (len-1); i++){
            u_future[i] = (2.0*(1.0-pow(r,2.0)))*u_present[i] - u_past[i] + (pow(r,2.0))*(u_present[i+1] +  u_present[i-1]);
           
        }  
        u_past = u_present;
        u_present = u_future;
        ofstream myfile;
        myfile.open ("datos1.dat", ios::out);
        streambuf* stream_buffer_cout1 = cout.rdbuf();
        streambuf* stream_buffer_myfile = myfile.rdbuf();
        cout.rdbuf(stream_buffer_myfile);
        for(i = 1; i<=len; i++){
                cout << u_present[i]<< " "  <<u_inicial[i] << " " << a[i] << endl;
        }    
        myfile.close();  
    }    
}    
    

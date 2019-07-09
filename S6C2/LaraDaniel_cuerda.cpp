#include <iostream>
#include <fstream>
#include <math.h> 

using namespace std;

double pde(int len, double h);

int main(){
    double h = 0.01;   
    double min_x = 0;
    double max_x = 1;
    int i;
    int len = ((max_x-min_x)/h);
    pde(len,h);
    
    return 0;    
}

double pde(int len, double h){
    double a[len];
    double u_inicial[len];
    double u_future[len];
    double u_past[len];
    double u_present[len];
    double delta_a, delta_t, c, r;
    a[1] = h;
    int i;
    int iter = 350;
    float A0 = 0.01;
    for(i = 2; i <= len; i++){
        a[i]  = a[i-1] + h;
    }  
    for(i = 1; i <= len/2; i++){
        u_inicial[i]  = A0/0.5*(a[i]);
    }   
    for(i = len/2+1; i <= len; i++){
        u_inicial[i]  = 2*A0-A0/0.5*(a[i]);
    }  
    
    
    delta_a = 0.005;  
    delta_t = (delta_a/c)*0.25;
    c = 300.0;
    r = 0.00125;
    
    u_inicial[0] = 0.0;
    u_inicial[len] = 0.0;
    
    for(i = 1; i <= len; i++){
        u_future[i] = 0.0;
     }
    
    for(i = 2; i <= (len-1); i++){
        u_future[i] = u_inicial[i]+(r*r/2.0)*(u_inicial[i+1]-2.0*u_inicial[i]+u_inicial[i-1]);
        cout << u_future[i]<< " " << u_inicial[i] <<endl;
    }   
    
    for(i = 1; i <= len; i++){
        u_past[i] = u_inicial[i];
        u_present[i] = u_future[i];
     }
    

  
    for(int j = 1; j <= iter; j++){
        for(i = 2; i <= (len-1); i++){
            u_future[i] = (2.0*(1.0-r*r))*u_present[i] - u_past[i] + (r*r)*(u_present[i+1] +  u_present[i-1]);
        }     
        for(i = 1; i <= len; i++){
            u_past[i] = u_present[i];
            u_present[i] = u_future[i];
        }
    }    
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
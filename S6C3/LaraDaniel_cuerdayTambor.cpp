#include <iostream>
#include <fstream>
#include <math.h> 

using namespace std;

double pde(int len, double h);
double pdelibre(int len, double h);
double pdeoscilacion(int len,double h, int L);

int main(){
    double h = 0.01;   
    double min_x = 0;
    double max_x = 1;
    int i;
    int L = 1;
    int len = ((max_x-min_x)/h);
    pde(len,h);
    pdelibre(len,h);
    pdeoscilacion(len,h, L);
    
    return 0;    
}

double pde(int len, double h){
    double a[len];
    double u_inicial[len];
    double u_future[len];
    double u_past[len];
    double u_present[len];
    double delta_a, delta_t, c, r;
    double t1[len],t2[len],t3[len],t4[len],t5[len], t6[len];
    a[1] = h;
    int i;
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
    c = 300.0;
    delta_t = (delta_a/c)*0.25;
    int iter = 0.1/delta_t;
    cout << iter;
    
    r = 0.00125;
    
    u_inicial[0] = 0.0;
    u_inicial[len] = 0.0;
    
    for(i = 1; i <= len; i++){
        u_future[i] = 0.0;
     }
    
    for(i = 2; i <= (len-1); i++){
        u_future[i] = u_inicial[i]+(r*r/2.0)*(u_inicial[i+1]-2.0*u_inicial[i]+u_inicial[i-1]);
    }   
    
    for(i = 1; i <= len; i++){
        u_past[i] = u_inicial[i];
        u_present[i] = u_future[i];
     }
    


    for(int j = 1; j <= iter; j++){
        
        for(i = 2; i <= (len-1); i++){
            u_future[i] = (2.0*(1.0-r*r))*u_present[i] - u_past[i] + (r*r)*(u_present[i+1] +  u_present[i-1]);
            u_future[1] = 0.0;
        }    
        
        
        for(i = 1; i <= len; i++){
            u_past[i] = u_present[i];
            u_present[i] = u_future[i];
        }
       if(j == 1000){
           for(i = 1; i <= len; i++){
            t6[i] = u_future[i];
          }
       }
        else if(j == 5000){
            for(i = 1; i <= len; i++){
            t1[i] = u_future[i];
            }
        } 
        else if(j == 10000){
            for(i = 1; i <= len; i++){
            t2[i] = u_future[i];
            }
        }
        else if(j == 15000){
            for(i = 1; i <= len; i++){
            t3[i] = u_future[i];
            }
        }
        else if(j == 20000){
            for(i = 1; i <= len; i++){
            t4[i] = u_future[i];
            }
        }
        else if(j == 24000){
            for(i = 1; i <= len; i++){
            t5[i] = u_future[i];
            }
        }

    }  
    
    ofstream myfile;
    myfile.open ("datos1.dat", ios::out);
    streambuf* stream_buffer_cout1 = cout.rdbuf();
    streambuf* stream_buffer_myfile = myfile.rdbuf();
    cout.rdbuf(stream_buffer_myfile);
    for(i = 1; i<=len; i++){
        cout << t6[i]<<" "<< t1[i]<< " "  << t2[i]<< " "  << t3[i]<< " "  << t4[i]<< " "  << t5[i]<< " "  << u_inicial[i] << " " << a[i] << endl;
    }    
    myfile.close();  
}    



double pdelibre(int len, double h){
    double a[len];
    double u_inicial[len];
    double u_future[len];
    double u_past[len];
    double u_present[len];
    double delta_a, delta_t, c, r;
    double t1[len],t2[len],t3[len],t4[len],t5[len], t6[len];
    a[1] = h;
    int i;
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
    c = 300.0;
    delta_t = (delta_a/c)*0.25;
    int iter = 0.1/delta_t;
    
    r = 0.00125;
    
    u_inicial[0] = 0.0;
    u_inicial[len] = 0.0;
    
    for(i = 1; i <= len; i++){
        u_future[i] = 0.0;
     }
    
    for(i = 2; i <= (len-1); i++){
        u_future[i] = u_inicial[i]+(r*r/2.0)*(u_inicial[i+1]-2.0*u_inicial[i]+u_inicial[i-1]);
    }   
    
    u_future[len] = u_future[len-1];
    
    for(i = 1; i <= len; i++){
        u_past[i] = u_inicial[i];
        u_present[i] = u_future[i];
     }
    


    for(int j = 1; j <= iter; j++){
        
        for(i = 2; i <= (len-1); i++){
            u_future[i] = (2.0* (1 - r*r))*u_present[i] - u_past[i] + (r*r)*(u_present[i+1] +  u_present[i-1]);
           
        }  
        for(i = 0; i <= len; i++){
            u_future[0] = 0.0;
            u_future[len] = u_future[len-1];
            u_past[i] = u_present[i];
            u_present[i] = u_future[i];
        }
       if(j == 1000){
           for(i = 1; i <= len; i++){
            t6[i] = u_future[i];
          }
       }
        else if(j == 5000){
            for(i = 1; i <= len; i++){
            t1[i] = u_future[i];
            }
        } 
        else if(j == 8000){
            for(i = 1; i <= len; i++){
            t2[i] = u_future[i];
            }
        }
        else if(j == 15000){
            for(i = 1; i <= len; i++){
            t3[i] = u_future[i];
            }
        }
        else if(j == 20000){
            for(i = 1; i <= len; i++){
            t4[i] = u_future[i];
            }
        }
        else if(j == 24000){
            for(i = 1; i <= len; i++){
            t5[i] = u_future[i];
            }
        }
    }   
    ofstream myfile;
    myfile.open ("datos2.dat", ios::out);
    streambuf* stream_buffer_cout1 = cout.rdbuf();
    streambuf* stream_buffer_myfile = myfile.rdbuf();
    cout.rdbuf(stream_buffer_myfile);
    for(i = 1; i<=len; i++){
        cout << t6[i]<<" "<< t1[i]<< " "  << t2[i]<< " "  << t3[i]<< " "  << t4[i]<< " "  << t5[i]<< " "  << u_inicial[i] << " " << a[i] << endl;
    }    
    myfile.close();  
}    

double pdeoscilacion(int len, double h, int L){
    
    double a[len];
    double u_inicial[len];
    double u_future[len];
    double u_past[len];
    double u_present[len];
    double delta_a, delta_t, c, r;
    double t1[len],t2[len],t3[len],t4[len],t5[len], t6[len];
    a[1] = h;
    int i;
    float A0 = 0.01;
    for(i = 2; i <= len; i++){
        a[i]  = a[i-1] + h;
    }  
    for(i = 1; i <= len; i++){
        u_inicial[i]  = 0;
    }      
    delta_a = 0.005;  
    c = 300.0;
    delta_t = (delta_a/c)*0.25;
    int iter = 0.1/delta_t;
    r = 0.00125;
    
    u_inicial[0] = 0.0;
    u_inicial[len] = 0.0;
    
    for(i = 1; i <= len; i++){
        u_future[i] = 0.0;
     }
    
    for(i = 2; i <= (len-1); i++){
        u_future[i] = u_inicial[i]+(r*r/2.0)*(u_inicial[i+1]-2.0*u_inicial[i]+u_inicial[i-1]);
    }   
    
    
    
    for(i = 1; i <= len; i++){
        u_past[i] = u_inicial[i];
        u_present[i] = u_future[i];
     }
    


    for(int j = 1; j <= iter; j++){
        
        for(i = 2; i <= (len-1); i++){
            u_future[i] = (2.0* (1 - r*r))*u_present[i] - u_past[i] + (r*r)*(u_present[i+1] +  u_present[i-1]);
            
            
        }    
        u_future[len] = A0*cos((3.0*c*j*3.1415167)/L);
        
        for(i = 0; i <= len; i++){    
            u_past[i] = u_present[i];
            u_present[i] = u_future[i];
        }
       if(j == 1000){
           for(i = 1; i <= len; i++){
            t6[i] = u_future[i];
          }
       }
        else if(j == 5000){
            for(i = 1; i <= len; i++){
            t1[i] = u_future[i];
            }
        } 
        else if(j == 8000){
            for(i = 1; i <= len; i++){
            t2[i] = u_future[i];
            }
        }
        else if(j == 15000){
            for(i = 1; i <= len; i++){
            t3[i] = u_future[i];
            }
        }
        else if(j == 20000){
            for(i = 1; i <= len; i++){
            t4[i] = u_future[i];
            }
        }
        else if(j == 24000){
            for(i = 1; i <= len; i++){
            t5[i] = u_future[i];
            }
        }
    }   
    ofstream myfile;
    myfile.open ("datos3.dat", ios::out);
    streambuf* stream_buffer_cout1 = cout.rdbuf();
    streambuf* stream_buffer_myfile = myfile.rdbuf();
    cout.rdbuf(stream_buffer_myfile);
    for(i = 1; i<=len; i++){
        cout << t6[i]<<" "<< t1[i]<< " "  << t2[i]<< " "  << t3[i]<< " "  << t4[i]<< " "  << t5[i]<< " "  << u_inicial[i] << " " << a[i] << endl;
    }    
    myfile.close();  
}    

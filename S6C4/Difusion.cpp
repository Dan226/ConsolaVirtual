#include <iostream>
#include <fstream>
#include <math.h> 

using namespace std;

double difusion(int len, double h);

int main(){
    float h = 0.01;
    float L = 1.0;
    int len = (L/h);
    difusion(len,h);
    return 0;
}       


double difusion(int len, double h){
    float v = 1e-4;
    double placa[len][len];
    double p_future[len][len];
    int i, j, t;
    float delta_t = ((h*h)/v)*0.25;
    int iter = 2500/delta_t;
    
    for(i = 0; i <= (len-1); i++){
        for(j = 0; j <= (len-1); j++){
            placa[i][j] = 50;
        }    
    } 
    for(i = 21; i <= 41; i++){
        for(j = 41; j < 61; j++){
            placa[i][j] = 100;
        }    
    }    

    ofstream myfile;
    myfile.open ("datos1.dat", ios::out);
    streambuf* stream_buffer_cout1 = cout.rdbuf();
    streambuf* stream_buffer_myfile = myfile.rdbuf();
    cout.rdbuf(stream_buffer_myfile);
    for(i = 0; i<=(len-1); i++){
        for(j = 0; j<=(len-1); j++){
            cout << placa[i][j] << " ";
        }    
        cout << endl;
    }    
    myfile.close(); 
    
    
    for(t = 0; t <= iter; t++){
        for(i = 1; i < (len-1); i++){
            for(j = 1; j < (len-1); j++){
                p_future[i][j] = placa[i][j] + v*(delta_t/(h*h))*(placa[i+1][j]+placa[i-1][j]) + v*(delta_t/(h*h))*(placa[i][j+1]+placa[i][j-1] - 4*placa[i][j]) ;
            }    
        } 
        for(i = 0; i <= (len-1); i++){
            for(j = 0; j <= (len-1); j++){
                p_future[0][j] = 50;
                p_future[len-1][j] = 50;
                p_future[i][0] = 50;
                p_future[i][len-1] = 50;
            }    
        } 
        
        for(i = 0; i <= (len-1); i++){
            for(j = 0; j <= (len-1); j++){
                placa[i][j] = p_future[i][j] ;
            }    
        } 
    
        
     if(t*delta_t == 100){
          ofstream myfile;
          myfile.open ("datos2.dat", ios::out);
          streambuf* stream_buffer_cout1 = cout.rdbuf();
          streambuf* stream_buffer_myfile = myfile.rdbuf();
          cout.rdbuf(stream_buffer_myfile);
          for(i = 0; i<=(len-1); i++){
              for(j = 0; j<=(len-1); j++){
                   cout << placa[i][j] << " ";
               }    
              cout << endl;
           }    
          myfile.close();  
      } 
      if(t*delta_t == 2500){
          ofstream myfile;
          myfile.open ("datos3.dat", ios::out);
          streambuf* stream_buffer_cout1 = cout.rdbuf();
          streambuf* stream_buffer_myfile = myfile.rdbuf();
          cout.rdbuf(stream_buffer_myfile);
          for(i = 0; i<=(len-1); i++){
              for(j = 0; j<=(len-1); j++){
                   cout << placa[i][j] << " ";
               }    
              cout << endl;
           }    
          myfile.close();  
      } 
    }  
}    
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
    float placa[len][len];
    int i, j;
    for(i = 0; i < (len-1); i++){
        for(j = 0; j < (len-1); j++){
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
    for(i = 0; i<(len-1); i++){
        for(j = 0; j<(len-1); j++){
            cout << placa[i][j] << " ";
        }    
        cout << endl;
    }    
    myfile.close(); 
    
}    
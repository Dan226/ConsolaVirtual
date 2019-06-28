#include<iostream>
#include<math.h>

using namespace std;

float rectangulo(int a,double b,int M);

int main(){
    int a = 0;
    double b = (3*3.141516)/2;
    int M = 1000;
    cout << rectangulo(a,b,M)<<endl;
    
    return 0;    
}


float rectangulo(int a,double b,int M){
    float h = (b-a)/(M-1);
    float x[M];
    float x1[M];
    double delta =b-a/(M-1);
    float suma;
    for (int i=0; i<M; ++i){
        x[i]=0 + (i*delta);
    }
    for (int i=0; i<M; ++i){
        x1[i] = cos(x[i])*h;
    }
    for (int i=0; i<M; ++i){
        suma += x1[i];
    }
    return suma;
}    
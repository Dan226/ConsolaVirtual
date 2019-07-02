#include<iostream>
#include<array>
#include<math.h>

using namespace std;

double derivada(int M, float *arrecos);

int main(){
    float int1;
    float int2;
    int puntos;
    cout << "limite 1" << endl;
    cin >> int1;
    cout << "limite 2" << endl;
    cin >> int2;
    cout << "numero de puntos" << endl;
    cin >> puntos;
    float y[puntos];
    float x[puntos];
    int i;
    float *y1;
    float h =  (int2-int1)/puntos;
    for (i = 1; i <= puntos; i++){
        x[i] = i*h;
    }    
    for (i = 1; i <= puntos; i++){
        y[i] = cos(x[i]);   
    } 
    y1 = y;
    cout << derivada(puntos, y1)[i] << endl;  

       
    return 0;    
}


double derivada(int M, float *arrecos){
    float *derivada;
    float deri[M];

    int i;
    for(i = 1; i <= (M - 1); i++){
        deri[i] = (arrecos[i+1]-arrecos[i])/(2);
    }    
    derivada = deri;
    for(i = 1; i <= M ; i++){
        cout << derivada[i] << endl;
    }    
    return *derivada;
}    
#include<iostream>
#include<array>

using namespace std;

int punto(int a[], int b[]);
double producto(int *a, int *b);

int main(){
    int *a;
    int *b;
    int x[5] = {1,2,3,4,5};
    int y[5] = {10,20,30,40,50};
    int i;
    a = x;
    b = y;
    cout << punto(a,b) << endl;
    cout << producto(a,b) << endl;
    return 0;    
}

int punto(int *a, int *b){
    int i;
    double suma;
    for (int i = 0; i < 5; i++){
           suma += a[i]*b[i];
    }    
    cout << suma << endl;
}    

double producto(int *a, int *b){
    int i;
    for (int i = 0; i < 5; i++){
        cout << a[i]*b[i] << endl;
    } 
}    
    
    
    
    
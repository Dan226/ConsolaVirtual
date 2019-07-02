#include<iostream>

using namespace std;

int main(){
    int n = 7, n1 = 77;
    int fact = 1;  
    double fact1 = 1;
    for(int i=2;i<=n;i++){
        fact = fact*i;
    }    
    cout << "el factorial de 7 es:" << fact<<endl;
    
    for(int i=2;i<=n1;i++){
        fact1 = fact1*i;
    }  
    cout << "el factorial de 77 es:" << fact1<<endl;
    
    return 0;    
}

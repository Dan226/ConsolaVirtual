#include<iostream>

using namespace std;

int main(){
    int n;
    cout << "dar valor entero" << endl;
    cin >> n;
    double fact = 1;  
    for(int i=2;i<=n;i++){
        fact = fact*i;
    }    
    cout << "el factorial de" << n << "es:" << fact <<endl;
    
    return 0;    
}

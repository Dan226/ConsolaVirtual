#include<iostream>

using namespace std;

int main(){
    int a = 100;
    int lista[a];
    for(int i = 1; i <= 100; i++){
        lista[i] = i;    
    }    
    for(int i = 1; i <= 100; i++){
        if(lista[i]%3 == 0 && lista[i]%5 != 0){
            cout << lista[i] << endl;
            
        }         
    } 
    return 0;    
}

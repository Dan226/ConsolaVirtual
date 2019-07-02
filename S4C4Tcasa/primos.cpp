#include<iostream>

using namespace std;

int main()[
  int n1,n2,i;
  cout << "dar valor entero 1" << endl;
  cin >> n1;
  cout << "dar valor entero 2 mayor que 1" << endl;
  cin >> n2;
  int n[n2-n1];
  int suma[n2-n1];
  for(i = 1; i <=(n2-n1); i++){
    for(j = 1; j <=n2; j++){
      n[i] = j;
    }
  }
  for(i = 1; i <=(n[i]+1); i++){
    if(n[i]%i==0){
      suma[i]+=1;
    }
  }
  for(i = 1; i <=(n2-n1); i++){
    if(suma[i]==2){
      cout<<n[i]
    }
  }
]

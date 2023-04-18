#include <iostream>
#include <math.h>
using namespace std;


double equation(double n){

    if(n==0){
        return 0;

    }
    else{
        return (((pow((-1),(n+1))/n))+equation(n-1));
    }

}

double equation(){

cout<<"Please enter a number: "<<endl;
int n;
cin>>n;

if(n==0){
    return 0;
}
else{
    return (((pow((-1),(n+1))/n))+equation(n-1));
}
}


int main(){

int n;
cout<<"Please enter a number: "<<endl;
cin>>n;
cout<<equation(n)<<endl;
cout<<equation()<<endl;


}

#include<iostream>
using namespace std;
int main()
{
  int a, b, c;
  cin>>a>>b;
  c = a * (bool)(a / b) + b * (bool)(b / a);
  cout<<c;
}

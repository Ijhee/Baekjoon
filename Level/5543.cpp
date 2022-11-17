#include <iostream>
using namespace std;

int main() {
    int burger[3];
    int beverage[2];
    int c_burger = 9999;
    int c_beverage = 9999;
    for(int i = 0; i < 3; i++) {
        cin >> burger[i];
        if(burger[i] < c_burger)
            c_burger = burger[i];
    }
    for(int i = 0; i < 2; i++)
    {
        cin >> beverage[i];
        if(beverage[i] < c_beverage)
            c_beverage = beverage[i];
    }
    cout << c_beverage+ c_burger - 50;
}

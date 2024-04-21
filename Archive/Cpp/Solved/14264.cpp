#include <iostream>
#include <cmath>

using namespace std;

int main(void) {
    long double n;
    cin >> n;
    cout << fixed;
    cout.precision(15);
    cout << n * n * sqrt(3) / 4 <<endl;
    return 0;
}
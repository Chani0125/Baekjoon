#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string a, b;
    cin >> a >> b;
    short i, j;
    bool isFind = false;
    for (i = 0; i < a.length(); i++) {
        for (j = 0; j < b.length(); j++) if (a[i] == b[j]) { isFind = true; break; }
        if (isFind) break;
    }
    for (short k = 0; k < b.length(); k++, cout << endl) for (short l = 0; l < a.length(); l++) {
        if (k == j) cout << a[l];
        else if (l == i) cout << b[k];
        else cout << ".";
    }
}
#include <iostream>
#include <list>
#include <algorithm>

using namespace std;

int main(void) {
    int t, x, y, prev, ans = 0;
    list<int> x_list, y_list;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> x >> y;
        x_list.push_back(x);
        y_list.push_back(y);
    }
    sort(x_list.begin(), x_list.end());
    sort(y_list.begin(), y_list.end());
    prev = x_list.front();
    for (list<int>::iterator i = x_list.begin(); i != x_list.end(); i++) {
        if (*i == prev) ans++;
        prev = *i;
    }
    prev = y_list.front();
    for (list<int>::iterator i = y_list.begin(); i != y_list.end(); i++) {
        if (*i == prev) ans++;
        prev = *i;
    }
    return 0;
}
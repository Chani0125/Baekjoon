#include <iostream>
#include <list>

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
    bool is_find = false;
    x_list.sort(); prev = x_list.front();
    for (list<int>::iterator i = ++(x_list.begin()); i != x_list.end(); i++) {
        if (*i == prev) {
            if (is_find) continue;
            ans++;
            is_find = true;
        } else {
            is_find = false;
            prev = *i;
        }
    }
    is_find = false;
    y_list.sort(); prev = y_list.front();
    for (list<int>::iterator i = ++(y_list.begin()); i != y_list.end(); i++) {
        if (*i == prev) {
            if (is_find) continue;
            ans++;
            is_find = true;
        } else {
            is_find = false;
            prev = *i;
        }
    }
    cout << ans << endl;
    return 0;
}
#include <iostream>

using namespace std;

int main(void) {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n;
        int r[n], s[n] = {};
        bool is_impossible = false;
        for (int i = 0; i < n; i++) cin >> r[i];
        for (int i = 0; i < n; i++) {
            int k = 0;
            for (int j = n-i; j < n; j++) {
                if (r[n-1-i] + k >= r[j]) k++;
            }
            if (k + r[n-1-i] >= n) {
                is_impossible = true;
                break;
            } else {
                s[n-1-i] = k + r[n-1-i] + 1;
            }
        }
        if(is_impossible) {
            cout << "IMPOSSIBLE";
        } else {
            for (int i = 0; i < n; i++) cout << s[i] << " ";
        }
        cout << endl;
    }
    return 0;
}
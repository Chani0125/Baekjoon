#include <iostream>
#include <string>

using namespace std;

int main(void) {
    int t, n, k;
    for (cin >> t; t--;) {
        cin >> n;
        string *robots = new string[n];
        bool is_lose[n] = {0, };
        for (int i = 0; i < n; i++) cin >> robots[i];
        k = robots->length();
        // for (int i = 0; i < n; i++, cout << endl) {
        //     cout << robots[i];
        // }
        int r, p, s;
        for (int i = 0; i < k; i++) {
            r = 0; p = 0; s = 0;
            for (int j = 0; j < n; j++) {
                if (is_lose[j]) continue;
                if      (robots[j][i] == 'R') r++;
                else if (robots[j][i] == 'P') p++;
                else                          s++;
            }
            // cout << r << " " << p << " " << s << endl;
            if ((r == 0 && p == 0) || (p == 0 && s == 0) || (s == 0 && r == 0) || (r != 0 && p != 0 && s != 0)) continue;
            else if (r == 0) {for (int j = 0; j < n; j++) if (robots[j][i] == 'P') is_lose[j] = true;}
            else if (p == 0) {for (int j = 0; j < n; j++) if (robots[j][i] == 'S') is_lose[j] = true;}
            else             {for (int j = 0; j < n; j++) if (robots[j][i] == 'R') is_lose[j] = true;}
        }
        int ans = 0;
        for (int i = 0; i < n; i++) if (!is_lose[i]) {
            if (ans == 0) ans = i+1;
            else { ans = 0; break; }
            // cout << ans << endl;
        }
        cout << ans << endl;
    }
    return 0;
}
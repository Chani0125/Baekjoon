#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a, a + n);
    // for (int i = 0; i < n; i++) cout << a[i] << endl;
    int prev = a[0];
    int ans = a[n-1] + 3;
    if (a[0] != 0) {
        ans = 0;
    } else if (a[n-1] == 0) {
        ans = 1;
    } else {
        for (int i = 1; i < n; i++) {
            if (a[i] == prev) continue;
            if (a[i] != prev + 1) {
                ans = prev + 3;
                break;
            }
            prev++;
        }
    }
    
    cout << ans << endl;
    return 0;
}
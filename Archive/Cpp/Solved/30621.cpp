#include <bits/stdc++.h>

using namespace std;

int _binary_search(vector<int> &t, int n, int s, int e)
{
    if (s > e) return s;

    int m = (s + e) / 2;

    if (t[m] == n) return m+1;
    if (t[m] < n)  return _binary_search(t, n, m+1, e);
    return _binary_search(t, n, s, m-1);
} 

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;

    vector<int> t(n), b(n), c(n);
    for (int i = 0; i < n; i++) cin >> t[i];
    for (int i = 0; i < n; i++) cin >> b[i];
    for (int i = 0; i < n; i++) cin >> c[i];

    vector<long long> chaos(n+1);
    for (int i = 0; i < n; i++)
        chaos[i+1] = max(chaos[i], chaos[_binary_search(t, t[i]-b[i]-1, 0, n-1)] + c[i]);
    
    // for (auto i : chaos) cout << i << " "; cout << "\n";
    
    cout << chaos[n] << "\n";    
    
    return 0;
}

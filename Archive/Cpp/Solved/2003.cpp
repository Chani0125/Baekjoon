#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, m, ans = 0;
    cin >> n >> m;

    vector<int> num(n);
    for (int i = 0; i < n; i++)
        cin >> num[i];

    int n_first = 0, n_last = 0, n_sum = num[0];
    while (n_last < n-1 || n_sum >= m)
    {   
        if (n_sum == m)
            ans++;

        if (n_sum >= m)
            n_sum -= num[n_first++];
        else if (n_sum < m)
            n_sum += num[++n_last];
    }
    
    cout << ans << "\n";

    return 0;
}

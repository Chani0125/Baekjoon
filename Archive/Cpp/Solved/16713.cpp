#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n, q;
    cin >> n >> q;

    vector<int> prefix_xor(n+1, 0);

    int num;
    for (int i = 0; i < n; i++)
    {
        cin >> num;
        prefix_xor[i+1] = prefix_xor[i] ^ num;
    } 

    int s, e, ans = 0;
    for (int i = 0; i < q; i++)
    {
        cin >> s >> e;  
        ans ^= prefix_xor[e] ^ prefix_xor[s-1];
    }

    cout << ans << "\n";

    return 0;
}   

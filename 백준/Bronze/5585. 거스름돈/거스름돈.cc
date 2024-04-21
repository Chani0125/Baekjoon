#include <bits/stdc++.h>

#define X first
#define Y second

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int p;
    cin >> p;
    p = 1000 - p;

    const vector<int> coins{500, 100, 50, 10, 5, 1};

    int ans = 0;
    for (int c : coins)
    {
        ans += p / c;
        p %= c;
    }

    cout << ans;

    return 0;
}
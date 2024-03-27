#include <bits/stdc++.h>

#define ll long long

using namespace std;

ll gcd(ll a, ll b)
{
    while (b != 0)
    {
        ll r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    ll n, b;
    cin >> n >> b;

    ll p = 0, q = 0;
    for (int i = 0; i < n; i++)
    {
        int x, y;
        cin >> x >> y;
        p += x;
        q += y;
    }
    q -= b * n;

    if (p == q || p == 0)
    {
        cout << "EZPZ" << "\n";
        return 0;
    }
    
    if (q % p == 0)
    {
        cout << q / p << "\n";
        return 0;
    }

    ll tmp = gcd(p, q);
    p /= tmp; q /= tmp;

    if (p < 0)
    {
        p *= -1; q *= -1;
    }
    
    cout << q << "/" << p << "\n";
    
    return 0;
}

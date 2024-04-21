#include <bits/stdc++.h>

using namespace std;

unsigned long long cost(vector<int> &x, unsigned long long p)
{
    unsigned long long c = 0;
    for (int i = 1; i < x.size(); i++)
    {
        if (x[i] >= p*i)
            c += x[i] - p*i;
        else
            c += p*i - x[i];
    }
    return c;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;
    vector<int> x(n);
    for (int i = 0; i < n; i++)
        cin >> x[i];
    
    if (n == 1)
    {
        cout << 0 << "\n";
        return 0;
    }

    unsigned long long lo = 0, hi = __INT_MAX__;
    unsigned long long p = lo, q = hi;
    unsigned long long cp, cq, c_min, c_now;
    while (hi - lo >= 3)
    {
        p = (lo * 2 + hi) / 3;
        q = (lo + hi * 2) / 3;

        cp = cost(x, p);
        cq = cost(x, q);

        if (cp <= cq) hi = q;
        else lo = p;
    }

    c_min = cost(x, lo);
    for (int i = lo+1; i <= hi; i++)
    {
        c_now = cost(x, i);
        if (c_now < c_min)
        {
            c_min = c_now;
            lo = i;
        }
    }

    cout << cost(x, lo) << "\n";
    
    return 0;
}

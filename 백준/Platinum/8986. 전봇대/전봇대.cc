#include <bits/stdc++.h>

using namespace std;

long long cost(vector<int> &x, int p)
{
    long long c = 0;
    for (int i = 1; i < x.size(); i++)
    {
        c += abs(x[i] - p*i);
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
    
    int lo = 0, hi = 10000;
    int p, q;
    long long cp, cq, c_min, c_now;
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

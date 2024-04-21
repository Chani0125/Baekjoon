#include <bits/stdc++.h>

#define ull unsigned long long

using namespace std;

ull cost(vector<ull> &a, vector<ull> &b, ull mid_h)
{
    int mid = a.size() / 2;
    ull c = 0;
    for (int i = 0; i < mid; i++)
    {
        if (mid_h + mid - i > a[i])
            c += (mid_h + mid - i) - a[i];
        else
            c += a[i] - (mid_h + mid - i);
        if (mid_h + mid - i > b[i])
            c += (mid_h + mid - i) - b[i];
        else
            c += b[i] - (mid_h + mid - i);
    }
    for (int i = mid; i < a.size(); i++)
    {
        if (mid_h + i - mid > a[i])
            c += (mid_h + i - mid) - a[i];
        else
            c += a[i] - (mid_h + i - mid);
        if (mid_h + i - mid > b[i])
            c += (mid_h + i - mid) - b[i];
        else
            c += b[i] - (mid_h + i - mid);
    }
    return c;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;
    vector<ull> a(n), b(n);
    ull max_num = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        max_num = (a[i] > max_num ? a[i] : max_num);
    }
    for (int i = 0; i < n; i++)
    {
        cin >> b[i];
        max_num = (a[i] > max_num ? a[i] : max_num);
    }

    ull lo = 0, hi = max_num;
    ull p, q, cp, cq;
    while (hi - lo >= 3)
    {
        p = (lo * 2 + hi) / 3;
        q = (lo + hi * 2) / 3;

        cp = cost(a, b, p);
        cq = cost(a, b, q);

        if (cp <= cq) hi = q;
        else lo = p; 
    }

    ull c_now, c_min = cost(a, b, lo);
    for (int i = lo+1; i <= hi; i++)
    {
        c_now = cost(a, b, i);
        if (c_now <= c_min)
        {
            c_min = c_now;
            lo = i;
        }
    }
    
    cout << cost(a, b, lo) << "\n";

    return 0;
}

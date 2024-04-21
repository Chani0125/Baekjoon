#include <bits/stdc++.h>

using namespace std;

struct asteroid
{
    int a, w;
};

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, m, pb = 1, pa = 0, p = 0;
    cin >> n >> m;

    vector<int> b(n);
    vector<asteroid> a(m);

    for (int i = 0; i < n; i++)
        cin >> b[i];
    sort(b.begin(), b.end());
    
    for (int i = 0; i < m; i++)
        cin >> a[i].a >> a[i].w;
    sort(a.begin(), a.end(), [](asteroid a, asteroid b) { return a.a < b.a; });
    
    if (n == 1)
    {
        while (pa < m)
        {
            p = max(p, abs(b[0] - a[pa].a) * a[pa].w);
            pa++;
        }
    }
    else
    {
        int p1, p2;
        while (pa < m && pb < n)
        {
            while (b[pb] < a[pa].a && pb < n-1)
                pb++;

            p1 = abs(b[pb-1] - a[pa].a);
            p2 = abs(b[pb]   - a[pa].a);

            p = max(p, min(p1, p2) * a[pa].w);
            pa++;
        }
    }

    
    cout << p << "\n";
    
    return 0;
}

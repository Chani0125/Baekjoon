#include <bits/stdc++.h>

using namespace std;

struct union_find
{
    vector<int> parent;
    union_find(int n) : parent(n+1)
    {
        for (int i = 1; i <= n; i++)
            parent[i] = i;
    }

    int find(int x)
    {
        if (x == parent[x])
            return x;
        return parent[x] = find(parent[x]);
    }

    int merge(int x, int y)
    {
        x = find(x);
        y = find(y);
        if (x != y)
        {
            parent[x] = y;
            return 1;
        }
        return 0;
    }
};

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, m;
    cin >> n >> m;

    int ans = 0;
    vector<array<int, 3>> graph(m+1, {0, 0, 0});
    union_find parent(n);

    for (int i = 0; i < m; i++)
    {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        graph[i] = {c, a, b};
        if (d)
        {
            ans -= c;
            parent.merge(a, b);
        }
    }

    sort(graph.begin(), graph.end(), greater<>());
    for (int i = 0; i < m; i++)
    {
        int c = graph[i][0];
        int a = graph[i][1];
        int b = graph[i][2];

        if (!parent.merge(a, b))
            ans += c;
    }

    cout << ans << "\n";
    
    return 0;
}
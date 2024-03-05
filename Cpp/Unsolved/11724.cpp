#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, m;
    cin >> n >> m;
    vector<vector<bool>> v(n+1, vector<bool>(n+1, false));
    
    int a, b;
    for (int i = 0; i < m; i++)
    {
        cin >> a >> b;
        v[a][b] = v[b][a] = true;
    }

    int cnt = 0;
    
    vector<bool> visited(n+1, false);

    stack<int> s;
    for (int i = 1; i <= n; i++)
        s.push(i);
    
    int now;
    while (!s.empty())
    {
        now = s.top();
        s.pop();
        
        if (visited[now]) continue;
        visited[now] = true;

        for (int i = 1; i <= n; i++)
        {
            if (v[now][i])
            {
                s.push(i);
                
            }
        }
    }
    
    return 0;
}

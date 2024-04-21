#include <bits/stdc++.h>

#define X first
#define Y second

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;

    int k;
    vector<int> s(n, 0);
    vector<vector<int>> t(n, vector<int>(n));
    priority_queue<pair<int, int>, vector<pair<int, int>>, less<pair<int, int>>> pq;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> t[i][j];

    for (int i = 0; i < n; i++)
        pq.emplace(t[n-1][i], i);
    
    pair<int, int> num_max;
    for (int i = 0; i < n-1; i++)
    {
        num_max = pq.top(); pq.pop();
        s[num_max.Y]++;
        pq.emplace(t[n-1-s[num_max.Y]][num_max.Y], num_max.Y);
    }

    cout << pq.top().X;
    
    return 0;
}

#include <bits/stdc++.h>

#define ull long long

using namespace std;

pair<int, int> dot_init[4];

ull dot_cost(ull x, int i[])
{
    ull cost = 0;

    cost += abs(dot_init[i[0]].first + x);
    cost += abs(dot_init[i[0]].second + x);

    cost += abs(dot_init[i[1]].first + x);
    cost += abs(dot_init[i[1]].second - x);

    cost += abs(dot_init[i[2]].first - x);
    cost += abs(dot_init[i[2]].second + x);

    cost += abs(dot_init[i[3]].first - x);
    cost += abs(dot_init[i[3]].second - x);

    return cost;
}

ull cost(ull x)
{

    int permu[4] = {0, 1, 2, 3};
    ull min_cost = LONG_LONG_MAX;
    
    do
    {
        min_cost = min(min_cost, dot_cost(x, permu));
    }
    while (next_permutation(permu, permu+4));

    return min_cost;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int max_num = 0, a, b;
    for (int i = 0; i < 4; i++)
    {
        cin >> a >> b;
        dot_init[i].first = a * 2;
        dot_init[i].second = b * 2;
        max_num = max(max_num, max(abs(dot_init[i].first), abs(dot_init[i].second)));
    }

    ull lo = 1, hi = INT_MAX, p, q, cp, cq;
    while (hi - lo >= 3)
    {
        p = (lo * 2 + hi) / 3;
        q = (lo + hi * 2) / 3;

        cp = cost(p);
        cq = cost(q);

        if (cp < cq) hi = q;
        else lo = p;
    }

    ull c_min = cost(lo), c_now;
    for (int i = lo+1; i <= hi; i++)
    {
        c_now = cost(i);
        if (c_now <= c_min)
        {
            c_min = c_now;
            lo = i;
        }
    }

    cout << lo << "\n";
    
    return 0;
}

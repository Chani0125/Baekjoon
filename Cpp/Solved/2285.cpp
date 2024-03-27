#include <bits/stdc++.h>

using namespace std;

long long dist(vector<pair<int, int>> &x, int y)
{
    long long dist = 0;
    for (int i = 0; i < x.size(); i++)
    {
        if (i == y) continue;
        dist += x[i].second * (i < y ? -1 : 1);
    }
    return abs(dist);
}

int ternary_search(vector<pair<int, int>> &x, int s, int e)
{
    int p, q;
    long long dist_p, dist_q;

    while (e - s >= 3)
    {
        p = (s * 2 + e) / 3;
        q = (s + e * 2) / 3;

        dist_p = dist(x, p);
        dist_q = dist(x, q);

        if (dist_p <= dist_q) e = q;
        else s = p;
    }

    long long dist_new, dist_min = dist(x, s);
    for (int i = s+1; i <= e; i++)
    {
        dist_new = dist(x, i);
        if (dist_new < dist_min)
        {
            dist_min = dist_new;
            s = i;
        }
    }

    return s;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;

    int y = 0, dy, a = 0;
    vector<pair<int, int>> x(n);
    for (int i = 0; i < n; i++)
    {
        cin >> x[i].first >> x[i].second;
        a += x[i].second;
    }
    sort(x.begin(), x.end());

    int ans = ternary_search(x, 0, n-1);
    cout << x[ans].first << "\n";

    return 0;
}





// #include <bits/stdc++.h>

// using namespace std;

// int main(void)
// {
//     ios_base::sync_with_stdio(0);
//     cin.tie(0);
    
//     int n; cin >> n;

//     long long y = 0, dy, a = 0;
//     vector<pair<int, int>> x(n);
//     for (int i = 0; i < n; i++)
//     {
//         cin >> x[i].first >> x[i].second;
//         a += x[i].second;
//     }
//     sort(x.begin(), x.end());

//     for (int i = 1; i < n; i++)
//     {
//         y += (x[i].first-x[0].first) * x[i].second;
//     }

//     int i;
//     for (i = 0; i < n-1; i++)
//     {
//         a -= x[i].second * 2;
//         dy = (x[i].first - x[i+1].first) * a;
        
//         if (dy < 0) y += dy;
//         else break;
//     }

//     y = 0;
//     for (int j = 0; j < n; j++)
//     {  
//         dy = x[i].first * x[i].second;
//         if (j <= i) dy *= -1;
//         y += dy;
//     }

//     dy = 0;
//     if (a == 0);
//     else if (abs((x[i].first+1) * -a + y) < abs(x[i].first * -a + y))
//     {
//         while (abs((x[i].first+dy+1) * -a + y) < abs((x[i].first+dy) * -a+ y)) dy++;
//     }
//     else
//     {
//         a += x[i].second * 2;
//         y += x[i].first * x[i].second * 2;

//         while (
//             x[i].first+dy-1 > x[i-1].first &&
//             abs((x[i].first+dy-1) * -a + y) <= abs((x[i].first+dy) * -a+ y)
//         ) dy--;
//     }

//     cout << x[i].first + dy << "\n";
    
//     return 0;
// }
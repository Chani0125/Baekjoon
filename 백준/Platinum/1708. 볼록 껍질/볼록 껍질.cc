#include <bits/stdc++.h>

#define ll long long

using namespace std;

struct Point
{
    int x, y;
    Point(): Point(0, 0) {}
    Point(int x, int y): x(x), y(y) {}

    Point operator-(const Point &p) const
    {
        return Point(x - p.x, y - p.y);
    }
};

ll ccw(const Point &p1, const Point &p2, const Point &p3)
{
    Point v1 = p2 - p1;
    Point v2 = p3 - p1;
    return (1LL * v1.x * v2.y) - (1LL * v1.y * v2.x);
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;
    vector<Point> p(n);
    for (int i = 0; i < n; i++)
    {
        cin >> p[i].x >> p[i].y;
    }

    sort(p.begin(), p.end(), [](const Point &a, const Point &b) -> bool
    {
        if (a.y == b.y) return a.x < b.x;
        return a.y < b.y;
    });

    for (int i = n-1; i >= 0; i--)
    {
        p[i] = p[i] - p[0];
    }

    sort(p.begin()+1, p.end(), [](const Point &a, const Point &b) -> bool
    {
        ll tmp = ccw(a, Point(0, 0), b);

        if (tmp == 0)
        {
            if (a.y == b.y) return a.x < b.x;
            return a.y < b.y;
        }
        return tmp < 0;
    });

    stack<int> s;
    s.push(0); s.push(1);
    int next = 2;

    while (next < n)
    {
        while (s.size() >= 2)
        {
            int first = s.top(); s.pop();
            int second = s.top();

            if (ccw(p[second], p[first], p[next]) > 0)
            {
                s.push(first);
                break;
            }
        }

        s.push(next++);
    }

    cout << s.size() << "\n";

    return 0;
}

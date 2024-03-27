#include <bits/stdc++.h>

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

int ccw(Point p1, Point p2, Point p3)
{
    Point v1 = p2 - p1;
    Point v2 = p3 - p1;
    long long tmp = 1LL * v1.x * v2.y - 1LL * v1.y * v2.x;

    if (tmp > 0) return 1;
    if (tmp < 0) return -1;
    return 0;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    Point p[3];
    for (int i = 0; i < 3; i++)
    {
        cin >> p[i].x >> p[i].y;
    }

    cout << ccw(p[0], p[1], p[2]);
    
    return 0;
}

#include <bits/stdc++.h>

using namespace std;

struct point
{
    int x;
    int y;
};

class line
{
public:
    point s;
    point e;
    int w;
    int num = 0;
    list<line*> meet;
    void set(int sx, int sy, int ex, int ey, int w)
    {
        this->s.x = sx;
        this->s.y = sy;
        this->e.x = ex;
        this->e.y = ey;
        this->w = w;
    }
friend bool operator<(const line& l1, const line& l2);
};

bool operator<(const line& l1, const line& l2)
{
    return l1 < l2;
}

int ccw(const point& p1, const point& p2, const point& p3)
{
    int s = p1.x*p2.y + p2.x*p3.y + p3.x*p1.y;
    s -= p2.x*p1.y + p3.x*p2.y + p1.x*p3.y;

    if (s == 0) return 0;
    else if (s > 0) return 1;
    else return -1;
}

bool check_inter(const line& l1, const line& l2)
{
    bool ccw_l1 = ccw(l1.s, l1.e, l2.s) * ccw(l1.s, l1.e, l2.e) < 0;
    bool ccw_l2 = ccw(l2.s, l2.e, l1.s) * ccw(l2.s, l2.e, l1.s) < 0;

    return ccw_l1 && ccw_l2;
}

int main(void)
{
    int n, score = 0; cin >> n;
    line* lines = new line[n];

    for (int i = 0; i < n; i++)
    {
        int sx, sy, ex, ey, w;
        cin >> sx >> sy >> ex >> ey >> w;
        lines[i].set(sx, sy, ex, ey, w);
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = i+1; j < n; j++)
        {
            if (check_inter(lines[i], lines[j]))
            {
                lines[i].meet.push_back(&lines[j]); lines[i].num += 1;
                lines[j].meet.push_back(&lines[i]); lines[j].num += 1;
            }
        }
    }

    sort(lines, lines + n);

    delete[] lines;
    return 0;
}
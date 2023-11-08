#include <bits/stdc++.h>

#define VVII vector<vector<int>>

using namespace std;

int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

bool is_in_bound (int &x, int &y, int &x_limit, int &y_limit, int &pos_x)
{
    if (!(x == pos_x && y == 0))
        if (!(x == pos_x + 1 && y == 0))
            if (0 <= x && x < x_limit)
                if (0 <= y && y < y_limit)
                    return true;
    return false;
}

inline void spread(int &r, int &c, VVII &v, int &pos_x)
{
    int num_spread, dx, dy;
    VVII u(r, vector<int>(c, 0));

    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (v[i][j])
            {
                num_spread = 0;
                for (int k = 0; k < 4; k++)
                {
                    dx = i + d[k][0];
                    dy = j + d[k][1];
                    if (is_in_bound(dx, dy, r, c, pos_x))
                    {
                        u[dx][dy] += v[i][j] / 5;
                        num_spread++;
                    }
                }
                u[i][j] -= (v[i][j] / 5) * num_spread;
            }
        }
    }
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            v[i][j] += u[i][j];
        }
    }
}

inline void cleaner(int &r, int &c, VVII &v, int &pos_x)
{
    for (int x = pos_x-2; x >= 0; x--)
    {
        v[x+1][0] = v[x][0];
    }
    for (int y = 1; y < c; y++)
    {
        v[0][y-1] = v[0][y];
    }
    for (int x = 1; x <= pos_x; x++)
    {
        v[x-1][c-1] = v[x][c-1];
    }
    for (int y = c-2; y > 0; y--)
    {
        v[pos_x][y+1] = v[pos_x][y];
    }
    v[pos_x][1] = 0;

    for (int x = pos_x+3; x < r; x++)
    {
        v[x-1][0] = v[x][0];
    }
    for (int y = 1; y < c; y++)
    {
        v[r-1][y-1] = v[r-1][y];
    }
    for (int x = r-2; x >= pos_x+1; x--)
    {
        v[x+1][c-1] = v[x][c-1];
    }
    for (int y = c-2; y > 0; y--)
    {
        v[pos_x+1][y+1] = v[pos_x+1][y];
    }
    v[pos_x+1][1] = 0;
}

inline int sum_v(VVII &v)
{
    int sum = 0;
    for (auto i : v)
        for (auto j : i)
            sum += j;
    return sum + 2;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int r, c, t;
    cin >> r >> c >> t;

    int pos_x = 0;

    VVII v(r, vector<int>(c));

    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            cin >> v[i][j];
            if (v[i][j] == -1 && pos_x == 0)
            {
                pos_x = i;
            }
        }
    }

    while (t--)
    {
        spread(r, c, v, pos_x);
        cleaner(r, c, v, pos_x);
    }

    cout << sum_v(v) << "\n";
    
    return 0;
}

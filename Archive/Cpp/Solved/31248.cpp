#include <bits/stdc++.h>

using namespace std;

int cnt;

void hanoi(int n, char from, char via, char to)
{
    if (n == 1)
    {
        if (n == cnt)
            cout << from << " D\n";
        else
            cout << from << " " << to << "\n";
        return;
    }

    if (n == cnt)
    {
        if (n < 3)
        {
            hanoi(n - 1, from, to, via);
            cout << from << " D\n";
            cnt -= 1;
            hanoi(n - 1, via, from, to);
        }
        else
        {
            hanoi(n - 2, from, to, via);
            cout << from << " " << to <<"\n";
            cout << from << " D\n";
            cout << to << " D\n";
            cnt -= 2;
            hanoi(n - 2, via, from, to);
        }
    }
    else
    {
        hanoi(n - 1, from, to, via);
        cout << from << " " << to << "\n";
        hanoi(n - 1, via, from, to);
    }
}

int pow_2(int n)
{
    int ret = 1;
    for (int i = 0; i < n; i++)
        ret <<= 1;
    return ret;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> cnt;

    int ans = 0;
    for (int i = cnt; i > 0; )
    {
        if (i >= 2)
        {
            i -= 2;
            ans += pow_2(i)-1;
            ans += 3;
        }
        else
        {
            i -= 1;
            ans += 1;
        }
    }
    cout << ans << "\n";

    hanoi(cnt, 'A', 'B', 'C');
    
    return 0;
}

#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, prev, now, a1 = 0, a2 = 0, max2 = 0, ans = 1;
    bool is_now_max = true, is_1_even = false;

    cin >> n;

    cin >> now;
    if (now == 1)
        a1++;
    else
        a2++;

    for (int i = 1; i < n; i++)
    {
        prev = now;
        cin >> now;

        if (now == 1) a1++; // prev == 1 or 2
        else
        {
            if (prev == now) // prev == 2, now == 2
            {
                a2++;
            }
            else // prev == 1, now == 2
            {
                if (a1 % 2 == 0)
                {
                    a2 += a1 / 2 + 1;
                }
                else
                {
                    max2 = max(max2, a2 + a1 / 2);
                    a2 = 1 + a1 / 2;
                }
                a1 = 0;
            }
        }
    }

    max2 = max(max2, a2 + a1 / 2);
    
    for (int i = max2; i > 0; i >>= 1)
        ans <<= 1;

    cout << ans << "\n";
    
    return 0;
}

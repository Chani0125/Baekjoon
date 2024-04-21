#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int n, k;
    cin >> n >> k;

    int* coins = new int[n];
    for (int i = 0; i < n; i++) cin >> coins[i];

    int* a = new int[k+1];
    a[0] = 0;

    for (int i = 1; i <= k; i++)
    {
        a[i] = -1;
        for (int j = 0; j < n; j++)
            if (i >= coins[j] && a[i-coins[j]] >=0 && (a[i] < 0 || a[i-coins[j]] + 1 < a[i]))
                a[i] = a[i-coins[j]] + 1;
    }

    // for (int i = 1; i < k; i++)
    //     cout << a[i] << " ";
    cout << a[k] << endl;

    return 0;
}

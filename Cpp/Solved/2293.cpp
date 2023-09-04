#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int n, k;
    cin >> n >> k;

    int* coins = new int[n];
    for (int i = 0; i < n; i++) cin >> coins[i];

    int* a = new int[k+1] {};
    a[0] = 1;

    for (int i = 0; i < n; i++)
    {
        for (int j = 1; j <= k; j++)
        {
            if (j >= coins[i]) a[j] += a[j-coins[i]];
        }
    }

    // for (int i = 1; i < k; i++) cout << a[i] << " ";
    cout << a[k] << endl;

    return 0;
}
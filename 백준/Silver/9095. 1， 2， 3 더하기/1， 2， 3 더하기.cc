#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int t; cin >> t;

    while (t--)
    {
        int n; cin >> n;
        int* a = new int[n+1];
        
        a[0] = 1;
        a[1] = 1;
        
        for (int i = 2; i <= n; i++)
        {   
            a[i] = 0;
            for (int j = i-1; j >= i-3 && j >= 0; j--)
            {   
                a[i] += a[j];
            }
        }

        cout << a[n] << endl;
    }

    return 0;
}

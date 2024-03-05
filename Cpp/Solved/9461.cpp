#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    vector<long long> p(101);
    p[1] = p[2] = p[3] = 1;
    p[4] = 2;

    long long t, l = 5;
    cin >> t;
    while(t--)
    {
        long long n;
        cin >> n;

        for (; l <= n; l++)
        {
            p[l] = p[l-1] + p[l-5];
        }

        cout << p[n] << "\n";      
    }
    
    return 0;
}

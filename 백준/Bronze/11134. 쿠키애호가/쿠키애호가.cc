#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int t; cin >> t;
    while (t--)
    {
        int n, c;
        cin >> n >> c;
        cout << n / c + (n % c != 0) << endl;
    }
    return 0;
}
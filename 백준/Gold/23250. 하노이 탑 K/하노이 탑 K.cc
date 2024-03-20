#include <bits/stdc++.h>

using namespace std;

void hanoi(int n, long long k, int from, int via, int to)
{
    if (n == 1)
    {
        cout << from << " " << to << "\n";
        return;
    }
    if (k == (long long)1 << (n-1))
    {
        cout << from << " " << to << "\n";
        return;
    }
    if (k < (long long)1 << (n-1))
    {
        hanoi(n-1, k, from, to, via);
    }
    else
    {
        hanoi(n-1, k - ((long long)1 << (n-1)), via, from, to);
    }
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    long long k;
    cin >> n >> k;

    hanoi(n, k, 1, 2, 3);
    
    return 0;
}

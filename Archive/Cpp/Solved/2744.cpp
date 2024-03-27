#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    string str; cin >> str;

    for (auto c : str)
    {
        if (c >= 'a')
            cout << (char)(c - 'a' + 'A');
        else
            cout << (char)(c - 'A' + 'a');
    }
    
    return 0;
}

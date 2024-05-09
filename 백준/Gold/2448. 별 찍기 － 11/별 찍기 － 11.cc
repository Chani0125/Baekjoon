#include <bits/stdc++.h>

#define vv vector<vector<bool>>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;
    int m = n / 3;

    vv prev = {
        {1},
        {1, 0, 1},
        {1, 1, 1, 1, 1}
    };
    vv ans = prev;

    for (; m != 1; m >>= 1)
    {
        vector<bool> tmp;
        for (int i = 0; i < prev.size(); i++)
        {
            tmp = vector<bool>((prev.size()-i)*2 - 1, 0);
            tmp.insert(tmp.begin(), prev[i].begin(), prev[i].end());
            tmp.insert(tmp.end(), prev[i].begin(), prev[i].end());

            ans.push_back(tmp);
        }
        prev = ans;
    }

    for (int i = 0; i < n; i++)
    {
        for (int k = 0; k < ans[n-1].size()/2 - i; k++)
        {
            cout << " ";
        }

        for (int j = 0; j < ans[i].size(); j++)
        {
            if (ans[i][j] == 1) cout << "*";
            else cout << " ";
        }
        
        for (int k = 0; k < ans[n-1].size()/2 - i; k++)
        {
            cout << " ";
        }
        cout << "\n";
    }
    
    return 0;
}

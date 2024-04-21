#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int t; cin >> t;
    while (t--)
    {
        int r, c;
        cin >> r >> c;
        
        vector<char> in_arr(c);
        vector<vector<char>> arr(r, in_arr);

        for (int i = 0; i < r; i++)
        {
            string s;
            cin >> s;
            for (int j = 0; j < c; j++)
                arr[i][j] = s[j];
        }

        int cnt, num_candy = 0;
        for (int i = 0; i < r; i++)
        {
            cnt = 0;
            for (int j = 0; j < c; j++)
            {
                if      (arr[i][j] == '>')             cnt = 1;
                else if (arr[i][j] == 'o' && cnt == 1) cnt++;
                else if (arr[i][j] == '<' && cnt == 2) { cnt = 0; num_candy++; }
                else cnt = 0;
            }
        }

        for (int i = 0; i < c; i++)
        {
            cnt = 0;
            for (int j = 0; j < r; j++)
            {
                if      (arr[j][i] == 'v')             cnt = 1;
                else if (arr[j][i] == 'o' && cnt == 1) cnt++;
                else if (arr[j][i] == '^' && cnt == 2) { cnt = 0; num_candy++; }
                else cnt = 0;
            }
        }

        cout << num_candy << endl;
    }
    return 0;
}
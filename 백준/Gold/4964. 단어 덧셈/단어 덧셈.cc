#include <bits/stdc++.h>

#define ALPHA_NUM 26

using namespace std;

int char_num[ALPHA_NUM];
bool not_zero[ALPHA_NUM];
bool usage[ALPHA_NUM];
int num_use[10];

int pow_10(int n)
{
    int result = 1;
    for (int i = 0; i < n; i++)
    {
        result *= 10;
    }
    return result;
}

int word_sum(int res, int n)
{
    if (n == ALPHA_NUM) return res == 0;
    if (!usage[n]) return word_sum(res, n+1);

    int ans = 0;
    if (!num_use[0] && !not_zero[n])
    {
        num_use[0] = true;
        ans += word_sum(res, n+1);
        num_use[0] = false;
    }
    for (int i = 1; i < 10; i++)
    {
        if (!num_use[i])
        {
            num_use[i] = true;
            ans += word_sum(res + char_num[n]*i, n+1);
            num_use[i] = false;
        }
    }
    
    return ans;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;
    
    while (n)
    {
        fill(char_num, char_num + (ALPHA_NUM), 0);
        fill(not_zero, not_zero + (ALPHA_NUM), false);
        fill(usage, usage + (ALPHA_NUM), false);
        fill(num_use, num_use + 10, false);

        string word;
        for (int i = 0; i < n; i++)
        {
            cin >> word;

            if (word.size() > 1)
                not_zero[word[0]-'A'] = true;
            
            for (int j = 0; j < word.size(); j++)
            {   
                usage[word[j]-'A'] = true;
                if (i == n-1)
                    char_num[word[j]-'A'] -= pow_10(word.size()-j-1);
                else
                    char_num[word[j]-'A'] += pow_10(word.size()-j-1);
            }
        }

        int ans = word_sum(0, 0);
        cout << ans << "\n";

        cin >> n;
    }

    return 0;
}

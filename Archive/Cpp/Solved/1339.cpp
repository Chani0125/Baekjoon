#include <bits/stdc++.h>

using namespace std;

unsigned long long pow_int(const int &x, const int &y)
{   
    unsigned long long ans = 1;
    for (int i = 0; i < y; i++)
        ans *= x;
    return ans;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;
    string s;
    vector<unsigned long long> a('Z'-'A'+1, 0);

    for (int i = 0; i < n; i++)
    {
        cin >> s;
        for (int j = 0; j < s.size(); j++)
            a[s[j]-'A'] += pow_int(10, s.size()-j-1);
    }

    sort(a.begin(), a.end(), greater<unsigned long long>());

    unsigned long long ans = 0;
    for (int i = 0; i < 10; i++)
        ans += a[i] * (9-i);

    cout << ans;

    return 0;
}

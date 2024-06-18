#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    string a, b;
    cin >> a >> b;

    int len_a = a.length();
    int len_b = b.length();

    for (int i = len_a; i < len_b; i++)
        a = "0" + a;

    for (int i = len_b; i < len_a; i++)
        b = "0" + b;

    int n = a.length();
    string ans = "";

    int c = 0, v = 0, msb = n;
    for (int i = n-1; i >= 0; i--)
    {
        int p = int(a[i]-'0'), q = int(b[i]-'0');

        v = c ^ p ^ q;
        c = (~c & (p & q)) | (c & (p | q));

        if (v) msb = i+1;
        ans = char(v+'0') + ans;
    }
    ans = char(c+'0') + ans;
    if (c) msb = 0;

    cout << ans.substr(msb, n+1) << "\n";
    
    return 0;
}


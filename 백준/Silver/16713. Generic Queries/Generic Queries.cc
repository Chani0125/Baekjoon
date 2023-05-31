#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int n, q;
    cin >> n >> q;

    vector<int> num(n);
    for (int i = 0; i < n; i++) scanf("%d", num.begin()+i);
    
    vector<int> cnt(n+1, 0);

    int s, e;
    for (int i = 0; i < q; i++)
    {
        scanf("%d %d", &s, &e);
        cnt[s-1]++; cnt[e]--;
    }

    int ans = 0, now_cnt = 0;
    for (int i = 0; i < n; i++)
    {
        now_cnt += cnt[i];
        if (now_cnt % 2 != 0)
            ans ^= num[i];
    }

    printf("%d\n", ans);

    return 0;
}   

#include <bits/stdc++.h>

using namespace std;

struct apart
{
    int pos;
    int peo;

    apart(const int pos, const int peo) : pos(pos), peo(peo) {}
};


int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, k, s;
    cin >> n >> k >> s;

    vector<apart> apts(n);

    int po, pe;
    for (int i = 0; i < 3; i++)
    {
        cin >> po >> pe;
        apts.push_back(apart(po, pe));
    }


    

    return 0;
}

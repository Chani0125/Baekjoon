#include <bits/stdc++.h>

using namespace std;

struct addict
{
    int s, e;
};

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;
    int s, e, adt = 0;
    vector<addict> v(n);
    vector<int> ans(n);

    for (int i = 0; i < n; i++)
    {
        cin >> s >> e;
        v[i] = {s, e};
    }
    
    // 처음 시작점만 중요 나머지는 7+0+0 vs 5+1+1의 차이임
    // 거꾸로 실행 / s, e와 교집합이 있느냐 판별
    for (int i = 1; i < n; i++)
    {   
        // Include
        if (v[i].s <= v[i-1].s && v[i].e >= v[i-1].e)
        {
            s = v[i].s;
            e = v[i].e;
            // adt += 0;
            continue;
        }

        // Intersection

        // No Intersection
        if (v[i].s > v[i-1].e)
        {
            s = v[i].s;
            adt += v[i].s - v[i-1].e;
            continue;
        }
        if (v[i].e > v[i-1].e)
        {

            adt += v[i].e - v[i-1].e;
        }
        
    }


    return 0;
}

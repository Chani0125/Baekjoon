#include <bits/stdc++.h>

#define DIVIDER 1000000007

using namespace std;

unsigned long long fibo[64][2][2];

void makeFibo()
{
    fibo[0][0][0] = 1; fibo[0][0][1] = 1;
    fibo[0][1][0] = 1; fibo[0][1][1] = 0;

    for (int i = 0; i < 63; i++)
    {
        fibo[i+1][0][0] = (fibo[i][0][0] * fibo[i][0][0] + fibo[i][0][1] * fibo[i][1][0]) % DIVIDER;
        fibo[i+1][0][1] = (fibo[i][0][0] * fibo[i][0][1] + fibo[i][0][1] * fibo[i][1][1]) % DIVIDER;
        fibo[i+1][1][0] = (fibo[i][1][0] * fibo[i][0][0] + fibo[i][1][1] * fibo[i][1][0]) % DIVIDER;
        fibo[i+1][1][1] = (fibo[i][1][0] * fibo[i][0][1] + fibo[i][1][1] * fibo[i][1][1]) % DIVIDER;
    }
}


int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    makeFibo();

    unsigned long long n;
    cin >> n;

    unsigned long long fibo_ans[2][2] = {{1, 1}, 
                                         {1, 0}};
    unsigned long long fibo_tmp[2][2];
    fibo_ans[0][0] = 1; fibo_ans[0][1] = 1;
    fibo_ans[1][0] = 1; fibo_ans[1][1] = 0;

    for (int i = 0; n > 0; n >>= 1, i++)
    {
        int tmp = n & 1;

        if (n & 1)
        {
            fibo_tmp[0][0] = fibo_ans[0][0]; fibo_tmp[0][1] = fibo_ans[0][1];
            fibo_tmp[1][0] = fibo_ans[1][0]; fibo_tmp[1][1] = fibo_ans[1][1];

            fibo_ans[0][0] = (fibo_tmp[0][0] * fibo[i][0][0] + fibo_tmp[0][1] * fibo[i][1][0]) % DIVIDER;
            fibo_ans[0][1] = (fibo_tmp[0][0] * fibo[i][0][1] + fibo_tmp[0][1] * fibo[i][1][1]) % DIVIDER;
            fibo_ans[1][0] = (fibo_tmp[1][0] * fibo[i][0][0] + fibo_tmp[1][1] * fibo[i][1][0]) % DIVIDER;
            fibo_ans[1][1] = (fibo_tmp[1][0] * fibo[i][0][1] + fibo_tmp[1][1] * fibo[i][1][1]) % DIVIDER;
        }
    }

    cout << fibo_ans[1][1] << "\n";
    
    return 0;
}

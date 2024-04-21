// #include <bits/stdc++.h>

// #define X first
// #define Y second

// using namespace std;

// int main(void)
// {
//     ios_base::sync_with_stdio(0);
//     cin.tie(0);

//     int x, lim[5], coin[4] = {0, 0, 0, 0};
//     int val[4] = {1, 5, 10, 50};

//     cin >> x >> lim[0] >> lim[1] >> lim[2] >> lim[4];
//     lim[3] = lim[4] / 2;

//     for (int i = 0; i < 4; i++)
//     {
//         coin[i] = lim[i];
//         x -= coin[i] * val[i];
//     }

//     x *= -1;

//     if (x >= 0)
//     {
//         for (int i = 3; i >= 0; i--)
//         {
//             int cnt = min(coin[i], x / val[i]);
//             coin[i] -= cnt;
//             x -= cnt * val[i];
//         }
//     }

//     coin[3] *= 2;

//     if (x >= -25 && coin[3] > 0)
//     {
//         int tmp_coin[4], tmp_x = x, total[2] = {0, 0};

//         for (int c : coin) total[0] += c;
//         copy(coin, coin+4, tmp_coin);

//         coin[3]--; x -= 25;

//         for (int i = 0; i < 3; i++)
//         {
//             x += (lim[i] - coin[i]) * val[i];
//             coin[i] = lim[i];
//         }
        
//         if (x >= 0)
//         {            
//             for (int i = 2; i >= 0; i--)
//             {
//                 int cnt = min(coin[i], x / val[i]);
//                 coin[i] -= cnt;
//                 x -= cnt * val[i];
//             }
//         }

//         for (int c : coin) total[1] += c;

//         if (total[0] > total[1] || x != 0)
//         {
//             copy(tmp_coin, tmp_coin+4, coin);
//             x = tmp_x;
//         }
//     }

//     if (lim[4] % 2 && x >= -25)
//     {
//         int tmp_coin[4], tmp_x = x, total[2] = {0, 0};

//         for (int c : coin) total[0] += c;
//         copy(coin, coin+4, tmp_coin);

//         coin[3]++; x += 25;

//         for (int i = 0; i < 3; i++)
//         {
//             x += (lim[i] - coin[i]) * val[i];
//             coin[i] = lim[i];
//         }

//         for (int i = 2; i >= 0; i--)
//         {
//             int cnt = min(coin[i], x / val[i]);
//             coin[i] -= cnt;
//             x -= cnt * val[i];
//         }

//         for (int c : coin) total[1] += c;
        
//         if (total[0] > total[1] || x != 0)
//         {
//             copy(tmp_coin, tmp_coin+4, coin);
//             x = tmp_x;
//         }
//     }
    
//     for (int i = 0; i < 4; i++)
//     {
//         if (x == 0)
//             cout << coin[i] << " ";
//         else
//             cout << "0 ";
//     }

//     return 0;
// }

#include <bits/stdc++.h>

#define X first
#define Y second

using namespace std;

pair<int, vector<int>> sv(int x, vector<int> &coin, vector<int> price)
{
    vector<int> use(coin.size());
    bool ch = false;

    for (int i = 0; i < coin.size(); i++)
    {
        use[i] = coin[i];
        x -= coin[i] * price[i];

        if (x <= 0)
        {
            x = -x;

            for (int j = i; j >= 0; j--)
            {
                int y = min(use[j], x / price[j]);
                x -= y * price[j];
                use[j] -= y;
            }

            ch = x == 0;
            break;
        }
    }

    if (!ch)
        for (auto &i : use)
            i = 0;
    
    int sum = 0;

    for (auto i : use)
        sum += i;
    
    return {sum, use};
}

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(0);
    vector<int> coin(4);
    int x;
    cin >> x;

    for (int i = 0; i < 4; i++)
        cin >> coin[i];
    
    int c = coin[3] % 2;
    coin[3] /= 2;

    auto A = sv(x, coin, {1, 5, 10, 50});

    A.X += A.Y[3];
    A.Y[3] *= 2;

    vector<int> ans = A.Y;

    if (coin[3] || c)
    {
        if (!c)
            coin[3] -= 1;
        auto B = sv(x - 25, coin, {1, 5, 10, 50});
        if (B.X != 0)
        {
            B.X += B.Y[3] + 1;
            B.Y[3] = B.Y[3] * 2 + 1;
            if (A.X < B.X)
                ans = B.Y;
        }
    }
    
    for (auto i : ans)
        cout << i << " ";
}
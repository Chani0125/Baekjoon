#include <bits/stdc++.h>

using namespace std;

void hanoi(int n, int from, int via, int to)
{
    if (n == 1)
    {
        cout << from << " " << to << "\n";
        return;
    }

    hanoi(n-1, from, to, via);
    cout << from << " " << to << "\n";
    hanoi(n-1, via, from, to);
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;
    vector<int> digit(1, 1);
    int carry = 0;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < digit.size(); j++)
        {
            digit[j] = digit[j] * 2 + carry;
            carry = digit[j] / 10;
            digit[j] %= 10;
        }
        while (carry > 0)
        {
            digit.push_back(carry % 10);
            carry /= 10;
        }
    }

    digit[0] -= 1;
    for (int i = 0; digit[i] < 0; i++)
    {
        digit[i] += 10;
        digit[i+1] -= 1;
    }

    for (auto it = digit.rbegin(); it != digit.rend(); it++)
    {
        if (it == digit.rbegin() && *it == 0)
            continue;
        cout << *it;
    }
    cout << "\n";

    if (n <= 20)
        hanoi(n, 1, 2, 3);
    
    return 0;
}

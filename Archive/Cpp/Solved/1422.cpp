#include <bits/stdc++.h>

using namespace std;

bool compare(int p, int q)
{
    if (p == q) return false;

    string a = to_string(p) + to_string(q);
    string b = to_string(q) + to_string(p);

    return a > b;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int k, n;
    cin >> k >> n;

    vector<int> nums(k);
    for (int i = 0; i < k; i++)
        cin >> nums[i];
    
    int max_num = *max_element(nums.begin(), nums.end());

    sort(nums.begin(), nums.end(), compare);

    bool is_print_max_num = false;
    for (auto i : nums)
    {
        if (!is_print_max_num && i == max_num)
        {
            is_print_max_num = true;
            for (int i = 0; i < n - k; i++)
            cout << max_num;
        }
        cout << i;
    }
    
    return 0;
}

#include <bits/stdc++.h>

using namespace std;

string grade_names[9] = {"A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"};
int grade_scores[9] = {450, 400, 350, 300, 250, 200, 150, 100, 0};


int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, x_100, g = 0, g_score = 0;
    double x;

    cin >> n >> x;
    x_100 = round(x * 100);

    int now_g;
    string now_g_name;
    for (int i = 0; i < n-1; i++)
    {
        cin >> now_g >> now_g_name;
        g += now_g;
        for (int j = 0; j < 9; j++)
        {
            if (now_g_name == grade_names[j])
            {
                g_score += now_g * grade_scores[j];
                break;
            }
        }
    }

    cin >> now_g;
    g += now_g;

    for (int i = 8; i >= 0; i--)
    {
        if ((g_score + now_g * grade_scores[i]) / g > x_100)
        {
            cout << grade_names[i] << "\n";
            return 0;
        }
    }

    cout << "impossible" << "\n";

    return 0;
}

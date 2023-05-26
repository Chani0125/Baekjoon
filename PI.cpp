#include <bits/stdc++.h>

using namespace std;

vector<string> sub(vector<string> m, const int& bits)
{
    vector<string> answer;
    
    for (int i = 0; i < m.size(); i++)
    {
        for (int j = i+1; j < m.size(); j++)
        {   
            int tmp = 0;
            bool flag = true;
            vector<int> bar_idx;

            for (int k = 0; k < bits; k++)
            {
                if ((m[i][k] == '-' && m[j][k] != '-') || (m[i][k] != '-' && m[j][k] == '-'))
                {
                    flag = false;
                    break;
                }
                if (m[i][k] == '-' && m[j][k] == '-') bar_idx.push_back(k);
                tmp += abs(m[i][k] - m[j][k]);
            }

            if (!flag) continue;
            
            if (tmp == 1)
            {
                char c[bits] = {};
                for (int k = 0; k < bits; k++)
                    c[k] = m[i][k];
                
                for (int k : bar_idx)
                {
                    c[k] = '-';
                }
                
                answer.push_back((string)c);
            }
        }
    }

    return answer;
}

vector<string> solution(vector<int> minterm)
{
    vector<string> answer;

    // 오름차순 정렬 및 중복 제거
    sort(minterm.begin(), minterm.end());
    minterm.erase(unique(minterm.begin(), minterm.end()), minterm.end());

    // 필요한 비트 수 확인
    int minterm_max = minterm.back();
    int num_bit = 0;
    for (int i = minterm_max; i != 0; i /= 2) num_bit++;

    bool num[(int)pow(2, num_bit)] = {};
    for (int i = 0; i < minterm.size(); i++) num[minterm[i]] = true;

    int interval = 1;
    for (int b = 0; b < num_bit; b++)
    {  
        for (int i = 0; i < minterm_max; i += interval * 2)
        {
            for (int j = 0; j < interval; j++)
            {   
                if (num[i+j+interval] && num[i+j])
                {   
                    char c[num_bit];
                    int tmp = i+j;
                    for (int k = 0; k < num_bit; k++)
                    {
                        c[num_bit-k-1] = '0' + tmp % 2;
                        tmp /= 2;
                    }
                    c[num_bit-b-1] = '-';
                    answer.push_back((string)c);
                }
            }
        }
        interval *= 2;
    }
    
    for (int i = 1; i < num_bit; i++)
    {
        vector<string> tmp;
        tmp = sub(answer, num_bit);
        if (tmp.size() == 0) break;
        answer = tmp;
    }

    return answer;
}

int main(void)
{
    vector<int> vect{3, 4, 0, 1, 2, 3};
    for (string s : solution(vect))
    {
        cout << s << " ";
    }
    cout << endl;
    return 0;
}
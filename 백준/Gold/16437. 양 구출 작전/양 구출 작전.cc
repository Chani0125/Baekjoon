#include <bits/stdc++.h>

using namespace std;

class island
{
public:
    int type;
    unsigned long num;
    island* next;
    int prev = 0;
    void set(char type, int num, island* next)
    {
        this->type = type;
        this->num = num;
        this->next = next;
    }
};

int main(void)
{
    int n; cin >> n;
    island* islands = new island[n];
    islands[0].set('F', 0, nullptr);

    deque<island*> dq;
    
    for (int i = 1; i < n; i++)
    {
        char type;
        unsigned long num;
        int next;
        cin >> type >> num >> next;
        islands[i].set(type, num, islands + next - 1);
        islands[next-1].prev += 1;
    }

    for (int i = 1; i < n; i++)
    {
        if (islands[i].prev == 0)
        {
            dq.push_back(&islands[i]);
        }
    }    

    while (!dq.empty())
    {
        char type = dq.front()->type;
        unsigned long num = dq.front()->num;
        island* next = dq.front()->next;

        dq.pop_front();
        next->prev -= 1;

        if (type == 'S')
        {
            if (next->type == 'W')
            {
                if (num > next->num)
                {
                    next->num = num - next->num;
                    next->type = 'S';
                }
                else next->num -= num;
            }
            else
            {
                next->num += num;
            }
        }

        if (next->type == 'F')
        {
            continue;
        }
        
        if (next->prev == 0)
        {
            dq.push_front(next);
        }
    }

    cout << islands[0].num << '\n';

    delete[] islands;
}
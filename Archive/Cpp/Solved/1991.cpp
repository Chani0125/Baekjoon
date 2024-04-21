#include <bits/stdc++.h>

using namespace std;

struct node
{
    char c1, c2;
    node() : node(0, 0) {}
    node(char c1, char c2) : c1(c1), c2(c2) {}
};

vector<node*> nodes;

void preorder(char root)
{
    node *now = nodes[root - 'A'];
    
    cout << root;
    if (now->c1) preorder(now->c1);
    if (now->c2) preorder(now->c2);
}

void inorder(char root)
{
    node *now = nodes[root - 'A'];
    
    if (now->c1) inorder(now->c1);
    cout << root;
    if (now->c2) inorder(now->c2);
}

void postorder(char root)
{
    node *now = nodes[root - 'A'];
    
    if (now->c1) postorder(now->c1);
    if (now->c2) postorder(now->c2);
    cout << root;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;

    char p, c1, c2;
    nodes = vector<node*>(n);
    for (int i = 0; i < n; i++)
    {
        cin >> p >> c1 >> c2;
        nodes[p-'A'] = new node();

        if (c1 != '.') nodes[p-'A']->c1 = c1;
        if (c2 != '.') nodes[p-'A']->c2 = c2;
    }

    char root = 'A';

    preorder(root); cout << "\n";
    inorder(root); cout << "\n";
    postorder(root); cout << "\n";
    
    
    return 0;
}

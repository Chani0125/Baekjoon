#include <iostream>

using namespace std;

class Point {
public:
    int x, y;
    void setPoint(int x, int y) {
        this->x = x;
        this->y = y;
    }
};

int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int main(void) {
    for (int t = 0; t < 3; t++) {
        int a[6][6], cnt = 0;
        Point p[6];
        for (int i = 0; i < 6; i++) for (int j = 0; j < 6; j++) {
            cin >> a[i][j];
            if (a[i][j] == 1) {
                p[cnt++].setPoint(i, j);
            }
        }
    }

    return 0;
}
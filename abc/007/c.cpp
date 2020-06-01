#include <iostream>
#include <queue>

using namespace std;

struct Point {
    int x;
    int y;
public:
    Point(const int x, const int y) : x(x), y(y) {}
};

int main() {

    int R, C, sy, sx, gy, gx;

    cin >> R >> C >> sy >> sx >> gy >> gx;

    sx -= 1;
    sy -= 1;
    gx -= 1;
    gy -= 1;

    int map[R][C];

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            char c;
            cin >> c;
            map[i][j] = (c == '#') ? -2 : -1;
        }
    }

    map[sy][sx] = 0;

    queue<Point> q;
    q.push(Point(sx, sy));

    while (!q.empty()) {
        Point p = q.front();
        // この地点までの手数
        int step = map[p.y][p.x];

        q.pop();
        Point diff[4] = {
            Point(0, -1), Point(0, 1), Point(-1, 0), Point(1, 0)
        };
        for(int i = 0; i < 4; i++) {
            Point next = Point(p.x + diff[i].x, p.y + diff[i].y);
            if (map[next.y][next.x] != -1) {
                // 訪問済みの場合何もしない
                continue;
            }
            // 初めて来た地点なら手数を記録
            map[next.y][next.x] = step + 1;
            // 探索キューに突っ込む
            q.push(next);
        }
    }

    // 探索が完了したのでゴールまでの手数を出力
    int result = map[gy][gx];
    cout << result << endl;

    return 0;
}
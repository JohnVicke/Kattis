#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t, i, j, n, out, avg;
    cin >> t;
    for (i = 0; i < t; i++)
    {
        avg = 0;
        out = 0;
        cin >> n;
        vector<int> pos(n);
        for (auto &i : pos)
        {
            cin >> i;
            avg += i;
        }
        avg = ceil(avg / n);
        int min = *min_element(pos.begin(), pos.end());
        int max = *max_element(pos.begin(), pos.end());
        cout << (abs(avg - min) + abs(avg - max)) * 2 << endl;
    }

    return 0;
}
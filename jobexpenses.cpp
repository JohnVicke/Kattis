
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main()
{
    int n, i, in, out = 0;
    cin >> n;
    for (i = 0; i < n; i++)
    {
        cin >> in;
        if (in < 0)
        {
            out += abs(in);
        }
    }

    cout << out << endl;

    return 0;
}
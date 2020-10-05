#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ll t, n;
    int i;
    cin >> t;

    for (i = 0; i < t; i++) {
        cin >> n;
        cout << ceil(n / 400) << endl;
    }

    return 0;
}
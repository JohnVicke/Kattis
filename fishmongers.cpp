#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ll n, m, i = 0, j = 0;
    ll monies = 0;

    cin >> n >> m;

    vector<ll> fish_w(n);
    vector<pair<ll, ll>> mongos(m);

    for (auto& i : fish_w) cin >> i;
    for (auto& i : mongos) cin >> i.second >> i.first;

    sort(fish_w.rbegin(), fish_w.rend());
    sort(mongos.rbegin(), mongos.rend());

    while (i < n) {
        monies += fish_w[i] * mongos[j].first;
        mongos[j].second--;
        if (mongos[j].second == 0) j++;
        i++;
    }
    cout << monies << endl;
    return 0;
}
#include <stdio.h>

int main() {
    int n, m, i, x, p;

    scanf("%d%d", &n, &m);
    int w[n];
    for (i = 0; i < n; ++i) {
        scanf("%d", &w[i]);
    }

    for (i = 0; i < m; ++i) {
        scanf("%d%d", &x, &p);
    }

    return 0;
}
#include <stdio.h>

int main() {
    double c, l, wi, li, total;
    scanf("%lf%lf", &c, &l);

    for (double i = 0; i < l; ++i) {
        scanf("%lf%lf", &wi, &li);
        total += wi * li * c;
    }
    fprintf(stdout, "%.8lf\n", total);
    return 0;
}
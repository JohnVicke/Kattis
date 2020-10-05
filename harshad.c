#include <stdio.h>

int check_harshad(int n) {
    int sum = 0;
    for (int i = n; i > 0; i /= 10) sum += i % 10;
    return (n % sum == 0);
}

int main() {
    int n;
    scanf("%d", &n);
    for (int i = n; i < 1000000001; ++i) {
        if (check_harshad(i)) {
            fprintf(stdout, "%d\n", i);
            break;
        }
    }
    return 0;
}
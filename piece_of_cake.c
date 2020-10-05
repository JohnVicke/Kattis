#include <stdio.h>

int main()
{
    int n, h, v;
    scanf("%d%d%d", &n, &h, &v);
    if (n - h > h)
    {
        h = n - h;
    }

    if (n - v > v)
    {
        v = n - v;
    }

    fprintf(stdout, "%d\n", h * v * 4);
    return 0;
}
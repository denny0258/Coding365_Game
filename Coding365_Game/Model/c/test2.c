

int a[10][10];

int main()
{
    a[2][2] = 12;
}

int get(int x, int y)
{
    return a[x][y];
}

void set(int ab[20][20])
{
    int i, j;
    for (i = 0; i < 20; i++)
        for (j = 0; j < 20; j++)
            a[i][j] = ab[i][j];
}
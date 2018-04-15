#include <stdio.h>
extern int func_a(void);
extern int func_b(void);

int main(void)
{
    printf("hello world!");
    func_a();
    func_b();
    return 0;
}

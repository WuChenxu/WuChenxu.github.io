#include "functions.h"
#include "func_internal.h"
static int func_internal_s(int a)
{
    printf("func B %d\n", a);
    return a;
}

int func_b(void)
{
    int a = func_internal(100);
    printf("this is func b. %d", a);
    printf("internal func %d\n.", func_internal_s(-100));
    return 0;    

}

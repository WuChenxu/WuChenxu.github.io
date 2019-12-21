#include "functions.h"
#include "func_internal.h"
static int func_internal_s(void)
{
return 1;
}

int func_a(void)
{
   int a = func_internal();
   printf("this is func a. %d\n", a);
    printf("this is static internal %d\n", func_internal_s());
    return 0;    

}

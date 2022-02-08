#include <stdio.h>
#include <unistd.h>

//
//void bar(void);
//
//void bar(void){
//	sleep(1);
//	bar2();
//}


void foo(void);

void foo(void) {

	bar();
	sleep(1);
}

#include <stdio.h>
int main(){
	double radius;
	scanf("%f",&radius);
	double euclid,taxi;
	euclid = radius*radius*3.14159265355820974944;
	taxi = 2*radius*radius;
	printf("%.6f\n%.6f",euclid,taxi);
	return 0;
}
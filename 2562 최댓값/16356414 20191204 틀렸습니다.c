#include <stdio.h>

int main() {
	int num[9];
	int max;
	scanf("%d",&num[0]);
	max = num[0];
	int sq;
	for(int i=1;i<9;i++){
		scanf("%d",&num[i]);
		if(num[i]>max){
			max = num[i];
			sq = i+1;
		}
	}
	printf("%d\n%d",max,sq);
	return 0;
}

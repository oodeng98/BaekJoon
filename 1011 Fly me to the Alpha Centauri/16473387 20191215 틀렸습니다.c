#include <stdio.h>
int main(){
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int now,des;
		scanf("%d",&now);
		scanf("%d",&des);
		int length = des-now;
		if(length == 1){
			printf("1\n");
			continue;
		}
		else if(length == 2){
			printf("2\n");
			continue;
		}
		int pn = 1;
		for(int j=2;j<100000;j++){
			pn+=j;
			if(length<=pn*2){
				if(pn*2-length<j){
					printf("%d\n",2*j);
				}
				else{
					printf("%d\n",2*j-1);
				}
				break;
			}
		}
	}
	return 0;
}
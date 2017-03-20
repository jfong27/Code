#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void process(int n, int i);
int check(int bits[]);

int main(){

   int n;
   int case_no = 1;

   scanf("%d", &n);
   while((scanf("%d",&n)) > 0){
      process(n, case_no++);
   }

   return 0;
}


void process(int n, int case_no){
   int bits[10] = {0};
   int i = 1; 
   int new;
   int a;
   int temp;
   
   if(n == 0){
      printf("Case #%d: INSOMNIA\n", case_no);
      return;
   }

   while(check(bits) < 0){
      new = n * i++;
      temp = new;
      while(new){
         a = new % 10;
         new /= 10;
         bits[a] = 1;
      }
   }
   printf("Case #%d: %d\n", case_no, temp);

}

int check(int bits[]){

   int i;
   for(i = 0; i < 10; i++){
      if(bits[i] == 0)
         return -1;
   }

   return 0;
}



   


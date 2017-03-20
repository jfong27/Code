#include <stdio.h>
#include <string.h>

int flip(char *stack);

int main(){
   int cases;
   int i; 
   int num_flips;
   char stack[100];

   scanf("%d", &cases);

   for(i = 1; i < cases + 1; i++){
      scanf("%s", stack);
      num_flips = flip(stack);
      printf("Case #%d: %d\n", i, num_flips );
   }

   return 0;

}

int flip(char *stack){
   int pos = 0;
   int flips = 0;
   char tail;
   char lead;
   int i;
   
   if(strlen(stack) == 1){
      if(*stack == '+')
         return 0;
      return 1;
   }

   while(pos < strlen(stack)-1){
      tail = stack[pos];
      lead = (char)stack[pos+1];
      if(tail != lead){
         flips++;
         for(i = 0; i < pos+1; i++){
            if(stack[i] == '+')
               stack[i] = '-';
            else{
               stack[i] = '+';
            }
         }
         pos = 0;
      }
      pos++;
   }
   if(stack[pos] == '-')
      flips++;
   return flips;
}

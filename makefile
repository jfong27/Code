

all : sheep

sheep : sheep.o 
   gcc -o sheep sheep.o

sheep.o : sheep.c
   gcc sheep.c -c 

#include <stdio.h>

int makeGuess(min_value, max_value){
   int stillGuessing = 1;
   int guess;
   while (stillGuessing) {
     printf("Pick a number between %d and %d\n", min_value, max_value);
     scanf("%d", &guess);
     if (guess >= min_value && guess <= max_value){
       stillGuessing = 0;
     }
   }
   return guess;
}

int main(void) {
  int answer = 5;
  int guess = -1;
  int min_value = 1;
  int max_value = 10;
  
  while (answer != guess){
    guess = makeGuess(min_value, max_value);
    
    if (guess < answer){
      printf("Your guess was too low!\n");
    } else if (guess > answer) {
      printf("Your guess was too high!\n");
    }
    
  }
  printf("You won!\n");
  return 0;
}
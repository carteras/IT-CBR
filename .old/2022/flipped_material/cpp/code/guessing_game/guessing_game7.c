#include <stdio.h>
#include <stdlib.h>

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

int fitnessTest(guess, answer){
  if (guess < answer) return -1;
  if (guess > answer) return 1;
  return 0;
}

void hint(int fitness) {
    if (fitness > 0) {
      printf("Your guess was too low!\n");
    } else if (fitness < 0) {
      printf("Your guess was too high!\n");
    } else {
      printf("You are the winner!\n");
    }
}

int autoGuess(int min_value, int max_value){
  int stillGuessing = 1;
  int guess;
  while (stillGuessing) {
    guess = rand() % max_value;
    if (guess >= min_value && guess <= max_value) {
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
  int fitness = 0;
  
  while (answer != guess){
    // guess = makeGuess(min_value, max_value);
    guess = autoGuess(min_value, max_value);
    fitness = fitnessTest(guess, answer);
    hint(fitness);
  }
  return 0;
}
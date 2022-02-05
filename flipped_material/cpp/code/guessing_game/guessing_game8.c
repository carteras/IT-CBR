#include <stdio.h>
#include <stdlib.h>
#include <time.h>

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

void hint(int fitness, int guess, int answer) {
    if (fitness < 0) {
      printf("Your guess %d was too low %d!\n", guess, answer);
    } else if (fitness > 0) {
      printf("Your guess %d was too high %d!\n", guess, answer);
    } else {
      printf("You are the winner!\n");
    }
}

int autoGuess(int min_value, int max_value){
  int stillGuessing = 1;
  int guess;
  while (stillGuessing) {
    
    guess = rand() % (max_value-min_value+1)+min_value;
    if (guess >= min_value && guess <= max_value) {
      stillGuessing = 0;
    }
  }
  return guess;
}


int main(void) {
  int min_value = 1;
  int max_value = 1000;
  int sum_of_moves = 0;
  int games_played = 0;
  int quickestGame = 9999;
  int longestGame = -1;
  srand(time(NULL));  
  for (int i = 0; i < 1000; i++){
    
    int answer = rand() % (max_value-min_value+1)+min_value;
    int guess = -1;
    int fitness = 0;
    int moves = 0;
    while (answer != guess){
      // guess = makeGuess(min_value, max_value);
      guess = autoGuess(min_value, max_value);
      moves++;
      fitness = fitnessTest(guess, answer);
      // hint(fitness, guess, answer);
    }
    sum_of_moves += moves;
    games_played++;
    if (moves > longestGame) longestGame = moves;
    if (moves < quickestGame) quickestGame = moves;
  }
  printf("You played a total of %d games\n", games_played);
  printf("On average, you took %d moves\n", sum_of_moves/games_played);
  printf("The quickest game was %d\n", quickestGame);
  printf("The longest game was %d\n", longestGame);
  return 0;
}
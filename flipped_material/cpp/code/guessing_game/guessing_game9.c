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

void hint(int fitness, int guess, int answer, int low, int high) {
    if (fitness < 0) {
      printf("Your guess %d was too low %d!", guess, answer);
    } else if (fitness > 0) {
      printf("Your guess %d was too high %d!", guess, answer);
    } else {
      printf("You are the winner!");
    }
    printf(" %d %d\n", low, high);
}

int autoGuess(int min_value, int max_value){
  return (min_value+max_value+1)/2;
}


int main(void) {
  int min_value = 1;
  int max_value = 1000;
  int numberOfGames = 1000;
  int sum_of_moves = 0;
  int games_played = 0;
  int quickestGame = 9999;
  int longestGame = -1;
  srand(time(NULL));  
  for (int i = 0; i < numberOfGames; i++){
    
    int answer = rand() % (max_value-min_value+1)+min_value;
    int guess = -1;
    int fitness = 0;
    int moves = 0;
    int lowGuess = -1;
    int highGuess = max_value+1;

    while (answer != guess){
      if (fitness > 0){
        highGuess = guess; 
      } else if (fitness < 0) {
        lowGuess = guess;
      }
      guess = autoGuess(lowGuess, highGuess);
      moves++;
      fitness = fitnessTest(guess, answer);
      hint(fitness, guess, answer, lowGuess, highGuess);
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
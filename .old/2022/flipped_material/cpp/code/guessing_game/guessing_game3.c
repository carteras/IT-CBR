#include <stdio.h>

int main(void) {
  int answer = 5;
  int guess = -1;
  
  while (answer != guess){
    printf("pick a number between 1 and 10\n");
    scanf("%d", &guess);
    if (guess == answer){
      printf("You win!");
    } else {
      if (guess < answer){
        printf("Your guess was too low!\n");
      } else {
        printf("Your guess was too high!\n");
      }
    }
  }
  return 0;
}
#include <stdio.h>

int main(void) {
  int answer = 5;
  int guess = -1;
  int min_value = 1;
  int max_value = 10;
  
  while (answer != guess){
    printf("pick a number between %d and %d\n", min_value, max_value);
    scanf("%d", &guess);
    if (guess < min_value || guess > max_value) {
      continue;
    }
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
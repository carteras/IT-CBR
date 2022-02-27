#include <stdio.h>

int main(void) {
  int answer = 5;
  int guess;
  printf("pick a number between 1 and 10\n");
  scanf("%d", &guess);
  if (guess == answer){
    printf("You win!");
  } else {
    printf("You lose!");
  }
  return 0;
}

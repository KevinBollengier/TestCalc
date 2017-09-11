/*Kevin Bollengier*/
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int number1;
    int number2;
    int addition;
    printf("Enter value 1:...\n");
    scanf("%i",&number1);
    printf("Enter value 2:...\n");
    scanf("%i",&number2);

    addition = number1 + number2;
    printf("%d",addition);

    return 0;
}

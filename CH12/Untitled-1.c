#include <stdio.h>

int main() {
  float radius, area, circumference;
  const float pi = 3.14159;

  // Prompt the user to enter the radius of the circle
  printf("Enter the radius of the circle: ");
  scanf("%f", &radius);

  // Calculate the area and circumference of the circle
  area = pi * radius * radius;
  circumference = 2 * pi * radius;

  // Print the results with two decimal places
  printf("The area of the circle is: %0.2f\n", area);
  printf("The circumference of the circle is: %0.2f\n", circumference);

  return 0;
}


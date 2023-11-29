def add_complex_numbers(num1, num2):
 result = num1 + num2
 return result

real_part1 = float(input("Enter the real part of the first complex number: "))
imag_part1 = float(input("Enter the imaginary part of the first complex number: "))
complex_num1 = complex(real_part1, imag_part1)
real_part2 = float(input("Enter the real part of the second complex number: "))
imag_part2 = float(input("Enter the imaginary part of the second complex number: "))
complex_num2 = complex(real_part2, imag_part2)

result_complex = add_complex_numbers(complex_num1, complex_num2)

print(f"The sum of {complex_num1} and {complex_num2} is: {result_complex}")
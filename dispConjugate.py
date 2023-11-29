def conjugate_complex_number(num):
 conjugate_num = num.conjugate()
 return conjugate_num

real_part = float(input("Enter the real part of the complex number: "))
imag_part = float(input("Enter the imaginary part of the complex number: "))
complex_num = complex(real_part, imag_part)

conjugate_result = conjugate_complex_number(complex_num)
print(f"The conjugate of {complex_num} is: {conjugate_result}")

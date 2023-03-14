.data
prompt: .asciiz "What shape do you want to work with?: "
option_1: .asciiz "\n1. Triangle"
option_2: .asciiz "\n2. Square"
option_3: .asciiz "\n3. Rectangle"
option_4: .asciiz "\n4. Circle"
option_5: .asciiz "\n5. Parallelogram\n"
triangle_a: .asciiz "Enter length of side a: "
triangle_b: .asciiz "Enter length of side b: "
triangle_c: .asciiz "Enter length of side c: "
triangle_per: .asciiz "The perimeter of the triangle is "
square: .asciiz "Enter the length of the side: "
square_per: .asciiz "The perimeter of the square is "
rectangle_a: .asciiz "Enter breadth: "
rectangle_b: .asciiz "Enter length: "
rectangle_per: .asciiz "The perimeter of the rectangle is "
circle: .asciiz "Enter the length of the radius: "
circle_per: .asciiz "The circumference is "
parallelogram_a: .asciiz "Enter length of base: "
parallelogram_b: .asciiz "Enter length of side: "
parallelogram_per: .asciiz "The perimeter of the parallelogram is "
error_statement: .asciiz "Number cannot be negative"
pi: .float 3.14159265359
one: .float 1
two: .float 2
three: .float 3
four: .float 4
five: .float 5

.text
#print the prompt to screen
la $a0, prompt
li $v0, 4
syscall
la $a0, option_1
li $v0, 4
syscall
la $a0, option_2
li $v0, 4
syscall
la $a0, option_3
li $v0, 4
syscall
la $a0, option_4
li $v0, 4
syscall
la $a0, option_5
li $v0, 4
syscall
#get the user's value
li $v0, 6
syscall
addu $s0, $v0, $zero


# if user input is 1
l.s $f1, one
c.eq.s $f0, $f1
bc1t finish

# if user input is 2
l.s $f2, two
c.eq.s $f0, $f2
bc1t end

# if user input is 3
l.s $f3, three
c.eq.s $f0, $f3
bc1t finni

# if user input is 4
l.s $f4, four
c.eq.s $f0, $f4
bc1t exit

# if user input is 5
l.s $f5, five
c.eq.s $f0, $f5
bc1t coda

# exit block
li $v0, 10
syscall

finni:
# get side a
la $a0, rectangle_a
li $v0, 4
syscall
li $v0, 6
syscall
addu $s0, $v0, $zero
mov.s $f1, $f0
# get side b
la $a0, rectangle_b
li $v0, 4
syscall
li $v0, 6
syscall
addu $s0, $v0, $zero
mov.s $f2, $f0
# write the perimeter statement
la $a0, rectangle_per
li $v0, 4
syscall
# calculate the perimeter
add.s $f3, $f1, $f1
add.s $f4, $f2, $f2
add.s $f4, $f4, $f3
mov.s $f12, $f4
li $v0, 2
syscall
li $v0, 10
syscall

finish:
# get side a
la $a0, triangle_a
li $v0, 4
syscall
li $v0, 6
syscall
addu $s0, $v0, $zero
mov.s $f1, $f0
# get side b
la $a0, triangle_b
li $v0, 4
syscall
li $v0, 6
syscall
addu $s0, $v0, $zero
mov.s $f2, $f0
# get side c
la $a0, triangle_c
li $v0, 4
syscall
li $v0, 6
syscall
addu $s0, $v0, $zero
mov.s $f3, $f0
# write the perimeter statement
la $a0, triangle_per
li $v0, 4
syscall
# calculate the perimeter
add.s $f4, $f1, $f2
add.s $f4, $f4, $f3
mov.s $f12, $f4
li $v0, 2
syscall
li $v0, 10
syscall



end:
# write square prompt and get user value
la $a0, square
li $v0, 4
syscall
li $v0, 6
syscall
addu $s0, $v0, $zero
# write the perimeter statement
la $a0, square_per
li $v0, 4
syscall
# calculate the perimeter
l.s $f1, four
mul.s $f1, $f1, $f0
mov.s $f12, $f1
li $v0, 2
syscall
li $v0, 10
syscall

exit:
# write circle prompt and get user value
la $a0, circle
li $v0, 4
syscall
li $v0, 6
syscall
addu $s0, $v0, $zero
# write the circle statement
la $a0, circle_per
li $v0, 4
syscall
# calculate the circumference
l.s $f1, two
l.s $f2, pi
mul.s $f1, $f1, $f2
mul.s $f3, $f1, $f0
mov.s $f12, $f3
li $v0, 2
syscall
li $v0, 10
syscall

coda:
# get side a
la $a0, parallelogram_a
li $v0, 4
syscall
li $v0, 6
syscall
addu $s0, $v0, $zero
mov.s $f1, $f0
# get side b
la $a0, parallelogram_b
li $v0, 4
syscall
li $v0, 6
syscall
addu $s0, $v0, $zero
mov.s $f2, $f0
# write the perimeter statement
la $a0, parallelogram_per
li $v0, 4
syscall
# calculate the perimeter
l.s $f3, two
add.s $f2, $f1, $f2
mul.s $f3, $f3, $f2
mov.s $f12, $f3
li $v0, 2
syscall
li $v0, 10
syscall

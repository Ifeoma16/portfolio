
.data

.text
li $t0, 10
li $t1, 50
add $t0, $t0, $t1
li $v0, 1
move $a0, $t0
syscall

li $v0, 10
syscall
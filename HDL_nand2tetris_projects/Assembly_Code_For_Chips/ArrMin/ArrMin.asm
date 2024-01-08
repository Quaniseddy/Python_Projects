// Finds the smallest element in the array of length R2 whose first element is at RAM[R1] and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

//get the first element
@R1
A=M
D=M
//to start with, assume the smallest element is the first element
@R0
M=D

//loop to find the smallest element
(LOOP)
    @R2
    MD=M-1
    @END
    D;JEQ
    @R1
    AM=M+1
    D=M // the value of RAM[M+1]
    @current // the value of RAM[M+1]
    M=D
    @R0
    D=M
    @current
    D=D-M
    @OVERWRITE //if d > 0 meaning current number is smallest so far
    D;JGT
    @LOOP //unconditionally loop
    0;JMP

(END)
    @END
    0;JMP

//change the smallest number stored
(OVERWRITE)
    @current
    D=M
    @R0
    M=D
    @LOOP
    0;JMP
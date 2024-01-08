// This file is based on part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: Mult.asm

// Multiplies R1 and R2 and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
//mutiply R1 and R2 by adding R1 to itself R2 times
//counts will be the times R2 represent
@R0 
M=0 //initialise RO to 0

//chekc the signs of R2
//if the sign is negetive make the counts positive, and implement the mutiplcation as mutiplied by a postive number
//*** just flip in the end to get to the final result ***
(Check_sign)
    @R2
    D=M
    @Make_positive
    D;JLT
    @counts
    M=D
    @LOOP
    0;JMP

//make counts positive
(Make_positive)
    @R2
    D=-M
    @counts
    M=D

//mutiplication loop
(LOOP)
    @counts
    D=M
    @Result_check
    D;JEQ

    @counts
    M=M-1

    @R0
    D=M
    @R1
    D=D+M
    @R0
    M=D

    @LOOP
    0;JMP

//check if in previous lines, we implement mutiplication by assuming R2 is positive
(Result_check)
    @R2
    D=M
    @Result_flip
    D;JLT
    @END
    0;JMP
//if we did then flip the result stored in R0
//else go to END
(Result_flip)
    @R0
    M=-M

(END)
    @END
    0;JMP


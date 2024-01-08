// Calculates the absolute value of R1 and stores the result in R0.
@R1           
D=M           
@R0           
M=D           
@END          
D;JGT         
D=-D          
@R0           
M=D           
(END)
    @END     
    0;JMP     
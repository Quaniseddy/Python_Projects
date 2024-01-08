// Sorts the array of length R2 whose first element is at RAM[R1] in ascending order in place. Sets R0 to True (-1) when complete.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// store the length of array in D
@R2
D=M
// store index of last element
@R1
D=M+D
D=D-1
@lastIndex
M=D
// interate from rightmost index until reach the second index
@decrementPtr
M=D

(OUTER_LOOP)
    //check if the address R1 holds out of range of the array
    @R1 // R1 functions as i and holds the address of the first element
    D=M // D gets the address of the first element
    @lastIndex // it holds the address of the last element
    D=M-D // (address)last element - first element
    @MAKE_RO_TRUE
    D;JEQ
    @Create_J
    0;JMP
    
    (INNER_LOOP)
        // j<length-1-i
        @j //inner index, inital value: firstIndexOfArray
        D=M
        @decrementPtr
        D=M-D
        @I_Index_Modification // if indexOfJ = lastIndexOfArray
        D;JEQ
        @j
        D=M
        @j+1
        M=D+1
    
(COMPARE)
    @j
    A=M // A points to the current index
    D=M // M holds the value of current index
    @J_POSITIVE
    D;JGE
    @J_NEGTIVE
    D;JLT

(SUBTRACT)
    @j // j's M holds the address of the current index
    A=M // A points to the current index
    D=M // M holds the value of current index
    @j+1 // j+1's M hold the address of the next index
    A=M // A points to the next index
    D=D-M // M holds the value of next index, D holds the value of cuurent index
    @INCREMENT_OF_J
    D;JLE  
    
(SWAP)
    @j // j holds the address of the current index
    A=M //the current index
    D=M // D = value of the current index
    @tmp
    M=D // tmp holds the value of the current index
    @j+1 // j holds the address of the next index
    A=M // next index
    D=M // D = value of the next index
    @j
    A=M // the address of the current index
    M=D // The current index's value = the next index
    @tmp //tmp holds the value of the current index
    D=M // D = value of the current index
    @j+1
    A=M // the address of the next index
    M=D // the next index's value = the currect index

(INCREMENT_OF_J)
    @j
    M=M+1
    @INNER_LOOP
    0;JMP

(I_Index_Modification)
    @R1 // R1 hold the address of index i
    M=M+1
    @decrementPtr //decrement right pointer
    M=M-1
    @OUTER_LOOP
    0;JMP

(MAKE_RO_TRUE)
    @R0
    M=-1 // true = -1

(END)
    @END
    0;JMP

(Create_J) // initial value of J: first index of the array
    // get length of the array
    @R2
    D=M // store length of array in D
    @lastIndex
    // firstIndexOfArray = lastIndex - length + 1
    D=M-D
    D=D+1
    @j
    M=D
    @INNER_LOOP
    0;JMP

(J_POSITIVE)
    @j+1
    A=M
    D=M
    @SUBTRACT // same sign
    D;JGE
    @SWAP // diff sign: j is pos, j+1 is neg
    D;JLT

(J_NEGTIVE)
    @j+1
    A=M
    D=M
    @INCREMENT_OF_J // diff sign: j is neg, j+1 is pos
    D;JGE
    @SUBTRACT// same sign
    D;JLT
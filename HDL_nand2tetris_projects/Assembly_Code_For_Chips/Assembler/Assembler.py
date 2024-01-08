instruction_type = ['NULL','A_INSTRUCTION','C_INSTRUCTION','L_INSTRUCTION']

instruction_dest = ['NULL','M','D','MD','A','AM','AD','AMD']

instruction_jump = ['NULL','JGT','JEQ','JGE','JLT','JNE','JLE','JMP']

instruction_comp = ['NULL',
                    '0','1','-1',
                    'A','M','D',
                    '!A','!M','!D',
                    '-A','-M','-D',
                    'A+1','M+1','D+1',
                    'A-1','M-1','D-1',
                    'D+A','D+M',
                    'D-A','D-M','A-D','M-D',
                    'D&A','D&M',
                    'D|A','D|M']

class SymbolTable:

    def __init__(self):
        """
        Symbol table constructor
        """
        self.symbols = []
        self.base = 16
        pass

    def addSymbol(self, symbol, value):
        flag = 0
        for sym in self.symbols:
            if(symbol == sym[0]):
                flag=1
        
        if(flag == 0):
            newSymbol = (symbol,value)
            self.symbols.append(newSymbol)
            self.base = self.base + 1
        """
        Adds a symbol to the symbol table

        @param symbol: The name of the symbol
        @param value: The address for the symbol
        """
        pass


    def getSymbol(self, symbol):
        sym = (symbol, -1)
        for symb in self.symbols:
            if(sym[0] == symb[0]):
                sym[1] == symb[1]
        """
        Gets a symbol from the symbol table
        
        @param symbol: The name of the symbol
        @return: The address for the symbol or -1 if the symbol isn't in the table
        """
        return sym[1]


class Assembler:

    def __init__(self):
        """
        Assembler constructor
        """
        pass

    def buildSymbolTable(self, instructions, symbolTable):
        symbolTable.symbols.append(("R0",0))
        symbolTable.symbols.append(("R1",1))
        symbolTable.symbols.append(("R2",2))
        symbolTable.symbols.append(("R3",3))
        symbolTable.symbols.append(("R4",4))
        symbolTable.symbols.append(("R5",5))
        symbolTable.symbols.append(("R6",6))
        symbolTable.symbols.append(("R7",7))
        symbolTable.symbols.append(("R8",8))
        symbolTable.symbols.append(("R9",9))
        symbolTable.symbols.append(("R10",10))
        symbolTable.symbols.append(("R11",11))
        symbolTable.symbols.append(("R12",12))
        symbolTable.symbols.append(("R13",13))
        symbolTable.symbols.append(("R14",14))
        symbolTable.symbols.append(("R15",15))
        symbolTable.symbols.append(("SP",0))
        symbolTable.symbols.append(("LCL",1))
        symbolTable.symbols.append(("ARG",2))
        symbolTable.symbols.append(("THIS",3))
        symbolTable.symbols.append(("THAT",4))
        symbolTable.symbols.append(("SCREEN",16384))
        symbolTable.symbols.append(("KBD",24576))
        lineNumber = []
        j=0
        for i in range(len(instructions)):
            j=j+1
            lineNumber.append(j)
            if(instructions[i][0] == '('):
                j=j-1
                symbolTable.symbols.append((instructions[i][1:-1],lineNumber[i]))
        """
        Assembler first pass; populates symbol table with label locations.

        @param instructions: A list of the assembly language instructions.
        @param symbolTable: The symbol table to populate.
        """
        pass
    

    def generateMachineCode(self, instructions, symbolTable):
        code = []
        for ins in instructions:
            type = self.parseInstructionType(ins)
            if (type == 'A_INSTRUCTION'):
                tmp = self.parseSymbol(ins)
                code.append(self.translateSymbol(tmp,symbolTable))
            if(type == 'C_INSTRUCTION'):
                whole = "111"
                part1 = self.translateDest(self.parseInstructionDest(ins))
                part2 = self.translateComp(self.parseInstructionComp(ins))
                part3 = self.translateJump(self.parseInstructionJump(ins))
                whole = whole+part2+part1+part3
                code.append(whole)
        """
        Assembler second pass; Translates a set of instructions to machine code.

        @param instructions: A list of the assembly language instructions to be converted to machine code.
        @param symbolTable: The symbol table to reference/update.
        @return: A String containing the generated machine code as strings of 16-bit binary instructions, 1-per-line.
        """
        return code
       
    def parseInstructionType(self, instruction):
        if (instruction[0]=='@'):
            insType = "A_INSTRUCTION"
        elif(instruction[0]=='('):
            insType = "L_INSTRUCTION"
        else:
            insType = "C_INSTRUCTION"

        """
        Parses the type of the provided instruction

        @param instruction: The assembly language representation of an instruction.
        @return: The type of the instruction (A_INSTRUCTION, C_INSTRUCTION, L_INSTRUCTION, NULL)
        """
        return insType
    

    def parseInstructionDest(self, instruction):
        dest = "NULL"
        for i in range(len(instruction)):
            if(instruction[i] == '='):
                dest=instruction[:i]

        """
        Parses the destination of the provided C-instruction

        @param instruction: The assembly language representation of a C-instruction.
        @return: The destination of the instruction (see instruction_dest) 
        """
        return dest
    

    def parseInstructionJump(self, instruction):
        jump = "NULL"
        for i in range(len(instruction)):
            if(instruction[i] == ';'):
                jump = instruction[i+1:]
        """
        Parses the jump condition of the provided C-instruction

        @param instruction: The assembly language representation of a C-instruction.
        @return: The jump condition for the instruction (see instruction_jump)
        """
        return jump
    

    def parseInstructionComp(self, instruction):
        comp = "NULL"
        equalFlag = -1
        semiFlag = -1
        for i in range(len(instruction)):
            if(instruction[i] == '='):
                equalFlag= i
            if(instruction[i] == ';'):
                semiFlag = i
        
        if(equalFlag == -1):
            comp = instruction[:semiFlag]
        else:
            if(semiFlag == -1):
                comp = instruction[equalFlag+1:]
            else:
                comp = instruction[equalFlag+1:semiFlag]
        """
        Parses the computation/op-code of the provided C-instruction

        @param instruction: The assembly language representation of a C-instruction.
        @return: The computation/op-code of the instruction (see instruction_comp)
        """
        return comp
    
    
    def parseSymbol(self, instruction):
        tmp = instruction[1:]
        """
        Parses the symbol of the provided A/L-instruction

        @param instruction: The assembly language representation of a A/L-instruction.
        @return: A string containing either a label name (L-instruction), 
                a variable name (A-instruction), or a constant integer value (A-instruction)
        """
        return tmp
    

    def translateDest(self, dest):
        if(dest == "A"):
            return "100"
        elif(dest == "D"):
            return "010"
        elif(dest == "M"):
            return "001"
        elif(dest == "AM"):
            return "101"
        elif(dest == "AD"):
            return "110"
        elif(dest == "MD"):
            return "011"
        elif(dest == "AMD"):
            return "111"
        else:
            return "000"
        """
        Generates the binary bits of the dest part of a C-instruction

        @param dest: The destination of the instruction
        @return: A String containing the 3 binary dest bits that correspond to the given dest value.
        """
    
    def translateJump(self, jump):
        if(jump == "JLT"):
            return "100"
        elif(jump == "JGT"):
            return "001"
        elif(jump == "JEQ"):
            return "010"
        elif(jump == "JGE"):
            return "011"
        elif(jump == "JLE"):
            return "110"
        elif(jump == "JNE"):
            return "101"
        elif(jump == "JMP"):
            return "111"
        else:
            return "000"
        """
        Generates the binary bits of the jump part of a C-instruction

        @param jump: The jump condition for the instruction
        @return: A String containing the 3 binary jump bits that correspond to the given jump value.
        """
    
    def translateComp(self, comp):
        if(comp == '0'):
            return "0101010"
        elif(comp == '1'):
            return "0111111"
        elif(comp == '-1'):
            return "0111010"
        elif(comp == 'A'):
            return "0110000"
        elif(comp == 'D'):
            return "0001100"
        elif(comp == 'M'):
            return "1110000"
        elif(comp == '!A'):
            return "0110001"
        elif(comp == '!D'):
            return "0001101"
        elif(comp == '!M'):
            return "1110001"
        elif(comp == '-A'):
            return "0110011"
        elif(comp == '-D'):
            return "0001111"
        elif(comp == '-M'):
            return "1110011"
        elif(comp == 'A+1'):
            return "0110111"
        elif(comp == 'D+1'):
            return "0011111"
        elif(comp == 'M+1'):
            return "1110111"
        elif(comp == 'A-1'):
            return "0110010"
        elif(comp == 'D-1'):
            return "0001110"
        elif(comp == 'M-1'):
            return "1110010"
        elif(comp == 'D+A' or comp == 'A+D'):
            return "0000010"
        elif(comp == 'D+M' or comp == 'M+D'):
            return "1000010"
        elif(comp == 'D-A'):
            return "0010011"
        elif(comp == 'D-M'):
            return "1010011"
        elif(comp == 'A-D'):
            return "0000111"
        elif(comp == 'M-D'):
            return "1000111"
        elif(comp == 'D&A'):
            return "0000000"
        elif(comp == 'D&M'):
            return "1000000"
        elif(comp == 'D|A' or comp == 'A|D'):
            return "0010101"
        elif(comp == 'D|M' or comp == 'M|D'):
            return "1010101"
        else:
            return "NULL"        
        """
        Generates the binary bits of the computation/op-code part of a C-instruction

        @param comp: The computation/op-code for the instruction
        @return: A String containing the 7 binary computation/op-code bits that correspond to the given comp value.
        """
    
    def translateSymbol(self, symbol, symbolTable):
        index = -1
        if not (symbol.isdecimal()):
            for s in symbolTable.symbols:
                if(s[0] == symbol):
                    index = s[1]
            if(index ==-1):
                index = symbolTable.base
                symbolTable.addSymbol(symbol,symbolTable.base)
        else:
            index = int(symbol)
        
        tmp = bin(index)
        tmp = tmp[2:]
        while(len(tmp) < 16):
            tmp = '0' + tmp
        """
        Generates the binary bits for an A-instruction, parsing the value, or looking up the symbol name.

        @param symbol: A string containing either a label name, a variable name, or a constant integer value
        @param symbolTable: The symbol table for looking up label/variable names
        @return: A String containing the 15 binary bits that correspond to the given sybmol.
        """
        return tmp
    

# A quick-and-dirty parser when run as a standalone script.
if __name__ == "__main__":
    import sys
    a=1
    if(a==1):#len(sys.argv) > 1):
        instructions = []
        # Open file
        with open("Assembler/Assembler600.asm", "r") as a_file:
            # Read line-by-line, skip comments and empty line
            for line in a_file:
                if line[0] != '/' and line[0] != "\n":
                    line = line.strip()
                    for i in range(len(line)):
                        if line[i] == '/' or line[i] == ' ':
                            line = line[:i]
                            break
                    instructions.append(line)
        assembler = Assembler()
        symbolTable = SymbolTable()
        # First pass
        assembler.buildSymbolTable(instructions,symbolTable)
        # Second pass
        code = assembler.generateMachineCode(instructions,symbolTable)
        # Print output
        for line in code:
            print(line)
            

import java.io.*;
import java.util.*;


public class VMTranslator {
    static int eqAddress, gtAddress, ltAddress, returnAddress, Counters = 0;
    /** Generate Hack Assembly code for a VM push operation */
    public static String vm_push(String segment, int offset){
        String translatedPush = "";
        if(segment.equals("this") || segment.equals("that") || segment.equals("local") || segment.equals("argument")){
            switch(segment){
                case "this":
                    translatedPush = translatedPush + "@THIS\n";
                    break;
                case "that":
                    translatedPush = translatedPush + "@THAT\n";
                    break;
                case "local":
                    translatedPush = translatedPush + "@LCL\n";
                    break;
                case "argument":
                    translatedPush = translatedPush + "@ARG\n";
                    break;
                
            }
            translatedPush = translatedPush + "D=M\n"; // store base address then new line
            translatedPush = translatedPush + "@" + offset + "\n"; 
            translatedPush = translatedPush + "A=D+A\n"; // store the address of the segment with the pushed value to stack then new line
            translatedPush = translatedPush + "D=M\n"; // store the value to be pushed onto stack later then new line
        } else if(segment.equals("pointer") ){
            if(offset == 0){ // when offset = 0 : this
                translatedPush = translatedPush + "@3\n" + "D=M\n"; // store the filed address to be pushed onto the stack
            } else if (offset == 1) { // when offset == 1 : that
                translatedPush = translatedPush + "@4\n" + "D=M\n"; // store the filed address to be pushed onto the stack
            }
        } else if(segment.equals("static") || segment.equals("temp")){
            if(segment.equals("static")){
                translatedPush = translatedPush + "@16\n"; // base address starting from 16
            } else{ // when segment = temp
                translatedPush = translatedPush + "@5\n"; // base address starting from 5 
            }
            translatedPush = translatedPush + "D=A\n";
            translatedPush = translatedPush + "@" + offset + "\n";
            translatedPush = translatedPush + "A=A+D\n";
            translatedPush = translatedPush + "D=M\n"; // store value to be pushed onto the stack
        } else { // when its a constant
            translatedPush = translatedPush + "@" + offset + "\n";
            translatedPush = translatedPush + "D=A\n"; // store value to be pushed onto the stack
        }
        translatedPush = translatedPush + "@SP\n";
        translatedPush = translatedPush + "AM=M+1\n";
        translatedPush = translatedPush + "A=A-1\n";
        translatedPush = translatedPush + "M=D\n";
        return translatedPush;
    }

    // RAM[1000] stores value to be popped off stack
    // RAM[1001] stores the destination address
    /** Generate Hack Assembly code for a VM pop operation */
    public static String vm_pop(String segment, int offset){
        String translatedPop = "";
        // decrement sp
        translatedPop = translatedPop + "@SP\n";
        translatedPop = translatedPop + "AM=M-1\n";
        translatedPop = translatedPop + "D=M\n"; // assign the value to be popped to D

        /*
         * store the value in RAM[1000] for later use
         */
        translatedPop = translatedPop + "@1000\n";
        translatedPop = translatedPop + "M=D\n";

        if(segment.equals("this")  || segment.equals("that") || segment.equals("local") || segment.equals("argument")){
            switch (segment) {
                case "this":
                    translatedPop = translatedPop + "@THIS\n";
                    break;
                case "that":
                    translatedPop = translatedPop + "@THAT\n";
                    break;
                case "local":
                    translatedPop = translatedPop + "@LCL\n";
                    break;
                case "argument":
                    translatedPop = translatedPop + "@ARG\n";
                    break;
            }
            translatedPop = translatedPop + "D=M\n";
        } else if (segment.equals("static")  || segment.equals("pointer") || segment.equals("temp")){
            switch (segment) {
                case "static":
                    translatedPop = translatedPop + "@16\n";
                    break;
                case "pointer":
                    translatedPop = translatedPop + "@3\n";
                    break;
                case "temp":
                    translatedPop = translatedPop + "@5\n";
                    break;
            }
            translatedPop = translatedPop + "D=A\n";
        }
        translatedPop = translatedPop + "@" + offset + "\n";
        translatedPop = translatedPop + "D=D+A\n"; // store the destionation address in D
        translatedPop = translatedPop + "@1001\n";
        translatedPop = translatedPop + "M=D\n"; // store the the destination address
        translatedPop = translatedPop + "@1000\n"; 
        translatedPop = translatedPop + "D=M\n"; // get the value to be popped off
        translatedPop = translatedPop + "@1001\n";
        translatedPop = translatedPop + "A=M\n"; // get the destination address
        translatedPop = translatedPop + "M=D\n"; // assign value to destination
        return translatedPop;
    }

    /** Generate Hack Assembly code for a VM add operation */
    public static String vm_add(){
        String translatedString = "@SP\n";
        translatedString += "AM=M-1\n";
        translatedString += "D=M\n";
        translatedString += "A=A-1\n";
        translatedString += "M=M+D\n";
        return translatedString;
    }

    /** Generate Hack Assembly code for a VM sub operation */
    public static String vm_sub(){
        String translatedString = "@SP\n";
        translatedString += "AM=M-1\n";
        translatedString += "D=M\n";
        translatedString += "A=A-1\n";
        translatedString += "M=M-D\n";
        return translatedString;
    }

    /** Generate Hack Assembly code for a VM neg operation */
    public static String vm_neg(){
        String translatedString = "@SP\n";
        translatedString += "A=M-1\n";
        translatedString += "M=-M\n";
        return translatedString;
    }

    /** Generate Hack Assembly code for a VM eq operation */
    public static String vm_eq(){
        eqAddress++; // increment
        String translated = "";
        translated = translated + "@SP" + "\n";
        translated = translated + "AM=M-1" + "\n";
        translated = translated + "D=M" + "\n";
        translated = translated + "@SP" + "\n";
        translated = translated + "AM=M-1" + "\n";
        translated = translated + "D=M-D" + "\n";
        translated = translated + "@EQUAL_TRUE" + eqAddress + "\n";
        translated = translated + "D;JEQ" + "\n";
        translated = translated + "D=0" + "\n";
        translated = translated + "@EQUAL_FALSE" + eqAddress + "\n";
        translated = translated + "0;JMP" + "\n";
        translated = translated + "(EQUAL_TRUE" + eqAddress + ")" + "\n";
        translated = translated + "D=-1" + "\n";
        translated = translated + "(EQUAL_FALSE" + eqAddress + ")" + "\n";
        translated = translated + "@SP" + "\n";
        translated = translated + "A=M" + "\n";
        translated = translated + "M=D" + "\n";
        translated = translated + "@SP" + "\n";
        translated = translated + "M=M+1" + "\n";
        return translated;
    }

    /** Generate Hack Assembly code for a VM gt operation */
    public static String vm_gt(){
        gtAddress++; // increment 
        String translated = "";
        translated = translated + "@SP" + "\n";
        translated = translated + "AM=M-1" + "\n";
        translated = translated + "D=M" + "\n";
        translated = translated + "@SP" + "\n";
        translated = translated + "AM=M-1" + "\n";
        translated = translated + "D=M-D" + "\n";
        translated = translated + "@GT_TRUE" + gtAddress + "\n";
        translated = translated + "D;JGT" + "\n";
        translated = translated + "D=0" + "\n";
        translated = translated + "@GT_FALSE" + gtAddress + "\n";
        translated = translated + "0;JMP" + "\n";
        translated = translated + "(GT_TRUE" + gtAddress + ")" + "\n";
        translated = translated + "D=-1" + "\n";
        translated = translated + "(GT_FALSE" + gtAddress + ")" + "\n";
        translated = translated + "@SP" + "\n";
        translated = translated + "A=M" + "\n";
        translated = translated + "M=D" + "\n";
        translated = translated + "@SP" + "\n";
        translated = translated + "M=M+1" + "\n";
        return translated;
    }


    /** Generate Hack Assembly code for a VM lt operation */
    public static String vm_lt(){
        ltAddress++;    //increment
        String translated = "";
        translated = translated + "@SP" + "\n";
        translated = translated + "AM=M-1" + "\n";
        translated = translated + "D=M" + "\n";
        translated = translated + "@SP" + "\n";
        translated = translated + "AM=M-1" + "\n";
        translated = translated + "D=M-D" + "\n";
        translated = translated + "@LT_TRUE" + ltAddress + "\n";
        translated = translated + "D;JLT" + "\n";
        translated = translated + "D=0" + "\n";
        translated = translated + "@LT_FALSE" + ltAddress + "\n";
        translated = translated + "0;JMP" + "\n";
        translated = translated + "(LT_TRUE" + ltAddress + ")" + "\n";
        translated = translated + "D=-1" + "\n";
        translated = translated + "(LT_FALSE" + ltAddress + ")" + "\n";
        translated = translated + "@SP" + "\n";
        translated = translated + "A=M" + "\n";
        translated = translated + "M=D" + "\n";
        translated = translated + "@SP" + "\n";
        translated = translated + "M=M+1" + "\n";
        return translated;
    }

    /** Generate Hack Assembly code for a VM and operation */
    public static String vm_and(){
        String translated = "";
        translated += "@SP\n";
        translated += "AM=M-1\n";
        translated += "D=M\n";
        translated += "A=A-1\n";
        translated += "M=D&M\n";
        return translated;
    }

    /** Generate Hack Assembly code for a VM or operation */
    public static String vm_or(){
        String translated = "";
        translated += "@SP\n";
        translated += "AM=M-1\n";
        translated += "D=M\n";
        translated += "A=A-1\n";
        translated += "M=D|M\n";
        return translated;
    }

    /** Generate Hack Assembly code for a VM not operation */
    public static String vm_not(){
        String translated = "";
        translated += "@SP\n";
        translated += "A=M-1\n";
        translated += "M=!M\n";
        return translated;
    }

    /** Generate Hack Assembly code for a VM label operation */
    public static String vm_label(String label){
        return "(" + label + ")\n";
    }

    /** Generate Hack Assembly code for a VM goto operation */
    public static String vm_goto(String label){
        return "@" + label + "\n0;JMP\n";
    }

    /** Generate Hack Assembly code for a VM if-goto operation */
    //if-goto only when not false(0)
    public static String vm_if(String label){
        String translated = "";
        translated += "@SP\n";
        translated += "AM=M-1\n";
        translated += "D=M\n";
        translated += "@" + label + "\n";
        translated += "D;JNE\n";
        return translated;
    }

    /** Generate Hack Assembly code for a VM function operation */
    public static String vm_function(String function_name, int n_vars){
        String translated = "(" + function_name + ")" + "\n";
        translated += "@SP\n";
        translated += "A=M\n";
        // insert n numbers of 0 onto stack
        for (int i = 0; i < n_vars; i++) {
            translated += "M=0\n";
            translated += "A=A+1\n";
        }
        translated += "D=A\n";
        translated += "@SP\n";
        translated += "M=D\n";
        return translated;
    }

    /** Generate Hack Assembly code for a VM call operation */
    public static String vm_call(String function_name, int n_args){
        //initialise return string
        String translatedCallFunc = "";
        returnAddress++;
        /*
         * saved frame of the caller
         */
        // push return address
        translatedCallFunc += "@RETURN_" + returnAddress + "\n";
        translatedCallFunc += "D=A\n";
        translatedCallFunc += "@SP\n";
        translatedCallFunc += "AM=M+1\n";
        translatedCallFunc += "A=A-1\n";
        translatedCallFunc += "M=D\n";
        // LCL
        translatedCallFunc += "@LCL\n";
        translatedCallFunc += "D=M\n";
        translatedCallFunc += "@SP\n";
        translatedCallFunc += "AM=M+1\n";
        translatedCallFunc += "A=A-1\n";
        translatedCallFunc += "M=D\n";
        // ARG
        translatedCallFunc += "@ARG\n";
        translatedCallFunc += "D=M\n";
        translatedCallFunc += "@SP\n";
        translatedCallFunc += "AM=M+1\n";
        translatedCallFunc += "A=A-1\n";
        translatedCallFunc += "M=D\n";
        // THIS (pointer 0, point this segment to object)
        //translated += vm_push("pointer", 0);
        translatedCallFunc += "@THIS\n";
        translatedCallFunc += "D=M\n";
        translatedCallFunc += "@SP\n";
        translatedCallFunc += "AM=M+1\n";
        translatedCallFunc += "A=A-1\n";
        translatedCallFunc += "M=D\n";
        // THAT (pointer 1 point that segment to array)
        //translated += vm_push("pointer", 1);
        translatedCallFunc += "@THAT\n";
        translatedCallFunc += "D=M\n";
        translatedCallFunc += "@SP\n";
        translatedCallFunc += "AM=M+1\n";
        translatedCallFunc += "A=A-1\n";
        translatedCallFunc += "M=D\n";

        /*
        reset
        */
        translatedCallFunc += "@SP\n";
        translatedCallFunc += "D=M\n";
        translatedCallFunc += "@" + n_args + "\n";
        translatedCallFunc += "D=D-A\n";
        translatedCallFunc += "@5\n";
        translatedCallFunc += "D=D-A\n";
        translatedCallFunc += "@ARG\n";
        translatedCallFunc += "M=D\n";

        // LCL: updated SP
        translatedCallFunc += "@SP\n";
        translatedCallFunc += "D=M\n";
        translatedCallFunc += "@LCL\n";
        translatedCallFunc += "M=D\n";
        
        /*
         * jump to callee
         */
        translatedCallFunc += vm_goto(function_name) + "\n";

        /* return label */
        translatedCallFunc += vm_label("RETURN_" + returnAddress) + "\n";
        return translatedCallFunc;
    }

    /** Generate Hack Assembly code for a VM return operation */
    public static String vm_return(){
        Counters++;
        //initialise return value
        String translated = "";
        String returnBase = "RETURN_BASE" + Counters;
        String returnAddress = "RETURN_ADDR" + Counters;

        /* get return frame base */
        translated += "@LCL\n";
        translated += "D=M\n";
        translated += "@" + returnBase + "\n";
        translated += "M=D\n";
        /* get return address */
        translated += "@5\n";
        translated += "A=D-A\n"; // go to saved return address
        translated += "D=M\n"; // get saved address
        translated += "@" + returnAddress + "\n";
        translated += "M=D\n";

        /* arg0 stores return value  */
        translated += vm_pop("argument", 0) + "\n";

        /* restore */
        // reset SP
        translated += "@ARG\n";
        translated += "D=M+1\n";
        translated += "@SP\n";
        translated += "M=D\n";
        // restore THAT
        translated += "@" + returnBase +"\n";
        translated += "A=M-1\n";
        translated += "D=M\n";
        translated += "@THAT\n";
        translated += "M=D\n";
        // restore THIS
        translated += "@" + returnBase +"\n";
        translated += "D=M\n";
        translated += "@2\n";
        translated += "A=D-A\n";
        translated += "D=M\n";
        translated += "@THIS\n";
        translated += "M=D\n";
        // restore ARG
        translated += "@" + returnBase + "\n";
        translated += "D=M\n";
        translated += "@3\n";
        translated += "A=D-A\n";
        translated += "D=M\n";
        translated += "@ARG\n";
        translated += "M=D\n";
        // restore LCL
        translated += "@" + returnBase +"\n";
        translated += "D=M\n";
        translated += "@4\n";
        translated += "A=D-A\n";
        translated += "D=M\n";
        translated += "@LCL\n";
        translated += "M=D\n";
        /* jump to return address */
        translated += "@" + returnAddress + "\n";
        translated += "A=M;JMP\n";
        return translated;
    }

    /** A quick-and-dirty parser when run standalone. */ 
    public static void main(String[] args){
        if(args.length > 0){
            try {
                Scanner sc = new Scanner(new File(args[0]));
                while (sc.hasNextLine()) {
                    String[] tokens = sc.nextLine().trim().toLowerCase().split("\\s+");
                    if(tokens.length==1){
                        if(tokens[0].equals("add")){
                            System.out.println(vm_add());
                        } else if(tokens[0].equals("sub")){
                            System.out.println(vm_sub());
                        } else if(tokens[0].equals("neg")){
                            System.out.println(vm_neg());
                        } else if(tokens[0].equals("eq")){
                            System.out.println(vm_eq());
                        } else if(tokens[0].equals("gt")){
                            System.out.println(vm_gt());
                        } else if(tokens[0].equals("lt")){
                            System.out.println(vm_lt());
                        } else if(tokens[0].equals("and")){
                            System.out.println(vm_and());
                        } else if(tokens[0].equals("or")){
                            System.out.println(vm_or());
                        } else if(tokens[0].equals("not")){
                            System.out.println(vm_not());
                        } else if(tokens[0].equals("return")){
                            System.out.println(vm_return());
                        }
                    } else if(tokens.length==2){
                        if(tokens[0].equals("label")){
                            System.out.println(vm_label(tokens[1]));
                        } else if(tokens[0].equals("goto")){
                            System.out.println(vm_goto(tokens[1]));
                        } else if(tokens[0].equals("if-goto")){
                            System.out.println(vm_if(tokens[1]));
                        }
                    } else if(tokens.length==3){
                        int t2;
                        try {
                            t2 = Integer.parseInt(tokens[2]);
                        } catch (Exception e) {
                            System.err.println("Unable to parse int.");
                            break;
                        }
                        if(tokens[0].equals("push")){
                            System.out.println(vm_push(tokens[1],t2));
                        } else if(tokens[0].equals("pop")){
                            System.out.println(vm_pop(tokens[1],t2));
                        } else if(tokens[0].equals("function")){
                            System.out.println(vm_function(tokens[1],t2));
                        } else if(tokens[0].equals("call")){
                            System.out.println(vm_call(tokens[1],t2));
                        }
                    }
                }
                sc.close();
            } catch (FileNotFoundException e) {
                System.err.println("File not found.");
            }
        }
    }
        
}
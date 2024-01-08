load Mult.asm,
output-file Mult05.out,
compare-to Mult05.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2;

set PC 0,
set RAM[0] 0,  // Set R0
set RAM[1] -1500,  // Set R1
set RAM[2] -2;  // Set R2
repeat 200 {
  ticktock;    // Run for 200 clock cycles
}
set RAM[1] -1500,  // Restore arguments in case program used them
set RAM[2] -2,
output;        // Output to file

set PC 0,
set RAM[0] 0,  // Set R0
set RAM[1] 1057,  // Set R1
set RAM[2] 31;  // Set R2
repeat 200 {
  ticktock;    // Run for 200 clock cycles
}
set RAM[1] 1057,  // Restore arguments in case program used them
set RAM[2] 31,
output;        // Output to file
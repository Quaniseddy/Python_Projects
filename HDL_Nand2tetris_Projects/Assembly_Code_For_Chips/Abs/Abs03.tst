load Abs.asm,
output-file Abs03.out,
compare-to Abs03.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2;

set PC 0,
set RAM[0] 0,  // Set R0
set RAM[1] -110;  // Set R1
repeat 100 {
  ticktock;    // Run for 100 clock cycles
}
set RAM[1] -110,  // Restore arguments in case program used them
output;        // Output to file

set PC 0,
set RAM[0] 0,  // Set R0
set RAM[1] 0;  // Set R1
repeat 100 {
  ticktock;    // Run for 100 clock cycles
}
set RAM[1] 0,  // Restore arguments in case program used them
output;        // Output to file

set PC 0,
set RAM[0] 0,  // Set R0
set RAM[1] 1;  // Set R1
repeat 100 {
  ticktock;    // Run for 100 clock cycles
}
set RAM[1] 1,  // Restore arguments in case program used them
output;        // Output to file

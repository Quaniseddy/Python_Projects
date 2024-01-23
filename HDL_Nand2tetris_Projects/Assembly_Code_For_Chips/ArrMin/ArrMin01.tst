load ArrMin.asm,
output-file ArrMin00.out,
compare-to ArrMin00.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2 RAM[20]%D2.6.2 RAM[21]%D2.6.2 RAM[22]%D2.6.2 RAM[23]%D2.6.2;

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  1000, // Set R1
set RAM[2]  4,  // Set R2
set RAM[1000] 1,  // Set Arr[0]
set RAM[1001] 2,  // Set Arr[1]
set RAM[1002] 3,  // Set Arr[2]
set RAM[1003] 4;  // Set Arr[3]
repeat 300 {
  ticktock;    // Run for 300 clock cycles
}
set RAM[1] 1000,  // Restore arguments in case program used them
set RAM[2] 4,
output;        // Output to file

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  1000, // Set R1
set RAM[2]  4,  // Set R2
set RAM[1000] 1,  // Set Arr[0]
set RAM[1001] 2,  // Set Arr[1]
set RAM[1002] 3,  // Set Arr[2]
set RAM[1003] -32768;  // Set Arr[3]
repeat 300 {
  ticktock;    // Run for 300 clock cycles
}
set RAM[1] 1000,  // Restore arguments in case program used them
set RAM[2] 4,
output;        // Output to file

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  1000, // Set R1
set RAM[2]  4,  // Set R2
set RAM[1000] 1,  // Set Arr[0]
set RAM[1001] 2,  // Set Arr[1]
set RAM[1002] 3,  // Set Arr[2]
set RAM[1003] 0;  // Set Arr[3]
repeat 300 {
  ticktock;    // Run for 300 clock cycles
}
set RAM[1] 1000,  // Restore arguments in case program used them
set RAM[2] 4,
output;        // Output to file

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  1000, // Set R1
set RAM[2]  7,  // Set R2
set RAM[1000] 1,  // Set Arr[0]
set RAM[1001] 2,  // Set Arr[1]
set RAM[1002] 3,  // Set Arr[2]
set RAM[1003] 4;  // Set Arr[3]
set RAM[1004] 5;  // Set Arr[4]
set RAM[1005] 6;  // Set Arr[5]
set RAM[1006] -32768;  // Set Arr[6]
repeat 300 {
  ticktock;    // Run for 300 clock cycles
}
set RAM[1] 1000,  // Restore arguments in case program used them
set RAM[2] 7,
output;        // Output to file

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  1000, // Set R1
set RAM[2]  7,  // Set R2
set RAM[1000] 0,  // Set Arr[0]
set RAM[1001] 0,  // Set Arr[1]
set RAM[1002] 0,  // Set Arr[2]
set RAM[1003] 0;  // Set Arr[3]
set RAM[1004] 0;  // Set Arr[4]
set RAM[1005] 0;  // Set Arr[5]
set RAM[1006] 0;  // Set Arr[6]
repeat 300 {
  ticktock;    // Run for 300 clock cycles
}
set RAM[1] 1000,  // Restore arguments in case program used them
set RAM[2] 7,
output;        // Output to file
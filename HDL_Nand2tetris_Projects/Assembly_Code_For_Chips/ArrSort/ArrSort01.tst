load ArrSort.asm,
output-file ArrSort01.out,
compare-to ArrSort01.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2 RAM[1000]%D2.9.2 RAM[1001]%D2.9.2 RAM[1002]%D2.9.2 RAM[1003]%D2.9.2 RAM[1004]%D2.9.2 RAM[1005]%D2.9.2 RAM[1006]%D2.9.2;

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  1000, // Set R1
set RAM[2]  4,  // Set R2
set RAM[1000] 1,  // Set Arr[0]
set RAM[1001] 2,  // Set Arr[1]
set RAM[1002] 3,  // Set Arr[2]
set RAM[1003] 4;  // Set Arr[3]
repeat 500 {
  ticktock;    // Run for 600 clock cycles
}
set RAM[1] 1000,  // Restore arguments in case program used them
set RAM[2] 4,
output;        // Output to file

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  1000, // Set R1
set RAM[2]  4,  // Set R2
set RAM[1000] 3,  // Set Arr[0]
set RAM[1001] 1,  // Set Arr[1]
set RAM[1002] 5,  // Set Arr[2]
set RAM[1003] 7;  // Set Arr[3]
repeat 500 {
  ticktock;    // Run for 600 clock cycles
}
set RAM[1] 1000,  // Restore arguments in case program used them
set RAM[2] 4,
output;        // Output to file

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  1000, // Set R1
set RAM[2]  7,  // Set R2
set RAM[1000] 1,  // Set Arr[0]
set RAM[1001] 25,  // Set Arr[1]
set RAM[1002] 9,  // Set Arr[2]
set RAM[1003] 9;  // Set Arr[3]
set RAM[1004] 36;  // Set Arr[4]
set RAM[1005] 14;  // Set Arr[5]
set RAM[1006] 5;  // Set Arr[6]
repeat 1500 {
  ticktock;    // Run for 600 clock cycles
}
set RAM[1] 1000,  // Restore arguments in case program used them
set RAM[2] 7,
output;        // Output to file

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  1000, // Set R1
set RAM[2]  6,  // Set R2
set RAM[1000] 0,  // Set Arr[0]
set RAM[1001] 0,  // Set Arr[1]
set RAM[1002] 0,  // Set Arr[2]
set RAM[1003] 0;  // Set Arr[3]
set RAM[1004] 0;  // Set Arr[4]
set RAM[1005] 0;  // Set Arr[5]
repeat 500 {
  ticktock;    // Run for 600 clock cycles
}
set RAM[1] 1000,  // Restore arguments in case program used them
set RAM[2] 4,
output;        // Output to file

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  1000, // Set R1
set RAM[2]  4,  // Set R2
set RAM[1000] -9,  // Set Arr[0]
set RAM[1001] -10,  // Set Arr[1]
set RAM[1002] -8,  // Set Arr[2]
set RAM[1003] -1;  // Set Arr[3]
repeat 500 {
  ticktock;    // Run for 600 clock cycles
}
set RAM[1] 1000,  // Restore arguments in case program used them
set RAM[2] 4,
output;        // Output to file

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  1000, // Set R1
set RAM[2]  4,  // Set R2
set RAM[1000] -2,  // Set Arr[0]
set RAM[1001] 1,  // Set Arr[1]
set RAM[1002] 0,  // Set Arr[2]
set RAM[1003] -3;  // Set Arr[3]
repeat 500 {
  ticktock;    // Run for 600 clock cycles
}
set RAM[1] 1000,  // Restore arguments in case program used them
set RAM[2] 4,
output;        // Output to file

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  1000, // Set R1
set RAM[2]  4,  // Set R2
set RAM[1000] 999,  // Set Arr[0]
set RAM[1001] 1,  // Set Arr[1]
set RAM[1002] 4,  // Set Arr[2]
set RAM[1003] 32767;  // Set Arr[3]
repeat 500 {
  ticktock;    // Run for 600 clock cycles
}
set RAM[1] 1000,  // Restore arguments in case program used them
set RAM[2] 4,
output;        // Output to file

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  1000, // Set R1
set RAM[2]  4,  // Set R2
set RAM[1000] -666,  // Set Arr[0]
set RAM[1001] -999,  // Set Arr[1]
set RAM[1002] 250,  // Set Arr[2]
set RAM[1003] -32768;  // Set Arr[3]
repeat 500 {
  ticktock;    // Run for 600 clock cycles
}
set RAM[1] 1000,  // Restore arguments in case program used them
set RAM[2] 4,
output;        // Output to file

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  1000, // Set R1
set RAM[2]  4,  // Set R2
set RAM[1000] 1314,  // Set Arr[0]
set RAM[1001] 1,  // Set Arr[1]
set RAM[1002] 520,  // Set Arr[2]
set RAM[1003] -32768;  // Set Arr[3]
repeat 500 {
  ticktock;    // Run for 600 clock cycles
}
set RAM[1] 1000,  // Restore arguments in case program used them
set RAM[2] 4,
output;        // Output to file

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  1000, // Set R1
set RAM[2]  4,  // Set R2
set RAM[1000] -520,  // Set Arr[0]
set RAM[1001] 38,  // Set Arr[1]
set RAM[1002] -1314,  // Set Arr[2]
set RAM[1003] 32767;  // Set Arr[3]
repeat 500 {
  ticktock;    // Run for 600 clock cycles
}
set RAM[1] 1000,  // Restore arguments in case program used them
set RAM[2] 4,
output;        // Output to file
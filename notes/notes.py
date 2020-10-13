import sys
# Memory in the computer:
# ------
# A big array of bytes
# To get the or set the data in memory you need the index in the array

# Terms 
# - Index into memory array
# - Address
# - Location
# - Pointer

# "opcode" == the instruction itself
# "operands" == args in the instruction
memory = [
    1,  # PRINT_LESLIE
    3,  # SAVE_REG1, 37     r1 = 37
    1,  
    37, 
    4,  # PRINT_REG  R1     print(r[1])
    1,  # R1
    1,  # PRINT_LESLIE
    2   # HALT
]

# variables are called "registers"
# * There are a fixed number
# * They have preset names: R0, R0, R1, R2, R3 ... R7
#
# Registers can each hold a single byte

register = [0] * 8

# start execution at address 0

# Keep track of the address of currently executing intruction
pc = 0 # Program counter, pointer the instruction we're executing

halted = False
  
PRINT_LESLIE = 1
HALT = 2
SAVE_REG = 3
PRINT_REG = 4

while not halted:
    instruction = memory[pc]

    if instruction == PRINT_LESLIE:
        print("Leslie!")
        pc += 1

    elif instruction == HALT:
        halted = True
        pc  += 1 

    elif instruction == SAVE_REG: # SAVE_REG
        reg_num = memory[pc+1]
        value = memory[pc+2]
        register[reg_num] = value

        print("register", register)
        pc += 3
        
        
    elif instruction == PRINT_REG:
        reg_num = memory[pc+1]
        print(register[reg_num])
        pc += 2
    
    else:
        print(f"Unknown instruction {instruction} at address {pc}")
        sys.exit(1)
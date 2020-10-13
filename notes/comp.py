import sys

print(sys.argv)
sys.exit()
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
memory = [0] * 265

# variables are called "registers"
# * There are a fixed number
# * They have preset names: R0, R0, R1, R2, R3 ... R7
#
# Registers can each hold a single byte

register = [0] * 8

# Read program data
if len(sys.argv != 2):
    print("usage: compy.py program")
    sys.exit(1)
try:
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()

        if line == '' or line[0] == "#":
            continue
        try:
            str_value = line.split('#')[0]
            value = int(str_value)

        except ValueError:
            print(f"Invalid number {str_value} ")
            sys.exit()

        print(value)
sys.exit()
except ValueError:
    print(f"File not found: {sys.argv[1]}")
    sys.exit(2)
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
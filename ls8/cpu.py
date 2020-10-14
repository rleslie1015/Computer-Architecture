"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010
class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.running = False

    def load(self):
        """Load a program into memory."""

        address = 0

        if len(sys.argv) != 2:
            print("usage: compy.py progname")
            sys.exit(1)
        # try to open the file from second arg     
        try:
            with open(sys.argv[1]) as f:
                for line in f:
                    line = line.strip()
                    # print(line)
                    if line == '' or line[0] == "#":
                        continue
                    # reading instructions line by line
                    try:
                        str_value = line.split("#")[0]
                        value = int(str_value, 2) # casting into inter with base of 2 (binary)
                    
                    except ValueError: 
                        print(f"Invalid number {str_value}")
                        sys.exit(1)
                    
                    self.ram[address] = value
                    address += 1

        except FileNotFoundError:
            print(f"File not found: {sys.argv[1]}")
            sys.exit(2)
        # For now, we've just hardcoded a program:
        # print(self.ram[:50])
        # sys.exit()
        # program = [
        #     # From print8.ls8
          
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, value, address):
        # print('address', address)
        # print('value', value)
        self.ram[address] = value

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        
        while not self.running:
            # self.trace()
            instruction = self.ram[self.pc]

            if instruction == HLT: 
                # self.pc += 1
                sys.exit()

            elif instruction == LDI:
                operand_a = self.ram_read(self.pc + 1)
                operand_b = self.ram_read(self.pc + 2)
                # print(instruction)
                self.reg[operand_a] = operand_b
                # print(self.reg) 
                # self.pc += 3
            
            elif instruction == PRN:
                reg_num = self.ram[self.pc+1]
                print(self.reg[reg_num])
                # self.pc += 2

            elif instruction == MUL:
                # print(instruction)
                num1 = self.reg[0]
                num2 = self.reg[1]
                product = num1 * num2
                operand_c = self.ram_read(self.pc+1)

                self.reg[operand_c] = product
                # self.pc += 3

            instruction_len = (instruction >> 6) + 1
            # print('instruction len', instruction_len)
            self.pc += instruction_len

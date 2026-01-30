**Tools PVM uses internally \& WHY (short + exam-friendly):**



**Interpreter**



Why: Reads bytecode and executes instructions one by one



Role: Fetch → Decode → Execute loop



**Operand Stack**



Why: To perform calculations and store temporary values



Role: Push operands, pop results (stack-based VM)



**Call Stack (Frame Stack)**



Why: To manage function calls



Role: Stores local variables, return addresses, execution state



**Heap (Memory Manager)**



Why: To store objects dynamically



Role: Manages object creation and deletion



**Garbage Collector**



Why: To free unused memory



Role: Uses reference counting + cyclic GC



**Bytecode Loader**



Why: To load compiled .pyc files



Role: Sends bytecode to PVM for execution



**Exception Handling System**



Why: To handle runtime errors safely



Role: Detects, propagates, and manages exceptions



**Standard C Runtime**



Why: PVM is written in C (CPython)



Role: Executes low-level operations efficiently









AND

a b a\&\&b

0 0 0

0 1 0

1 0 0

1 1 1



OR

a b a||b

0 0 0

0 1 1

1 0 1

1 1 1



NOT

a ~a

0 1

1 0


msg="your:UD2345.hello"
id=msg.split(":")[1].split("")[0]


msg="sam sum sri"
if "sam" in msg:
  print("yes")

msg="sam sum sri"
print(msg.find("sam"))

day topics 
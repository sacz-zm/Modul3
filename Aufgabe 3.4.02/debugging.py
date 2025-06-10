

def SagHallo():
    SagDuDochHallo()

# Call Stack
def SagDuDochHallo():
    print("Hallo World!")

# Breakpoints - Step Over springt in die nächste Zeile, Step Into springt in die Funktion
SagHallo()
SagHallo()
SagHallo()

# Locals, Watch
variable1 = 1
variable2 = "abc"

variable1 = 21
variable2 = "x"


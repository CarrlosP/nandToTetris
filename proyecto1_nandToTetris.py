
# Online Python - IDE, Editor, Compiler, Interpreter

def NAND(a, b):
    return int(not (a and b))

def NOT(a):
    return NAND(a, a)

def AND(a, b):
    return NOT(NAND(a, b))

def OR(a, b):
    return NAND(NOT(a), NOT(b))

def XOR(a, b):
    return AND(NAND(a, b), OR(a, b))

def MUX(a, b, sel):
    not_sel = NOT(sel)
    and_a = AND(a, not_sel)
    and_b = AND(b, sel)
    return OR(and_a, and_b)
    
def DMUX(a, sel):
    not_sel = NOT(sel)
    out1 = AND(a, not_sel)
    out2 = AND(a, sel)
    return out1, out2

def NOT16(a):
    return [NOT(a[i]) for i in range(16)]
    
def AND16(a, b):
    return [AND(a[i], b[i]) for i in range(16)]

def OR16(a, b):
    return [OR(a[i], b[i]) for i in range(16)]
    
def MUX16(a, b, sel):
    return [MUX(a[i], b[i], sel) for i in range(16)]
    
def OR8WAY(inputs):
    temp1 = OR(inputs[0], inputs[1])
    temp2 = OR(inputs[2], inputs[3])
    temp3 = OR(inputs[4], inputs[5])
    temp4 = OR(inputs[6], inputs[7])
    temp5 = OR(temp1, temp2)
    temp6 = OR(temp3, temp4)
    return OR(temp5, temp6)
    
def MUX4WAY16(a, b, c, d, sel):
    ab = MUX16(a, b, sel[1])
    cd = MUX16(c, d, sel[1])
    return MUX16(ab, cd, sel[0])

def MUX8WAY16(a, b, c, d, e, f, g, h, sel):
    ab = MUX16(a, b, sel[2])
    cd = MUX16(c, d, sel[2])
    ef = MUX16(e, f, sel[2])
    gh = MUX16(g, h, sel[2])
    abcd = MUX16(ab, cd, sel[1])
    efgh = MUX16(ef, gh, sel[1])
    return MUX16(abcd, efgh, sel[0])
    
def DMUX4WAY(a, sel):
    out1, out2 = DMUX(a, sel[0])
    out1a, out1b = DMUX(out1, sel[1])
    out2a, out2b = DMUX(out2, sel[1])
    return out1a, out1b, out2a, out2b
    
def DMUX8WAY(a, sel):
    out1, out2 = DMUX(a, sel[0])
    out1a, out1b = DMUX(out1, sel[1])
    out2a, out2b = DMUX(out2, sel[1])
    out1aa, out1ab = DMUX(out1a, sel[2])
    out1ba, out1bb = DMUX(out1b, sel[2])
    out2aa, out2ab = DMUX(out2a, sel[2])
    out2ba, out2bb = DMUX(out2b, sel[2])
    return out1aa, out1ab, out1ba, out1bb, out2aa, out2ab, out2ba, out2bb
    
# Menu de seleccion 

def menu():
    print("\nMenú de compuertas lógicas:")
    print("1. NAND")
    print("2. NOT")
    print("3. AND")
    print("4. OR")
    print("5. XOR")
    print("6. MUX")
    print("7. DMUX")
    print("8. NOT16")
    print("9. AND16")
    print("10. OR16")
    print("11. MUX16")
    print("12. OR8WAY")
    print("13. MUX4WAY16")
    print("14. MUX8WAY16")
    print("15. DMUX4WAY")
    print("16. DMUX8WAY")
    print("0. Salir")
    return int(input("Selecciona una opción: "))
    
# main

def main():
    while True:
        opcion = menu()
        
        if opcion == 0:
            print("Saliendo del programa...")
            break
        elif opcion == 1:
            a = int(input("Entrada A: "))
            b = int(input("Entrada B: "))
            print("Resultado NAND:", NAND(a, b))
        elif opcion == 2:
            a = int(input("Entrada A: "))
            print("Resultado NOT:", NOT(a))
        elif opcion == 3:
            a = int(input("Entrada A: "))
            b = int(input("Entrada B: "))
            print("Resultado AND:", AND(a, b))
        elif opcion == 4:
            a = int(input("Entrada A: "))
            b = int(input("Entrada B: "))
            print("Resultado OR:", OR(a, b))
        elif opcion == 5:
            a = int(input("Entrada A: "))
            b = int(input("Entrada B: "))
            print("Resultado XOR:", XOR(a, b))
        elif opcion == 6:
            a = int(input("Entrada A: "))
            b = int(input("Entrada B: "))
            sel = int(input("Entrada de selección: "))
            print("Resultado MUX:", MUX(a, b, sel))
        elif opcion == 7:
            a = int(input("Entrada A: "))
            sel = int(input("Entrada de selección: "))
            out1, out2 = DMUX(a, sel)
            print("Resultado DMUX: out1 =", out1, ", out2 =", out2)
        elif opcion == 8:
            a = [int(x) for x in input("Entrada A (16 bits, separados por espacio): ").split()]
            print("Resultado NOT16:", NOT16(a))
        elif opcion == 9:
            a = [int(x) for x in input("Entrada A (16 bits, separados por espacio): ").split()]
            b = [int(x) for x in input("Entrada B (16 bits, separados por espacio): ").split()]
            print("Resultado AND16:", AND16(a, b))
        elif opcion == 10:
            a = [int(x) for x in input("Entrada A (16 bits, separados por espacio): ").split()]
            b = [int(x) for x in input("Entrada B (16 bits, separados por espacio): ").split()]
            print("Resultado OR16:", OR16(a, b))
        elif opcion == 11:
            a = [int(x) for x in input("Entrada A (16 bits, separados por espacio): ").split()]
            b = [int(x) for x in input("Entrada B (16 bits, separados por espacio): ").split()]
            sel = int(input("Entrada de selección: "))
            print("Resultado MUX16:", MUX16(a, b, sel))
        elif opcion == 12:
            inputs = [int(x) for x in input("Entradas (8 bits, separados por espacio): ").split()]
            print("Resultado OR8WAY:", OR8WAY(inputs))
        elif opcion == 13:
            a = [int(x) for x in input("Entrada A (16 bits, separados por espacio): ").split()]
            b = [int(x) for x in input("Entrada B (16 bits, separados por espacio): ").split()]
            c = [int(x) for x in input("Entrada C (16 bits, separados por espacio): ").split()]
            d = [int(x) for x in input("Entrada D (16 bits, separados por espacio): ").split()]
            sel = [int(x) for x in input("Entradas de selección (2 bits, separados por espacio): ").split()]
            print("Resultado MUX4WAY16:", MUX4WAY16(a, b, c, d, sel))
        elif opcion == 14:
            a = [int(x) for x in input("Entrada A (16 bits, separados por espacio): ").split()]
            b = [int(x) for x in input("Entrada B (16 bits, separados por espacio): ").split()]
            c = [int(x) for x in input("Entrada C (16 bits, separados por espacio): ").split()]
            d = [int(x) for x in input("Entrada D (16 bits, separados por espacio): ").split()]
            e = [int(x) for x in input("Entrada E (16 bits, separados por espacio): ").split()]
            f = [int(x) for x in input("Entrada F (16 bits, separados por espacio): ").split()]
            g = [int(x) for x in input("Entrada G (16 bits, separados por espacio): ").split()]
            h = [int(x) for x in input("Entrada H (16 bits, separados por espacio): ").split()]
            sel = [int(x) for x in input("Entradas de selección (3 bits, separados por espacio): ").split()]
            print("Resultado MUX8WAY16:", MUX8WAY16(a, b, c, d, e, f, g, h, sel))
        elif opcion == 15:
            a = int(input("Entrada A: "))
            sel = [int(x) for x in input("Entradas de selección (2 bits, separados por espacio): ").split()]
            out1, out2, out3, out4 = DMUX4WAY(a, sel)
            print("Resultado DMUX4WAY: out1 =", out1, ", out2 =", out2, ", out3 =", out3, ", out4 =", out4)
        elif opcion == 16:
            a = int(input("Entrada A: "))
            sel = [int(x) for x in input("Entradas de selección (3 bits, separados por espacio): ").split()]
            out1, out2, out3, out4, out5, out6, out7, out8 = DMUX8WAY(a, sel)
            print("Resultado DMUX8WAY: out1 =", out1, ", out2 =", out2, ", out3 =", out3, ", out4 =", out4, ", out5 =", out5, ", out6 =", out6, ", out7 =", out7, ", out8 =", out8)
        else:
            print("Opción no válida, intenta de nuevo.")
        
        input()
    
main()

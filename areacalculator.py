import math
ch='y'
while ch=='y' or ch=='Y':
    print("Menu for Calcultors.")
    print("1.For normal Calculator.")
    print("2.For area and perimeter Calculator.")
    print("3.For surface area and volume Calculator.")
    cal=input("Enter a number from the above menu: ")
    if cal == '1':
        n1 = float(input('Enter the first number: '))
        print('You can use the following operations. +, -, /(For quotient in decimal), //(For quotient without decimal), *, **(Exponential), sqrt, sin, cos, tan, cot, sec, cosec.')
        op = input('Enter the operation you wish to use: ')
        if op == '+':
            n2 = float(input('Enter the second number: '))
            ans = n1 + n2
            print('The sum of', n1, 'and', n2, 'is', ans)
        elif op == '-':
            n2 = float(input('Enter the second number: '))
            ans = n1 - n2
            print('The difference of', n1, 'and', n2, 'is', ans)
        elif op == '*':
            n2 = float(input('Enter the second number: '))
            ans = n1 * n2
            print('The product of', n1, 'and', n2, 'is', ans)
        elif op == '/':
            n2 = float(input('Enter the second number: '))
            ans = n1 / n2
            print('The quotient of', n1, 'and', n2, 'is', ans)
        elif op == '//':
            n2 = float(input('Enter the second number: '))
            ans = n1 // n2
            print('The quotient of', n1, 'and', n2, 'is', ans)
        elif op == '':
            n2 = float(input('Enter the second number: '))
            ans = n1 ** n2
            print(n1, 'raised to the power', n2, 'is', ans)
        elif op == 'sqrt':
            ans = math.sqrt(n1)
            print('Square root of', n1, 'is', ans)
        elif op == 'sin':
            a = math.radians(n1)
            ans = math.sin(a)
            print('sin', n1, 'is', ans)
        elif op == 'cos':
            a = math.radians(n1)
            ans = math.cos(a)
            print('cos', n1, 'is', ans)
        elif op == 'tan':
            a = math.radians(n1)
            ans = math.tan(a)
            print('tan', n1, 'is', ans)
        elif op == 'cot':
            a = math.radians(n1)
            ans = 1/(math.tan(a))
            print('cot', n1, 'is', ans)
        elif op == 'sec':
            a = math.radians(n1)
            ans = 1/(math.cos(a))
            print('sec', n1, 'is', ans)
        elif op == 'cosec':
            a = math.radians(n1)
            ans = 1/(math.sin(a))                
            print('cosec', n1, 'is', ans)
        else:
            print("Operator not present here!!!")
    elif cal=='2':
        print("Menu or shapes.")
        print("1.Square")
        print("2.Rect5angle")
        print("3.Triangle")
        print("4.Circle")
        print("5.Parallelogram")
        shp=int(input("Enter the number of a shape from the above menu: "))
        if shp==1:
            r=int(input("Enter side of square (in m): "))
            perimeter=4*r
            area=r*r
            print('Area of square is: ' ,area, 'metre square')
            print('Perimeter of square is: ' ,perimeter, 'metre')
        elif shp==2:
            l=int(input("Enter length of rectangle (in m): "))
            b=int(input("Enter breadth of rectangle (in m): "))
            perimeter=2*(l+b)
            area=l*b
            print('Area of rectangle is: ' ,area, 'metre square')
            print('Perimeter of rectangle is: ' ,perimeter, 'metre')
        elif shp==3:
            h=int(input("Enter height of triangle (in m): "))
            b=int(input("Enter base(first side) of triangle (in m): "))
            s=int(input("Enter second side of triangle (in m): "))
            t=int(input("Enter third side of triangle (in m): "))
            perimeter=s+t+b
            area=(1/2)*b*h
            print('Area of traingle is: ' ,area, 'metre square')
            print('Perimeter of triangle is: ' ,perimeter, 'metre')
        elif shp==4:
            r=int(input("Enter radius of circle (in m): "))
            perimeter=2*(math.pi)*r
            area=r*r*(math.pi)
            print('Area of circle is: ' ,area, 'metre square')
            print('Perimeter of circle is: ' ,perimeter, 'metre')
        elif shp==5:
            b=int(input("Enter base(first side) of parallelogram (in m): "))
            a=int(input("Enter second side of parallelogram (in m): "))
            h=int(input("Enter height of parallelogram (in m): "))
            perimeter=2*(a+b)
            area=b*h
            print('Area of parallelogram is: ' ,area, 'metre square')
            print('Perimeter of parallelogram is: ',perimeter, 'metre')
        else:
            print("Please enter a number from the above menu.")
    elif cal=='3':
        print("Menu for 3-D shapes.")
        print("1.Cube")
        print("2.Cuboid")
        print("3.Cone")
        print("4.Sphere")
        print("5.Cylinder")
        k=int(input("Choose a 3-D shape from type above menu: "))
        if k==1:
            f=float(input("Enter length of side of cube: "))
            surf=6*f*f
            vol=f**3
            print("Total Surface Area and Volume of Cube is: ", surf, 'square metre and', vol, 'cubic metre')
        elif k==2:
            l=float(input("Enter length of side of cuboid (in m): "))
            b=float(input("Enter breadth of side of cuboid (in m): "))
            h=float(input("Enter height of side of cuboid (in m): "))
            surf=2*(l*b+b*h+l*h)
            vol=l*b*h
            print("Total Surface Area and Volume of Cuboid is: ", surf, 'square metre and', vol, 'cubic metre')
        elif k==3:
            r=float(input("Enter radius of cone (in m): "))
            h=float(input("Enter height of cone (in m): "))
            l=math.sqrt((r*2+h*2))
            surf=math.pi*r*(l+r)
            vol=(1/3)*math.pi*(r**2)*h
            print("Total Surface Area and Volume of Cone is: ", surf, 'square metre and', vol, 'cubic metre')
        elif k==4:
            r=float(input("Enter radius of sphere (in m): "))
            surf=4*math.pi*(r**2)
            vol=(4/3)*math.pi*(r**3)
            print("Total Surface Area and Volume of Sphere is: ", surf, 'square metre and', vol, 'cubic metre')
        elif k==5:
            r=float(input("Enter radius of cylinder (in m): "))
            h=float(input("Enter height of cylinder (in m): "))
            surf=2*math.pi*r*(h+r)
            vol=math.pi*(r**2)*h
            print("Total Surface Area and Volume of Cylinder is: ", surf, 'square metre and', vol, 'cubic metre')
        else:
            print("Please enter a number from the above menu.")
    else:
        print("Please enter a number from the above menu.")
    ch=input("Do you want to continue (y/n): ")
    if ch=='n' or ch=='N':
        print("Thank you for using our program")
        break

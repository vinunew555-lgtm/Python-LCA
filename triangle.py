def triangle():
    s1=int(input("enter the length of the first side"))
    s2=int(input("enter the length of the second side"))
    s3=int(input("enter the length of the third side"))

    if  s1==s2 and s2==s3:
       print("the triangle is an equilatral triangle")

    elif s1==s2 or s2==s3 or s1==s3:
        print("the triangle is an isosceles triangle")

    else:
        print("the triangle is a scalene triangle")




triangle()
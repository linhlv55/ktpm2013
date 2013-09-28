def checkTriangle(a, b, c):  #a,b,c kieu float
    if (  a*a == (b*b + c*c) or b*b == (a*a + c*c) or c*c == (a*a + b*b )):
        check1 = 1
    else :
        check1 = 0
    if (a==b or a==c or b==c):
        check2 = 1
    else :
        check2 = 0
    if( a<=0 or b<=0 or c<=0 or a> 10**38 or b >  10**38 or c>10 **38 ):
        return -1 # dữ liệu không hợp lệ
    elif( a+b < c or b+c < a or a+c < b):
        return 0 # không phải 3 cạnh của tam giác
    elif( a==b and b==c):
        return 1 # tam giác đều
    elif( check1 == 1 and check2 == 1):
        return 2 # tam giác vuông cân
    elif(check1 == 1 and check2 == 0 ) :
        return 3 # tam giác vuông
    elif ( check1 == 0 and check2 == 1):
        return 4 # tam giac cân
    else :
        return 5 # tam giác thường

               

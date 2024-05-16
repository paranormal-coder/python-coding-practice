print("\npattern 1 ")
"""Printing pattern
* * * * *
* * * * *
* * * * *
* * * * *
* * * * * """
for i in range (0,5):
    for j in range(0,5):
        print("*", end = " ")
    print( )

print("\npattern 2 ")

"""Printing pattern
* * * * *
* * * * 
* * * 
* * 
*  """
for i in range (0,5):
    for j in range(5-i):
        print("*", end = " ")  
    print( )

print("\npattern 3 ")
"""Printing pattern
* 
* * 
* * * 
* * * * 
* * * * * """
for i in range (0,5):
    for j in range(i+1):
        print("*", end = " ")  
    print( )

print("\npattern 4")
"""Printing pattern
    *
   * *
  * * *
 * * * *
* * * * *
"""
for i in range(0,5):
    for j in range(5-i-1):
        print(end = " ")
    for j in range(0,i+1):
        print("*", end = " ")
    print( )


print("\npattern 5")
"""Printing pattern
* * * * *
 * * * *
  * * *
   * * 
    *
 """
for i in range(0,5):
    for j in range(0, i+1):
        print(end = " ")
    for j in range(0,5-i):
        print("*",end = " ")
    print(" ")

print("\npattern 6")
"""Printing pattern
         *
        * *
       * * *
      * * * *
     * * * * *
    * * * * * *
   * * * * * * *
  * * * * * * * *
 * * * * * * * * *
* * * * * * * * * *
 * * * * * * * * *
  * * * * * * * *
   * * * * * * *
    * * * * * *
     * * * * *
      * * * * 
       * * *
        * *
         *
 """
x =10
for i in range(0,x):
    print(" "*(x-i-1)+ "* "*(i+1))
for j in range(x-1, 0, -1):
    print(" "*(x-j)+ "* "*(j))

print("\npattern 7")
"""* * * * *
 * * * *
  * * *
   * * 
    *
   * *
  * * *
 * * * *
* * * * *"""
for i in range(0,5):
    print(" "*i + "* "*(5-i))
for j in range(4,0,-1):
    print(" "*(j-1) + "* "*(5-j+1))

print("\npattern 8")
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5  """
for i in range(0,5):
    for j in range(0,i+1):
        print(j+1, end=" ")
    print()

print("\npattern 9")
"""
1 2 3 4 5 6
1 2 2 3 4 5
1 2 3 2 3 4
1 2 3 4 2 3
1 2 3 4 5 2
"""

for i in range(0,5):
    for j in range(0,i+1):
        print(j+1, end=" ")
    for p in range(0,5-i):
        print(p+2,end= " ")
    print()

print("\npattern 10")
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
for i in range(0,5):
    for j in range(0,i+1):
        print(j+1, end=" ")
    print()
for i in range(0,5):
    for p in range(0,5-i-1):
        print(p+1,end= " ")
    print()

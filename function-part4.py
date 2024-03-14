# WRITE A PYTHON FUNCTION CALLED MAX_NUM() TO FIND THE MAXIMUM OF THREE NUMBERS

def max_num(a, b, c):
  return max(a, b, c)

print (max_num(3, 5, 2))
print (max_num(1, 2, 3))

# WRITE A PYTHON FUNCTION CALLED MULT_LIST() TO MULTIPLY ALL THE NUMBERS IN A LIST

def mult_list(lst):
  result = 1
  for num in lst:
    result *= num
  return result

print(mult_list([2, 3, 4]))
print(mult_list([1, 2, 3]))

# WRITE A PYTHON FUNCTION CALLED REV_STRING() TO REVERSE A STRING

def rev_string(string):
  return string[::-1]

print(rev_string("cat"))  

# WRITE A PYTHON FUNCTION CALLED NUM_WITHIN() TO CHECK WHETHER A NUMBER FALLS IN A GIVEN RANGE. THE FUNCTION ACCEPTS THE NUMBER, BEGINNING OF RANGE, AND END OF RANGE (INCLUSIVE) AS ARGUMENTS. EXAMPLE: NUM_WITHIN(3,2,4) RETURNS TRUE, NUM_WITHIN(3,1,3) RETURNS TRUE, NUM_WITHIN(10,2,5) RETURNS FALSE

def num_within(num, start, end) :
  return start <=num <=end

print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))

# WRITE A PYTHON FUNCTION CALLED PASCAL() THAT PRINTS OUT THE FIRST n ROWS OF PASCAL'S TRIANGLE. THE FUNCTION ACCEPTS THE NUMBER n, THE NUMBER OF ROWS TO PRINT. NOTE: PASCAL'S TRIANGLE IS AN ARITHMETIC AND GEOMETRIC FIGURE FIRST IMAGINED BY BLAISE PASCAL. EACH NUMBER IS THE TWO NUMBERS ABOVE IT ADDED TOGETHER.
  
def pascal(n):
    for line in range(1, n + 1):
        num = 1
        for i in range(1, line + 1):
            print(num, end=" ")
            num = num * (line - i) // i
        print()

pascal(10)
pascal(6)  



# Program to find the number of zero bits and one bits present in a number

#Function taking our number as input
def numberOfBits(n):
  ones = 0
  zeroes= 0

  #While our number is greater than xero check last bit and right shift
  while (n):

      # Use AND operator to check if last bit is 0 or 1
      if (n & 1 == 1):
          ones += 1
      else:
          zeroes += 1
      # Right shift the number removethe last bit that we just checked above 
      n >>= 1
  print("\n\nOnes: ", ones, "\nZeroes: ", zeroes)

number = int(input("Enter your number: "))
numberOfBits(number)
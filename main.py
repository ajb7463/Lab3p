# Author:
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 
# Breakout:

def sum_n(n):
  n = int(n)
  
  if(n==1):
    return(1)
  elif(n==0):
    return(0)
  elif(n>1):
   return(n+sum_n(n-1))
  else:
   return(0)

def print_n(s,n):
  n = int(n)
  if(n>=1):
    n = n-1
    print(s)
    print_n(s,n)
  else:
    return()

def run():
  n = input("Enter an int: ")
  print(f"sum is {sum_n(n)}.")
  s = input("Enter a string: ")
  print_n(s,n)

if __name__ == "__main__":
  run()
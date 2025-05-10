def main():
  #Ask the user: What is your name?
  name = input("What is your name? ")

  #Display how many characters the name contains
  print(len(name))

  #Convert the name to uppercase letters
  name = name.upper()

  #Display the "lowest" character in the name
  print(min(name))


if __name__ == "__main__":
  main()

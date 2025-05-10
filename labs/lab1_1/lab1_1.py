
def main():
  x = int(input("x: "))
  y = int(input("y: "))
  sum = x + y

  print(f"Sum: {float(sum) if isinstance(sum, float) else sum}")


if __name__ == "__main__":
  main()

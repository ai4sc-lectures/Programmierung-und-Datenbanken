# Übung 5.1 - Debugging

Gegeben ist ein Taschenrechner-Programm, welches fehlerhaften Code beinhaltet.
In dieser Übung sollen diese Fehler im Code gefunden und verbessert werden. Führe dazu den Code aus und achte auf Fehlermeldungen. Kommst du nicht weiter, versuche den Debugger zu nutzen um den Code Schritt-für-Schritt zu durchlaufen.

Tipp: Versuche den Taschenrechner erst per eigener Nutzereingaben zu testen anstatt direkt den replit-Tests zu folgen - beim händischen Ausprobieren kann man Abläufe methodisch verfolgen, anstatt direkt mit einem Endergebnis konfrontiert zu sein.

## Vorgegebener Code

```python
# A simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return y - x

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(y, x):
    try:
      z = x // y
    except ZeroDivisionError:
      return None
    return z

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice : input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4')
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

      elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if the answer is no
        nextcalculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")

  ```
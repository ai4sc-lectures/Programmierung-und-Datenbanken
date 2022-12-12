# Musterlösung

**Fehlerauflistung:**

* subtract()-Funktion hat vertauschte Variablen in der Subtraktion
* divide()-Funktion hat vertauschte Argumente
* In Zeile 32 wird ein : anstatt ein = genutzt
* In Zeile 35 fehlt ein Doppelpunkt
* Zeile 42 hat eine falsche Einrückung
* nextcalculation in Zeile 53 sollte next_calculation
* In Zeile 31 wird eine integer-Division statt einer float-Division ausgeführt

**Korrektes Programm:**

```python
# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    try:
      z = x / y
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
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
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
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
```
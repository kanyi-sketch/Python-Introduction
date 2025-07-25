num1 = input("enter a num: ") 
num2 = input("enter a num: ")

print("1.Add")
print("2.Divide")
print("3.Subtract")
print("4.Multiply")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print(f"{num1} + {num2}") 
elif choice == '2':
    print(f"{num1} - {num2}")
elif choice == '3':
    print(f"{num1} * {num2}")
elif choice == '4':
    print(f"{num1} / {num2}")
else:
    print("Invalid option.")
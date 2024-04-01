import matplotlib.pyplot as plt
import numpy as np

# Read data from "data2.txt"
with open("data2.txt", "r") as file:
    data = file.read().splitlines()  # Read the entire file (data2.txt) content and split it by newline
numbers_list = [int(num) for num in data] #Convert the content of the file (String -> int)

def equation_1():
    return [x ** 2 + 7 * x + 2 for x in numbers_list]

def equation_2():
    return [3 * x + 2 for x in numbers_list]

def equation_3():
    return [x ** 2 for x in numbers_list]

def equation_4():
    return [x ** 3 for x in numbers_list]

def equation_5():
    return [x ** 5 for x in numbers_list]

def equation_6():
    return [x ** 3 + 2 * x ** 2 + x + 10 for x in numbers_list]

def equation_7():
    return [x ** 4 - 3 * x ** 3 + 2 * x ** 2 - x + 11 for x in numbers_list]

def equation_8():
    return [np.sin(x) for x in numbers_list]

def equation_9():
    return [np.cos(x) for x in numbers_list]

def equation_10():
    return [x ** 5 + 4 * x ** 4 + x ** 3 - 2 * x ** 2 + 100 for x in numbers_list]

#Use dictionary for easy access
equations = {
    1: equation_1,
    2: equation_2,
    3: equation_3,
    4: equation_4,
    5: equation_5,
    6: equation_6,
    7: equation_7,
    8: equation_8,
    9: equation_9,
    10: equation_10
}

colors = ['red', 'green', 'blue', 'orange', 'silver', 'yellow', 'pink', 'black', 'gray', 'brown']

# Write the results of the equations to 'all_results.txt'
with open("all_results.txt", "w") as result_file:
    for eq_num, equation in equations.items():
        results = equation()
        result_file.write(f"Problem {eq_num}: {results}\n")

# Plot graphs
while True:
    problem_number = int(input("1.) x^2 + 7x + 2\n" + "2.) 3x + 2\n" + "3.)  x^2\n" + "4.) x^3\n" + "5.)  x^5\n" +
                               "6.) x^3 + 2x^2 + x + 10\n" + "7.) x^4 - 3x^3 + 2x^2 + 100\n" + "8.) sin(x)\n" + "9.) cos(x)\n" + "10.) x^5 + 4x^4 + x^3 - 2x^2 + 100\n" +
                               "\nEnter the problem number (1-10) or 11 to combine all graphs: "))
    if problem_number == 11:
        plt.figure(figsize=(12, 8)) # (12 inches wide, 8 inches tall)
        for i, (eq_num, equation) in enumerate(equations.items()): #This iterates over the equations dictionary using enumerate(), which provides both the index i and the key-value pair (eq_num, equation)
            plt.plot(numbers_list, equation(), colors[i % len(colors)], label=f"Problem {eq_num}")
        plt.ylabel('Result')
        plt.xlabel('Data')
        plt.legend(loc='best')
        plt.grid(True, color="grey", linewidth="1.5", linestyle="--")  # Add grid line
        plt.show()
    elif problem_number in equations:
        plt.figure(figsize=(10, 6))
        plt.plot(numbers_list, equations[problem_number](), colors[(problem_number - 1) % len(colors)], label=f"Problem {problem_number}")

        plt.ylabel('Result')
        plt.xlabel('Data')
        plt.legend(loc='best')
        plt.grid(True, color="grey", linewidth="1.5", linestyle="--")  # Add grid line
        plt.show()
    else:
        print("Invalid input. Please enter a number between 1 and 11.")
        continue

    another_graph = input("Do you want to view another graph? (yes/no): ")
    if another_graph.lower() != 'yes':
        break
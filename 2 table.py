# Open a file for writing
with open('table_of_2.txt', 'w') as file:
    i = 1
    product = 2
    while i <= 10:
        file.write(f"{i} x 2 = {product}\n")
        i += 1
        product = 2 * i

# Print
print("Table of 2 written to file 'table_of_2.txt'")
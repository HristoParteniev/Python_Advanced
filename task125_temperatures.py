""" Function checking value"""
def is_number(string):
    """ Checking if number is value is valid temperature"""
    try:
        float(string)
        return True
    except ValueError:
        return False


"""prompting user for absolute file path"""
file_location = input("Please insert 'temperatures.txt' file path.")

# actual location: C:\Users\Hristo.Parteniev\OneDrive - Adastra, s.r.o\Desktop\temperatures.txt
source_values = []
convert_values = []

try:
    # Example:with open('C:\\Users\\Hristo.Parteniev\
    # \OneDrive - Adastra, s.r.o\\Desktop\\temperatures.txt', 'r') as f:
    with open(file_location, 'r', encoding="utf-8") as f:
        source_values = f.readlines()
except FileNotFoundError as e:
    print("Wrong or not existing file/filepath.")


for x in source_values:
    x = x.strip("\n")
    for char in x:
        if char == " ":
            x = x.replace(" ","")
    y = x[:-1]
    if x != "" and is_number(y) is True:
        if x[-1] == "F":
            convert_values.append(x)
        elif x[-1] == "C":
            value = x[:-1]
            # formula:  (x°C × 9/5) + 32 = y°F
            f_conv_val = round(float(value) * 9/5 + 32, 2)
            f_string = f"{f_conv_val}F"
            convert_values.append(f_string)
    else:
        print(f"'{x}' is not in the correct format and has been omitted.")
        continue

with open('F_temperatures.txt', 'w', encoding="utf-8") as final_file:
    for x in convert_values:
        final_file.write(f"{x}\n")

"""Input values used:
12$C
aaaaaasd123F
FFASDa$$#@#C
    a     s        d  C
a s  d  F
                 
10.55 F
11.1F

0C
-12.89C
12.44C
123.777C
124.105F
23.105C
4234.0C
5.99999C
4356.909C
456C
7.54321C
-565.99F
20.101C
43F
34C
34F
 """

values = []
my_file = open('shampoo_sales_.txt', 'r')

def my_fun(values):
    sum = 0;
    for i in range(len(values)):
        sum += values[i]
    return sum

for line in my_file:
    elements = line.split(',')
    
    if elements [0] != 'Date':
        date  = elements [0]
        value = elements [1]

        values.append(float(value))
        
        my_fun(values)

print("Somma: {}" .format (my_fun(values)) )
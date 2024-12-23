
"""

Filename: Spike_and_burst_of_neuron_graph.py
Name: Khang Ly 
Description: 
    This script runs a specific initial condition through sets of loops with 
    specific parameters to generate the spiking and bursting behavior of neuron. 

"""

import matplotlib.pyplot as plt 

# Set the value of parameters a & b 
a = 6
o = -0.1
u = 0.001
 

X = []
Y = []

# x and y are initial conditions 

x = -1.2
y = -3.93

def nonlinear_function(a,x,y):
    if x <= 0:
        return (a / (1-x)) + y
    elif x < (a+y):
        return (a+y)
    else:
        return -1 

for n in range(2000):       # Get rid of transient 
    print(n,x,y)
    x1 = nonlinear_function(a, x, y)
    y1 = y - u*(x+1) + (u*o)
    
    x = x1
    y = y1

for n in range(4000):
    print(n,x,y)
    x1 = nonlinear_function(a, x, y)
    y1 = y - u*(x+1) + (u*o)
    
    X.append(x1)
    Y.append(y1)
    
    x = x1
    y = y1

fig, (ax1) = plt.subplots(1, 1, figsize=(16, 9))
                               #sharex=True)
ax1.plot(Y,X)

# Increase the size of tick labels on both x and y axes
plt.xticks(fontsize=25)  # Adjust the fontsize as needed
plt.yticks(fontsize=25)  # Adjust the fontsize as needed

# Adding labels and title
plt.xlabel('y', fontsize=25)  # Adjust the fontsize as needed
plt.ylabel('x', fontsize=25)  # Adjust the fontsize as needed
plt.title('Spike and Burst of neuron', fontsize=30)  # Adjust the fontsize as needed

plt.legend(fontsize = 25) # Adjust the fontsize as needed 



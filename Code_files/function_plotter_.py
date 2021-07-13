import matplotlib.pyplot as plt
import numpy as np


def f(function,val):
    x=val
    return eval(function.replace('^','**'))

def plot(function,min,max):
    x_axis=np.linspace(min,max,num=50)
    y_axis=f(function,x_axis)

    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('plotted x and y values')
    plt.legend(['line 1'])

    # save the figure
    plt.plot(x_axis,y_axis)
    plt.savefig('Code_files/graphs/graph.png', dpi=80, bbox_inches='tight')




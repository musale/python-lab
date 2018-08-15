'''Gradient descent.'''
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib import pyplot as plt


def load_file(src):
    '''loads the population_vs_profit text file data.'''
    with open(src, encoding='utf-8', mode='r') as f:
        data_set = f.readlines()
    data = [data.strip().split(',') for data in data_set]
    return data


def get_xs(data):
    '''Get the x points in a data set.'''
    return [float(d[0]) for d in data]


def get_ys(data):
    '''Get the y points in a data set.'''
    return [float(d[1]) for d in data]


def linear_regression(data, iterations=1000, alpha=.0001):
    '''Plot the data in a scatter plot diagram.'''
    x_points = get_xs(data)
    y_points = get_ys(data)
    m, c = 0.0, 0.0
    r = range_x(data)
    for i in range(iterations):
        dm, dc = gradient(data, m=m, c=c)
        print(f'gradient(m={m},c={c} = {[dm, dc]}')
        m += -dm * alpha
        c += -dc * alpha

    print(f'cost at compute_cost(m={m},c={c}) = {compute_cost(data, m, c)} r = {r}')
    plt.plot(x_points, y_points, 'r+')
    plt.plot(r, [r[0]*m+c, r[1]*m+c])
    plt.xlabel('Population')
    plt.ylabel('Profit')
    plt.show()


def compute_cost(data, m=0, c=0):
    '''Calculate the sum of errors.'''
    cost = 0.0
    for d in data:
        x, y = float(d[0]), float(d[1])
        y_diff = (y - (m*x + c))**2
        cost += y_diff
    return cost / len(data)


def gradient(data, m, c):
    '''Calculate the gradient.'''
    N = len(data)
    dm, dc = 0.0, 0.0
    for d in data:
        x, y = float(d[0]), float(d[1])
        y_diff = y - (m*x + c)
        dm += -x * y_diff
        dc += -y_diff
    return [2/N * dm, 2/N * dc]


def range_x(data):
    '''Find the min and max xs.'''
    min_x, max_y = min(get_xs(data)), max(get_xs(data))
    return [min_x, max_y]


if __name__ == '__main__':
    data = load_file('population_vs_profit.txt')
    linear_regression(data)

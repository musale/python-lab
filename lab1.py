'''Lab 1.'''
import random
import math
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


def mean(marks):
    '''Get the average mark.'''
    return sum(marks) / len(marks)


def mode(marks):
    '''Get the mode mark in a list of mark.'''
    marks = sorted(marks)
    print(marks)
    center = len(marks) // 2
    if len(marks) % 2 == 0:
        center_marks = marks[center] + marks[center - 1]
        return center_marks / 2
    else:
        return marks[center]


def sample_std(marks):
    '''Get the sample standard deviation of marks.'''
    mean_mark = mean(marks)
    num_total = 0
    for m in marks:
        num_total += (m - mean_mark) ** 2

    return math.sqrt(num_total/(len(marks) - 1))


def variance(marks):
    '''Calculate the variance of the marks.'''
    mean_mark = mean(marks)
    num_total = 0
    for m in marks:
        num_total += (m - mean_mark) ** 2
    return num_total/len(marks)


def plot_sample_vs_variance(marks):
    '''Plot marks against variance.'''
    v = variance(marks)
    print(f'variance = {v}')
    plt.figure()
    ax = plt.axes()
    y = []
    for mark in marks:
        y.append(v)
    x = np.array(marks)
    y = np.array(y)
    ax.plot(x, y, color='yellow')
    plt.xlabel('Marks')
    plt.ylabel('Variance')
    plt.show()


if __name__ == '__main__':
    random.seed(100)
    marks = [random.randint(0, 100) for i in range(100)]
    print(len(marks))
    print(mode(marks))
    print(sample_std(marks))
    plot_sample_vs_variance(marks)

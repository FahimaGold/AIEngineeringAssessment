#--------------------Fahima Mokhtari's assignment----------------------


import numpy as np
import pandas as pd

#Task 0
#This function returns the mean average of an array
def average(array):

    return sum(array)/len(array)

#----------------------Task 1------------------------------
#Internship days
def internship_days(income, travel_costs, rent, other_expenses):
    nb = income // (travel_costs + rent + other_expenses)
    if(nb > 30):
        nb = nb = 30
    return (nb )

#---------------------Task 2-------------------------------
#Coutning payment
def calculate_payment(order):
    total_sum = 0
    for i in order:
        if(i == 'B'):
            total_sum = total_sum + 2.00
        elif(i == 'W'):
            total_sum = total_sum + 2.50
        elif(i == 'S'):
            total_sum = total_sum + 1.50
        else:
            total_sum = total_sum
    return total_sum

#--------------------Task 3-------------------------------
#Returns the max  value of a colum in a given dataframe
def maximum_by(data, col):
    return data[col].max()

#-------------------Task 4--------------------------------
#Kullback-Leibler divergence
def KL(p, q):
    kl = 0.0

    if(sum(p)> 1):
      p = p / sum(p)
    if(sum (q) > 1):
      q = q / sum(q)

    for pi, qi in zip(p, q):
        kl += pi*np.log(pi/qi)

    return kl

#------------------Task 5---------------------------------
#Kullback-Leibler divergence

def diag(size):
    return [(i, i) for i in range(size)]

def is_in_matrix(matrix, pair):
    return 0 <= pair[0] < matrix[0] and 0 <= pair[1] < matrix[1]

def transpose(ray, amount):
    return [(x-amount, y) for (x,y) in ray]

def diagonals(a):
    h = len(a)
    w = len(a[0])
    print("-----")

    b = np.arange(4)
    for offset in reversed(range(-w, h)):

        diagonal = [p for p in transpose(diag(w), offset) if is_in_matrix([h, w], p)]
        if diagonal:


               print("[", end='')
               for x in diagonal:
                   #print(x)
                   print(a[x[0]][x[1]], end='. ')

               print("]")

    if(w !=h):
            print("[", end='')
            print(a[h-1][0], end ='. ')
            print("]", end='.')


#--------------------END---------------------------------



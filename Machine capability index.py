# Author: Jennifer Hayes (Gemini soft)

import math

population = [59.09, 60.1, 60.09, 60.1, 60.09, 60.1] #out of range

#population = [60, 59.8, 59.9, 60.08, 60.09, 60.1] #in range

count = len(population)
sum_v = sum(population)
mean = sum_v / count

#-----------------------------------------------
part_length = 60
tol = 0.15
LSL = part_length - tol
USL = part_length + tol

#-----------------------------------------------

for i in range(count):

    population[i] = (population[i] - mean) ** 2  
    new_pop = sum(population)
    mean_2 = new_pop / count
    #print mean_2
    stdv = math.sqrt(mean_2)
    if i == count - 1:
        print 'Standard Deviation: ', stdv
#-----------------------------------------------
C_m = (USL - LSL) / (6 * stdv)
print 'Cm value: ', C_m

C_lo = (mean - LSL) / (3 * stdv)
print 'Clo value: ', C_lo

C_up = (USL - mean) / (3 * stdv)
print 'Cup value: ', C_up
#------------------------------------------------
if C_lo <= C_up:
    print 'Cmk value: ', C_lo
else:
    print 'Cmk value out of range'
#-----------------------------------------------


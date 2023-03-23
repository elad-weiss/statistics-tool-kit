import numpy

# input

print("Enter experiment result with a space between each result: ")
results = input()
results = results.split(" ")

print("Enter the machine error: ")
machine_error = float(input())

# average

average = 0

for result in results:
    average += float(result)

average = average/len(results)

print("average:", numpy.round(average, 2))

# standard deviation

std_var = 0

for result in results:
    std_var += (float(result) - average)**2

std_var = numpy.sqrt(std_var/(len(results)-1))

print("standard deviation:", numpy.round(std_var, 2))

# statistical error
stat_err = std_var/(numpy.sqrt(len(results)))

print("statistical error:", numpy.round(stat_err, 2))

# total error
tot_err = numpy.sqrt(machine_error**2 + stat_err**2)

print("total error:", numpy.round(tot_err, 2))

# total result
print("TOTAL RESULT:", numpy.round(average, 2),
      "\u00b1", numpy.round(tot_err, 2))

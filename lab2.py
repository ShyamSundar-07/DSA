a=[90,76,7,5,89,300,78,44,22,45]
max=a[0]
min=a[0]
smax=a[0]
smin=a[0]
for i in a:
    if i> max:
        max=i
        if i < min:
            min=i
if smax < max:
    smax=i
if smin >min:
 smin=i
print("Second smallest number is: ",smax)
print("Second largest number is: ",smin) 
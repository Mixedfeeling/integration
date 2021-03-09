
import math
import random
def function(x):
	return 2*x**2+1
low_lim=0
up_lim= 1


def integrate(func,lower_limit,upper_limit,iterate):
	random_lst_x=[lower_limit,upper_limit]
	random_lst_y=[]
	result=0
	for i in range(iterate):
		random_lst_x.append(random.uniform(lower_limit,upper_limit))
	random_lst_x.sort()
	####
	for x in random_lst_x:
		random_lst_y.append(function(x))

	for j in range(len(random_lst_x)-1):
		rectriangle_area=(random_lst_x[j+1]-random_lst_x[j])*(random_lst_y[j])
		triangle_area=((random_lst_x[j+1]-random_lst_x[j])*(random_lst_y[j+1]-random_lst_y[j]))/2
		area=rectriangle_area+triangle_area
		result+=area
	return result

print(integrate(function,low_lim,up_lim,999998))
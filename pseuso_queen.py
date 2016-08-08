# Code to see the expected value of pseudo-queen

import random

def mean(data):
    """Return the sample arithmetic mean of data."""
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    return sum(data)/n # in Python 2 use sum(data)/float(n)

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def pstdev(data):
    """Calculates the population standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/n # the population variance
    return pvar**0.5
# We have to create a random permutation of the girls' qualities standing in a row. 
k_val=[]
i=2
while i<=1000:								#1000 is the number of guls
	k_val.append(i)
	i=i+1
k_max= 2
max_val=0
#val=[]
for k in k_val:
	#print k
	best_list=[]
	iteration=1
	while (iteration<100000):
		queue=[]
		n = 1000				# Number of girls 
		i = 0 
		while (i<n):
			r = random.randint(1,n)
			if r not in queue:
				queue.append(r)
				i=i+1
		#print queue

		# We take different values of k and plot the value of the expected queen we are getting. The best value, which is of the Queen is 10000

		#k = 1000 # We look at the sample of size k 
		best = 0 
		for i in range (0,k):
			#print i,
			if queue[i] > best:
				best = queue[i]

		for i in range(k,n):
			#print i,
			#print 'for'
			if queue[i] > best:
				best = queue[i]
				#print 'best at',i,'=',best
				break
		if best == 1000:
			best= queue[len(queue)-1]
		#print best
		best_list.append(best)
		iteration=iteration+1
	print k,mean(best_list)
	if mean(best_list)>max_val:
		max_k=k
		max_val=mean(best_list)
print max_k
		

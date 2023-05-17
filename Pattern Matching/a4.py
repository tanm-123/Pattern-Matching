import random
import math
#this is helper function time complexity order n and this is used so that space complexity does not exceed te given bounds as in power the value will always be less than q while multiplying
def power(x,n,q):
	p=1
	for i in range(0,n):
		p=(p*(x%q))%q
	return (p)
#To generate random prime less than N
def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

# To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#pattern matching
def randPatternMatch(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatch(q,p,x)
#the time complexity and space complexity will be same as modpattern matching as find N runs in constant time and we have to ignore time of rand prime
#the only difference is that here instead of q, N will be there as q can attain maximum value of N. so logq is of order log(m/eps)
#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)
#the time complexity and space complexity will be same as modpattern matching as find N runs in constant time and we have to ignore time of rand prime
#the only difference is that here instead of q, N will be there as q can attain maximum value of N. so logq is of order log(m/eps)
# return appropriate N that satisfies the error bounds
def findN(eps,m):
	y=m*math.log(26,2)
	return (int(math.pow((2*y/eps),2)))
# this is achieved using the two inequalities given. we know that the hash value of pattern and substring of x is of order 26^m in decimal and so in bits it is of order mlog26 to base 2.
#x!=y but xmodq=ymodq, x is hash value of pattern and y is of substring
#so x-y is divisible by q
#so so x-y can be written as q1,q2,q3....qi--where i can max be log2(x-y)
#x-y is of order mlog26 base 2 in bits and so in decimal is of order 2^mlog26 base 2
#so taking log gives mlog26 base 2
# now eps is upper bound probability that q lies in q1....qi
#eps=mlog26base2/pie(N)
#solving this will give us N/2logN>=mlog26/eps
# Return sorted list of starting indices where p matches x
def modPatternMatch(q,p,x):
	l=[]
	m=len(p)
	n=len(x)
	if n>=m:
		#hash function of p
		f=0
		k=1
		for i in range(m-1,-1,-1):
			f=(f+((ord(p[i])-ord('A'))*k)%q)%q
			k=(k*(26%q))%q
		#hash value of x
		s=0
		k=1
		for i in range(m-1,-1,-1):
			s=(s+((ord(x[i])-ord('A'))*k)%q)%q
			k=(k*(26%q))%q
		if s==f:
			l.append(0)
		t=power(26,m-1,q)
		for i in range (1,n-m+1):
			s=(s-((ord(x[i-1])-ord('A'))*t)%q)%q
			s=(s*(26%q))%q
			s=(s+(ord(x[i+m-1])-ord('A'))%q)%q
			if s==f:
				l.append(i)
	return(l)
#time complexity is order (n+m)logq as we are iterating twice to find hash of pattern and initial hash of substring and everytime we are using mod q so that max can be q.
#space complexity -- list ->k
					#for index i->logn (as maximum value of i can be n-1 )
					#for storing hash value-> logq as maximum can be q only(as we are using mod q and also even if it is more than q then also the order will always be logq) 

# Return sorted list of starting indices where p matches x
def modPatternMatchWildcard(q,p,x):
	l=[]
	m=len(p)
	n=len(x)
	if n>=m:
		#hash function of p
		f=0
		k=1
		for i in range(m-1,-1,-1):
			if p[i]=='?':
				c=i
				k=(k*(26%q))%q
				continue
			f=(f+((ord(p[i])-ord('A'))*k)%q)%q
			k=(k*(26%q))%q
		#rolling hash function of x
		s=0
		k=1
		for i in range(m-1,-1,-1):
			if i==c:
				k=(k*(26%q))%q
				continue
			s=(s+((ord(x[i])-ord('A'))*k)%q)%q
			k=(k*(26%q))%q
		if s==f:
			l.append(0)
		t=power(26,m-c-1,q)
		z=power(26,m-1,q)
		for i in range (1,n-m+1):
			s=(s+((ord(x[i-1+c])-ord('A'))*t)%q)%q
			s=(s-((ord(x[i-1])-ord('A'))*z)%q)%q
			s=(s*(26%q))%q
			s=(s+(ord(x[i+m-1])-ord('A'))%q)%q
			s=(s-((ord(x[i+c])-ord('A'))*t)%q)%q
			if s==f:
				l.append(i)
	return(l)

#time complexity is order (n+m)logq as we are iterating twice to find hash of pattern and initial hash of substring and everytime we are using mod q so that max can be q.
#space complexity -- list ->k
					#for index i->logn (as maximum value of i can be n-1 )
					#for storing hash value-> logq as maximum can be q only(as we are using mod q and also even if it is more than q then also the order will always be logq) 
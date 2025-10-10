from math import comb

a = int(input()) / 100
b = int(input()) / 100

primes = {2, 3, 5, 7, 11, 13, 17}
no_primes = [i for i in range(19) if i not in primes]

# prob = Decimal(0)
# for p in no_primes:
#     for q in no_primes:
#         # print(p, q, comb(45, p)*(a**p)*((1-a)**(45-p)), comb(45, q)*(b**q)*((1-b)**(45-q)))
#         prob += Decimal(comb(45, p)*(a**p)*((1-a)**(45-p))) * Decimal(comb(45, q)*(b**q)*((1-b)**(45-q)))
prob = 0
for p in no_primes:
    for q in no_primes:
        # print(p, q, comb(45, p)*(a**p)*((1-a)**(45-p)), comb(45, q)*(b**q)*((1-b)**(45-q)))
        prob += comb(18, p)*(a**p)*((1-a)**(18-p)) * comb(18, q)*(b**q)*((1-b)**(18-q))
# for p in no_primes:
#     for q in no_primes:
#         prob += comb(45, p)*(a**p)*((1-a)**(45-p)) * comb(45, q)*(b**q)*((1-b)**(45-q))

# let, X~B(45, a), Y~B(45, b) (0<=a,b<=1)
# prob = P(X=i, Y=j) = P(X=i) * P(Y=j) = P(X=i) + P(Y=j) - P(X=i or Y=j)

print(1 - prob)


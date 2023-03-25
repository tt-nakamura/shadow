# derive equations (44)(45)(46)(48)(49)(51)(52) of
#  J. M. Bardeen,
#  "Timelike and Null Geodesics in the Kerr Metric"
#   in Les Houches 1972 summer school lectures

from sympy import symbols,diff,solve,factor

r,a,lam,eta = symbols('r,a,lambda,eta')

Delta = r**2 + a**2 - 2*r # mass = 1
K = eta + (a - lam)**2
R = (r**2 + a**2 - a*lam)**2 - K*Delta

dR = diff(R,r)
s = solve((R, dR), (lam, eta))
t = [s.subs(a,1) for s in s[1]]
print(factor(s))
print(factor(t))

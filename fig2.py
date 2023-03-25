import matplotlib.pyplot as plt
from PlotKerrShadow import PlotKerrShadow

plt.figure(figsize=(5,3.75))

PlotKerrShadow(0.999, color='k')

plt.xlabel(r'$\alpha$  / $M$')
plt.ylabel(r'$\beta$  / $M$')
plt.text(7.3, 4.8, r'$a = 0.999$')
plt.text(7.3, 4, r'$\theta = \pi/2$')
plt.axis('equal')
plt.tight_layout()
plt.savefig('fig2.eps')
plt.show()

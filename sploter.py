import pylab 
import skrf as rf

n = rf.Network('CAKE_22.Dec.2017.11.53.s2p')
pylab.figure(num=1,figsize=(8.9,5),dpi=150)
pylab.title('Cake Pan Feed')
n.frequency.unit = 'GHz'
n.plot_s_db(m=0,n=0,label='Feed S11')
pylab.savefig('cakeFeed.pdf', bbbox_inches='tight')
pylab.show()

n2 = rf.Network('CAV_21.Dec.2017.14.42.s2p')
pylab.figure(num=2,figsize=(8.9,5),dpi=150)
pylab.title('Cavity Filter')
n2.frequency.unit = 'GHz'
n2.plot_s_db(m=1,n=0,label='Cavity  S21')
pylab.savefig('cavityFilter.pdf', bbbox_inches='tight')
pylab.show()

n3 = rf.Network('CAN_22.Dec.2017.11.52.s2p')
pylab.figure(num=2,figsize=(8.9,5),dpi=150)
pylab.title('Horn Waveguide')
n3.frequency.unit = 'GHz'
n3.plot_s_db(m=0,n=0,label='Cavity  S11')
pylab.savefig('hornWaveguide.pdf', bbbox_inches='tight')
pylab.show()

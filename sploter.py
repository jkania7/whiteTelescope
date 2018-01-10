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

n4 = rf.Network('RAS1_22.Dec.2017.12.08.s2p')
pylab.figure(num=2,figsize=(8.9,5),dpi=150)
pylab.title('Radio Astronomy Supplies LNA 1')
n4.frequency.unit = 'GHz'
n4.plot_s_db(m=0,n=1,label='LNA S12')
pylab.savefig('RASLNA1.pdf', bbbox_inches='tight')
pylab.show()

n5 = rf.Network('RAS2_22.Dec.2017.12.13.s2p')
pylab.figure(num=2,figsize=(8.9,5),dpi=150)
pylab.title('Radio Astronomy Supplies LNA 2')
n5.frequency.unit = 'GHz'
n5.plot_s_db(m=0,n=1,label='LNA S12')
pylab.savefig('RASLNA2.pdf', bbbox_inches='tight')
pylab.show()

n6 = rf.Network('CANNEW.s2p')
pylab.figure(num=2,figsize=(8.9,5),dpi=150)
pylab.title('Can New')
n6.frequency.unit = 'GHz'
n6.plot_s_db(m=1,n=1,label='Can S22')
pylab.savefig('canNew.pdf', bbbox_inches='tight')
pylab.show()

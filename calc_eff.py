from math import sqrt
import numpy as np

evtN_var = 'control'
subtract_X, subtract_psi = False, True

file_in_MC_psi = open('/home/yaourt/Study/Bs_resonances/psi_fit_results/psi_MC_evtN.txt', 'r')
file_in_MC_X = open('/home/yaourt/Study/Bs_resonances/X_fit_results/X_MC_evtN.txt', 'r')
file_in_data_psi = open('/home/yaourt/Study/Bs_resonances/psi_fit_results/psi_data_evtN.txt', 'r')
file_in_data_X = open('/home/yaourt/Study/Bs_resonances/X_fit_results/X_data_evtN.txt', 'r')


X_MC_evtN = dict(zip(['Bs', 'phi', 'control'], [map(float, x[:-2].split(' ')) for x in list(file_in_MC_X)]))
psi_MC_evtN = dict(zip(['Bs', 'phi', 'control'], [map(float, x[:-2].split(' ')) for x in list(file_in_MC_psi)]))
X_data_evtN = dict(zip(['1', '2', '3', '4'], [map(float, x[:-2].split(' ')) for x in list(file_in_data_X)]))
psi_data_evtN = dict(zip(['1', '2', '3', '4'], [map(float, x[:-2].split(' ')) for x in list(file_in_data_psi)]))


######
# Bs #

# N_reco_psi = 74899.
# err_N_reco_psi = 307.
# ##
# N_reco_X = 31517.
# err_N_reco_X = 199.


######
# B+ #

# N_reco_psi = 72941.
# err_N_reco_psi = 268.
# ##
# N_reco_X = 29082.
# err_N_reco_X = 196.

N_reco_psi, err_N_reco_psi = map(round, psi_MC_evtN[evtN_var])
N_reco_X, err_N_reco_X = map(round, X_MC_evtN[evtN_var])


#-----------------------------

######
# Bs #

# N_data_psi = 2469.   ##### Numbers from the 14 June talk @LPI group meeting
# err_N_data_psi = 57.
# ##
# N_data_X = 115.   #83 +- 12; 90 +- 12
# err_N_data_X = 12.


# N_data_psi = 2511.    ##### Numbers from the 7 May talk @CMS meeting
# err_N_data_psi = 57.
# ##
# N_data_X = 90.   #83 +- 12; 90 +- 12
# err_N_data_X = 12.

N_data_psi_2, err_N_data_psi_2, N_data_psi_4, err_N_data_psi_4 = map(round,psi_data_evtN['2'] + psi_data_evtN['4'])
N_data_X_2, err_N_data_X_2, N_data_X_4, err_N_data_X_4 = map(round,X_data_evtN['2'] + X_data_evtN['4'])

if subtract_psi:
    N_data_psi, err_N_data_psi = N_data_psi_2 - N_data_psi_4, sqrt(err_N_data_psi_2**2 + err_N_data_psi_4**2)
else:
    N_data_psi, err_N_data_psi = N_data_psi_2, err_N_data_psi_2

if subtract_X:
    N_data_X, err_N_data_X = N_data_X_2 - N_data_X_4, sqrt(err_N_data_X_2**2 + err_N_data_X_4**2)
else:
    N_data_X, err_N_data_X = N_data_X_2, err_N_data_X_2


######
# B+ #

# N_data_psi = 44030. # 45828 +- 216
# err_N_data_psi = 213.
# ##
# N_data_X = 1301.   # 1238 +- 45;
# err_N_data_X = 41.

#-----------------------------

######
# Bs #

DAS_psi = 4033332.
DAS_X   = 2747175.

######
# B+ #

# DAS_psi = 2940939.
# DAS_X   = 2119518.

#-----------------------------

######
# Bs #

eff_filter_psi = 0.0256162397293
err_eff_filter_psi = 0.0004641394136
##
eff_filter_X = 0.0345138639742
err_eff_filter_X = 0.0005844468818

######
# B+ #

# eff_filter_psi = 0.0252452209
# err_eff_filter_psi = 0.0004197452
# ##
# eff_filter_X = 0.0356669123
# err_eff_filter_X = 0.0005628742

#-----------------------------
eff_reco_psi = N_reco_psi / DAS_psi
err_eff_reco_psi = err_N_reco_psi / DAS_psi
##
eff_reco_X = N_reco_X / DAS_X
err_eff_reco_X = err_N_reco_X / DAS_X

#-----------------------------
total_eff_psi = eff_reco_psi * eff_filter_psi
total_eff_X = eff_reco_X * eff_filter_X
err_total_eff_psi = total_eff_psi * sqrt( (err_eff_reco_psi / eff_reco_psi)**2 + (err_eff_filter_psi / eff_filter_psi)**2)
err_total_eff_X = total_eff_X * sqrt( (err_eff_reco_X / eff_reco_X)**2 + (err_eff_filter_X / eff_filter_X)**2)

#-----------------------------
R_eps = total_eff_psi / total_eff_X
R_n = N_data_X / N_data_psi
Rs = R_eps * R_n
err_Rs_stat = Rs * sqrt( (err_N_data_X / N_data_X)**2 + (err_N_data_psi / N_data_psi)**2 )
err_Rs_eff = Rs * sqrt( (err_total_eff_psi / total_eff_psi)**2 + (err_total_eff_X / total_eff_X )**2 )

#-----------------------------
print '\n'
print 'number of events on MC for psi =',  int(N_reco_psi), '+-', int(err_N_reco_psi)
print 'number of events on MC for X =',  int(N_reco_X), '+-', int(err_N_reco_X)
print 'number of events on data for psi =',  int(N_data_psi), '+-', int(err_N_data_psi)
print 'number of events on data for X =',  int(N_data_X), '+-', int(err_N_data_X)
print '\n~~~\nX:\n~~~\n'
print 'number of events for sPlot 1 =',  int(X_data_evtN['1'][0]), '+-', int(X_data_evtN['1'][1])
print 'number of events for sPlot 2 =',  int(X_data_evtN['2'][0]), '+-', int(X_data_evtN['2'][1])
print 'number of events for sPlot 3 =',  int(X_data_evtN['3'][0]), '+-', int(X_data_evtN['3'][1])
print 'number of events for sPlot 4 =',  int(X_data_evtN['4'][0]), '+-', int(X_data_evtN['4'][1])
print '\n~~~~~~~~~\npsi(2S):\n~~~~~~~~~\n'
print 'number of events for sPlot 1 =',  int(psi_data_evtN['1'][0]), '+-', int(psi_data_evtN['1'][1])
print 'number of events for sPlot 2 =',  int(psi_data_evtN['2'][0]), '+-', int(psi_data_evtN['2'][1])
print 'number of events for sPlot 3 =',  int(psi_data_evtN['3'][0]), '+-', int(psi_data_evtN['3'][1])
print 'number of events for sPlot 4 =',  int(psi_data_evtN['4'][0]), '+-', int(psi_data_evtN['4'][1])

print '\nfinal number of events for psi =',  int(N_data_psi), '+-', int(err_N_data_psi)
print 'final number of events for X =',  int(N_data_X), '+-', int(err_N_data_X)

print '\n***********************************\n'


print 'filter efficiency for psi =',  round(eff_filter_psi, 10), '+-', round(err_eff_filter_psi, 10)
print 'filter efficiency for X =',  round(eff_filter_X, 10), '+-', round(err_eff_filter_X, 10)
print '\n'
print 'reco efficiency for psi =',  round(eff_reco_psi, 10), '+-', round(err_eff_reco_psi, 10)
print 'reco efficiency for X =',  round(eff_reco_X, 10), '+-', round(err_eff_reco_X, 10)
print '\n'
print 'total efficiency for psi =',  round(total_eff_psi, 10), '+-', round(err_total_eff_psi, 10)
print 'total efficiency for X =',  round(total_eff_X, 10), '+-', round(err_total_eff_X, 10)
print '\n'
print 'Rs =', round(Rs, 10), '+-', round(err_Rs_stat, 10), '(stat.)', '+-', round(err_Rs_eff, 10), '(eff.)'

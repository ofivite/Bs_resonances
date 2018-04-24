from math import sqrt

N_reco_psi = 73491.
err_N_reco_psi = 306.
##
N_reco_X = 31267.
err_N_reco_X = 202.

#-----------------------------
N_data_psi = 2487.
err_N_data_psi = 54.
##
N_data_X = 83.
err_N_data_X = 12.

#-----------------------------
DAS_psi = 4033332.
DAS_X   = 2747175.

#-----------------------------
eff_filter_psi = 0.0256162397293
err_eff_filter_psi = 0.0004641394136
##
eff_filter_X = 0.0345138639742
err_eff_filter_X = 0.0005844468818

#-----------------------------
eff_reco_psi = N_reco_psi / DAS_psi
err_eff_reco_psi = err_N_reco_psi / DAS_psi
##
eff_reco_X = N_reco_X / DAS_X
err_eff_reco_X = err_N_reco_X / DAS_X

#-----------------------------
total_eff_psi = eff_reco_psi * eff_filter_psi
total_eff_X = eff_reco_X * eff_filter_X
err_total_eff_psi = eff_reco_psi * err_eff_filter_psi + eff_filter_psi * err_eff_reco_psi
err_total_eff_X =eff_reco_X * err_eff_filter_X + eff_filter_X * err_eff_reco_X

#-----------------------------
R_eps = total_eff_psi / total_eff_X
R_n = N_data_X / N_data_psi
Rs = R_eps * R_n
err_Rs = R_eps * ( err_N_data_X / N_data_psi + err_N_data_psi * (N_data_X / N_data_psi**2) ) + R_n * ( err_total_eff_psi / total_eff_X + err_total_eff_X * (total_eff_psi / total_eff_X**2) )

#-----------------------------
print '\n'
print 'filter efficiency for psi =',  round(eff_filter_psi, 10), '+-', round(err_eff_filter_psi, 10)
print 'filter efficiency for X =',  round(eff_filter_X, 10), '+-', round(err_eff_filter_X, 10)
print '\n'
print 'reco efficiency for psi =',  round(eff_reco_psi, 10), '+-', round(err_eff_reco_psi, 10)
print 'reco efficiency for X =',  round(eff_reco_X, 10), '+-', round(err_eff_reco_X, 10)
print '\n'
print 'total efficiency for psi =',  round(total_eff_psi, 10), '+-', round(err_total_eff_psi, 10)
print 'total efficiency for X =',  round(total_eff_X, 10), '+-', round(err_total_eff_X, 10)
print '\n'
print 'Rs =', round(Rs, 10), '+-', round(err_Rs, 10)

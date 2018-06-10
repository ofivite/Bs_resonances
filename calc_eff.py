from math import sqrt

# N_reco_psi = 74899.
# err_N_reco_psi = 307.
# ##
# N_reco_X = 31517.
# err_N_reco_X = 199.

N_reco_psi = 72941.
err_N_reco_psi = 268.
##
N_reco_X = 29082.
err_N_reco_X = 196.

#-----------------------------
# N_data_psi = 2511.
# err_N_data_psi = 57.
# ##
# N_data_X = 90.   #83 +- 12; 90 +- 12
# err_N_data_X = 12.

N_data_psi = 44030. # 45828 +- 216
err_N_data_psi = 213.
##
N_data_X = 1301.   # 1238 +- 45;
err_N_data_X = 41.

#-----------------------------
# DAS_psi = 4033332.
# DAS_X   = 2747175.
DAS_psi = 2940939.
DAS_X   = 2119518.
#-----------------------------
# eff_filter_psi = 0.0256162397293
# err_eff_filter_psi = 0.0004641394136
#
# ##
# eff_filter_X = 0.0345138639742
# err_eff_filter_X = 0.0005844468818

eff_filter_psi = 0.0252452209
err_eff_filter_psi = 0.0004197452
##
eff_filter_X = 0.0356669123
err_eff_filter_X = 0.0005628742

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

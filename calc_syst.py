from math import sqrt

b = 0.057 ## used to be 0.057 for some reason. 0.058 is for the ci 028fc; now it is indeed 0.057, but before it was 0.058 (hmm)
MC_variable = 0.06
MC_stat = b + 0.001  ## rounding ???????? originally 0.0014826768
phi_sig_model = 0.053
phi_bkgr_model = 0.065
Bs_sig_model = 0.056
Bs_bkgr_model = 0.06
Kstar = 0.058
fit_2D = 0.044

syst = sqrt( (b - MC_variable)**2 + (b - MC_stat)**2 + (b - phi_sig_model)**2 + (b - phi_bkgr_model)**2 + (b - Bs_sig_model)**2 + (b - Bs_bkgr_model)**2 + (b - Kstar)**2 + (b - fit_2D)**2)
print syst, syst / b

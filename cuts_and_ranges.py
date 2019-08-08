from MODE import *#MODE
from RooSpace import *#var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp

lrn_discr_data   = [5.27, 5.47, 40] # 5.3669 + 0.1
lrn_discr_MC     = [5.3669 - 0.035, 5.3669 + 0.035, 35]
lrn_phi_data     = {'X': [0.99, 1.055, 13],                    'psi': [1.0195 - 0.030, 1.0195 + 0.030, 30]}
lrn_phi_MC       = {'X': [1.0195 - 0.016, 1.0195 + 0.016, 32], 'psi': [1.0195 - 0.016, 1.0195 + 0.016, 32]}
lrn_control_data = {'X': [3.872 - 0.06, 3.872 + 0.06, 30],     'psi': [3.686 - 0.05, 3.686 + 0.05, 50]}
lrn_control_MC   = {'X': [3.872 - 0.02, 3.872 + 0.02, 40],     'psi': [3.686 - 0.02, 3.686 + 0.02, 40]}

left_jpsi = 3.094 - 0.1; right_jpsi = 3.094 + 0.1; nbins_jpsi = 100
left_discr_data, right_discr_data, nbins_discr_data = lrn_discr_data
left_discr_MC, right_discr_MC, nbins_discr_MC = lrn_discr_MC
left_phi_data, right_phi_data, nbins_phi_data = lrn_phi_data[MODE]
left_phi_MC, right_phi_MC, nbins_phi_MC = lrn_phi_MC[MODE]
left_control_MC, right_control_MC, nbins_control_MC = lrn_control_MC[MODE]
left_control_data, right_control_data, nbins_control_data = lrn_control_data[MODE]

var_discr.setMin(left_discr_data); var_discr.setMax(right_discr_data); var_discr.setBins(nbins_discr_data)
PHI_mass_Cjp.setMin(left_phi_data); PHI_mass_Cjp.setMax(right_phi_data); PHI_mass_Cjp.setBins(nbins_phi_data)
var_control.setMin(left_control_data); var_control.setMax(right_control_data);  var_control.setBins(nbins_control_data)

cuts_Bs_MC = f'{var_discr.GetName()} > {left_discr_MC} && {var_discr.GetName()} < {right_discr_MC}'  # + '&& PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15'
cuts_Bs_data = f'{var_discr.GetName()} > {left_discr_data} && {var_discr.GetName()} < {right_discr_data}'   # + '&& PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15'

cuts_phi_MC = f'{PHI_mass_Cjp.GetName()} > {left_phi_MC} && {PHI_mass_Cjp.GetName()} < {right_phi_MC}'  # TMath::Abs(PHI_mass_Cjp - 1.02)<0.01 &&
cuts_phi_data = f'{PHI_mass_Cjp.GetName()} > {left_phi_data} && {PHI_mass_Cjp.GetName()} < {right_phi_data}'

cuts_control_MC = f'{var_control.GetName()} > {left_control_MC} && {var_control.GetName()} < {right_control_MC}'
cuts_control_data = f'{var_control.GetName()} > {left_control_data} && {var_control.GetName()} < {right_control_data}'

cuts_pipi = {'X': f'{PIPI_mass_Cjp.GetName()} > 0.65 && {PIPI_mass_Cjp.GetName()} < 0.78', 'psi': f'{PIPI_mass_Cjp.GetName()} > 0.4 && {PIPI_mass_Cjp.GetName()} < 0.6'}
cuts_match_dR = 'dR_mup < 0.05 && dR_mum < 0.05 && dR_pip < 0.05 && dR_pim < 0.05 && dR_Kp < 0.05 && dR_Km < 0.05'

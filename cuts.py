mode = 'psi'
refl_ON = True
get_MC_N_evts = False

sPlot_from_1 = 'Bs'; sPlot_from_2 = 'phi';
sPlot_cut = 'control'; sPlot_from = 'Bs'; sPlot_to = 'phi'
if sPlot_from != 'Bs': refl_ON = False
sPlot_from_text = mode if sPlot_from == 'control' else sPlot_from
sPlot_to_text = mode if sPlot_to == 'control' else sPlot_to

refl_line = '_refl' if refl_ON else ''
# gStyle.SetTitleFontSize(.085)

left_discr_data =  5.3669 - 0.2; right_discr_data = 5.3669 + 0.2; nbins_discr_data = 40
left_discr_MC =  5.3669 - 0.035; right_discr_MC = 5.3669 + 0.035; nbins_discr_MC = 35

# lrn_phi_data = {'X': [1.0195 - 0.016, 1.0195 + 0.016, 32], 'psi': [1.0195 - 0.016, 1.0195 + 0.016, 32]}
lrn_phi_data = {'X': [1.0195 - 0.030, 1.0195 + 0.030, 30], 'psi': [1.0195 - 0.030, 1.0195 + 0.030, 30]}
left_phi_data, right_phi_data, nbins_phi_data = lrn_phi_data[mode]

# lrn_phi_MC = {'X': [1.0195 - 0.016, 1.0195 + 0.016, 32], 'psi': [1.0195 - 0.0155, 1.0195 + 0.0155, 31]}
lrn_phi_MC = {'X': [1.0195 - 0.016, 1.0195 + 0.016, 32], 'psi': [1.0195 - 0.016, 1.0195 + 0.016, 32]}
left_phi_MC, right_phi_MC, nbins_phi_MC = lrn_phi_MC[mode]

# lrn = left, right, nbins
lrn_control_MC = {'X': [3.872 - 0.025, 3.872 + 0.025, 50], 'psi': [3.686 - 0.025, 3.686 + 0.025, 50]}
# lrn_control_data = {'X': [3.872 - 0.065, 3.872 + 0.065, 65], 'psi': [3.686 - 0.05, 3.686 + 0.05, 50]}
lrn_control_data = {'X': [3.872 - 0.06, 3.872 + 0.06, 30], 'psi': [3.686 - 0.05, 3.686 + 0.05, 50]}

left_control_MC, right_control_MC, nbins_control_MC = lrn_control_MC[mode]
left_control_data, right_control_data, nbins_control_data = lrn_control_data[mode]

# means = {'X': 3.872, 'psi': 3.686}
# window = {'X': 0.018, 'psi': 0.018}

# var_discr.setRange('dicsr_range_MC', left_discr_MC, right_discr_MC)
# PHI_mass_Cjp.setRange('phi_range_MC', left_phi_MC, right_phi_MC)


cuts_Bs_MC = 'BU_mass_Cjp > ' + str(left_discr_MC) + ' && BU_mass_Cjp < ' + str(right_discr_MC)  # + '&& PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15'
cuts_Bs_data = 'BU_mass_Cjp > ' + str(left_discr_data) + ' && BU_mass_Cjp < ' + str(right_discr_data)   # + '&& PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15'

cuts_phi_MC = 'PHI_mass_Cjp > ' + str(left_phi_MC) + ' && PHI_mass_Cjp < ' + str(right_phi_MC)  # TMath::Abs(PHI_mass_Cjp - 1.02)<0.01 &&
cuts_phi_data = 'PHI_mass_Cjp > ' + str(left_phi_data) + ' && PHI_mass_Cjp < ' + str(right_phi_data)

cuts_control_MC = 'X_mass_Cjp >' + str(left_control_MC) + ' && X_mass_Cjp < ' + str(right_control_MC)
cuts_control_data = 'X_mass_Cjp >' + str(left_control_data) + ' && X_mass_Cjp < ' + str(right_control_data)

cuts_pipi = {'X': 'PIPI_mass_Cjp > 0.65 && PIPI_mass_Cjp < 0.78', 'psi': 'PIPI_mass_Cjp > 0.4 && PIPI_mass_Cjp < 0.6'}

cuts_match_dR = 'dR_mu1 < 0.05 && dR_mu2 < 0.05 && dR_pi1 < 0.05 && dR_pi2 < 0.05 && dR_K1 < 0.05 && dR_K2 < 0.05'
# cuts_match_ID = {'X': 'MoID_mu1 == 443 && MoID_mu2 == 443 && MoID_pi1 == 113 && MoID_pi2 == 113 && MoID_K1 == 333 && MoID_K2 == 333',
#                  'psi': 'MoID_mu1 == 443 && MoID_mu2 == 443 && MoID_pi1 == 100443 && MoID_pi2 == 100443 && MoID_K1 == 333 && MoID_K2 == 333'}
# cuts_match_dR = 'TMath::Min(dR_mu1, dR_mu1_vv) < 0.05 && TMath::Min(dR_mu2, dR_mu2_vv) < 0.05 && TMath::Min(dR_pi1, dR_pi1_vv) < 0.05 && TMath::Min(dR_pi2, dR_pi2_vv) < 0.05 && TMath::Min(dR_K1, dR_K1_vv) < 0.05 && TMath::Min(dR_K2, dR_K2_vv) < 0.05'
cuts_match_ID = {'X': '1 > 0', 'psi': '1 > 0'}

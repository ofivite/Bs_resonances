mode = 'X'
# gStyle.SetTitleFontSize(.085)

left_discr_data =  5.3669 - 0.21; right_discr_data = 5.3669 + 0.21; nbins_discr_data = 42
left_discr_MC =  5.37 - 0.04; right_discr_MC = 5.37 + 0.04; nbins_discr_MC = 40

left_phi_data = 1.0195 - 0.025; right_phi_data = 1.0195 + 0.025; nbins_phi_data = 50
left_phi_MC = 1.0195 - 0.015; right_phi_MC = 1.0195 + 0.015; nbins_phi_MC = 50

# mwn = mean, window, nbins
mwn_MC = {'X':[3.872, 0.08, 16], 'psi':[3.686, 0.02, 40]}
mwn_data = {'X':[3.872, 0.08, 16], 'psi':[3.686, 0.06, 60]}

left_control_MC = mwn_MC[mode][0] - mwn_MC[mode][1]; right_control_MC = mwn_MC[mode][0] + mwn_MC[mode][1]; nbins_control_MC = mwn_MC[mode][2]
left_control_data = mwn_data[mode][0] - mwn_data[mode][1]; right_control_data = mwn_data[mode][0] + mwn_data[mode][1]; nbins_control_data = mwn_data[mode][2]

window = {'X': 0.018, 'psi': 0.018}

# var_discr.setRange('dicsr_range_MC', left_discr_MC, right_discr_MC)
# PHI_mass_Cjp.setRange('phi_range_MC', left_phi_MC, right_phi_MC)

cuts_dR = '1 > 0'
# cuts_dR = 'dR_mu1 < 0.005 && dR_mu2 < 0.005 && dR_pi1 < 0.01 && dR_pi2 < 0.01 && dR_K1 < 0.01 && dR_K2 < 0.01'

cuts_Bs_MC = 'BU_mass_Cjp > ' + str(left_discr_MC) + ' && BU_mass_Cjp < ' + str(right_discr_MC)  # + '&& PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15'
cuts_Bs_data = 'BU_mass_Cjp > ' + str(left_discr_data) + ' && BU_mass_Cjp < ' + str(right_discr_data)   # + '&& PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15'

cuts_phi_MC = 'PHI_mass_Cjp > ' + str(left_phi_MC) + ' && PHI_mass_Cjp < ' + str(right_phi_MC)  # TMath::Abs(PHI_mass_Cjp - 1.02)<0.01 &&
cuts_phi_data = 'PHI_mass_Cjp > ' + str(left_phi_data) + ' && PHI_mass_Cjp < ' + str(right_phi_data)

cuts_pipi = {'X': 'PIPI_mass_Cjp > 0.65 && PIPI_mass_Cjp < 0.78', 'psi': 'PIPI_mass_Cjp > 0.4 && PIPI_mass_Cjp < 0.6'}
cuts_control_MC = 'X_mass_Cjp >' + str(left_control_MC) + ' && X_mass_Cjp < ' + str(right_control_MC) + ' && ' + cuts_pipi[mode]
cuts_control_data = 'X_mass_Cjp >' + str(left_control_data) + ' && X_mass_Cjp < ' + str(right_control_data)  + ' && ' + cuts_pipi[mode]

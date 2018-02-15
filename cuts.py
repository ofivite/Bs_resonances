left_discr_data =  5.3669 - 0.21; right_discr_data = 5.3669 + 0.21; nbins_discr_data = 42
left_discr_MC =  5.37 - 0.04; right_discr_MC = 5.37 + 0.04; nbins_discr_MC = 40

left_phi_data = 1.0195 - 0.025; right_phi_data = 1.0195 + 0.025; nbins_phi_data = 50
left_phi_MC = 1.0195 - 0.015; right_phi_MC = 1.0195 + 0.015; nbins_phi_MC = 50

# left_psi = 3.686 - 0.03; right_psi = 3.686 + 0.03; nbins_psi = 60
left_psi_data = 3.686 - 0.025; right_psi_data = 3.686 + 0.025; nbins_psi_data = 50
left_psi_MC = 3.686 - 0.02; right_psi_MC = 3.686 + 0.02; nbins_psi_MC = 40

left_X = 3.872 - 0.08; right_X = 3.872 + 0.08; nbins_X = 32

psi_window = 0.018

cuts_dR = '1 > 0'
# cuts_dR = 'dR_mu1 < 0.005 && dR_mu2 < 0.005 && dR_pi1 < 0.01 && dR_pi2 < 0.01 && dR_K1 < 0.01 && dR_K2 < 0.01'

cuts_Bs_data = 'BU_mass_Cjp > ' + str(left_discr_data) + ' && BU_mass_Cjp < ' + str(right_discr_data)   # + '&& PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15'
cuts_Bs_MC = 'BU_mass_Cjp > ' + str(left_discr_MC) + ' && BU_mass_Cjp < ' + str(right_discr_MC)  # + '&& PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15'

cuts_phi_data = 'PHI_mass_Cjp > ' + str(left_phi_data) + ' && PHI_mass_Cjp < ' + str(right_phi_data)
cuts_phi_MC = 'PHI_mass_Cjp > ' + str(left_phi_MC) + ' && PHI_mass_Cjp < ' + str(right_phi_MC)  # TMath::Abs(PHI_mass_Cjp - 1.02)<0.01 &&

cuts_psi_data = 'X_mass_Cjp >' + str(left_psi_data) + ' && X_mass_Cjp < ' + str(right_psi_data)  + ' && PIPI_mass_Cjp > 0.4 && PIPI_mass_Cjp < 0.6'
cuts_psi_MC = 'X_mass_Cjp >' + str(left_psi_MC) + ' && X_mass_Cjp < ' + str(right_psi_MC)  + ' && PIPI_mass_Cjp > 0.4 && PIPI_mass_Cjp < 0.6'
cuts_X = 'X_mass_Cjp >' + str(left_X) + ' && X_mass_Cjp < ' + str(right_X)  + ' && PIPI_mass_Cjp > 0.65 && PIPI_mass_Cjp < 0.78'

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("mode", help="mode to study: psi/X", type=str)
args = parser.parse_args()
if args.mode not in ['psi', 'X']:
    raise argparse.ArgumentTypeError('wrong naming, enter psi or X')

mode = args.mode
refl_ON = False
get_MC_N_evts = False

sPlot_from_1 = 'Bs'; sPlot_from_2 = 'phi';
sPlot_cut = 'control'; sPlot_from = 'Bs'; sPlot_to = 'phi'
if sPlot_from != 'Bs': refl_ON = False
sPlot_from_text = mode if sPlot_from == 'control' else sPlot_from
sPlot_to_text = mode if sPlot_to == 'control' else sPlot_to

refl_line = '_refl' if refl_ON else ''
# gStyle.SetTitleFontSize(.085)

left_jpsi = 3.094 - 0.1; right_jpsi = 3.094 + 0.1; nbins_jpsi = 100

left_discr_data =  5.27; right_discr_data = 5.47; nbins_discr_data = 40 # 5.3669 + 0.1
left_discr_MC =  5.3669 - 0.035; right_discr_MC = 5.3669 + 0.035; nbins_discr_MC = 35

# lrn_phi_data = {'X': [1.0195 - 0.016, 1.0195 + 0.016, 32], 'psi': [1.0195 - 0.016, 1.0195 + 0.016, 32]}
lrn_phi_data = {'X': [0.99, 1.055, 13], 'psi': [1.0195 - 0.030, 1.0195 + 0.030, 30]} # 0.99 1.055
left_phi_data, right_phi_data, nbins_phi_data = lrn_phi_data[mode]

lrn_phi_MC = {'X': [1.0195 - 0.016, 1.0195 + 0.016, 32], 'psi': [1.0195 - 0.016, 1.0195 + 0.016, 32]}
left_phi_MC, right_phi_MC, nbins_phi_MC = lrn_phi_MC[mode]

lrn_control_MC = {'X': [3.872 - 0.02, 3.872 + 0.02, 40], 'psi': [3.686 - 0.02, 3.686 + 0.02, 40]}
lrn_control_data = {'X': [3.872 - 0.06, 3.872 + 0.06, 30], 'psi': [3.686 - 0.05, 3.686 + 0.05, 50]}

left_control_MC, right_control_MC, nbins_control_MC = lrn_control_MC[mode]
left_control_data, right_control_data, nbins_control_data = lrn_control_data[mode]

cuts_Bs_MC = 'BU_mass_Cjp > ' + str(left_discr_MC) + ' && BU_mass_Cjp < ' + str(right_discr_MC)  # + '&& PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15'
cuts_Bs_data = 'BU_mass_Cjp > ' + str(left_discr_data) + ' && BU_mass_Cjp < ' + str(right_discr_data)   # + '&& PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15'

cuts_phi_MC = 'PHI_mass_Cjp > ' + str(left_phi_MC) + ' && PHI_mass_Cjp < ' + str(right_phi_MC)  # TMath::Abs(PHI_mass_Cjp - 1.02)<0.01 &&
cuts_phi_data = 'PHI_mass_Cjp > ' + str(left_phi_data) + ' && PHI_mass_Cjp < ' + str(right_phi_data)

cuts_control_MC = 'X_mass_Cjp >' + str(left_control_MC) + ' && X_mass_Cjp < ' + str(right_control_MC)
cuts_control_data = 'X_mass_Cjp >' + str(left_control_data) + ' && X_mass_Cjp < ' + str(right_control_data)

cuts_pipi = {'X': 'PIPI_mass_Cjp > 0.65 && PIPI_mass_Cjp < 0.78', 'psi': 'PIPI_mass_Cjp > 0.4 && PIPI_mass_Cjp < 0.6'}
cuts_match_dR = 'dR_mup < 0.05 && dR_mum < 0.05 && dR_pip < 0.05 && dR_pim < 0.05 && dR_Kp < 0.05 && dR_Km < 0.05'

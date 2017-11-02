import ROOT

var_discr = ROOT.RooRealVar('BU_mass_Cjp', 'm(J/#psi#pi^{+}#pi^{-}#phi) [GeV]', 5.3669 - 0.2, 5.3669 + 0.2)
var_control = ROOT.RooRealVar('X_mass_Cjp', 'm(J/#psi#pi^{+}#pi^{-}) [GeV]', 3.4, 4.2)
PIPI_mass_Cjp = ROOT.RooRealVar('PIPI_mass_Cjp', 'PIPI_mass_Cjp', 0.2, 1.2)
PHI_mass_Cjp = ROOT.RooRealVar('PHI_mass_Cjp', 'PHI_mass_Cjp', 0., 2.)

mean_Bs = ROOT.RooRealVar("mean_Bs", "", 5.36, 5.33, 5.39)
sigma_Bs_1 = ROOT.RooRealVar("sigma_Bs_1", "", 0.1, 0.001, 0.05)
sigma_Bs_2 = ROOT.RooRealVar("sigma_Bs_2", "", 0.1, 0.001, 0.05)
exp_par = ROOT.RooRealVar('exp_par', '', -0.01, -6., -0.00001)
a1 = ROOT.RooRealVar('a1', 'a1', 0.5, 0., 1.)
a2 = ROOT.RooRealVar('a2', 'a2', 0.5, 0., 1.)
a3 = ROOT.RooRealVar('a3', 'a3', 0.5, 0., 1.)

N_sig_discr = ROOT.RooRealVar('N_sig_discr', '', 30000., 1., 100000)
fr_Bs = ROOT.RooRealVar('fr_Bs', 'fr_Bs', 0.5 , 0., 1.)
N_sig_1 = ROOT.RooFormulaVar('N_sig_1', 'N_sig_discr * fr_Bs', ROOT.RooArgList(N_sig_discr, fr_Bs))
N_sig_2 = ROOT.RooFormulaVar('N_sig_2', 'N_sig_discr * (1-fr_Bs)', ROOT.RooArgList(N_sig_discr, fr_Bs))

sig_Bs_1 = ROOT.RooGaussian("gauss_Bs_1", "", var_discr, mean_Bs, sigma_Bs_1)
sig_Bs_2 = ROOT.RooGaussian("gauss_Bs_2", "", var_discr, mean_Bs, sigma_Bs_2)
# bkgr_Bs = ROOT.RooExponential('bkgr_Bs', '', var_discr, exp_par)
bkgr_Bs = ROOT.RooBernstein('bkgr_Bs', '', var_discr, ROOT.RooArgList(a1, a2))
N_bkgr_discr = ROOT.RooRealVar('N_bkgr_discr', '', 100000., 1., 1000000)

#############################################################################################
# psi and X control

mean_psi = ROOT.RooRealVar("mean_psi", "", 3.68, 3.6, 3.8)
sigma_psi_1 = ROOT.RooRealVar("sigma_psi_1", "", 0.01, 0.001, 0.05)
sigma_psi_2 = ROOT.RooRealVar("sigma_psi_2", "", 0.01, 0.001, 0.05)
# sigma_psi = ROOT.RooRealVar("sigma_psi", "", 0.01, 0.001, 0.5)
N_sig_psi = ROOT.RooRealVar('N_sig_psi', '', 1000., 1., 10000)
fr_psi = ROOT.RooRealVar('fr_psi', 'fr_psi', 0.5 , 0., 1.)
N_sig_psi_1 = ROOT.RooFormulaVar('N_sig_psi_1', 'N_sig_psi * fr_psi', ROOT.RooArgList(N_sig_psi, fr_psi))
N_sig_psi_2 = ROOT.RooFormulaVar('N_sig_psi_2', 'N_sig_psi * (1-fr_psi)', ROOT.RooArgList(N_sig_psi, fr_psi))
sig_psi_1 = ROOT.RooGaussian("sig_psi_1", "", var_control, mean_psi, sigma_psi_1)
sig_psi_2 = ROOT.RooGaussian("sig_psi_2", "", var_control, mean_psi, sigma_psi_2)
# signal_psi = ROOT.RooGaussian("signal_psi", "", var_control, mean_psi, sigma_psi)

mean_X = ROOT.RooRealVar("mean_X", "", 3.8717, 3.8717 - 0.1, 3.8717 + 0.1)
sigma_X = ROOT.RooRealVar("sigma_X", "", 0.0051, 0.001, 0.01)
N_sig_X = ROOT.RooRealVar('N_sig_X', '', 100., 1., 1000)
signal_X = ROOT.RooGaussian("signal_X", "", var_control, mean_X, sigma_X)

bkgr_control = ROOT.RooBernstein('bkgr_control', '', var_control, ROOT.RooArgList(a1))
N_bkgr_control = ROOT.RooRealVar('N_bkgr_control', '', 1000., 1., 10000)


#############################################################################################

model_discr = ROOT.RooAddPdf('model_discr', 'model_discr', ROOT.RooArgList(sig_Bs_1, bkgr_Bs), ROOT.RooArgList(N_sig_discr, N_bkgr_discr))
# model_discr = ROOT.RooAddPdf('model_discr', 'model_discr', ROOT.RooArgList(sig_Bs_1, sig_Bs_2, bkgr_Bs), ROOT.RooArgList(N_sig_1, N_sig_2, N_bkgr_discr))
# model_control = ROOT.RooAddPdf('model_control', 'model_control', ROOT.RooArgList(signal_psi, signal_X, bkgr_control), ROOT.RooArgList(N_sig_psi, N_sig_X, N_bkgr_control))
model_control = ROOT.RooAddPdf('model_control', 'model_control', ROOT.RooArgList(sig_psi_1, sig_psi_2, signal_X, bkgr_control), ROOT.RooArgList(N_sig_psi_1, N_sig_psi_2, N_sig_X, N_bkgr_control))
# model_control = ROOT.RooAddPdf('model_control', 'model_control', ROOT.RooArgList(signal_psi, signal_X), ROOT.RooArgList(N_sig_psi, N_sig_X))
model_X = ROOT.RooAddPdf('model_X', 'model_X', ROOT.RooArgList(signal_X, bkgr_control), ROOT.RooArgList(N_sig_X, N_bkgr_control))
model_psi = ROOT.RooAddPdf('model_psi', 'model_psi', ROOT.RooArgList(sig_psi_1, sig_psi_2, bkgr_control), ROOT.RooArgList(N_sig_psi_1, N_sig_psi_2, N_bkgr_control))

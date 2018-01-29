import ROOT

var_discr = ROOT.RooRealVar('BU_mass_Cjp', 'm(J/#psi#pi^{+}#pi^{-}#phi) [GeV]', 5.1, 5.6)
var_control = ROOT.RooRealVar('X_mass_Cjp', 'm(J/#psi#pi^{+}#pi^{-}) [GeV]', 3.4, 4.2)
PIPI_mass_Cjp = ROOT.RooRealVar('PIPI_mass_Cjp', 'PIPI_mass_Cjp', 0.2, 1.2)
PHI_mass_Cjp = ROOT.RooRealVar('PHI_mass_Cjp', 'PHI_mass_Cjp', 0., 2.)

dR_mu1 = ROOT.RooRealVar('dR_mu1', '', 0., 0.5)
dR_mu2 = ROOT.RooRealVar('dR_mu2', '', 0., 0.5)
dR_pi1 = ROOT.RooRealVar('dR_pi1', '', 0., 0.5)
dR_pi2 = ROOT.RooRealVar('dR_pi2', '', 0., 0.5)
dR_K1 = ROOT.RooRealVar('dR_K1', '', 0., 0.5)
dR_K2 = ROOT.RooRealVar('dR_K2', '', 0., 0.5)

#############################################################################################
# Bs

mean_Bs = ROOT.RooRealVar("mean_Bs", "", 5.36, 5.33, 5.39)
sigma_Bs = ROOT.RooRealVar("sigma_Bs", "", 0.01, 0.001, 0.05)
sigma_Bs_1 = ROOT.RooRealVar("sigma_Bs_1", "", 0.02, 0.001, 0.05)
sigma_Bs_2 = ROOT.RooRealVar("sigma_Bs_2", "", 0.01, 0.001, 0.05)
gamma_BW_Bs = ROOT.RooRealVar("gamma_BW_Bs","gamma_BW_Bs", 2., 0., 10.)
exp_par = ROOT.RooRealVar('exp_par', '', -0.01, -6., -0.00001)
a1 = ROOT.RooRealVar('a1', 'a1', 0.5, 0., 1.)
a2 = ROOT.RooRealVar('a2', 'a2', 0.5, 0., 1.)
a3 = ROOT.RooRealVar('a3', 'a3', 0.5, 0., 1.)
a4 = ROOT.RooRealVar('a4', 'a4', 0.5, 0., 1.)

N_sig_discr = ROOT.RooRealVar('N_sig_discr', '', 3000., 0., 200000)
fr_Bs = ROOT.RooRealVar('fr_Bs', 'fr_Bs', 0.5, 0., 1.)
N_sig_1 = ROOT.RooFormulaVar('N_sig_1', 'N_sig_discr * fr_Bs', ROOT.RooArgList(N_sig_discr, fr_Bs))
N_sig_2 = ROOT.RooFormulaVar('N_sig_2', 'N_sig_discr * (1-fr_Bs)', ROOT.RooArgList(N_sig_discr, fr_Bs))

sig_Bs_1 = ROOT.RooGaussian("sig_Bs_1", "", var_discr, mean_Bs, sigma_Bs_1)
sig_Bs_2 = ROOT.RooGaussian("sig_Bs_2", "", var_discr, mean_Bs, sigma_Bs_2)
signal_Bs = ROOT.RooVoigtian("signal_Bs", "signal_Bs", var_discr, mean_Bs, gamma_BW_Bs, sigma_Bs)

# bkgr_Bs = ROOT.RooExponential('bkgr_Bs', '', var_discr, exp_par)
bkgr_Bs = ROOT.RooBernstein('bkgr_Bs', '', var_discr, ROOT.RooArgList(a1, a2))
N_bkgr_discr = ROOT.RooRealVar('N_bkgr_discr', '', 30000., 0., 500000)

#############################################################################################
# psi(2S)

mean_psi = ROOT.RooRealVar("mean_psi", "", 3.68, 3.6, 3.8)
sigma_psi = ROOT.RooRealVar("sigma_psi", "", 0.02, 0.001, 0.05)
sigma_psi_1 = ROOT.RooRealVar("sigma_psi_1", "", 0.02, 0.001, 0.05)
sigma_psi_2 = ROOT.RooRealVar("sigma_psi_2", "", 0.01, 0.001, 0.05)
# sigma_psi = ROOT.RooRealVar("sigma_psi", "", 0.01, 0.001, 0.5)
gamma_BW_psi = ROOT.RooRealVar("gamma_BW_psi","gamma_BW_psi", 2., 0., 10.)

N_sig_psi = ROOT.RooRealVar('N_sig_psi', '', 2000., 0., 200000)
fr_psi = ROOT.RooRealVar('fr_psi', 'fr_psi', 0.5 , 0., 1.)
N_sig_psi_1 = ROOT.RooFormulaVar('N_sig_psi_1', 'N_sig_psi * fr_psi', ROOT.RooArgList(N_sig_psi, fr_psi))
N_sig_psi_2 = ROOT.RooFormulaVar('N_sig_psi_2', 'N_sig_psi * (1-fr_psi)', ROOT.RooArgList(N_sig_psi, fr_psi))
sig_psi_1 = ROOT.RooGaussian("sig_psi_1", "", var_control, mean_psi, sigma_psi_1)
sig_psi_2 = ROOT.RooGaussian("sig_psi_2", "", var_control, mean_psi, sigma_psi_2)

signal_psi = ROOT.RooVoigtian("signal_psi", "signal_psi", var_control, mean_psi, gamma_BW_psi, sigma_psi)
# signal_psi = ROOT.RooGaussian("signal_psi", "", var_control, mean_psi, sigma_psi)

#############################################################################################
# X(3872)

mean_X = ROOT.RooRealVar("mean_X", "", 3.8717, 3.8717 - 0.1, 3.8717 + 0.1)
sigma_X = ROOT.RooRealVar("sigma_X", "", 0.005, 0.001, 0.08)
sigma_X_1 = ROOT.RooRealVar("sigma_X_1", "", 0.005, 0.001, 0.02)
sigma_X_2 = ROOT.RooRealVar("sigma_X_2", "", 0.005, 0.001, 0.02)
N_sig_X = ROOT.RooRealVar('N_sig_X', '', 30000., 0., 100000)
fr_X = ROOT.RooRealVar('fr_X', 'fr_X', 0.5 , 0., 1.)
N_sig_X_1 = ROOT.RooFormulaVar('N_sig_X_1', 'N_sig_X * fr_X', ROOT.RooArgList(N_sig_X, fr_X))
N_sig_X_2 = ROOT.RooFormulaVar('N_sig_X_2', 'N_sig_X * (1-fr_X)', ROOT.RooArgList(N_sig_X, fr_X))

sig_X_1 = ROOT.RooGaussian("sig_X_1", "", var_control, mean_X, sigma_X_1)
sig_X_2 = ROOT.RooGaussian("sig_X_2", "", var_control, mean_X, sigma_X_2)
###
# sigma_CB = ROOT.RooRealVar("sigma_CB", "sigma_CB", 0.06, 0., 1.)
# alpha_CB = ROOT.RooRealVar("alpha_CB", "alpha_CB", -0.1, -10., 10.)
# n_CB = ROOT.RooRealVar("n_CB", "n_CB", 0.01, 0., 10)
# crystal = ROOT.RooCBShape("crystal", "crystal", var_control, mean_X, sigma_CB, alpha_CB, n_CB)
# gauss_X = ROOT.RooGaussian("gauss_X", "", var_control, mean_X, sigma_X)

mass_BW = ROOT.RooRealVar("mass_BW", "mass_BW", 0.)
gamma_BW_X = ROOT.RooRealVar("gamma_BW_X","gamma_BW_X", 2., 0., 10.)
BW = ROOT.RooBreitWigner("BW", "BW", var_control, mass_BW, gamma_BW_X)

# signal_X = ROOT.RooFFTConvPdf("signal_X", "signal_X", var_control, crystal, gauss_X)
signal_X = ROOT.RooVoigtian("signal_X", "signal_X", var_control, mean_X, gamma_BW_X, sigma_X)

bkgr_control = ROOT.RooBernstein('bkgr_control', '', var_control, ROOT.RooArgList(a1, a2))
# bkgr_control = ROOT.RooExponential('bkgr_control', '', var_control, exp_par)
N_bkgr_control = ROOT.RooRealVar('N_bkgr_control', '', 10000., 0., 500000)

#############################################################################################
# B0->psi(2S)K*0 reflection

file_B0_refl_ws = ROOT.TFile('~/Study/Bs_resonances/file_B0_refl_ws_after_cuts_dR0p05_5MeV_DC.root')
w = file_B0_refl_ws.Get('w')

B0_refl = w.pdf('B0_refl')
N_B0_refl = ROOT.RooRealVar('N_B0_refl', '', 990., 0., 1000.)

#############################################################################################
# Models

# model_discr = ROOT.RooAddPdf('model_discr', 'model_discr', ROOT.RooArgList(signal_Bs, bkgr_Bs, B0_refl), ROOT.RooArgList(N_sig_discr, N_bkgr_discr, N_B0_refl))
# model_discr = ROOT.RooAddPdf('model_discr', 'model_discr', ROOT.RooArgList(signal_Bs, bkgr_Bs), ROOT.RooArgList(N_sig_discr, N_bkgr_discr))
model_discr = ROOT.RooAddPdf('model_discr', 'model_discr', ROOT.RooArgList(sig_Bs_1, sig_Bs_2, bkgr_Bs), ROOT.RooArgList(N_sig_1, N_sig_2, N_bkgr_discr))

# model_control = ROOT.RooAddPdf('model_control', 'model_control', ROOT.RooArgList(signal_psi, signal_X, bkgr_control), ROOT.RooArgList(N_sig_psi, N_sig_X, N_bkgr_control))
# model_control = ROOT.RooAddPdf('model_control', 'model_control', ROOT.RooArgList(sig_psi_1, sig_psi_2, signal_X, bkgr_control), ROOT.RooArgList(N_sig_psi_1, N_sig_psi_2, N_sig_X, N_bkgr_control))
# model_control = ROOT.RooAddPdf('model_control', 'model_control', ROOT.RooArgList(signal_psi, signal_X), ROOT.RooArgList(N_sig_psi, N_sig_X))

model_X = ROOT.RooAddPdf('model_X', 'model_X', ROOT.RooArgList(signal_X, bkgr_control), ROOT.RooArgList(N_sig_X, N_bkgr_control))
# model_X = ROOT.RooAddPdf('model_X', 'model_X', ROOT.RooArgList(sig_X_1, sig_X_2, bkgr_control), ROOT.RooArgList(N_sig_X_1, N_sig_X_2, N_bkgr_control))
# model_psi = ROOT.RooAddPdf('model_psi', 'model_psi', ROOT.RooArgList(sig_psi_1, sig_psi_2, bkgr_control), ROOT.RooArgList(N_sig_psi_1, N_sig_psi_2, N_bkgr_control))
model_psi = ROOT.RooAddPdf('model_psi', 'model_psi', ROOT.RooArgList(signal_psi, bkgr_control), ROOT.RooArgList(N_sig_psi, N_bkgr_control))
#############################################################################################

plot_discr_param = ROOT.RooArgSet(mean_Bs, gamma_BW_Bs, sigma_Bs, N_sig_discr, N_bkgr_discr, N_B0_refl)
plot_psi_param = ROOT.RooArgSet(mean_psi, gamma_BW_psi, sigma_psi, N_sig_psi, N_bkgr_control)
plot_X_param = ROOT.RooArgSet(mean_X, gamma_BW_X, sigma_X, N_sig_X, N_bkgr_control)

N_sig_discr.setPlotLabel("N_{B_{s}^{0}}");
N_sig_X.setPlotLabel('N_{X}')
N_sig_psi.setPlotLabel('N_{#psi(2S)}')
N_bkgr_control.setPlotLabel('N_{bkgr}')
N_bkgr_discr.setPlotLabel('N_{bkgr}')
N_B0_refl.setPlotLabel('N(B^{0}#rightarrow#psi(2S)K^{*0})')

#
a1.setPlotLabel('a_{1}')
a2.setPlotLabel('a_{2}')
a3.setPlotLabel('a_{3}')
a4.setPlotLabel('a_{4}')
exp_par.setPlotLabel('#lambda_{bkgr}')
#
mean_X.setPlotLabel("m[X]");
sigma_X.setPlotLabel("#sigma[X]");
sigma_X_1.setPlotLabel("#sigma_{1}[X]");
sigma_X_2.setPlotLabel("#sigma_{2}[X]");
gamma_BW_X.setPlotLabel('#Gamma_{BW}[X]')
#
mean_psi.setPlotLabel("m[#psi(2S)]");
sigma_psi.setPlotLabel("#sigma[#psi(2S)]");
sigma_psi_1.setPlotLabel("#sigma_{1}[#psi(2S)]");
sigma_psi_2.setPlotLabel("#sigma_{2}[#psi(2S)]");
gamma_BW_psi.setPlotLabel('#Gamma_{BW}[#psi(2S)]')
fr_psi.setPlotLabel('fr_{#psi(2S)}')
#
mean_Bs.setPlotLabel('m[B_{s}^{0}]')
sigma_Bs.setPlotLabel('#sigma[B_{s}^{0}]')
sigma_Bs_1.setPlotLabel('#sigma_{1}[B_{s}^{0}]')
sigma_Bs_2.setPlotLabel('#sigma_{2}[B_{s}^{0}]')
gamma_BW_Bs.setPlotLabel('#Gamma_{BW}[B_{s}^{0}]')
fr_Bs.setPlotLabel('fr_{B_{s}^{0}}')

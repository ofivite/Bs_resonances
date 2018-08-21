import os
import sys
from datetime import datetime

import ROOT
from ROOT import RooFit as RF
from cuts import *
import CMS_tdrStyle_lumi

var_discr = ROOT.RooRealVar('BU_mass_Cjp', 'm(J/#psi#pi^{+}#pi^{#font[122]{\55}}K^{+}K^{#font[122]{\55}}) [GeV]', 5.1, 5.6)
var_control = ROOT.RooRealVar('X_mass_Cjp', 'm(J/#psi#pi^{+}#pi^{#font[122]{\55}}) [GeV]', 3.4, 4.2)
PIPI_mass_Cjp = ROOT.RooRealVar('PIPI_mass_Cjp', 'm(#pi^{+}#pi^{#font[122]{\55}}) [GeV]', 0.2, 1.2)
PHI_mass_Cjp = ROOT.RooRealVar('PHI_mass_Cjp', 'm(K^{+}K^{#font[122]{\55}}) [GeV]', 0., 2.)
SAMEEVENT = ROOT.RooRealVar('SAMEEVENT', 'SAMEEVENT', 0., 2.)

mu_max_pt = ROOT.RooRealVar('mu_max_pt', 'p_{T}^{max}(#mu) [GeV]', 0., 400.)
mu_min_pt = ROOT.RooRealVar('mu_min_pt', 'p_{T}^{min}(#mu) [GeV]', 0., 200.)
mu_max_eta = ROOT.RooRealVar('mu_max_eta', '#eta^{max}(#mu)', -2.5, 2.5)
mu_min_eta = ROOT.RooRealVar('mu_min_eta', '#eta^{min}(#mu)', -2.5, 2.5)

K_max_pt = ROOT.RooRealVar('K_max_pt', 'p_{T}^{max}(K) [GeV]', 0., 150.)
K_min_pt = ROOT.RooRealVar('K_min_pt', 'p_{T}^{min}(K) [GeV]', 0., 150.)
K_max_eta = ROOT.RooRealVar('K_max_eta', '#eta^{max}(K)', -2.5, 2.5)
K_min_eta = ROOT.RooRealVar('K_min_eta', '#eta^{min}(K)', -2.5, 2.5)

pi_max_pt = ROOT.RooRealVar('pi_max_pt', 'p_{T}^{max}(#pi) [GeV]', 0., 100.)
pi_min_pt = ROOT.RooRealVar('pi_min_pt', 'p_{T}^{min}(#pi) [GeV]', 0., 400.)
pi_max_eta = ROOT.RooRealVar('pi_max_eta', '#eta^{max}(#pi)', -2.5, 2.5)
pi_min_eta = ROOT.RooRealVar('pi_min_eta', '#eta^{min}(#pi)', -2.5, 2.5)

BU_pt_Cjp = ROOT.RooRealVar('BU_pt_Cjp', 'p_{T}(B_{s}^{0}) [GeV]', 0, 800)
BU_eta_Cjp = ROOT.RooRealVar('BU_eta_Cjp', '#eta(B_{s}^{0})', -2.5, 2.5)

PHI_mass_Cjp.setBins(10000, "cache")
# PHI_mass_Cjp.setBins(nbins_phi_data)
# PHI_mass_Cjp.setRange(left_phi_data, right_phi_data)

dR_mu1 = ROOT.RooRealVar('dR_mu1', '', 0., 5.)
dR_mu2 = ROOT.RooRealVar('dR_mu2', '', 0., 5.)
dR_pi1 = ROOT.RooRealVar('dR_pi1', '', 0., 5.)
dR_pi2 = ROOT.RooRealVar('dR_pi2', '', 0., 5.)
dR_K1 = ROOT.RooRealVar('dR_K1', '', 0., 5.)
dR_K2 = ROOT.RooRealVar('dR_K2', '', 0., 5.)

dR_mu1_vv = ROOT.RooRealVar('dR_mu1_vv', '', 0., 5.)
dR_mu2_vv = ROOT.RooRealVar('dR_mu2_vv', '', 0., 5.)
dR_pi1_vv = ROOT.RooRealVar('dR_pi1_vv', '', 0., 5.)
dR_pi2_vv = ROOT.RooRealVar('dR_pi2_vv', '', 0., 5.)
dR_K1_vv = ROOT.RooRealVar('dR_K1_vv', '', 0., 5.)
dR_K2_vv = ROOT.RooRealVar('dR_K2_vv', '', 0., 5.)

MoID_mu1 = ROOT.RooRealVar('MoID_mu1', '', -1., 1000000)
MoID_mu2 = ROOT.RooRealVar('MoID_mu2', '', -1, 1000000)
MoID_pi1 = ROOT.RooRealVar('MoID_pi1', '', -1, 1000000)
MoID_pi2 = ROOT.RooRealVar('MoID_pi2', '', -1, 1000000)
MoID_K1 = ROOT.RooRealVar('MoID_K1', '', -1, 1000000)
MoID_K2 = ROOT.RooRealVar('MoID_K2', '', -1, 1000000)

#############################################################################################
# Bs

mean_Bs = ROOT.RooRealVar("mean_Bs", "", 5.36, 5.33, 5.39)
sigma_Bs = ROOT.RooRealVar("sigma_Bs", "", 0.01, 0.001, 0.05)
sigma_Bs_1 = ROOT.RooRealVar("sigma_Bs_1", "", 0.02, 0.001, 0.05)
sigma_Bs_2 = ROOT.RooRealVar("sigma_Bs_2", "", 0.01, 0.001, 0.05)
sigma_Bs_3 = ROOT.RooRealVar("sigma_Bs_3", "", 0.01, 0.001, 0.05)
gamma_BW_Bs = ROOT.RooRealVar("gamma_BW_Bs","gamma_BW_Bs", 0.005, 0., 1.)
exp_par = ROOT.RooRealVar('exp_par', '', -0.01, -6., -0.00001)
a1 = ROOT.RooRealVar('a1', 'a1', 0.01, 0., 1.)
a2 = ROOT.RooRealVar('a2', 'a2', 0.01, 0., 1.)
a3 = ROOT.RooRealVar('a3', 'a3', 0.01, 0., 1.)
a4 = ROOT.RooRealVar('a4', 'a4', 0.01, 0., 1.)

a1_ext = ROOT.RooRealVar('a1_ext', 'a1_ext', 0.01, -10., 10.)
a2_ext = ROOT.RooRealVar('a2_ext', 'a2_ext', 0.01, -10., 10.)
a3_ext = ROOT.RooRealVar('a3_ext', 'a3_ext', 0.01, -10., 10.)
a4_ext = ROOT.RooRealVar('a4_ext', 'a4_ext', 0.01, -10., 10.)

N_sig_Bs = ROOT.RooRealVar('N_sig_Bs', '', 30000., 0., 100000)
fr_Bs = ROOT.RooRealVar('fr_Bs', 'fr_Bs', 0.5, 0., 1.)
fr_Bs_1 = ROOT.RooRealVar('fr_Bs_1', 'fr_Bs_1', 0.5, 0., 1.)
fr_Bs_2 = ROOT.RooRealVar('fr_Bs_2', 'fr_Bs_2', 0.5, 0., 1.)
N_sig_1 = ROOT.RooFormulaVar('N_sig_1', 'N_sig_Bs * fr_Bs', ROOT.RooArgList(N_sig_Bs, fr_Bs))
N_sig_2 = ROOT.RooFormulaVar('N_sig_2', 'N_sig_Bs * (1-fr_Bs)', ROOT.RooArgList(N_sig_Bs, fr_Bs))

sig_Bs_1 = ROOT.RooGaussian("sig_Bs_1", "", var_discr, mean_Bs, sigma_Bs_1)
sig_Bs_2 = ROOT.RooGaussian("sig_Bs_2", "", var_discr, mean_Bs, sigma_Bs_2)
sig_Bs_3 = ROOT.RooGaussian("sig_Bs_3", "", var_discr, mean_Bs, sigma_Bs_3)

signal_Bs = ROOT.RooAddPdf("signal_Bs", "signal_Bs", ROOT.RooArgList(sig_Bs_1, sig_Bs_2), ROOT.RooArgList(fr_Bs))  ## ---- BASELINE
# signal_Bs = ROOT.RooAddPdf("signal_Bs", "signal_Bs", ROOT.RooArgList(sig_Bs_1, sig_Bs_2, sig_Bs_3), ROOT.RooArgList(fr_Bs_1, fr_Bs_2))
# signal_Bs = ROOT.RooVoigtian("signal_Bs", "signal_Bs", var_discr, mean_Bs, gamma_BW_Bs, sigma_Bs)

# bkgr_Bs = ROOT.RooExponential('bkgr_Bs', '', var_discr, exp_par)
# bkgr_Bs = ROOT.RooBernstein('bkgr_Bs', '', var_discr, ROOT.RooArgList(a1, a2))
# bkgr_Bs = ROOT.RooBernstein('bkgr_Bs', '', var_discr, ROOT.RooArgList(a1, a2, a3))
# bkgr_Bs = ROOT.RooBernstein('bkgr_Bs', '', var_discr, ROOT.RooArgList(a1, a2, a3, a4))
bkgr_Bs = ROOT.RooChebychev('bkgr_Bs', '', var_discr, ROOT.RooArgList(a1_ext, a2_ext))
# bkgr_Bs = ROOT.RooChebychev('bkgr_Bs', '', var_discr, ROOT.RooArgList(a1_ext, a2_ext, a3_ext, a4_ext))

N_bkgr_Bs = ROOT.RooRealVar('N_bkgr_Bs', '', 30000., 0., 100000)

#############################################################################################
# psi(2S)

mean_psi = ROOT.RooRealVar("mean_psi", "", 3.685, 3.675, 3.695)
sigma_psi = ROOT.RooRealVar("sigma_psi", "", 0.02, 0.001, 0.05)
sigma_psi_1 = ROOT.RooRealVar("sigma_psi_1", "", 0.02, 0.001, 0.05)
sigma_psi_2 = ROOT.RooRealVar("sigma_psi_2", "", 0.01, 0.001, 0.05)
sigma_psi_3 = ROOT.RooRealVar("sigma_psi_3", "", 0.01, 0.001, 0.05)
# sigma_psi = ROOT.RooRealVar("sigma_psi", "", 0.01, 0.001, 0.5)
gamma_BW_psi = ROOT.RooRealVar("gamma_BW_psi","gamma_BW_psi", 0.005, 0., 1.)

N_sig_psi = ROOT.RooRealVar('N_sig_psi', '', 20000., 0., 100000)
fr_psi = ROOT.RooRealVar('fr_psi', 'fr_psi', 0.5 , 0., 1.)
fr_psi_1 = ROOT.RooRealVar('fr_psi_1', 'fr_psi_1', 0.5 , 0., 1.)
fr_psi_2 = ROOT.RooRealVar('fr_psi_2', 'fr_psi_2', 0.5 , 0., 1.)
N_sig_psi_1 = ROOT.RooFormulaVar('N_sig_psi_1', 'N_sig_psi * fr_psi', ROOT.RooArgList(N_sig_psi, fr_psi))
N_sig_psi_2 = ROOT.RooFormulaVar('N_sig_psi_2', 'N_sig_psi * (1-fr_psi)', ROOT.RooArgList(N_sig_psi, fr_psi))
sig_psi_1 = ROOT.RooGaussian("sig_psi_1", "", var_control, mean_psi, sigma_psi_1)
sig_psi_2 = ROOT.RooGaussian("sig_psi_2", "", var_control, mean_psi, sigma_psi_2)
sig_psi_3 = ROOT.RooGaussian("sig_psi_3", "", var_control, mean_psi, sigma_psi_3)

# signal_psi = ROOT.RooGaussian("signal_psi", "", var_control, mean_psi, sigma_psi)
signal_psi = ROOT.RooAddPdf("signal_psi", "signal_psi", ROOT.RooArgList(sig_psi_1, sig_psi_2), ROOT.RooArgList(fr_psi))  ## ---- BASELINE
# signal_psi = ROOT.RooAddPdf("signal_psi", "signal_psi", ROOT.RooArgList(sig_psi_1, sig_psi_2, sig_psi_3), ROOT.RooArgList(fr_psi_1, fr_psi_2), ROOT.kTRUE)
# signal_psi = ROOT.RooVoigtian("signal_psi", "signal_psi", var_control, mean_psi, gamma_BW_psi, sigma_psi)
# signal_psi = ROOT.RooBreitWigner("signal_psi", "signal_psi", var_control, mean_psi, gamma_BW_psi)

#############################################################################################
# X(3872)

mean_X = ROOT.RooRealVar("mean_X", "", 3.8717, 3.8717 - 0.01, 3.8717 + 0.01)
sigma_X = ROOT.RooRealVar("sigma_X", "", 0.005, 0.001, 0.08)
sigma_X_1 = ROOT.RooRealVar("sigma_X_1", "", 0.005, 0.001, 0.02)
sigma_X_2 = ROOT.RooRealVar("sigma_X_2", "", 0.005, 0.001, 0.02)
sigma_X_3 = ROOT.RooRealVar("sigma_X_3", "", 0.005, 0.001, 0.02)

N_sig_X = ROOT.RooRealVar('N_sig_X', '', 30000., 0., 100000)
fr_X = ROOT.RooRealVar('fr_X', 'fr_X', 0.5 , 0., 1.)
fr_X_1 = ROOT.RooRealVar('fr_X_1', 'fr_X_1', 0.5 , 0., 1.)
fr_X_2 = ROOT.RooRealVar('fr_X_2', 'fr_X_2', 0.5 , 0., 1.)
N_sig_X_1 = ROOT.RooFormulaVar('N_sig_X_1', 'N_sig_X * fr_X', ROOT.RooArgList(N_sig_X, fr_X))
N_sig_X_2 = ROOT.RooFormulaVar('N_sig_X_2', 'N_sig_X * (1-fr_X)', ROOT.RooArgList(N_sig_X, fr_X))

sig_X_1 = ROOT.RooGaussian("sig_X_1", "", var_control, mean_X, sigma_X_1)
sig_X_2 = ROOT.RooGaussian("sig_X_2", "", var_control, mean_X, sigma_X_2)
sig_X_3 = ROOT.RooGaussian("sig_X_3", "", var_control, mean_X, sigma_X_3)
###
# sigma_CB = ROOT.RooRealVar("sigma_CB", "sigma_CB", 0.06, 0., 1.)
# alpha_CB = ROOT.RooRealVar("alpha_CB", "alpha_CB", -0.1, -10., 10.)
# n_CB = ROOT.RooRealVar("n_CB", "n_CB", 0.01, 0., 10)
# crystal = ROOT.RooCBShape("crystal", "crystal", var_control, mean_X, sigma_CB, alpha_CB, n_CB)
# gauss_X = ROOT.RooGaussian("gauss_X", "", var_control, mean_X, sigma_X)

mass_BW = ROOT.RooRealVar("mass_BW", "mass_BW", 3.8717, 3.8717 - 0.01, 3.8717 + 0.01)
gamma_BW_X = ROOT.RooRealVar("gamma_BW_X","gamma_BW_X", 0.005, 0., 1.)
BW = ROOT.RooBreitWigner("BW", "BW", var_control, mass_BW, gamma_BW_X)


# signal_X = ROOT.RooFFTConvPdf("signal_X", "signal_X", var_control, crystal, gauss_X)

# signal_X = sig_X_1
signal_X = ROOT.RooAddPdf("signal_X", "signal_X", ROOT.RooArgList(sig_X_1, sig_X_2), ROOT.RooArgList(fr_X))  ## ---- BASELINE
# signal_X = ROOT.RooAddPdf("signal_X", "signal_X", ROOT.RooArgList(sig_X_1, sig_X_2, sig_X_3), ROOT.RooArgList(fr_X_1, fr_X_2), ROOT.kTRUE)
# signal_X = ROOT.RooVoigtian("signal_X", "signal_X", var_control, mean_X, gamma_BW_X, sigma_X)
# signal_X = ROOT.RooBreitWigner("signal_X", "signal_X", var_control, mean_X, gamma_BW_X)


# bkgr_control = ROOT.RooBernstein('bkgr_control', '', var_control, ROOT.RooArgList(a1))
bkgr_control = ROOT.RooBernstein('bkgr_control', '', var_control, ROOT.RooArgList(a1, a2))  ## ---- BASELINE
# bkgr_control = ROOT.RooBernstein('bkgr_control', '', var_control, ROOT.RooArgList(a1, a2, a3))
# bkgr_control = ROOT.RooBernstein('bkgr_control', '', var_control, ROOT.RooArgList(a1, a2, a3, a4))

# bkgr_control = ROOT.RooChebychev('bkgr_control', '', var_control, ROOT.RooArgList(a1_ext))
# bkgr_control = ROOT.RooChebychev('bkgr_control', '', var_control, ROOT.RooArgList(a1_ext, a2_ext))
# bkgr_control = ROOT.RooChebychev('bkgr_control', '', var_control, ROOT.RooArgList(a1_ext, a2_ext, a3_ext))
# bkgr_control = ROOT.RooChebychev('bkgr_control', '', var_control, ROOT.RooArgList(a1_ext, a2_ext, a3_ext, a4_ext))

# bkgr_control = ROOT.RooPolynomial('bkgr_control', '', var_control, ROOT.RooArgList(a1_ext))
# bkgr_control = ROOT.RooPolynomial('bkgr_control', '', var_control, ROOT.RooArgList(a1_ext, a2_ext))
# bkgr_control = ROOT.RooPolynomial('bkgr_control', '', var_control, ROOT.RooArgList(a1_ext, a2_ext, a3_ext))
# bkgr_control = ROOT.RooPolynomial('bkgr_control', '', var_control, ROOT.RooArgList(a1_ext, a2_ext, a3_ext, a4_ext))

# bkgr_control = ROOT.RooExponential('bkgr_control', '', var_control, exp_par)

N_bkgr_control = ROOT.RooRealVar('N_bkgr_control', '', 10000., 0., 100000)

#############################################################################################
# Phi

mean_phi = ROOT.RooRealVar("mean_phi", "", 1.020, 1.015, 1.025)
sigmaCB_phi_1 = ROOT.RooRealVar("sigmaCB_phi_1", "", 0.04, 0., 0.5)
alpha_phi_1 = ROOT.RooRealVar('alpha_phi_1', '', -1., -10., -0.0001)
n_phi_1 = ROOT.RooRealVar('n_phi_1', '', .8, 0.01, 10.)

sigmaCB_phi_2 = ROOT.RooRealVar("sigmaCB_phi_2", "", 0.04, 0., 0.5)
alpha_phi_2 = ROOT.RooRealVar('alpha_phi_2', '', 1., 0.0001, 10.)
n_phi_2 = ROOT.RooRealVar('n_phi_2', '', .8, 0.01, 10.)

mean_zero_phi = ROOT.RooRealVar("mean_zero_phi", "", 0)
sigma_gauss_phi = ROOT.RooRealVar("sigma_gauss_phi", "",  0.004, 0.001, 0.5)

sigma_phi = ROOT.RooRealVar("sigma_phi", "", 0.01, 0.001, 0.05)
sigma_phi_1 = ROOT.RooRealVar("sigma_phi_1", "", 0.01, 0.001, 0.05)
sigma_phi_2 = ROOT.RooRealVar("sigma_phi_2", "", 0.01, 0.001, 0.05)
gamma_BW_phi = ROOT.RooRealVar("gamma_BW_phi","gamma_BW_phi", 0.01, 0., 0.5 )

N_sig_phi = ROOT.RooRealVar('N_sig_phi', '', 20000., 0., 100000)
fr_phi = ROOT.RooRealVar('fr_phi', 'fr_phi', 0.5 , 0., 1.)
# N_sig_psi_1 = ROOT.RooFormulaVar('N_sig_psi_1', 'N_sig_psi * fr_psi', ROOT.RooArgList(N_sig_psi, fr_psi))
# N_sig_psi_2 = ROOT.RooFormulaVar('N_sig_psi_2', 'N_sig_psi * (1-fr_psi)', ROOT.RooArgList(N_sig_psi, fr_psi))
sig_phi_1 = ROOT.RooGaussian("sig_phi_1", "", PHI_mass_Cjp, mean_phi, sigma_phi_1)
sig_phi_2 = ROOT.RooGaussian("sig_phi_2", "", PHI_mass_Cjp, mean_phi, sigma_phi_2)

a1_phi = ROOT.RooRealVar('a1_phi', 'a1_phi', 0.01, 0., 1.)
a2_phi = ROOT.RooRealVar('a2_phi', 'a2_phi', 0.01, 0., 1.)
a3_phi = ROOT.RooRealVar('a3_phi', 'a3_phi', 0.01, 0., 1.)
a4_phi = ROOT.RooRealVar('a4_phi', 'a4_phi', 0.01, 0., 1.)

CB_phi_1 = ROOT.RooCBShape('CB_phi_1', '', PHI_mass_Cjp, mean_phi, sigmaCB_phi_1, alpha_phi_1, n_phi_1)
CB_phi_2 = ROOT.RooCBShape('CB_phi_2', '', PHI_mass_Cjp, mean_phi, sigmaCB_phi_2, alpha_phi_2, n_phi_2)
gauss_phi = ROOT.RooGaussian('gauss_phi', '', PHI_mass_Cjp, mean_zero_phi, sigma_gauss_phi)
relBW_phi = ROOT.RooGenericPdf("relBW_phi", "relBW_phi", "(1. / ( TMath::Power( (PHI_mass_Cjp * PHI_mass_Cjp - mean_phi * mean_phi) , 2) + TMath::Power( mean_phi * gamma_BW_phi , 2))) ", ROOT.RooArgList(PHI_mass_Cjp, mean_phi, gamma_BW_phi))
BW_phi = ROOT.RooBreitWigner('BW_phi', '', PHI_mass_Cjp, mean_zero_phi, gamma_BW_phi)
voig_phi = ROOT.RooVoigtian("voig_phi", "voig_phi", PHI_mass_Cjp, mean_zero_phi, gamma_BW_phi, sigma_phi)

signal_phi = ROOT.RooAddPdf("CB+CB", "signal_phi", ROOT.RooArgList(CB_phi_1, CB_phi_2), ROOT.RooArgList(fr_phi)) ## ---- BASELINE
# signal_phi =  ROOT.RooGenericPdf("relBW", '', "(1. / ( TMath::Power( (PHI_mass_Cjp * PHI_mass_Cjp - mean_phi * mean_phi) , 2) + TMath::Power( mean_phi * gamma_BW_phi , 2))) ", ROOT.RooArgList(PHI_mass_Cjp, mean_phi, gamma_BW_phi))
# signal_phi = ROOT.RooFFTConvPdf('CBxBW', '', PHI_mass_Cjp, CB_phi_1, BW_phi)
# signal_phi = ROOT.RooFFTConvPdf('CBxGauss', '', PHI_mass_Cjp, CB_phi_1, gauss_phi )
# signal_phi = ROOT.RooFFTConvPdf('CBxVoig', '', PHI_mass_Cjp, CB_phi_1, voig_phi)
# signal_phi = ROOT.RooFFTConvPdf('relBWxGauss', '', PHI_mass_Cjp, relBW_phi, gauss_phi)
# signal_phi = ROOT.RooFFTConvPdf('relBWxBW', '', PHI_mass_Cjp, relBW_phi, BW_phi)

N_sig_phi = ROOT.RooRealVar('N_sig_phi', '', 20000., 0., 100000)

# relBW_phi = ROOT.RooGenericPdf("relBW_phi", "relBW_phi", "(1. / ( TMath::Power( (PHI_mass_Cjp * PHI_mass_Cjp - mean_phi * mean_phi) , 2) + TMath::Power( mean_phi * gamma_BW_phi , 2))) ", ROOT.RooArgList(PHI_mass_Cjp, mean_phi, gamma_BW_phi))
# gauss_phi = ROOT.RooGaussian('gauss_phi', '', PHI_mass_Cjp, mean_zero_phi, sigma_gauss_phi)
# signal_phi = ROOT.RooFFTConvPdf('signal_phi', '', PHI_mass_Cjp, relBW_phi, gauss_phi)
# signal_phi = relBW_phi


# bkgr_phi = ROOT.RooBernstein('bkgr_phi', '', PHI_mass_Cjp, ROOT.RooArgList(a1_phi))
bkgr_phi = ROOT.RooBernstein('bkgr_phi', '', PHI_mass_Cjp, ROOT.RooArgList(a1_phi, a2_phi))   ## ---- BASELINE
# bkgr_phi = ROOT.RooBernstein('bkgr_phi', '', PHI_mass_Cjp, ROOT.RooArgList(a1_phi, a2_phi, a3_phi))

# bkgr_phi = ROOT.RooChebychev('bkgr_phi', '', PHI_mass_Cjp, ROOT.RooArgList(a1_ext))
# bkgr_phi = ROOT.RooChebychev('bkgr_phi', '', PHI_mass_Cjp, ROOT.RooArgList(a1_ext, a2_ext))
# bkgr_phi = ROOT.RooChebychev('bkgr_phi', '', PHI_mass_Cjp, ROOT.RooArgList(a1_ext, a2_ext, a3_ext))
# bkgr_phi = ROOT.RooChebychev('bkgr_phi', '', PHI_mass_Cjp, ROOT.RooArgList(a1_ext, a2_ext, a3_ext, a4_ext))

# bkgr_phi = ROOT.RooPolynomial('bkgr_phi', '', PHI_mass_Cjp, ROOT.RooArgList(a1_ext))
# bkgr_phi = ROOT.RooPolynomial('bkgr_phi', '', PHI_mass_Cjp, ROOT.RooArgList(a1_ext, a2_ext))
# bkgr_phi = ROOT.RooPolynomial('bkgr_phi', '', PHI_mass_Cjp, ROOT.RooArgList(a1_ext, a2_ext, a3_ext))
# bkgr_phi = ROOT.RooPolynomial('bkgr_phi', '', PHI_mass_Cjp, ROOT.RooArgList(a1_ext, a2_ext, a3_ext, a4_ext))


N_bkgr_phi = ROOT.RooRealVar('N_bkgr_phi', '', 10000., 0., 100000)

#############################################################################################
# B0->psi(2S)K*0 reflection

# file_B0_refl_ws = ROOT.TFile('~/Study/Bs_resonances/file_B0_refl_ws_data_cuts_dR0p05_SC.root')
file_B0_refl_ws = ROOT.TFile('~/Study/Bs_resonances/file_B0_refl_dR0p05_from_a1c59b9.root')
w = file_B0_refl_ws.Get('w')

# B0_refl = w.pdf('B0_refl')
B0_refl = w.pdf('B0_refl_SR')
N_B0_refl = ROOT.RooRealVar('N_B0_refl', '', 990., 0., 1000.)

#############################################################################################
# Backgrounds

a1_sb = ROOT.RooRealVar('a1_sb', 'a1_sb', 0.01, 0., 1.)
a2_sb = ROOT.RooRealVar('a2_sb', 'a2_sb', 0.01, 0., 1.)
a3_sb = ROOT.RooRealVar('a3_sb', 'a3_sb', 0.01, 0., 1.)
a4_sb = ROOT.RooRealVar('a4_sb', 'a4_sb', 0.01, 0., 1.)

a1_bs = ROOT.RooRealVar('a1_bs', 'a1_bs', 0.01, 0., 1.)
a2_bs = ROOT.RooRealVar('a2_bs', 'a2_bs', 0.01, 0., 1.)
a3_bs = ROOT.RooRealVar('a3_bs', 'a3_bs', 0.01, 0., 1.)
a4_bs = ROOT.RooRealVar('a4_bs', 'a4_bs', 0.01, 0., 1.)

a1_bb_1 = ROOT.RooRealVar('a1_bb_1', 'a1_bb_1', 0.01, 0., 1.)
a2_bb_1 = ROOT.RooRealVar('a2_bb_1', 'a2_bb_1', 0.01, 0., 1.)
a3_bb_1 = ROOT.RooRealVar('a3_bb_1', 'a3_bb_1', 0.01, 0., 1.)
a4_bb_1 = ROOT.RooRealVar('a4_bb_1', 'a4_bb_1', 0.01, 0., 1.)

a1_bb_2 = ROOT.RooRealVar('a1_bb_2', 'a1_bb_2', 0.01, 0., 1.)
a2_bb_2 = ROOT.RooRealVar('a2_bb_2', 'a2_bb_2', 0.01, 0., 1.)
a3_bb_2 = ROOT.RooRealVar('a3_bb_2', 'a3_bb_2', 0.01, 0., 1.)
a4_bb_2 = ROOT.RooRealVar('a4_bb_2', 'a4_bb_2', 0.01, 0., 1.)

bkgr_sb = ROOT.RooBernstein('bkgr_sb', '', PHI_mass_Cjp, ROOT.RooArgList(a1_sb, a2_sb, a3_sb))# , a4_sb))
bkgr_bs = ROOT.RooBernstein('bkgr_bs', '', var_discr, ROOT.RooArgList(a1_bs, a2_bs, a3_bs))# , a4_bs))
bkgr_bb_1 = ROOT.RooBernstein('bkgr_bb_1', '', var_discr, ROOT.RooArgList(a1_bb_1, a2_bb_1, a3_bb_1))# , a4_bb_1))
bkgr_bb_2 = ROOT.RooBernstein('bkgr_bb_2', '', PHI_mass_Cjp, ROOT.RooArgList(a1_bb_2, a2_bb_2, a3_bb_2))# , a4_bb_2))


#############################################################################################
# Models

N_ss_2D_vals = {'X': [120., 40., 190. ], 'psi': [2500., 2000., 3500.]}
N_sb_2D_vals = {'X': [100., 0., 500. ], 'psi': [500., 0., 1000.]}
N_ss_2D = ROOT.RooRealVar('N_ss_2D', '', N_ss_2D_vals[mode][0], N_ss_2D_vals[mode][1], N_ss_2D_vals[mode][2])
N_sb_2D = ROOT.RooRealVar('N_sb_2D', '', N_sb_2D_vals[mode][0], N_sb_2D_vals[mode][1], N_sb_2D_vals[mode][2])
N_bs_2D = ROOT.RooRealVar('N_bs_2D', '', 300., 0., 50000.)
N_bb_2D = ROOT.RooRealVar('N_bb_2D', '', 30000., 20000., 60000.)
# ----------------------------------------------------------------------------------------------------------------------------


model_X = ROOT.RooAddPdf('model_X', 'model_X', ROOT.RooArgList(signal_X, bkgr_control), ROOT.RooArgList(N_sig_X, N_bkgr_control))
# model_X = ROOT.RooAddPdf('model_X', 'model_X', ROOT.RooArgList(sig_X_1, sig_X_2, bkgr_control), ROOT.RooArgList(N_sig_X_1, N_sig_X_2, N_bkgr_control))
model_psi = ROOT.RooAddPdf('model_psi', 'model_psi', ROOT.RooArgList(signal_psi, bkgr_control), ROOT.RooArgList(N_sig_psi, N_bkgr_control))
# model_psi = ROOT.RooAddPdf('model_psi', 'model_psi', ROOT.RooArgList(signal_psi, bkgr_control), ROOT.RooArgList(N_sig_psi, N_bkgr_control))
model_1D_phi = ROOT.RooAddPdf('model_1D_phi', 'model_1D_phi', ROOT.RooArgList(signal_phi, bkgr_phi), ROOT.RooArgList(N_sig_phi, N_bkgr_phi))
# model_1D_Bs = ROOT.RooAddPdf('model_1D_Bs', 'model_1D_Bs', ROOT.RooArgList(signal_Bs, bkgr_Bs), ROOT.RooArgList(N_sig_Bs, N_bkgr_Bs))
model_1D_Bs = ROOT.RooAddPdf('model_1D_Bs', 'model_1D_Bs', ROOT.RooArgList(signal_Bs, bkgr_Bs, B0_refl), ROOT.RooArgList(N_sig_Bs, N_bkgr_Bs, N_B0_refl))

# ----------------------------------------------------------------------------------------------------------------------------
control_signals = {'X': signal_X, 'psi': signal_psi}
signal_control = control_signals[mode]

control_models = {'X': model_X, 'psi': model_psi}
model_control = control_models[mode]
N_control = {'X': N_sig_X, 'psi': N_sig_psi}
mean_control = {'X': mean_X, 'psi': mean_psi}

var = {'Bs': var_discr, 'phi': PHI_mass_Cjp, 'control': var_control}
left = {'Bs': left_discr_data, 'phi': left_phi_data, 'control': left_control_data}
right = {'Bs': right_discr_data, 'phi': right_phi_data, 'control': right_control_data}
nbins = {'Bs': nbins_discr_data, 'phi': nbins_phi_data, 'control': nbins_control_data}

model = {'Bs': model_1D_Bs, 'phi': model_1D_phi, 'control': model_control}
signal = {'Bs': signal_Bs, 'phi': signal_phi, 'control': signal_control}
N = {'Bs': N_sig_Bs, 'phi': N_sig_phi, 'control': N_control[mode]}
N_bkgr =  {'Bs': N_bkgr_Bs, 'phi': N_bkgr_phi, 'control': N_bkgr_control}
mean = {'Bs': mean_Bs, 'phi': mean_phi, 'control': mean_control[mode]}

# ----------------------------------------------------------------------------------------------------------------------------

model_ss_2D = ROOT.RooProdPdf('model_ss_2D', 'model_ss_2D', ROOT.RooArgList(signal[sPlot_from_1], signal[sPlot_from_2]))
model_bb_2D = ROOT.RooProdPdf('model_bb_2D', 'model_bb_2D', ROOT.RooArgList(bkgr_bb_1, bkgr_bb_2))
model_sb_2D = ROOT.RooProdPdf('model_sb_2D', 'model_sb_2D', ROOT.RooArgList(signal[sPlot_from_1], bkgr_sb))
model_bs_2D = ROOT.RooProdPdf('model_bs_2D', 'model_bs_2D', ROOT.RooArgList(bkgr_bs, signal[sPlot_from_2]))

model_2D_data = ROOT.RooAddPdf('model_2D_data', 'model_2D_data', ROOT.RooArgList(model_ss_2D, model_bb_2D, model_sb_2D, model_bs_2D), ROOT.RooArgList(N_ss_2D, N_bb_2D, N_sb_2D, N_bs_2D))
# model_2D_data = ROOT.RooAddPdf('model_2D_data', 'model_2D_data', ROOT.RooArgList(model_ss_2D, model_bb_2D, model_sb_2D), ROOT.RooArgList(N_ss_2D, N_bb_2D, N_sb_2D))
model_2D_MC = ROOT.RooAddPdf('model_2D_MC', 'model_2D_MC', ROOT.RooArgList(model_ss_2D, model_bb_2D), ROOT.RooArgList(N_ss_2D, N_bb_2D))


#############################################################################################

#
plot_discr_param = ROOT.RooArgSet(mean_Bs, sigma_Bs_1, sigma_Bs_2, fr_Bs, N_sig_Bs, N_bkgr_Bs)
plot_psi_param = ROOT.RooArgSet(mean_psi, sigma_psi_1, sigma_psi_2, fr_psi, N_sig_psi, N_bkgr_control)
plot_phi_param = ROOT.RooArgSet(ROOT.RooArgSet(mean_phi), ROOT.RooArgSet(sigmaCB_phi_1, sigmaCB_phi_2, alpha_phi_1, alpha_phi_2, n_phi_1, n_phi_2, N_sig_phi, N_bkgr_phi, fr_phi))
# plot_phi_param = ROOT.RooArgSet(mean_phi, gamma_BW_phi, sigma_phi_1, sigma_phi_2, sigmaCB_phi_1, sigmaCB_phi_2, alpha_phi_1, alpha_phi_2, n_phi_1, n_phi_2, N_sig_phi, N_bkgr_phi, fr_phi)
plot_X_param = ROOT.RooArgSet(mean_X, sigma_X_1, sigma_X_2, fr_X, N_sig_X, N_bkgr_control)
plot_control_param = {'X': plot_X_param, 'psi': plot_psi_param}
plot_param = {'Bs': plot_discr_param, 'phi': plot_phi_param, 'control': plot_control_param[mode]}

#
N_sig_Bs.setPlotLabel("N_{B_{s}^{0}}");
N_sig_X.setPlotLabel('N_{X}')
N_sig_psi.setPlotLabel('N_{#psi(2S)}')
N_sig_phi.setPlotLabel('N_{#phi}')
N_bkgr_control.setPlotLabel('N_{bkgr}')
N_bkgr_phi.setPlotLabel('N_{bkgr}')
N_bkgr_Bs.setPlotLabel('N_{bkgr}')
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
fr_Bs.setPlotLabel('fr[B_{s}^{0}]')
#
mean_phi.setPlotLabel('m[#phi]')
sigmaCB_phi_1.setPlotLabel('#sigma_{1}[#phi]')
gamma_BW_phi.setPlotLabel('#Gamma_{BW}[#phi]')
alpha_phi_1.setPlotLabel('#alpha_{1}[#phi]')
n_phi_1.setPlotLabel('n_{1}[#phi]')
sigmaCB_phi_2.setPlotLabel('#sigma_{2}[#phi]')
alpha_phi_2.setPlotLabel('#alpha_{2}[#phi]')
n_phi_2.setPlotLabel('n_{2}[#phi]')
sigma_phi_1.setPlotLabel('#sigma_{1}[#phi]')
sigma_phi_2.setPlotLabel('#sigma_{2}[#phi]')

def plot_on_frame(roovar, data, model, title, left, right, nbins, plot_par, isMC):
    frame = ROOT.RooPlot(" ", title, roovar, left, right, nbins);
    # if SumW2 == 1:
    #     data.plotOn(frame, RF.DataError(ROOT.RooAbsData.SumW2))
    # else:
    #     data.plotOn(frame, RF.DataError(ROOT.RooAbsData.SumW2))
    data.plotOn(frame, RF.DataError(ROOT.RooAbsData.Auto))
    # model.paramOn(frame, RF.Layout(0.55, 0.96, 0.9), RF.Parameters(plot_par))
    # frame.getAttText().SetTextSize(0.053)
    model.plotOn(frame, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5)) #, RF.NormRange("full"), RF.Range('full')
    floatPars = model.getParameters(data).selectByAttrib('Constant', ROOT.kFALSE)
    print '\n\n' + 30*'<' + '\n\n         ndf = ' + str(floatPars.getSize()) + ';    chi2/ndf = ' + str(frame.chiSquare(floatPars.getSize())) + ' for ' + str(model.GetName()) + ' and ' + str(data.GetName()) + '         \n\n' + 30*'>' + '\n\n'

    model.plotOn(frame, RF.Components("model_bb_2D"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kGreen-2), RF.LineWidth(4) );
    model.plotOn(frame, RF.Components("model_bs_2D"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kAzure+3), RF.LineWidth(4));
    model.plotOn(frame, RF.Components("model_sb_2D"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
    model.plotOn(frame, RF.Components("model_ss_2D"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kOrange+7), RF.LineWidth(4) );
# , RF.Range(mean_phi.getValV() - 15 * gamma_BW_phi.getValV(), mean_phi.getValV() + 15 * gamma_BW_phi.getValV())
    model.plotOn(frame, RF.Components("sig_Bs_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    model.plotOn(frame, RF.Components("sig_Bs_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    model.plotOn(frame, RF.Components('sig_' + str(mode) + '_1'), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    model.plotOn(frame, RF.Components('sig_' + str(mode) + '_2'), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    # model.plotOn(frame_control, RF.Components("signal_X"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    model.plotOn(frame, RF.Components("bkgr_control"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
    model.plotOn(frame, RF.Components("bkgr_phi"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
    model.plotOn(frame, RF.Components("bkgr_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
    # model.plotOn(frame, RF.Components("signal_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 15 * sigma_Bs.getValV(), mean_Bs.getValV() + 15 * sigma_Bs.getValV()));
    model.plotOn(frame, RF.Components("signal_phi"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    if refl_ON: model.plotOn(frame, RF.Components("B0_refl_SR"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kGreen-5), RF.LineWidth(4), RF.Normalization(1.0), RF.Name('B0_refl_SR'), RF.Range(5.32, 5.44));
    data.plotOn(frame, RF.DataError(ROOT.RooAbsData.Auto))

    frame.GetYaxis().SetTitle('Candidates / ' + str(int((right - left) / nbins * 1000.)) + ' MeV')
    frame.GetXaxis().SetTitleSize(0.04)
    frame.GetYaxis().SetTitleSize(0.04)
    frame.GetXaxis().SetLabelSize(0.033)
    frame.GetYaxis().SetLabelSize(0.033)
    frame.GetXaxis().SetTitleOffset(1.05)
    frame.GetYaxis().SetTitleOffset(1.3)
    frame.Draw()


def _import(wsp, obj):
    getattr(wsp, 'import')(obj)

def get_timestamp(fmt='%Y-%m-%d-%a-%H-%M'):
    """Return formatted timestamp."""
    return datetime.strftime(datetime.today(), fmt)

def get_file(fname, mode='read'):
    """Open and return a ROOT file."""
    if os.path.exists(fname):
        return ROOT.TFile(fname, mode)
    else:
        raise IOError('File %s does not exist!' % fname)

def save_in_workspace(rfile, **argsets):
    """Save RooFit objects in workspace and persistify.
    Pass the different types of objects as a keyword arguments. e.g.
    save_in_workspace(pdf=[pdf1, pdf2], variable=[var1, var2])
    """

    # from rplot.fixes import ROOT
    import traceback
    # Persistify variables, PDFs and datasets
    workspace = ROOT.RooWorkspace('workspace', 'Workspace saved at %s' % get_timestamp())
    keys = argsets.keys()
    for key in keys:
        print 'Importing RooFit objects in %s list.' % key
        for arg in argsets[key]:
            try:
                _import(workspace, arg)
            except TypeError:
                print type(arg), arg
                traceback.print_exc()
    rfile.WriteTObject(workspace)
    print 'Saving arguments to file: %s' % rfile.GetName()


def get_workspace(fname, wname):
    """Read and return RooWorkspace from file."""
    ffile = get_file(fname, 'read')
    workspace = ffile.Get(wname)
    return workspace, ffile

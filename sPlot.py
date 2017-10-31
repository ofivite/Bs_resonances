import ROOT
from ROOT import RooFit as RF
import math

var_discr = ROOT.RooRealVar('BU_mass_Cjp', 'm(J/#psi#pi^{+}#pi^{-}#phi) [GeV]', 5.3669 - 0.2, 5.3669 + 0.2)
var_control = ROOT.RooRealVar('X_mass_Cjp', 'm(J/#psi#pi^{+}#pi^{-}) [GeV]', 3.38, 4.24)

mean_Bs = ROOT.RooRealVar("mean_Bs", "", 5.36, 5.33, 5.39)
sigma_Bs_1 = ROOT.RooRealVar("sigma_Bs_1", "", 0.1, 0.001, 0.5)
sigma_Bs_2 = ROOT.RooRealVar("sigma_Bs_2", "", 0.1, 0.001, 0.5)
exp_par = ROOT.RooRealVar('exp_par', '', -0.01, -6., -0.00001)
a1 = ROOT.RooRealVar('a1', 'a1', 0.5, 0., 1.)
a2 = ROOT.RooRealVar('a2', 'a2', 0.5, 0., 1.)
a3 = ROOT.RooRealVar('a3', 'a3', 0.5, 0., 1.)

N_sig = ROOT.RooRealVar('N_sig', '', 30000., 1., 100000)
N_bkgr = ROOT.RooRealVar('N_bkgr', '', 100000., 1., 1000000)
fr_Bs = ROOT.RooRealVar('fr_Bs', 'fr_Bs', 0.5 , 0., 1.)
N_sig_1 = ROOT.RooFormulaVar('N_sig_1', 'N_sig * fr_Bs', ROOT.RooArgList(N_sig, fr_Bs))
N_sig_2 = ROOT.RooFormulaVar('N_sig_2', 'N_sig * (1-fr_Bs)', ROOT.RooArgList(N_sig, fr_Bs))

sig_Bs_1 = ROOT.RooGaussian("gauss_Bs_1", "", var_discr, mean_Bs, sigma_Bs_1)
sig_Bs_2 = ROOT.RooGaussian("gauss_Bs_2", "", var_discr, mean_Bs, sigma_Bs_2)
# bkgr_Bs = ROOT.RooExponential('bkgr_Bs', '', var_discr, exp_par)
bkgr_Bs = ROOT.RooBernstein('bkgr_Bs', '', var_discr, ROOT.RooArgList(a1, a2, a3))

mean_psi = ROOT.RooRealVar("mean_psi", "", 3.68, 3.6, 3.8)
sigma_psi_1 = ROOT.RooRealVar("sigma_psi_1", "", 0.01, 0.001, 0.5)
sigma_psi_2 = ROOT.RooRealVar("sigma_psi_2", "", 0.01, 0.001, 0.5)
# sigma_psi = ROOT.RooRealVar("sigma_psi", "", 0.01, 0.001, 0.5)
mean_X = ROOT.RooRealVar("mean_X", "", 3.8717, 3.8717 - 0.1, 3.8717 + 0.1)
sigma_X = ROOT.RooRealVar("sigma_X", "", 0.0051, 0.003, 0.01)

N_sig_psi = ROOT.RooRealVar('N_sig_psi', '', 1000., 1., 10000)
fr_psi = ROOT.RooRealVar('fr_psi', 'fr_psi', 0.5 , 0., 1.)
N_sig_psi_1 = ROOT.RooFormulaVar('N_sig_psi_1', 'N_sig_psi * fr_psi', ROOT.RooArgList(N_sig_psi, fr_psi))
N_sig_psi_2 = ROOT.RooFormulaVar('N_sig_psi_2', 'N_sig_psi * (1-fr_psi)', ROOT.RooArgList(N_sig_psi, fr_psi))

N_sig_X = ROOT.RooRealVar('N_sig_X', '', 100., 1., 1000)

sig_psi_1 = ROOT.RooGaussian("sig_psi_1", "", var_control, mean_psi, sigma_psi_1)
sig_psi_2 = ROOT.RooGaussian("sig_psi_2", "", var_control, mean_psi, sigma_psi_2)
# signal_psi = ROOT.RooGaussian("signal_psi", "", var_control, mean_psi, sigma_psi)
signal_X = ROOT.RooGaussian("signal_X", "", var_control, mean_X, sigma_X)
bkgr_X = ROOT.RooBernstein('bkgr_X', '', var_control, ROOT.RooArgList(a1, a2))

model_discr = ROOT.RooAddPdf('model_discr', 'model_discr', ROOT.RooArgList(sig_Bs_1, sig_Bs_1, bkgr_Bs), ROOT.RooArgList(N_sig_1, N_sig_2, N_bkgr))
# model_control = ROOT.RooAddPdf('model_control', 'model_control', ROOT.RooArgList(signal_psi, signal_X, bkgr_X), ROOT.RooArgList(N_sig_psi, N_sig_X, N_bkgr))
model_control = ROOT.RooAddPdf('model_control', 'model_control', ROOT.RooArgList(sig_psi_1, sig_psi_2, signal_X, bkgr_X), ROOT.RooArgList(N_sig_psi_1, N_sig_psi_2, N_sig_X, N_bkgr))
# model_control = ROOT.RooAddPdf('model_control', 'model_control', ROOT.RooArgList(signal_psi, signal_X), ROOT.RooArgList(N_sig_psi, N_sig_X))
model_X = ROOT.RooAddPdf('model_X', 'model_X', ROOT.RooArgList(signal_X, bkgr_X), ROOT.RooArgList(N_sig_X, N_bkgr))


file_data = ROOT.TFile('new.root')

PIPI_mass_Cjp = ROOT.RooRealVar('PIPI_mass_Cjp', 'PIPI_mass_Cjp', 0.2, 1.2)
PHI_mass_Cjp = ROOT.RooRealVar('PHI_mass_Cjp', 'PHI_mass_Cjp', 0., 2.)
cuts = 'TMath::Abs(PHI_mass_Cjp - 1.02)<0.005 && PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15' #PIPI_mass_Cjp > 0.65 && PIPI_mass_Cjp < 0.78 &&

# cuts1 = 'PIPI_mass_Cjp > 0.65 && PIPI_mass_Cjp < 0.78  && ROOT::TMath::Abs(X_mass_Cjp-3.872)<0.010 && ROOT::TMath::Abs(PHI_mass_Cjp - 1.02)<0.005 && ROOT::TMath::Abs(BU_mass_Cjp-5.367-X_mass_Cjp+3.686)<110.015 && BU_pt_Cjp > 15 && BU_pvcos2_Cjp > 0.999 && BU_vtxprob_Cjp > 0.10 && BU_pvdistsignif2_Cjp > 5 && K1_pt > .7 && K2_pt > .7 && PI1_pt > 0.6 && PI2_pt > 0.6'
# cuts2 = 'PIPI_mass_Cjp > 0.65  && PIPI_mass_Cjp < 0.78 && ROOT::TMath::Abs(PHI_mass_Cjp - 1.02)<0.005 && ROOT::TMath::Abs(BU_mass_Cjp-5.367-X_mass_Cjp+3.872)<0.015 && BU_pt_Cjp > 15 && BU_pvcos2_Cjp > 0.999 && BU_vtxprob_Cjp > 0.10 && BU_pvdistsignif2_Cjp > 5 && K1_pt > .7 && K2_pt > .7 && PI1_pt > 0.6 && PI2_pt > 0.6'
# cuts3 = 'ROOT::TMath::Abs(X_mass_Cjp-3.872)<0.010 && ROOT::TMath::Abs(PHI_mass_Cjp - 1.02)<0.005 && ROOT::TMath::Abs(BU_mass_Cjp-5.367-X_mass_Cjp+3.872)<0.015 && BU_pt_Cjp > 15 && BU_pvcos2_Cjp > 0.999 && BU_vtxprob_Cjp > 0.10 && BU_pvdistsignif2_Cjp > 5 && K1_pt > .7 && K2_pt > .7 && PI1_pt > 0.6 && PI2_pt > 0.6'
# cuts4 = 'PIPI_mass_Cjp > 0.65 && PIPI_mass_Cjp < 0.78 && ROOT::TMath::Abs(X_mass_Cjp-3.872)<0.010 && ROOT::TMath::Abs(PHI_mass_Cjp - 1.02)<10.010 && ROOT::TMath::Abs(BU_mass_Cjp-5.367-X_mass_Cjp+3.872)<0.015 && BU_pt_Cjp > 15 && BU_pvcos2_Cjp > 0.999 && BU_vtxprob_Cjp > 0.10 && BU_pvdistsignif2_Cjp > 5 && K1_pt > .7 && K2_pt > .7 && PI1_pt > 0.6 && PI2_pt > 0.6'

data = ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), cuts)
model_discr.fitTo(data)
model_discr.fitTo(data)
# Compute sWeights
ROOT.RooStats.SPlot(
    'sData', 'sData', data, model_discr,
    ROOT.RooArgList(N_sig,N_bkgr)
)

data_sig_weighted = ROOT.RooDataSet(data.GetName(),data.GetTitle(),data, data.get(),'X_mass_Cjp > 3.6 && X_mass_Cjp < 4.1', "N_sig_sw") ;
data_bkgr_weighted = ROOT.RooDataSet(data.GetName(),data.GetTitle(),data, data.get(),'',"N_bkgr_sw") ;

# # Import the dataset so we can easily access everything
# # getattr(w, 'import')(data, ROOT.RooCmdArg())
#
# # # Plot the fit
# # frame_fit = x.frame(RF.Title('Gaussian + polynomial fit'))
# # data.plotOn(frame_fit)
# # tot_pdf.plotOn(frame_fit, RF.Components('bkg_pdf'), RF.LineColor(ROOT.kRed))
# # tot_pdf.plotOn(frame_fit, RF.Components('sig_pdf'), RF.LineStyle(ROOT.kDashed))
# # tot_pdf.plotOn(frame_fit)
# #
# # # Plot the signal sWeights
# # nsig_sw = w.var('nsig_sw')
# # nsig_sw.SetTitle('Signal sWeight')
# # nsig_sw.setRange(-1.0, 1.5)
# # frame_sigsw = nsig_sw.frame(RF.Title('Signal sWeights'))
# # data.plotOn(frame_sigsw)
# #
# # # Plot the background sWeights
# # nbkg_sw = w.var('nbkg_sw')
# # nbkg_sw.SetTitle('Background sWeight')
# # nbkg_sw.setRange(-0.5, 2.0)
# # frame_bkgsw = w.var('nbkg_sw').frame(RF.Title('Background sWeights'))
# # data.plotOn(frame_bkgsw)
#


# # Plot the signal sWeight against the observable x


c = ROOT.TCanvas("c", "c", 1700, 800)
c.Divide(3,2)

c.cd(1)
frame_discr = var_discr.frame(RF.Title('m(J/#psi#pi^{+}#pi^{-}#phi)'))
data.plotOn(frame_discr)
model_discr.paramOn(frame_discr)
model_discr.plotOn(frame_discr)
frame_discr.Draw()

c.cd(4)
frame_control_bkgr = var_control.frame(RF.Title('sPlot for background'))
data_bkgr_weighted.plotOn(frame_control_bkgr)
frame_control_bkgr.Draw()

c.cd(5)
frame_control_pipi_bkgr = PIPI_mass_Cjp.frame(RF.Title('sPlot for background m(#pi^{+}#pi^{-})'))
data_bkgr_weighted.plotOn(frame_control_pipi_bkgr)
frame_control_pipi_bkgr.Draw()

c.cd(6)
PIPI_mass_Cjp.setRange(0.36, 0.86)
frame_control_pipi_sig = PIPI_mass_Cjp.frame(RF.Title('sPlot for signal m(#pi^{+}#pi^{-})'), RF.Bins(50))
_data = data_sig_weighted.reduce('PIPI_mass_Cjp > 0.36 && PIPI_mass_Cjp < 0.86')
_data.plotOn(frame_control_pipi_sig)
frame_control_pipi_sig.Draw()


sigma_X.setConstant(1)


c.cd(2)
left = 3.6; right = 3.95; nbins = 70
var_control.setRange(left, right)
frame_control_sig = var_control.frame(RF.Title('sPlot for the signal'), RF.Bins(nbins))
_data = data_sig_weighted.reduce('X_mass_Cjp >' + str(left) + ' && X_mass_Cjp <' + str(right) )
# data_sig_weighted = ROOT.RooDataSet(data.GetName(),data.GetTitle(),data, data.get(),'X_mass_Cjp > 3.6 && X_mass_Cjp < 3.95', "N_sig_sw") ;

print '\n\n#################################\n\n\n           background only now\n\n\n#################################\n\n'
# ---- bkgr only fit
N_sig_X.setVal(0)
N_sig_X.setConstant(1)
# mean_X.setConstant(1)
model_control.fitTo(_data)
model_control.fitTo(_data)
model_control.fitTo(_data)
rrr_null = model_control.fitTo(_data, RF.Save())

print '\n\n#################################\n\n\n           sig+bkgr now\n\n\n#################################\n\n'
# ---- sig+bkgr fit
N_sig_X.setVal(100)
N_sig_X.setConstant(0)
# mean_X.setConstant(1)
model_control.fitTo(_data)
model_control.fitTo(_data)
rrr_sig = model_control.fitTo(_data, RF.Save())

_data.plotOn(frame_control_sig)
model_control.paramOn(frame_control_sig)
model_control.plotOn(frame_control_sig)

frame_control_sig.Draw()

c.cd(3)
left = 3.872 - 0.15; right = 3.872 + 0.15; nbins = 60
var_control.setRange(left, right)
frame_control_X = var_control.frame(RF.Title('sPlot for X(3872)'), RF.Bins(nbins))
_data = data_sig_weighted.reduce('X_mass_Cjp >' + str(left) + ' && X_mass_Cjp <' + str(right) )

print '\n\n#################################\n\n\n           X now\n\n\n#################################\n\n'
model_X.fitTo(_data)
model_X.fitTo(_data)
_data.plotOn(frame_control_X)
model_X.paramOn(frame_control_X)
model_X.plotOn(frame_control_X)
frame_control_X.Draw()


nll_sig  = rrr_sig.minNll()
nll_null = rrr_null.minNll()
P = ROOT.TMath.Prob(nll_null - nll_sig, 3)## !!! Change delta of ndf appropriately
S = ROOT.TMath.ErfcInverse(P) * math.sqrt(2)
print 'P=', P, ' nll_sig=', nll_sig, ' nll_null=', nll_null, '\n', 'S=', S

c.SaveAs('sPlot.png')

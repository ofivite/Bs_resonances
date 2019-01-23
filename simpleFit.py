from RooSpace import *
from cuts import *


var_discr.setMin(left_discr_data); var_discr.setMax(right_discr_data); var_discr.setBins(nbins_discr_data)
PHI_mass_Cjp.setMin(left_phi_data); PHI_mass_Cjp.setMax(right_phi_data); PHI_mass_Cjp.setBins(nbins_phi_data)
var_control.setMin(left_control_data); var_control.setMax(right_control_data);  var_control.setBins(nbins_control_data)
jpsi_left = 3.094 - 0.1; jpsi_right = 3.094 + 0.1; jpsi_nbins = 100
jpsi_mass = ROOT.RooRealVar('JPSI_mass_Cmumu', 'm(#mu^{+}#mu^{-}) [GeV]', jpsi_left, jpsi_right)

file_data = ROOT.TFile('new_2_with_more_B0_jpsi_.root')
data = (ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp, jpsi_mass),
                                    cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data  + ' && ' + cuts_pipi[mode]))


##        ---------------       ##
##             MODEL            ##
##        ---------------       ##


mean_jpsi = ROOT.RooRealVar("mean_jpsi", "", 3.094, jpsi_left, jpsi_right)
sigma_jpsi = ROOT.RooRealVar("sigma_jpsi", "", 0.02, 0.001, 0.05)
sigma_jpsi_1 = ROOT.RooRealVar("sigma_jpsi_1", "", 0.02, 0.001, 0.05)
sigma_jpsi_2 = ROOT.RooRealVar("sigma_jpsi_2", "", 0.01, 0.001, 0.05)
sigma_jpsi_3 = ROOT.RooRealVar("sigma_jpsi_3", "", 0.01, 0.001, 0.05)
# gamma_BW_psi = ROOT.RooRealVar("gamma_BW_psi","gamma_BW_psi", 0.005, 0., 1.)

N_sig_jpsi = ROOT.RooRealVar('N_sig_jpsi', '', 200000., 0., 1000000)
fr_jpsi = ROOT.RooRealVar('fr_jpsi', 'fr_jpsi', 0.5 , 0., 1.)
fr_jpsi_1 = ROOT.RooRealVar('fr_jpsi_1', 'fr_jpsi_1', 0.5 , 0., 1.)
fr_jpsi_2 = ROOT.RooRealVar('fr_jpsi_2', 'fr_jpsi_2', 0.5 , 0., 1.)
N_sig_jpsi_1 = ROOT.RooFormulaVar('N_sig_jpsi_1', 'N_sig_jpsi * fr_jpsi', ROOT.RooArgList(N_sig_jpsi, fr_jpsi))
N_sig_jpsi_2 = ROOT.RooFormulaVar('N_sig_jpsi_2', 'N_sig_jpsi * (1-fr_jpsi)', ROOT.RooArgList(N_sig_jpsi, fr_jpsi))
sig_jpsi_1 = ROOT.RooGaussian("sig_jpsi_1", "", jpsi_mass, mean_jpsi, sigma_jpsi_1)
sig_jpsi_2 = ROOT.RooGaussian("sig_jpsi_2", "", jpsi_mass, mean_jpsi, sigma_jpsi_2)
sig_jpsi_3 = ROOT.RooGaussian("sig_jpsi_3", "", jpsi_mass, mean_jpsi, sigma_jpsi_3)

# signal_psi = ROOT.RooGaussian("signal_psi", "", var_control, mean_psi, sigma_psi)
signal_jpsi = ROOT.RooAddPdf("signal_jpsi", "signal_jpsi", ROOT.RooArgList(sig_jpsi_1, sig_jpsi_2), ROOT.RooArgList(fr_jpsi))  ## ---- BASELINE
#
a1 = ROOT.RooRealVar('a1', 'a1', 0.01, 0., 1.)
a2 = ROOT.RooRealVar('a2', 'a2', 0.01, 0., 1.)
bkgr_control = ROOT.RooBernstein('bkgr_control', '', jpsi_mass, ROOT.RooArgList(a1, a2))  ## ---- BASELINE
N_bkgr_control = ROOT.RooRealVar('N_bkgr_control', '', 10000., 0., 100000)
#
model_jpsi = ROOT.RooAddPdf('model_jpsi', 'model_jpsi', ROOT.RooArgList(signal_jpsi, bkgr_control), ROOT.RooArgList(N_sig_jpsi, N_bkgr_control))


##        -----------------       ##
##           FIT OF DATA          ##
##        -----------------       ##

CMS_tdrStyle_lumi.extraText = "Preliminary"
CMS_tdrStyle_lumi.setTDRStyle()
print ('\n\n' + 30*'#' + '\n\n\n         MC psi(2S): Bs mass now         \n\n\n' + 30*'#' + '\n\n')

mean_jpsi.setConstant(1)
model_jpsi.fitTo(data, RF.Extended(ROOT.kTRUE))
model_jpsi.fitTo(data, RF.Extended(ROOT.kTRUE))
a1.setConstant(1); a2.setConstant(1); mean_jpsi.setConstant(0)
model_jpsi.fitTo(data, RF.Extended(ROOT.kTRUE))
a1.setConstant(0); a2.setConstant(0)


##        ----------       ##
##           PLOT          ##
##        ----------       ##

c_MC_3 = ROOT.TCanvas("c_MC_3", "c_MC_3", 800, 600)
frame = ROOT.RooPlot(" ", 'm(#mu^{+}#mu^{-})', jpsi_mass, jpsi_left, jpsi_right, jpsi_nbins);
plot_jpsi_param = ROOT.RooArgSet(mean_jpsi, sigma_jpsi_1, sigma_jpsi_2, fr_jpsi, N_sig_jpsi, N_bkgr_control)

data.plotOn(frame, RF.DataError(ROOT.RooAbsData.Auto))
model_jpsi.paramOn(frame, RF.Layout(0.65, 0.96, 0.85), RF.Parameters(plot_jpsi_param))
# frame.getAttText().SetTextSize(0.053)
model_jpsi.plotOn(frame, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5)) #, RF.NormRange("full"), RF.Range('full')
floatPars = model_jpsi.getParameters(data).selectByAttrib('Constant', ROOT.kFALSE)

model_jpsi.plotOn(frame, RF.Components('sig_jpsi_1'), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
model_jpsi.plotOn(frame, RF.Components('sig_jpsi_2'), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
model_jpsi.plotOn(frame, RF.Components("bkgr_control"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
data.plotOn(frame, RF.DataError(ROOT.RooAbsData.Auto))

frame.GetYaxis().SetTitle('Candidates / ' + str(int((jpsi_right - jpsi_left) / jpsi_nbins * 1000.)) + ' MeV')
frame.GetXaxis().SetTitleSize(0.04)
frame.GetYaxis().SetTitleSize(0.04)
frame.GetXaxis().SetLabelSize(0.033)
frame.GetYaxis().SetLabelSize(0.033)
frame.GetXaxis().SetTitleOffset(1.05)
frame.GetYaxis().SetTitleOffset(1.3)
frame.Draw()

CMS_tdrStyle_lumi.CMS_lumi( c_MC_3, 0, 0 );
c_MC_3.Update(); c_MC_3.RedrawAxis(); c_MC_3.GetFrame().Draw();
c_MC_3.SaveAs('~/Study/Bs_resonances/jpsi_mass_psi.pdf')

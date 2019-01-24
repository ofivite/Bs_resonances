from RooSpace import *
from cuts import *


var_discr.setMin(left_discr_data); var_discr.setMax(right_discr_data); var_discr.setBins(nbins_discr_data)
PHI_mass_Cjp.setMin(left_phi_data); PHI_mass_Cjp.setMax(right_phi_data); PHI_mass_Cjp.setBins(nbins_phi_data)
var_control.setMin(left_control_data); var_control.setMax(right_control_data);  var_control.setBins(nbins_control_data)
jpsi_mass.setMin(left_jpsi); jpsi_mass.setMax(right_jpsi); jpsi_mass.setBins(nbins_jpsi)
gen_phi_mass.setMin(left_phi_MC); gen_phi_mass.setMax(right_phi_MC); gen_phi_mass.setBins(nbins_phi_MC)
# gen_phi_mass.setMin(1.008); gen_phi_mass.setMax(1.03); gen_phi_mass.setBins(nbins_phi_MC)

var_to_fit = gen_phi_mass

file_data = ROOT.TFile('BsToPsiPhi_Smatch_v1_pair_dR_phi_genmass.root')
data = (ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp, jpsi_mass, delta_phi_mass, gen_phi_mass ), '1>0'))
                                    # cuts_Bs_MC + '&&' + cuts_phi_MC + '&&' + cuts_control_MC + ' && ' + cuts_pipi[mode]))
# data_matched = data.reduce(cuts_match_ID[mode] + '&&' + cuts_match_dR)

##        ---------------       ##
##             MODEL            ##
##        ---------------       ##

# signal_phi = ROOT.RooAddPdf("CB+CB", "signal_phi", ROOT.RooArgList(CB_phi_1, CB_phi_2), ROOT.RooArgList(fr_phi)) ## ---- BASELINE
signal_phi =  ROOT.RooGenericPdf("relBW", '', "(1. / ( TMath::Power( (gen_phi_mass * gen_phi_mass - mean_phi * mean_phi) , 2) + TMath::Power( mean_phi * gamma_BW_phi , 2))) ", ROOT.RooArgList(gen_phi_mass, mean_phi, gamma_BW_phi))
# signal_phi = ROOT.RooFFTConvPdf('CBxBW', '', PHI_mass_Cjp, CB_phi_1, BW_phi)
# signal_phi = ROOT.RooFFTConvPdf('CBxGauss', '', PHI_mass_Cjp, CB_phi_1, gauss_phi )
# signal_phi = ROOT.RooFFTConvPdf('CBxVoig', '', PHI_mass_Cjp, CB_phi_1, voig_phi)
# signal_phi = ROOT.RooFFTConvPdf('relBWxGauss', '', PHI_mass_Cjp, relBW_phi, gauss_phi)
# signal_phi = ROOT.RooFFTConvPdf('relBWxBW', '', PHI_mass_Cjp, relBW_phi, BW_phi)

N_sig_phi = ROOT.RooRealVar('N_sig_phi', '', 200000., 0., 400000)
bkgr_phi = ROOT.RooBernstein('bkgr_phi', '', gen_phi_mass, ROOT.RooArgList(a1, a2))   ## ---- BASELINE
N_bkgr_phi = ROOT.RooRealVar('N_bkgr_phi', '', 1000., 0., 100000)

model_to_fit = ROOT.RooAddPdf('model_to_fit', 'model_to_fit', ROOT.RooArgList(signal_phi, bkgr_phi), ROOT.RooArgList(N_sig_phi, N_bkgr_phi))

##        -----------------       ##
##           FIT OF DATA          ##
##        -----------------       ##

CMS_tdrStyle_lumi.extraText = "Preliminary"
CMS_tdrStyle_lumi.setTDRStyle()
print ('\n\n' + 30*'#' + '\n\n\n         MC psi(2S): Bs mass now         \n\n\n' + 30*'#' + '\n\n')

mean_phi.setConstant(1);
gamma_BW_phi.setVal(0.0042);# gamma_BW_phi.setConstant(1)
N_bkgr_phi.setVal(0.); N_bkgr_phi.setConstant(1)
model_to_fit.fitTo(data, RF.Extended(ROOT.kTRUE))
model_to_fit.fitTo(data, RF.Extended(ROOT.kTRUE))
a1.setConstant(1); a2.setConstant(1); mean_phi.setConstant(0)
model_to_fit.fitTo(data, RF.Extended(ROOT.kTRUE))
a1.setConstant(0); a2.setConstant(0)


##        ----------       ##
##           PLOT          ##
##        ----------       ##

c_MC_3 = ROOT.TCanvas("c_MC_3", "c_MC_3", 800, 600)
# frame = ROOT.RooPlot(" ", 'm(#mu^{+}#mu^{-})', var_to_fit, var_to_fit.getMin(), var_to_fit.getMax(), var_to_fit.getBins());
plot_param = ROOT.RooArgSet(mean_phi, gamma_BW_phi, N_sig_phi, N_bkgr_phi)

plot_on_frame(var_to_fit, data, model_to_fit, 'MC: m(K^{+}K^{#font[122]{\55}})', left_phi_MC, right_phi_MC, nbins_phi_MC, plot_param, True)

# data.plotOn(frame, RF.DataError(ROOT.RooAbsData.Auto))
# # model_1D_phi.paramOn(frame, RF.Layout(0.65, 0.96, 0.85), RF.Parameters(plot_param))
# # frame.getAttText().SetTextSize(0.053)
# model_to_fit.plotOn(frame, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5)) #, RF.NormRange("full"), RF.Range('full')
# floatPars = model_to_fit.getParameters(data).selectByAttrib('Constant', ROOT.kFALSE)
#
# # model_1D_phi.plotOn(frame, RF.Components('sig_jpsi_1'), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
# # model_1D_phi.plotOn(frame, RF.Components('sig_jpsi_2'), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
# model_to_fit.plotOn(frame, RF.Components("bkgr_phi"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
# data.plotOn(frame, RF.DataError(ROOT.RooAbsData.Auto))
#
# frame.GetYaxis().SetTitle('Candidates / ' + str(int((var_to_fit.getMax() - var_to_fit.getMin()) / var_to_fit.getBins() * 1000.)) + ' MeV')
# frame.GetXaxis().SetTitleSize(0.04)
# frame.GetYaxis().SetTitleSize(0.04)
# frame.GetXaxis().SetLabelSize(0.033)
# frame.GetYaxis().SetLabelSize(0.033)
# frame.GetXaxis().SetTitleOffset(1.05)
# frame.GetYaxis().SetTitleOffset(1.3)
# frame.Draw()

CMS_tdrStyle_lumi.CMS_lumi( c_MC_3, 0, 0 );
c_MC_3.Update(); c_MC_3.RedrawAxis(); c_MC_3.GetFrame().Draw();
c_MC_3.SaveAs('~/Study/Bs_resonances/gen_mass_phi.pdf')

from RooSpace import *
from cuts import *
from math import sqrt


file_data = ROOT.TFile('new_2_with_more_B0_e3de87.root')
# file_data = ROOT.TFile('~/Study/Bs_resonances_ML/masses_tree_RF_0p9_both.root')
# file_data = ROOT.TFile('new_noKaon_fabs_76e92fd.root')
# file_data = ROOT.TFile('new_noKaon_9988200.root')
# file_data = ROOT.TFile('new.root')

w_Bs, f_Bs = get_workspace('workspace_' + mode + '_Bs.root', 'workspace')
w_psi, f_psi = get_workspace('workspace_psi_control.root', 'workspace')
w_X, f_X = get_workspace('workspace_X_control.root', 'workspace')
w_phi, f_phi = get_workspace('workspace_' + mode + '_phi.root', 'workspace')

w_delta_phi, f_delta_phi = get_workspace('workspace_' + mode + '_delta_gen_phi_dRmatched_qM.root', 'workspace')
sigma_delta_1.setVal(w_delta_phi.var('sigma_delta_1').getVal());  sigma_delta_2.setVal(w_delta_phi.var('sigma_delta_2').getVal());
fr_delta.setVal(w_delta_phi.var('fr_delta').getVal()); # fr_Bs_1 = w_Bs.var('fr_Bs_1'); fr_Bs_2 = w_Bs.var('fr_Bs_2')
# mean_delta.setVal(w_delta_phi.var('mean_delta').getVal());
sigma_delta_1.setConstant(1); sigma_delta_2.setConstant(1); fr_delta.setConstant(1);
mean_delta.setVal(0.); mean_delta.setConstant(1)

sigma_Bs_1.setVal(w_Bs.var('sigma_Bs_1').getVal());  sigma_Bs_2.setVal(w_Bs.var('sigma_Bs_2').getVal());
# sigma_Bs_3.setVal(w_Bs.var('sigma_Bs_3').getVal());
# sigma_Bs.setVal(w_Bs.var('sigma_Bs').getVal());
# gamma_BW_Bs.setVal(w_Bs.var('gamma_BW_Bs').getVal());
fr_Bs.setVal(w_Bs.var('fr_Bs').getVal());
# fr_Bs_1.setVal(w_Bs.var('fr_Bs_1').getVal()); fr_Bs_2.setVal(w_Bs.var('fr_Bs_2').getVal());
mean_Bs.setVal(w_Bs.var('mean_Bs').getVal());

sigmaCB_phi_1.setVal(w_phi.var('sigmaCB_phi_1').getVal()); alpha_phi_1.setVal(w_phi.var('alpha_phi_1').getVal()); n_phi_1.setVal(w_phi.var('n_phi_1').getVal())
sigmaCB_phi_2.setVal(w_phi.var('sigmaCB_phi_2').getVal()); alpha_phi_2.setVal(w_phi.var('alpha_phi_2').getVal()); n_phi_2.setVal(w_phi.var('n_phi_2').getVal())
fr_phi.setVal(w_phi.var('fr_phi').getVal());
# gamma_BW_phi.setVal(w_phi.var('gamma_BW_phi').getVal());
# sigma_gauss_phi.setVal(w_phi.var('sigma_gauss_phi').getVal());
# sigma_phi.setVal(w_phi.var('sigma_phi').getVal());
# mean_zero_phi.setVal(w_phi.var('mean_zero_phi').getVal());
mean_phi.setVal(w_phi.var('mean_phi').getVal());

sigma_psi_1.setVal(w_psi.var('sigma_psi_1').getVal()); sigma_psi_2.setVal(w_psi.var('sigma_psi_2').getVal());
# sigma_psi_3.setVal(w_psi.var('sigma_psi_3').getVal());
# sigma_psi.setVal(w_psi.var('sigma_psi').getVal());
# gamma_BW_psi.setVal(w_psi.var('gamma_BW_psi').getVal());
fr_psi.setVal(w_psi.var('fr_psi').getVal()); # fr_psi_1.setVal(w_psi.var('fr_psi_1').getVal()); fr_psi_2.setVal(w_psi.var('fr_psi_2').getVal());
mean_psi.setVal(w_psi.var('mean_psi').getVal());

sigma_X_1.setVal(w_X.var('sigma_X_1').getVal()); sigma_X_2.setVal(w_X.var('sigma_X_2').getVal());
# sigma_X_3.setVal(w_X.var('sigma_X_3').getVal());
# sigma_X.setVal(w_X.var('sigma_X').getVal());
# gamma_BW_X.setVal(w_X.var('gamma_BW_X').getVal());
fr_X.setVal(w_X.var('fr_X').getVal()); # fr_X_1.setVal(w_X.var('fr_X_1').getVal()); fr_X_2.setVal(w_X.var('fr_X_2').getVal());
mean_X.setVal(w_X.var('mean_X').getVal());


sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); sigma_Bs_3.setConstant(1);
sigma_Bs.setConstant(1); gamma_BW_Bs.setConstant(1);
fr_Bs.setConstant(1); fr_Bs_1.setConstant(1); fr_Bs_2.setConstant(1);

sigmaCB_phi_1.setConstant(1); alpha_phi_1.setConstant(1); n_phi_1.setConstant(1);
sigmaCB_phi_2.setConstant(1); alpha_phi_2.setConstant(1); n_phi_2.setConstant(1);
gamma_BW_phi.setConstant(1); sigma_gauss_phi.setConstant(1); sigma_phi.setConstant(1)
fr_phi.setConstant(1); mean_zero_phi.setConstant(1)

sigma_psi_1.setConstant(1); sigma_psi_2.setConstant(1); sigma_psi_3.setConstant(1);
sigma_psi.setConstant(1); gamma_BW_psi.setConstant(1)
fr_psi.setConstant(1);  fr_psi_1.setConstant(1); fr_psi_2.setConstant(1)

sigma_X_1.setConstant(1); sigma_X_2.setConstant(1); sigma_X_3.setConstant(1);
sigma_X.setConstant(1); gamma_BW_X.setConstant(1)
fr_X.setConstant(1); fr_X_1.setConstant(1); fr_X_2.setConstant(1)

N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)

###-----###  phi model

sig_delta_1 = ROOT.RooGaussian("sig_delta_1", "", PHI_mass_Cjp, mean_delta, sigma_delta_1)
sig_delta_2 = ROOT.RooGaussian("sig_delta_2", "", PHI_mass_Cjp, mean_delta, sigma_delta_2)
signal_delta = ROOT.RooAddPdf("signal_delta", "signal_delta", ROOT.RooArgList(sig_delta_1, sig_delta_2), ROOT.RooArgList(fr_delta))  ## ---- BASELINE

CB_sum = ROOT.RooAddPdf("CB+CB", "CB_sum", ROOT.RooArgList(CB_phi_1, CB_phi_2), ROOT.RooArgList(fr_phi)) ## ---- BASELINE
# signal_phi = ROOT.RooFFTConvPdf('resolxrelBW', '', PHI_mass_Cjp, relBW_phi, signal_delta)
signal_phi = ROOT.RooFFTConvPdf('resolxCB_sum', '', PHI_mass_Cjp, CB_sum, signal_delta)
model_1D_phi = ROOT.RooAddPdf('model_1D_phi', 'model_1D_phi', ROOT.RooArgList(signal_phi, bkgr_phi), ROOT.RooArgList(N_sig_phi, N_bkgr_phi))

model = {'Bs': model_1D_Bs, 'phi': model_1D_phi, 'control': model_control}
signal = {'Bs': signal_Bs, 'phi': signal_phi, 'control': signal_control}
N = {'Bs': N_sig_Bs, 'phi': N_sig_phi, 'control': N_control[mode]}
N_bkgr =  {'Bs': N_bkgr_Bs, 'phi': N_bkgr_phi, 'control': N_bkgr_control}
mean = {'Bs': mean_Bs, 'phi': mean_phi, 'control': mean_control[mode]}

#############################################################################################

CMS_tdrStyle_lumi.extraText = "Preliminary"

var_discr.setMin(left_discr_data); var_discr.setMax(right_discr_data); var_discr.setBins(nbins_discr_data)
PHI_mass_Cjp.setMin(left_phi_data); PHI_mass_Cjp.setMax(right_phi_data); PHI_mass_Cjp.setBins(nbins_phi_data)
var_control.setMin(left_control_data); var_control.setMax(right_control_data);  var_control.setBins(nbins_control_data)

fr = {'X': fr_X.getVal(), 'psi': fr_psi.getVal()}
sigma_1 = {'X': sigma_X_1.getVal(), 'psi': sigma_psi_1.getVal()}
sigma_2 = {'X': sigma_X_2.getVal(), 'psi': sigma_psi_2.getVal()}
mean_control_MC = {'X': mean_X.getVal(), 'psi': mean_psi.getVal()}
mean_phi_MC = mean_phi.getVal()
mean_Bs_MC = mean_Bs.getVal()

sigma_eff_control = sqrt( fr[mode] * sigma_1[mode]**2 + (1 - fr[mode]) * sigma_2[mode]**2)
sigma_eff_Bs = sqrt( fr_Bs.getVal() * sigma_Bs_1.getVal()**2 + (1 - fr_Bs.getVal()) * sigma_Bs_2.getVal()**2)
window_control = 3 * sigma_eff_control
window_Bs = 3 * sigma_eff_Bs

data = ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp))
data = data.reduce(cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data + ' && ' + cuts_pipi[mode])

#############################################################################################
# control variable

# data_control = data.reduce('TMath::Abs(BU_mass_Cjp - ' + str(mean_Bs_MC) + ') < ' + str(window_Bs) + ' && TMath::Abs(PHI_mass_Cjp - ' + str(mean_phi_MC) + ') < 0.01')
# mean_X.setConstant(1); mean_psi.setConstant(1)
# model_control.fitTo(data_control, RF.Extended(ROOT.kTRUE))
# mean_X.setConstant(0); mean_psi.setConstant(0)
# model_control.fitTo(data_control, RF.Extended(ROOT.kTRUE))
# rrr_sig = model_control.fitTo(data_control, RF.Extended(ROOT.kTRUE), RF.Save())
#
# c_control = ROOT.TCanvas("c_control", "c_control", 800, 600)
# plot_on_frame(var_control, data_control, model_control, ' ', left_control_data, right_control_data, nbins_control_data, plot_control_param[mode], False)
# CMS_tdrStyle_lumi.CMS_lumi( c_control, 2, 0 );
# c_control.Update(); c_control.RedrawAxis(); #c_control.GetFrame().Draw();
# c_control.SaveAs('~/Study/Bs_resonances/preliminary_look_plots/c_control_prelim_' + str(mode) + '.pdf')
#
# ###--- plotting ll ---###
#
# nll = model_control.createNLL(data_control)
# pll = nll.createProfile(ROOT.RooArgSet(N_control[mode]))
#
# c_ll = ROOT.TCanvas("c_ll", "c_ll", 800, 600); ll_left = 0; ll_right = 200
# frame_nll = N_control[mode].frame(RF.Bins(100), RF.Range(ll_left, ll_right)) #N_sig_Bs.getVal() + 40
# frame_nll.SetTitle('')
#
# nll.plotOn(frame_nll, RF.ShiftToZero(), RF.LineColor(ROOT.kGreen))
# # nll.plotOn(frame_nll, RF.LineColor(ROOT.kGreen))
# pll.plotOn(frame_nll, RF.LineColor(ROOT.kRed))
#
# frame_nll.SetMaximum(30.)
# frame_nll.SetMinimum(0.)
# frame_nll.Draw()
#
# line_width = 4
# line_5sigma = ROOT.TLine(ll_left, 12.5, ll_right, 12.5)
# line_5sigma.SetLineWidth(line_width); line_5sigma.SetLineColor(47)
# line_5sigma.Draw();
#
# CMS_tdrStyle_lumi.CMS_lumi( c_ll, 2, 0 );
# c_ll.Update(); c_ll.RedrawAxis(); # c_inclus.GetFrame().Draw();
# c_ll.SaveAs('prelim_control_pll.pdf')
#
#
# # ###-----###
#
# w = ROOT.RooWorkspace("w", True)
# Import = getattr(ROOT.RooWorkspace, 'import')
# Import(w, model_control)
# mc = ROOT.RooStats.ModelConfig("ModelConfig",w)
# mc.SetPdf(w.pdf(model_control.GetName()))
# mc.SetParametersOfInterest(ROOT.RooArgSet(w.var(N_control[mode].GetName())))
# # w.var("N_sig_X").setError(20.)
# mc.SetObservables(ROOT.RooArgSet(w.var(var_control.GetName())))
# # mc.SetNuisanceParameters(ROOT.RooArgSet(w.var('a1_phi' if sPlot_to == 'phi' else 'a1'), w.var('a2_phi' if sPlot_to == 'phi' else 'a2'), w.var(N_bkgr_Bs.GetName()), w.var(mean_Bs.GetName())))
# mc.SetSnapshot(ROOT.RooArgSet(w.var(N_control[mode].GetName())))
# Import(w, mc)
#
# sbModel = w.obj("ModelConfig")
# sbModel.SetName("S+B_model")
# poi = sbModel.GetParametersOfInterest().first()
# bModel = sbModel.Clone()
# bModel.SetName("B_only_model")
# oldval = poi.getVal()
# poi.setVal(0)
# bModel.SetSnapshot(ROOT.RooArgSet(poi))
# poi.setVal(oldval)
# ac = ROOT.RooStats.AsymptoticCalculator(data_control, sbModel, bModel)
# ac.SetOneSidedDiscovery(True)
# asResult = ac.GetHypoTest()
# print ('*' * 40, '\n\n\n\n\n\n', asResult.Print(), '\n\n\n\n\n\n', '*' * 40)

# a1.setConstant(0); a2.setConstant(0); a3.setConstant(0);
# a1_phi.setConstant(0); a2_phi.setConstant(0); a3_phi.setConstant(0);
# N_control[mode].setVal(0); N_control[mode].setConstant(1);
# model_control.fitTo(data_control, RF.Extended(ROOT.kTRUE))
# rrr_null = model_control.fitTo(data_control, RF.Extended(ROOT.kTRUE), RF.Save())
#
# nll_sig  = rrr_sig.minNll()
# nll_null = rrr_null.minNll()
# P = ROOT.TMath.Prob(2*(nll_null - nll_sig), 1) ## !!! Change delta of ndf appropriately
# # S = ROOT.TMath.ErfcInverse(P) * sqrt(2)
# S = ROOT.Math.gaussian_quantile_c(P, 1)
# print ('P=', P, ' nll_sig=', nll_sig, ' nll_null=', nll_null, '\n', 'S=', S)

#############################################################################################
# Bs

# data_Bs = data.reduce('TMath::Abs(X_mass_Cjp - ' + str(mean_control_MC[mode]) + ') < ' + str(window_control) + ' && TMath::Abs(PHI_mass_Cjp - ' + str(mean_phi_MC) + ') < 0.01')
# model_1D_Bs.fitTo(data_Bs, RF.Extended(ROOT.kTRUE))
# model_1D_Bs.fitTo(data_Bs, RF.Extended(ROOT.kTRUE))
# rrr_sig = model_1D_Bs.fitTo(data_Bs, RF.Extended(ROOT.kTRUE), RF.Save())
#
# c_Bs = ROOT.TCanvas("c_Bs", "c_Bs", 800, 600)
# plot_on_frame(var_discr, data_Bs, model_1D_Bs, '', left_discr_data, right_discr_data, nbins_discr_data, plot_discr_param, False)
# CMS_tdrStyle_lumi.CMS_lumi( c_Bs, 2, 0 );
# c_Bs.Update(); c_Bs.RedrawAxis(); #c_Bs.GetFrame().Draw();
# # c_Bs.SaveAs('~/Study/Bs_resonances/preliminary_look_plots/c_Bs_prelim_' + str(mode) + '.pdf')
#
# ###--- plotting ll ---###
#
# nll = model_1D_Bs.createNLL(data_Bs)
# pll = nll.createProfile(ROOT.RooArgSet(N_sig_Bs))
#
# c_ll = ROOT.TCanvas("c_ll", "c_ll", 800, 600); ll_left = 0; ll_right = 200
# frame_nll = N_sig_Bs.frame(RF.Bins(100), RF.Range(ll_left, ll_right)) #N_sig_Bs.getVal() + 40
# frame_nll.SetTitle('')
#
# nll.plotOn(frame_nll, RF.ShiftToZero(), RF.LineColor(ROOT.kGreen))
# # nll.plotOn(frame_nll, RF.LineColor(ROOT.kGreen))
# pll.plotOn(frame_nll, RF.LineColor(ROOT.kRed))
#
# frame_nll.SetMaximum(30.)
# frame_nll.SetMinimum(0.)
# frame_nll.Draw()
#
# line_width = 4
# line_5sigma = ROOT.TLine(ll_left, 12.5, ll_right, 12.5)
# line_5sigma.SetLineWidth(line_width); line_5sigma.SetLineColor(47)
# line_5sigma.Draw();
#
# CMS_tdrStyle_lumi.CMS_lumi( c_ll, 2, 0 );
# c_ll.Update(); c_ll.RedrawAxis(); # c_inclus.GetFrame().Draw();
# c_ll.SaveAs('prelim_Bs_pll.pdf')


# # ###---- Significance ----####
#
# w = ROOT.RooWorkspace("w", True)
# Import = getattr(ROOT.RooWorkspace, 'import')
# Import(w, model_1D_Bs)
# mc = ROOT.RooStats.ModelConfig("ModelConfig",w)
# mc.SetPdf(w.pdf(model_1D_Bs.GetName()))
# mc.SetParametersOfInterest(ROOT.RooArgSet(w.var(N_sig_Bs.GetName())))
# # w.var("N_sig_X").setError(20.)
# mc.SetObservables(ROOT.RooArgSet(w.var(var_discr.GetName())))
# # mc.SetNuisanceParameters(ROOT.RooArgSet(w.var('a1_phi' if sPlot_to == 'phi' else 'a1'), w.var('a2_phi' if sPlot_to == 'phi' else 'a2'), w.var(N_bkgr_Bs.GetName()), w.var(mean_Bs.GetName())))
# mc.SetSnapshot(ROOT.RooArgSet(w.var(N_sig_Bs.GetName())))
# Import(w, mc)
#
# sbModel = w.obj("ModelConfig")
# sbModel.SetName("S+B_model")
# poi = sbModel.GetParametersOfInterest().first()
# bModel = sbModel.Clone()
# bModel.SetName("B_only_model")
# oldval = poi.getVal()
# poi.setVal(0)
# bModel.SetSnapshot(ROOT.RooArgSet(poi))
# poi.setVal(oldval)
# ac = ROOT.RooStats.AsymptoticCalculator(data_Bs, sbModel, bModel)
# ac.SetOneSidedDiscovery(True)
# asResult = ac.GetHypoTest()
# print ('*' * 40, '\n\n\n\n\n\n', asResult.Print(), '\n\n\n\n\n\n', '*' * 40)


# a1.setConstant(0); a2.setConstant(0); a3.setConstant(0);
# a1_phi.setConstant(0); a2_phi.setConstant(0); a3_phi.setConstant(0);
# N_sig_Bs.setVal(0); N_sig_Bs.setConstant(1);
# model_1D_Bs.fitTo(data_Bs, RF.Extended(ROOT.kTRUE))
# rrr_null = model_1D_Bs.fitTo(data_Bs, RF.Extended(ROOT.kTRUE), RF.Save())
#
# nll_sig  = rrr_sig.minNll()
# nll_null = rrr_null.minNll()
# P = ROOT.TMath.Prob(2*(nll_null - nll_sig), 1) ## !!! Change delta of ndf appropriately
# # S = ROOT.TMath.ErfcInverse(P) * sqrt(2)
# S = ROOT.Math.gaussian_quantile_c(P, 1)
# print ('P=', P, ' nll_sig=', nll_sig, ' nll_null=', nll_null, '\n', 'S=', S)

# c_ll = ROOT.TCanvas("c_ll", "c_ll", 800, 600)
# frame_nll = N[sPlot_to].frame(RF.Bins(80), RF.Range(80,160))
#
# nll.plotOn(frame_nll, RF.ShiftToZero())
# nll.plotOn(frame_nll, RF.LineColor(ROOT.kGreen))
# pll.plotOn(frame_nll, RF.LineColor(ROOT.kRed))
#
# frame_nll.SetMaximum(3.)
# frame_nll.SetMinimum(0.)
# frame_nll.Draw()
# c_ll.SaveAs('pll.pdf')


#############################################################################################
# phi

data_phi = data.reduce('TMath::Abs(BU_mass_Cjp - ' + str(mean_Bs_MC) + ') < ' + str(window_Bs) + ' && TMath::Abs(X_mass_Cjp - ' + str(mean_control_MC[mode]) + ') < ' + str(window_control))
mean_phi.setConstant(1);
model_1D_phi.fitTo(data_phi, RF.Extended(ROOT.kTRUE))
mean_phi.setConstant(0);
model_1D_phi.fitTo(data_phi, RF.Extended(ROOT.kTRUE))
rrr_sig = model_1D_phi.fitTo(data_phi, RF.Extended(ROOT.kTRUE), RF.Save())

c_phi = ROOT.TCanvas("c_phi", "c_phi", 800, 600)
plot_on_frame(PHI_mass_Cjp, data_phi, model_1D_phi, ' ', left_phi_data, right_phi_data, nbins_phi_data, plot_phi_param, False)
CMS_tdrStyle_lumi.CMS_lumi( c_phi, 2, 0 );
c_phi.Update(); c_phi.RedrawAxis(); #c_phi.GetFrame().Draw();
# c_phi.SaveAs('~/Study/Bs_resonances/preliminary_look_plots/c_phi_prelim_' + str(mode) + '.pdf')


###--- plotting ll ---###

nll = model_1D_phi.createNLL(data_phi)
pll = nll.createProfile(ROOT.RooArgSet(N_sig_phi))

c_ll = ROOT.TCanvas("c_ll", "c_ll", 800, 600); ll_left = 0; ll_right = 200
frame_nll = N_sig_phi.frame(RF.Bins(100), RF.Range(ll_left, ll_right)) #N_sig_Bs.getVal() + 40
frame_nll.SetTitle('')

nll.plotOn(frame_nll, RF.ShiftToZero(), RF.LineColor(ROOT.kGreen))
# nll.plotOn(frame_nll, RF.LineColor(ROOT.kGreen))
pll.plotOn(frame_nll, RF.LineColor(ROOT.kRed))

frame_nll.SetMaximum(30.)
frame_nll.SetMinimum(0.)
frame_nll.Draw()

line_width = 4
line_5sigma = ROOT.TLine(ll_left, 12.5, ll_right, 12.5)
line_5sigma.SetLineWidth(line_width); line_5sigma.SetLineColor(47)
line_5sigma.Draw();

CMS_tdrStyle_lumi.CMS_lumi( c_ll, 2, 0 );
c_ll.Update(); c_ll.RedrawAxis(); # c_inclus.GetFrame().Draw();
c_ll.SaveAs('prelim_phi_pll.pdf')

# # ###-----###
#
# w = ROOT.RooWorkspace("w", True)
# Import = getattr(ROOT.RooWorkspace, 'import')
# Import(w, model_1D_phi)
# mc = ROOT.RooStats.ModelConfig("ModelConfig",w)
# mc.SetPdf(w.pdf(model_1D_phi.GetName()))
# mc.SetParametersOfInterest(ROOT.RooArgSet(w.var(N_sig_phi.GetName())))
# # w.var("N_sig_X").setError(20.)
# mc.SetObservables(ROOT.RooArgSet(w.var(PHI_mass_Cjp.GetName())))
# # mc.SetNuisanceParameters(ROOT.RooArgSet(w.var('a1_phi' if sPlot_to == 'phi' else 'a1'), w.var('a2_phi' if sPlot_to == 'phi' else 'a2'), w.var(N_bkgr_Bs.GetName()), w.var(mean_Bs.GetName())))
# mc.SetSnapshot(ROOT.RooArgSet(w.var(N_sig_phi.GetName())))
# Import(w, mc)
#
# sbModel = w.obj("ModelConfig")
# sbModel.SetName("S+B_model")
# poi = sbModel.GetParametersOfInterest().first()
# bModel = sbModel.Clone()
# bModel.SetName("B_only_model")
# oldval = poi.getVal()
# poi.setVal(0)
# bModel.SetSnapshot(ROOT.RooArgSet(poi))
# poi.setVal(oldval)
# ac = ROOT.RooStats.AsymptoticCalculator(data_phi, sbModel, bModel)
# ac.SetOneSidedDiscovery(True)
# asResult = ac.GetHypoTest()
# print ('*' * 40, '\n\n\n\n\n\n', asResult.Print(), '\n\n\n\n\n\n', '*' * 40)



# a1.setConstant(0); a2.setConstant(0); a3.setConstant(0);
# a1_phi.setConstant(0); a2_phi.setConstant(0); a3_phi.setConstant(0);
# N_sig_phi.setVal(0); N_sig_phi.setConstant(1);
# model_1D_phi.fitTo(data_phi, RF.Extended(ROOT.kTRUE))
# rrr_null = model_1D_phi.fitTo(data_phi, RF.Extended(ROOT.kTRUE), RF.Save())
#
# nll_sig  = rrr_sig.minNll()
# nll_null = rrr_null.minNll()
# P = ROOT.TMath.Prob(2*(nll_null - nll_sig), 1) ## !!! Change delta of ndf appropriately
# # S = ROOT.TMath.ErfcInverse(P) * sqrt(2)
# S = ROOT.Math.gaussian_quantile_c(P, 1)
# print ('P=', P, ' nll_sig=', nll_sig, ' nll_null=', nll_null, '\n', 'S=', S)

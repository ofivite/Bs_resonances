from RooSpace import *
from cuts import *
from math import sqrt

file_data = ROOT.TFile('new_noKaon_fabs_with_pt&eta_979cfd3.root')
# file_data = ROOT.TFile('new_noKaon_fabs_76e92fd.root')
# file_data = ROOT.TFile('new_noKaon_9988200.root')
# file_data = ROOT.TFile('new.root')

w_Bs, f_Bs = get_workspace('workspace_' + mode + '_Bs.root', 'workspace')
w_psi, f_psi = get_workspace('workspace_psi_control.root', 'workspace')
w_X, f_X = get_workspace('workspace_X_control.root', 'workspace')
w_phi, f_phi = get_workspace('workspace_' + mode + '_phi.root', 'workspace')


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


##   ----------------------    ##
##      DATA: cut & plot       ##
##   ----------------------    ##

CMS_tdrStyle_lumi.extraText       = "Preliminary"

fr = {'X': fr_X.getVal(), 'psi': fr_psi.getVal()}
sigma_1 = {'X': sigma_X_1.getVal(), 'psi': sigma_psi_1.getVal()}
sigma_2 = {'X': sigma_X_2.getVal(), 'psi': sigma_psi_2.getVal()}
mean_control_MC = {'X': mean_X.getVal(), 'psi': mean_psi.getVal()}
mean_phi_MC = mean_phi.getVal()
mean_Bs_MC = mean_Bs.getVal()
sigma_eff_control = sqrt( fr[mode] * sigma_1[mode]**2 + (1 - fr[mode]) * sigma_2[mode]**2)
window_control = 3 * sigma_eff_control

sigma_eff_Bs = sqrt( fr_Bs.getVal() * sigma_Bs_1.getVal()**2 + (1 - fr_Bs.getVal()) * sigma_Bs_2.getVal()**2)
window_Bs = 3 * sigma_eff_Bs


# sigma_eff_Bs = 0.009723228705468944; sigma_eff_control = 0.004677264225365235;
# mean_Bs_MC = 5.369978885882736; mean_phi_MC = 1.019470200920036; mean_control_MC = 3.6862772970893425

var_discr.setMin(left_discr_data); var_discr.setMax(right_discr_data)
PHI_mass_Cjp.setMin(left_phi_data); PHI_mass_Cjp.setMax(right_phi_data)
var_control.setMin(left_control_data); var_control.setMax(right_control_data)
data = ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp, SAMEEVENT), cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data  + ' && ' + cuts_pipi[mode])
#
# #
# # bkgr_control = ROOT.RooBernstein('bkgr_control', '', var_control, ROOT.RooArgList(a1, a2, a3, a4))
# model_X = ROOT.RooAddPdf('model_X', 'model_X', ROOT.RooArgList(signal_X, bkgr_control), ROOT.RooArgList(N_sig_X, N_bkgr_control))
# model_psi = ROOT.RooAddPdf('model_psi', 'model_psi', ROOT.RooArgList(signal_psi, bkgr_control), ROOT.RooArgList(N_sig_psi, N_bkgr_control))
# control_models = {'X': model_X, 'psi': model_psi}
# model_control = control_models[mode]


#############################################################################################
# control variable

# data_control = data.reduce('TMath::Abs(BU_mass_Cjp - ' + str(mean_Bs_MC) + ') < ' + str(window_Bs) + ' && TMath::Abs(PHI_mass_Cjp - ' + str(mean_phi_MC) + ') < 0.01')
# mean_X.setConstant(1); mean_psi.setConstant(1)
# model_control.fitTo(data_control, RF.Extended(ROOT.kTRUE))
# model_control.fitTo(data_control, RF.Extended(ROOT.kTRUE))
# mean_X.setConstant(0); mean_psi.setConstant(0)
# model_control.fitTo(data_control, RF.Extended(ROOT.kTRUE))
# model_control.fitTo(data_control, RF.Extended(ROOT.kTRUE))
#
# # model_control.fitTo(data, RF.Extended(ROOT.kTRUE))
# # model_control.fitTo(data, RF.Extended(ROOT.kTRUE))
# c_control = ROOT.TCanvas("c_control", "c_control", 800, 600)
# plot_on_frame(var_control, data_control, model_control, ' ', left_control_data, right_control_data, nbins_control_data, plot_control_param[mode], False)
# CMS_tdrStyle_lumi.CMS_lumi( c_control, 2, 0 );
# c_control.Update(); c_control.RedrawAxis(); #c_control.GetFrame().Draw();
# c_control.SaveAs('~/Study/Bs_resonances/preliminary_look_plots/c_control_prelim_' + str(mode) + '.pdf')
#
# ###-----###
#
# w = ROOT.RooWorkspace("w", True)
# Import = getattr(ROOT.RooWorkspace, 'import')
# Import(w, model_control)
# mc = ROOT.RooStats.ModelConfig("ModelConfig",w)
# mc.SetPdf(w.pdf("model_" + str(mode)))
# mc.SetParametersOfInterest(ROOT.RooArgSet(w.var("N_sig_" + str(mode))))
# # w.var("N_sig_X").setError(20.)
# mc.SetObservables(ROOT.RooArgSet(w.var("X_mass_Cjp")))
# mc.SetNuisanceParameters(ROOT.RooArgSet(w.var("a1"), w.var("a2"), w.var("N_bkgr_control"), w.var("mean_" + str(mode))))
# mc.SetSnapshot(ROOT.RooArgSet(w.var("N_sig_" + str(mode))))
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
# asResult.Print()


#############################################################################################
# Bs

# data_Bs = data.reduce('TMath::Abs(X_mass_Cjp - ' + str(mean_control_MC[mode]) + ') < ' + str(window_control) + ' && TMath::Abs(PHI_mass_Cjp - ' + str(mean_phi_MC) + ') < 0.01')
# model_1D_Bs.fitTo(data_Bs, RF.Extended(ROOT.kTRUE))
# model_1D_Bs.fitTo(data_Bs, RF.Extended(ROOT.kTRUE))
# model_1D_Bs.fitTo(data_Bs, RF.Extended(ROOT.kTRUE))
#
# c_Bs = ROOT.TCanvas("c_Bs", "c_Bs", 800, 600)
# plot_on_frame(var_discr, data_Bs, model_1D_Bs, '', left_discr_data, right_discr_data, nbins_discr_data, plot_discr_param, False)
# CMS_tdrStyle_lumi.CMS_lumi( c_Bs, 2, 0 );
# c_Bs.Update(); c_Bs.RedrawAxis(); #c_Bs.GetFrame().Draw();
# c_Bs.SaveAs('~/Study/Bs_resonances/preliminary_look_plots/c_Bs_prelim_' + str(mode) + '.pdf')
#
# ###-----###
#
# w = ROOT.RooWorkspace("w", True)
# Import = getattr(ROOT.RooWorkspace, 'import')
# Import(w, model_1D_Bs)
# mc = ROOT.RooStats.ModelConfig("ModelConfig",w)
# mc.SetPdf(w.pdf('model_1D_Bs'))
# mc.SetParametersOfInterest(ROOT.RooArgSet(w.var('N_sig_Bs')))
# # w.var("N_sig_X").setError(20.)
# mc.SetObservables(ROOT.RooArgSet(w.var("BU_mass_Cjp")))
# mc.SetNuisanceParameters(ROOT.RooArgSet(w.var("a1"), w.var("a2"), w.var("N_bkgr_Bs"), w.var('mean_Bs')))
# mc.SetSnapshot(ROOT.RooArgSet(w.var('N_sig_Bs')))
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
# asResult.Print()

#############################################################################################
# phi

data_phi = data.reduce('TMath::Abs(BU_mass_Cjp - ' + str(mean_Bs_MC) + ') < ' + str(window_Bs) + ' && TMath::Abs(X_mass_Cjp - ' + str(mean_control_MC[mode]) + ') < ' + str(window_control))
model_1D_phi.fitTo(data_phi, RF.Extended(ROOT.kTRUE))
model_1D_phi.fitTo(data_phi, RF.Extended(ROOT.kTRUE))
model_1D_phi.fitTo(data_phi, RF.Extended(ROOT.kTRUE))

c_phi = ROOT.TCanvas("c_phi", "c_phi", 800, 600)
plot_on_frame(PHI_mass_Cjp, data_phi, model_1D_phi, ' ', left_phi_data, right_phi_data, nbins_phi_data, plot_phi_param, False)
CMS_tdrStyle_lumi.CMS_lumi( c_phi, 2, 0 );
c_phi.Update(); c_phi.RedrawAxis(); #c_phi.GetFrame().Draw();
c_phi.SaveAs('~/Study/Bs_resonances/preliminary_look_plots/c_phi_prelim_' + str(mode) + '.pdf')

###-----###

w = ROOT.RooWorkspace("w", True)
Import = getattr(ROOT.RooWorkspace, 'import')
Import(w, model_1D_phi)
mc = ROOT.RooStats.ModelConfig("ModelConfig",w)
mc.SetPdf(w.pdf('model_1D_phi'))
mc.SetParametersOfInterest(ROOT.RooArgSet(w.var('N_sig_phi')))
# w.var("N_sig_X").setError(20.)
mc.SetObservables(ROOT.RooArgSet(w.var("PHI_mass_Cjp")))
mc.SetNuisanceParameters(ROOT.RooArgSet(w.var("a1_phi"), w.var("a2_phi"), w.var("N_bkgr_phi"), w.var('mean_phi')))
mc.SetSnapshot(ROOT.RooArgSet(w.var('N_sig_phi')))
Import(w, mc)

sbModel = w.obj("ModelConfig")
sbModel.SetName("S+B_model")
poi = sbModel.GetParametersOfInterest().first()
bModel = sbModel.Clone()
bModel.SetName("B_only_model")
oldval = poi.getVal()
poi.setVal(0)
bModel.SetSnapshot(ROOT.RooArgSet(poi))
poi.setVal(oldval)
ac = ROOT.RooStats.AsymptoticCalculator(data_phi, sbModel, bModel)
ac.SetOneSidedDiscovery(True)
asResult = ac.GetHypoTest()
asResult.Print()

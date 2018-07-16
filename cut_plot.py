from RooSpace import *
from cuts import *
from math import sqrt

files_MC = {'X': 'BsToXPhi_Smatch_v1_min_e233994.root', 'psi':'BsToPsiPhi_Smatch_v1_min_with_pt&eta_8e25fe7.root'}
# files_MC = {'X': 'BsToXPhi_step3_6c21fba.root', 'psi':'BsToPsiPhi_step3_4a91161.root'}
# files_MC = {'X': 'BsToXPhi_matched_all_1892449.root', 'psi':'BsToPsiPhi_matched_all_1519f1b.root'}
# files_MC = {'X': 'SimpleFileMC_b715x_0_14000.root', 'psi':'SimpleFileMC_b715psi_0_14000.root'}
file_MC = ROOT.TFile(files_MC[mode])

# file_data = ROOT.TFile('new.root')
# file_data = ROOT.TFile('new_noKaon_9988200.root')
file_data = ROOT.TFile('new_noKaon_fabs_with_pt&eta_979cfd3.root')



# c = ROOT.TCanvas("c", "c", 1700, 650)
# c.Divide(3,1)

var_discr.setMin(left_discr_MC); var_discr.setMax(right_discr_MC)
PHI_mass_Cjp.setMin(left_phi_MC); PHI_mass_Cjp.setMax(right_phi_MC)
var_control.setMin(left_control_MC); var_control.setMax(right_control_MC)

data_MC = (ROOT.RooDataSet('data_MC', '', file_MC.Get('mytree'), ROOT.RooArgSet(ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp),
ROOT.RooArgSet(MoID_mu1, MoID_mu2, MoID_pi1, MoID_pi2, MoID_K1, MoID_K2)), ROOT.RooArgSet(ROOT.RooArgSet(ROOT.RooArgSet(mu_max_pt, mu_min_pt, mu_max_eta, mu_min_eta),
ROOT.RooArgSet(K_max_pt, K_min_pt, K_max_eta, K_min_eta, pi_max_pt, pi_min_pt, pi_max_eta, pi_min_eta)), ROOT.RooArgSet(dR_mu1, dR_mu2, dR_pi1, dR_pi2, dR_K1, dR_K2, BU_pt_Cjp, BU_eta_Cjp))),
                   cuts_Bs_MC + '&&' + cuts_phi_MC + '&&' + cuts_control_MC + ' && ' + cuts_pipi[mode] + '&&' + cuts_match_ID[mode] + '&&' + cuts_match_dR))

##        ---------------       ##
##           FIT OF MC          ##
##        ---------------       ##

CMS_tdrStyle_lumi.extraText       = "Simulation Preliminary"
CMS_tdrStyle_lumi.setTDRStyle()
print '\n\n' + 30*'#' + '\n\n\n         MC psi(2S): Bs mass now         \n\n\n' + 30*'#' + '\n\n'

###-----###

model_1D_Bs.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
model_1D_Bs.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
mean_Bs.setVal(5.366);
mean_Bs.setMin(mean_Bs.getVal() - 0.005); mean_Bs.setMax(mean_Bs.getVal() + 0.005)
sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); sigma_Bs_3.setConstant(1); fr_Bs.setConstant(1); fr_Bs_1.setConstant(1); fr_Bs_2.setConstant(1);
a1.setConstant(1); a2.setConstant(1);
model_1D_Bs.fitTo(data_MC, RF.Extended(ROOT.kTRUE))

###-----###

mean_phi.setVal(1.0195);
# gamma_BW_phi.setVal(0.004247); gamma_BW_phi.setConstant(1)
model_1D_phi.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
model_1D_phi.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
sigmaCB_phi_1.setConstant(1); alpha_phi_1.setConstant(1); n_phi_1.setConstant(1); fr_phi.setConstant(1)
sigmaCB_phi_2.setConstant(1); alpha_phi_2.setConstant(1); n_phi_2.setConstant(1);
a1_phi.setConstant(1); a2_phi.setConstant(1);
gamma_BW_phi.setConstant(1);
model_1D_phi.fitTo(data_MC, RF.Extended(ROOT.kTRUE))

###-----###

model_control.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
model_control.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
sigma_psi_1.setConstant(1); sigma_psi_2.setConstant(1); sigma_psi_3.setConstant(1); fr_psi.setConstant(1); fr_psi_1.setConstant(1); fr_psi_2.setConstant(1)
sigma_X_1.setConstant(1); sigma_X_2.setConstant(1); sigma_X_3.setConstant(1); fr_X.setConstant(1); fr_X_1.setConstant(1); fr_X_2.setConstant(1)
a1.setConstant(1); a2.setConstant(1)
model_control.fitTo(data_MC, RF.Extended(ROOT.kTRUE))

###-----###

mean_Bs.setMin(mean_Bs.getVal() - 0.005); mean_Bs.setMax(mean_Bs.getVal() + 0.005)
sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); sigma_Bs_3.setConstant(1); fr_Bs.setConstant(1); fr_Bs_1.setConstant(1); fr_Bs_2.setConstant(1);
# a1.setVal(0.2); a2.setVal(0.2); a3.setVal(0.2); a4.setVal(0.2)
# a1_phi.setVal(0.2); a2_phi.setVal(0.2); a3_phi.setVal(0.2); a4_phi.setVal(0.2)
# N_sig_2D.setVal(100.); N_sig_2D.setMax(200.)
# N_bb_2D.setVal(30000.); N_sb_2D.setVal(400.); N_bs_2D.setVal(450.); N_ss_2D.setVal(2700.);
# N_bb_2D.setMin(5000.); N_sb_2D.setMin(10000.); N_bs_2D.setMin(0.); N_ss_2D.setMin(1000.);
# N_bb_2D.setMax(30000.); N_sb_2D.setMax(30000.); N_bs_2D.setMax(1000.); N_ss_2D.setMax(4000.);
# N_ss_2D.setConstant(1); N_bs_2D.setConstant(1); N_sb_2D.setConstant(1); N_bb_2D.setConstant(1);
# sigma_phi_1.setConstant(1); sigma_phi_2.setConstant(1); fr_phi.setConstant(1);
# mean_phi.setConstant(1); sigmaCB_phi_1.setConstant(1); alpha_phi_1.setConstant(1); n_phi_1.setConstant(1);
# mean_phi.setMin(mean_phi.getVal() - 0.0005); mean_phi.setMax(mean_phi.getVal() + 0.0005)
sigmaCB_phi_1.setConstant(1); alpha_phi_1.setConstant(1); n_phi_1.setConstant(1); fr_phi.setConstant(1)
sigmaCB_phi_2.setConstant(1); alpha_phi_2.setConstant(1); n_phi_2.setConstant(1);

# mean_phi.setConstant(1);
sigma_psi_1.setConstant(1); sigma_psi_2.setConstant(1); sigma_psi_3.setConstant(1); fr_psi.setConstant(1); fr_psi_1.setConstant(1); fr_psi_2.setConstant(1)
sigma_X_1.setConstant(1); sigma_X_2.setConstant(1); sigma_X_3.setConstant(1); fr_X.setConstant(1); fr_X_1.setConstant(1); fr_X_2.setConstant(1)
# gamma_BW_X.setConstant(1); sigma_X.setConstant(1)
a1_phi.setConstant(0); a2_phi.setConstant(0);
a1.setConstant(0); a2.setConstant(0);


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

data_control = data.reduce('TMath::Abs(BU_mass_Cjp - ' + str(mean_Bs_MC) + ') < ' + str(window_Bs) + ' && TMath::Abs(PHI_mass_Cjp - ' + str(mean_phi_MC) + ') < 0.01')
mean_X.setConstant(1); mean_psi.setConstant(1)
model_control.fitTo(data_control, RF.Extended(ROOT.kTRUE))
model_control.fitTo(data_control, RF.Extended(ROOT.kTRUE))
mean_X.setConstant(0); mean_psi.setConstant(0)
model_control.fitTo(data_control, RF.Extended(ROOT.kTRUE))
model_control.fitTo(data_control, RF.Extended(ROOT.kTRUE))

# model_control.fitTo(data, RF.Extended(ROOT.kTRUE))
# model_control.fitTo(data, RF.Extended(ROOT.kTRUE))
c_control = ROOT.TCanvas("c_control", "c_control", 800, 600)
plot_on_frame(var_control, data_control, model_control, ' ', left_control_data, right_control_data, nbins_control_data, plot_control_param[mode], False)
CMS_tdrStyle_lumi.CMS_lumi( c_control, 2, 0 );
c_control.Update(); c_control.RedrawAxis(); c_control.GetFrame().Draw();
c_control.SaveAs('~/Study/Bs_resonances/Bs_' + str(mode) + 'phi_plots/c_control_prelim_' + str(mode) + '.pdf')

###-----###

w = ROOT.RooWorkspace("w", True)
Import = getattr(ROOT.RooWorkspace, 'import')
Import(w, model_control)
mc = ROOT.RooStats.ModelConfig("ModelConfig",w)
mc.SetPdf(w.pdf("model_" + str(mode)))
mc.SetParametersOfInterest(ROOT.RooArgSet(w.var("N_sig_" + str(mode))))
# w.var("N_sig_X").setError(20.)
mc.SetObservables(ROOT.RooArgSet(w.var("X_mass_Cjp")))
mc.SetNuisanceParameters(ROOT.RooArgSet(w.var("a1"), w.var("a2"), w.var("N_bkgr_control"), w.var("mean_" + str(mode))))
mc.SetSnapshot(ROOT.RooArgSet(w.var("N_sig_" + str(mode))))
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
ac = ROOT.RooStats.AsymptoticCalculator(data_control, sbModel, bModel)
ac.SetOneSidedDiscovery(True)
asResult = ac.GetHypoTest()
asResult.Print()


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
# c_Bs.Update(); c_Bs.RedrawAxis(); c_Bs.GetFrame().Draw();
# c_Bs.SaveAs('~/Study/Bs_resonances/Bs_' + str(mode) + 'phi_plots/c_Bs_prelim_' + str(mode) + '.pdf')
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

# data_phi = data.reduce('TMath::Abs(BU_mass_Cjp - ' + str(mean_Bs_MC) + ') < ' + str(window_Bs) + ' && TMath::Abs(X_mass_Cjp - ' + str(mean_control_MC[mode]) + ') < ' + str(window_control))
# model_1D_phi.fitTo(data_phi, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
# model_1D_phi.fitTo(data_phi, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
# model_1D_phi.fitTo(data_phi, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
#
# c_phi = ROOT.TCanvas("c_phi", "c_phi", 800, 600)
# plot_on_frame(PHI_mass_Cjp, data_phi, model_1D_phi, ' ', left_phi_data, right_phi_data, nbins_phi_data, plot_phi_param, False)
# CMS_tdrStyle_lumi.CMS_lumi( c_phi, 2, 0 );
# c_phi.Update(); c_phi.RedrawAxis(); c_phi.GetFrame().Draw();
# c_phi.SaveAs('~/Study/Bs_resonances/Bs_' + str(mode) + 'phi_plots/c_phi_prelim_' + str(mode) + '.pdf')
#
# ###-----###
#
# w = ROOT.RooWorkspace("w", True)
# Import = getattr(ROOT.RooWorkspace, 'import')
# Import(w, model_1D_phi)
# mc = ROOT.RooStats.ModelConfig("ModelConfig",w)
# mc.SetPdf(w.pdf('model_1D_phi'))
# mc.SetParametersOfInterest(ROOT.RooArgSet(w.var('N_sig_phi')))
# # w.var("N_sig_X").setError(20.)
# mc.SetObservables(ROOT.RooArgSet(w.var("PHI_mass_Cjp")))
# mc.SetNuisanceParameters(ROOT.RooArgSet(w.var("a1_phi"), w.var("a2_phi"), w.var("N_bkgr_phi"), w.var('mean_phi')))
# mc.SetSnapshot(ROOT.RooArgSet(w.var('N_sig_phi')))
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
# asResult.Print()

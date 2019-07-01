from RooSpace import *
from DataExplorer import DataExplorer
import CMS_tdrStyle_lumi

from math import sqrt
import json
from numpy import array

CMS_tdrStyle_lumi.extraText = "Preliminary"
#
var_discr.setMin(left_discr_data); var_discr.setMax(right_discr_data); var_discr.setBins(nbins_discr_data)
PHI_mass_Cjp.setMin(left_phi_data); PHI_mass_Cjp.setMax(right_phi_data); PHI_mass_Cjp.setBins(nbins_phi_data)
var_control.setMin(left_control_data); var_control.setMax(right_control_data);  var_control.setBins(nbins_control_data)
#
file_data = ROOT.TFile('new_2_with_more_B0_e3de87.root')
data = ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp))
data = data.reduce(cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data + ' && ' + cuts_pipi[MODE])
#
chi2_results = {}

            #------------------#
            ##  fixing shape  ##
            #------------------#

w_Bs, f_Bs = get_workspace('workspace_' + MODE + '_Bs.root', 'workspace')
w_psi, f_psi = get_workspace('workspace_psi_control.root', 'workspace')
w_X, f_X = get_workspace('workspace_X_control.root', 'workspace')
w_phi, f_phi = get_workspace('workspace_' + MODE + '_phi.root', 'workspace')

###
w_delta_phi, f_delta_phi = get_workspace('workspace_' + MODE + '_delta_gen_phi_dRmatched_qM.root', 'workspace')
sigma_delta_1.setVal(w_delta_phi.var('sigma_delta_1').getVal());  sigma_delta_2.setVal(w_delta_phi.var('sigma_delta_2').getVal());
fr_delta.setVal(w_delta_phi.var('fr_delta').getVal()); # fr_Bs_1 = w_Bs.var('fr_Bs_1'); fr_Bs_2 = w_Bs.var('fr_Bs_2')
# mean_delta.setVal(w_delta_phi.var('mean_delta').getVal());

###
sigma_Bs_1.setVal(w_Bs.var('sigma_Bs_1').getVal());  sigma_Bs_2.setVal(w_Bs.var('sigma_Bs_2').getVal());
# sigma_Bs_3.setVal(w_Bs.var('sigma_Bs_3').getVal());
# sigma_Bs.setVal(w_Bs.var('sigma_Bs').getVal());
# gamma_BW_Bs.setVal(w_Bs.var('gamma_BW_Bs').getVal());
fr_Bs.setVal(w_Bs.var('fr_Bs').getVal());
# fr_Bs_1.setVal(w_Bs.var('fr_Bs_1').getVal()); fr_Bs_2.setVal(w_Bs.var('fr_Bs_2').getVal());
mean_Bs.setVal(w_Bs.var('mean_Bs').getVal());

###
sigmaCB_phi_1.setVal(w_phi.var('sigmaCB_phi_1').getVal()); alpha_phi_1.setVal(w_phi.var('alpha_phi_1').getVal()); n_phi_1.setVal(w_phi.var('n_phi_1').getVal())
sigmaCB_phi_2.setVal(w_phi.var('sigmaCB_phi_2').getVal()); alpha_phi_2.setVal(w_phi.var('alpha_phi_2').getVal()); n_phi_2.setVal(w_phi.var('n_phi_2').getVal())
fr_phi.setVal(w_phi.var('fr_phi').getVal());
# gamma_BW_phi.setVal(w_phi.var('gamma_BW_phi').getVal());
# sigma_gauss_phi.setVal(w_phi.var('sigma_gauss_phi').getVal());
# sigma_phi.setVal(w_phi.var('sigma_phi').getVal());
# mean_zero_phi.setVal(w_phi.var('mean_zero_phi').getVal());
mean_phi.setVal(w_phi.var('mean_phi').getVal());

###
sigma_psi_1.setVal(w_psi.var('sigma_psi_1').getVal()); sigma_psi_2.setVal(w_psi.var('sigma_psi_2').getVal());
# sigma_psi_3.setVal(w_psi.var('sigma_psi_3').getVal());
# sigma_psi.setVal(w_psi.var('sigma_psi').getVal());
# gamma_BW_psi.setVal(w_psi.var('gamma_BW_psi').getVal());
fr_psi.setVal(w_psi.var('fr_psi').getVal()); # fr_psi_1.setVal(w_psi.var('fr_psi_1').getVal()); fr_psi_2.setVal(w_psi.var('fr_psi_2').getVal());
mean_psi.setVal(w_psi.var('mean_psi').getVal());

###
sigma_X_1.setVal(w_X.var('sigma_X_1').getVal()); sigma_X_2.setVal(w_X.var('sigma_X_2').getVal());
# sigma_X_3.setVal(w_X.var('sigma_X_3').getVal());
# sigma_X.setVal(w_X.var('sigma_X').getVal());
# gamma_BW_X.setVal(w_X.var('gamma_BW_X').getVal());
fr_X.setVal(w_X.var('fr_X').getVal()); # fr_X_1.setVal(w_X.var('fr_X_1').getVal()); fr_X_2.setVal(w_X.var('fr_X_2').getVal());
mean_X.setVal(w_X.var('mean_X').getVal());

###########################################################################################################

sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); sigma_Bs_3.setConstant(1);
sigma_Bs.setConstant(1); gamma_BW_Bs.setConstant(1);
fr_Bs.setConstant(1); fr_Bs_1.setConstant(1); fr_Bs_2.setConstant(1);

sigma_delta_1.setConstant(1); sigma_delta_2.setConstant(1); fr_delta.setConstant(1);
mean_delta.setVal(0.); mean_delta.setConstant(1)

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


            #---------------#
            ##  Inclusive  ##
            #---------------#

# file_out_data = open('/home/yaourt/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/' + MODE +'_data_evtN.txt', 'w')

DE_inclus = DataExplorer(data, model[sPlot_cut], var[sPlot_cut], poi=N[sPlot_cut], name=MODE)
DE_inclus.fit(is_extended=True, is_sum_w2=False)
#
DE_inclus.set_regions()
data_sig, data_side = DE_inclus.get_regions()
#
c_inclus = ROOT.TCanvas("c_inclus", "c_inclus", 800, 600); CMS_tdrStyle_lumi.CMS_lumi(c_inclus, 2, 0);
frame_inclus = DE_inclus.plot_on_var();
chi2_results.update(DE_inclus.chi2_test(frame_inclus))
#
frame_inclus_max = frame_inclus.GetMaximum(); coeffs = array([0.75, 0.85, 0.95]) if MODE == 'X' else array([0.5, 0.62, 0.75])
y_sdb_left, y_sr, y_sdb_right = frame_inclus_max*coeffs
frame_inclus = DE_inclus.plot_regions(frame_inclus, y_sdb_left, y_sr, y_sdb_right)
frame_inclus.Draw()
# c_inclus.Update(); c_inclus.RedrawAxis(); #c_inclus.GetFrame().Draw();
# c_inclus.SaveAs('~/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/c_inclus___' + str(MODE) + refl_line + '.pdf')

            #-------------#
            ##  sPlot I  ##
            #-------------#

if REFL_ON and MODE == 'psi':  N_B0_refl.setVal(9.); N_B0_refl.setConstant(0)
else:        N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)
if sPlot_from == 'Bs' and MODE == 'X': mean[sPlot_from].setConstant(1)

DE_1 = DataExplorer(data=data_sig, model=model[sPlot_from], var=var[sPlot_from], poi=N[sPlot_from], name=sPlot_from)
DE_1.fit(fix_float=[a1, a2, a3, a4], is_extended=True, is_sum_w2=False)
#
c_sPlot_1 = ROOT.TCanvas("c_sPlot_1", "c_sPlot_1", 800, 600); CMS_tdrStyle_lumi.CMS_lumi(c_sPlot_1, 2, 0);
frame_DE_1 = DE_1.plot_on_var()
chi2_results.update(DE_1.chi2_test(frame_DE_1))
frame_DE_1.Draw()
# c_sPlot_1.Update(); c_sPlot_1.RedrawAxis(); # c_sPlot_1.GetFrame().Draw();
# c_sPlot_1.SaveAs('~/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/c_sPlot_1_' + str(MODE) + refl_line + '.pdf')

# file_out_data.write(str(N[sPlot_to].getVal()) + ' ' + str(N[sPlot_to].getError()) + '\n')

            #--------------#
            ##  sPlot II  ##
            #--------------#

sPlot_list = ROOT.RooArgList(N[sPlot_from], N_bkgr[sPlot_from], N_B0_refl) if sPlot_from == 'Bs' else ROOT.RooArgList(N[sPlot_from], N_bkgr[sPlot_from])
sData_sig = ROOT.RooStats.SPlot('sData_sig', 'sData_sig', data_sig, model[sPlot_from], sPlot_list)
data_sig_w = ROOT.RooDataSet(data_sig.GetName(), data_sig.GetTitle(), data_sig, data_sig.get(), '1 > 0', N[sPlot_from].GetName() + '_sw')
data_sig_w.SetName('sig_w')
hist_sig_weighted = ROOT.RooDataHist('hist_sig_weighted', 'hist_sig_weighted', ROOT.RooArgSet(var[sPlot_to]), data_sig_w) ### binning for this var was already previously set
#
mean_phi.setVal(1.01946); mean_phi.setConstant(1)
DE_2 = DataExplorer(data=hist_sig_weighted, model=model[sPlot_to], var=var[sPlot_to], poi = fr_model_phi, name=sPlot_to)
# DE_2.chi2_fit(is_extended=False)
# fr_model_phi.setVal(0.); fr_model_phi.setConstant(1)
# chi2_2_b = DE_2.chi2_fit(is_extended=False)

df = DE_2.tnull_toys(n_toys = 40000, seed = 332, save=False)
df.to_pickle('t_more.pkl')
# with open('./tnull_toys/t.txt', 'w') as f:
#     for item in t_list:
#         f.write(f'{item}\n')


c_sPlot_2 = ROOT.TCanvas("c_sPlot_2", "c_sPlot_2", 800, 600); CMS_tdrStyle_lumi.CMS_lumi(c_sPlot_2, 2, 0);
frame_DE_2 = DE_2.plot_on_var()
chi2_results.update(DE_2.chi2_test(frame_DE_2))
frame_DE_2.Draw()
# c_sPlot_2.Update(); c_sPlot_2.RedrawAxis(); # c_sPlot_2.GetFrame().Draw();
# c_sPlot_2.SaveAs('~/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/c_sPlot_1_' + str(MODE) + refl_line + '.pdf')

#             #---------------#
#             ##  sPlot III  ##
#             #---------------#
#
# mean[sPlot_from].setConstant(1)
# N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)
#
# DE_3 = DataExplorer(data=data_side, model=model[sPlot_from], var=var[sPlot_from], poi=N[sPlot_from], name=sPlot_from)
# DE_3.fit(fix_float=[a1, a2, a3, a4], is_extended=True, is_sum_w2=False)
# #
# w3 = DE_3.prepare_workspace(poi=N[sPlot_from], nuisances=[a1, a2, mean_Bs, N_bkgr_Bs])
# asympt_rrr = DE_3.asympt_signif(w=w3)
# asympt_rrr.Print()
# #
# c_sPlot_3 = ROOT.TCanvas("c_sPlot_3", "c_sPlot_3", 800, 600); CMS_tdrStyle_lumi.CMS_lumi(c_sPlot_3, 2, 0);
# frame_DE_3 = DE_3.plot_on_var()
# chi2_results.update(DE_3.chi2_test(frame_DE_3))
# frame_DE_3.Draw()
# # c_sPlot_3.Update(); c_sPlot_3.RedrawAxis(); # c_sPlot_3.GetFrame().Draw();
# # c_sPlot_3.SaveAs('~/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/c_sPlot_3_' + str(MODE) + refl_line + '.pdf')
#
# # file_out_data.write(str(N[sPlot_from].getVal()) + ' ' + str(N[sPlot_from].getError()) + '\n')
#
#             #--------------#
#             ##  sPlot IV  ##
#             #--------------#
#
# mean[sPlot_to].setConstant(1)
#
# sData_side = ROOT.RooStats.SPlot('sData_side', 'sData_side', data_side, model[sPlot_from], sPlot_list)
# data_side_w = ROOT.RooDataSet(data_side.GetName(), data_side.GetTitle(), data_side, data_side.get(), '1 > 0', N[sPlot_from].GetName() + '_sw')
# data_side_w.SetName('side_w')
# hist_side_weighted = ROOT.RooDataHist('hist_side_weighted', 'hist_side_weighted', ROOT.RooArgSet(var[sPlot_to]), data_side_w) ### binning for this var was already previously set
# #
# DE_4 = DataExplorer(data=hist_side_weighted, model=model[sPlot_to], var=var[sPlot_to], poi = fr_model_phi, name=sPlot_to)
# DE_4.chi2_fit(is_extended=False)
# # #
# # w4 = DE_4.prepare_workspace(poi = fr_model_phi, nuisances = [a1_phi, a2_phi, mean_phi])
# # asympt_rrr = DE_4.asympt_signif(w = w4)
# # asympt_rrr.Print()
# # #
# c_sPlot_4 = ROOT.TCanvas("c_sPlot_4", "c_sPlot_4", 800, 600); CMS_tdrStyle_lumi.CMS_lumi(c_sPlot_4, 2, 0);
# frame_DE_4 = DE_4.plot_on_var()
# chi2_results.update(DE_4.chi2_test(frame_DE_4))
# frame_DE_4.Draw()
# # c_sPlot_4.Update(); c_sPlot_4.RedrawAxis(); # c_sPlot_4.GetFrame().Draw();
# # c_sPlot_4.SaveAs('~/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/c_sPlot_4_' + str(MODE) + refl_line + '.pdf')

            #-------------#
            ##  Writing  ##
            #-------------#

# file_out_data.write(str(N[sPlot_to].getVal()) + ' ' + str(N[sPlot_to].getError()) + '\n')
# file_out_data.close()

# with open('./fit_validation/chis_' + MODE + '.txt', 'w') as file:
#     file.write(json.dumps(chi_dict))

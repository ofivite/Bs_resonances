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
# file_out_data = open('/home/yaourt/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/' + MODE +'_data_evtN.txt', 'w')

            #-------------------#
            ##  fixing shapes  ##
            #-------------------#

w_Bs = ROOT.TFile('workspace_' + MODE + '_Bs.root').Get('workspace')
w_psi = ROOT.TFile('workspace_psi_control.root').Get('workspace')
w_X = ROOT.TFile('workspace_X_control.root').Get('workspace')
w_phi = ROOT.TFile('workspace_' + MODE + '_phi.root').Get('workspace')
w_delta_phi = ROOT.TFile('workspace_' + MODE + '_delta_gen_phi_dRmatched_qM.root').Get('workspace')
w_dict = {'Bs': w_Bs, 'X': w_X, 'psi': w_psi, 'phi': w_phi, 'delta': w_delta_phi}

for key, s in list(signal.items()) + [('delta', signal_delta)]:
    iter = s.getVariables().iterator()
    iter_comp = iter.Next()
    while iter_comp:
        if iter_comp.GetName() not in [v.GetName() for v in var.values()]:
            val = w_dict[key].var(iter_comp.GetName()).getVal()
            iter_comp.setVal(val)
            if 'mean_' not in iter_comp.GetName():
                iter_comp.setConstant(1)
        iter_comp = iter.Next()

mean_delta.setVal(0.); mean_delta.setConstant(1)
N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)

            #---------------#
            ##  Inclusive  ##
            #---------------#

DE_inclus = DataExplorer(label=REGIONS_FROM, data=data, model=model[REGIONS_FROM])
fit_res_inclus = DE_inclus.fit(is_sum_w2=False)
#
DE_inclus.set_regions()
data_sig, data_side = DE_inclus.get_regions()
#
c_inclus = ROOT.TCanvas("c_inclus", "c_inclus", 800, 600); CMS_tdrStyle_lumi.CMS_lumi(c_inclus, 2, 0);
frame_inclus = DE_inclus.plot_on_var(plot_params=plot_param[REGIONS_FROM]);
frame_inclus_max = frame_inclus.GetMaximum(); coeffs = array([0.75, 0.85, 0.95]) if MODE == 'X' else array([0.5, 0.62, 0.75])
y_sdb_left, y_sr, y_sdb_right = frame_inclus_max*coeffs
frame_inclus = DE_inclus.plot_regions(frame_inclus, y_sdb_left, y_sr, y_sdb_right)
frame_inclus.Draw()
#
chi2_results.update(DE_inclus.chi2_test())
# c_inclus.Update(); c_inclus.RedrawAxis(); #c_inclus.GetFrame().Draw();
# c_inclus.SaveAs('~/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/c_inclus___' + MODE + refl_line + '.pdf')

            #-------------#
            ##  sPlot I  ##
            #-------------#

if REFL_ON and MODE == 'psi':  N_B0_refl.setVal(9.); N_B0_refl.setConstant(0)
else:        N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)
#
DE_1 = DataExplorer(label=SPLOT_FROM, data=data_sig, model=model[SPLOT_FROM])
fit_res_1 = DE_1.fit(fix_float=bkgr_params[SPLOT_FROM], is_sum_w2=False)
#
c_sPlot_1 = ROOT.TCanvas("c_sPlot_1", "c_sPlot_1", 800, 600); CMS_tdrStyle_lumi.CMS_lumi(c_sPlot_1, 2, 0);
frame_DE_1 = DE_1.plot_on_var(plot_params=plot_param[SPLOT_FROM])
frame_DE_1.Draw()
#
chi2_results.update(DE_1.chi2_test())
# w1 = DE_1.prepare_workspace(poi = N_sig[SPLOT_FROM], nuisances=bkgr_params[SPLOT_FROM] + [mean[SPLOT_FROM], N_bkgr[SPLOT_FROM]])
# DE_1.toy_signif(w=w1, n_toys = 10, seed=333)

# c_sPlot_1.Update(); c_sPlot_1.RedrawAxis(); # c_sPlot_1.GetFrame().Draw();
# c_sPlot_1.SaveAs('~/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/c_sPlot_1_' + MODE + refl_line + '.pdf')
#
# # file_out_data.write(str(N_sig[SPLOT_FROM].getVal()) + ' ' + str(N_sig[SPLOT_FROM].getError()) + '\n')

            #--------------#
            ##  sPlot II  ##
            #--------------#

sPlot_list = ROOT.RooArgList(N_sig[SPLOT_FROM], N_bkgr[SPLOT_FROM], N_B0_refl) if SPLOT_FROM == 'Bs' else ROOT.RooArgList(N_sig[SPLOT_FROM], N_bkgr[SPLOT_FROM])
sData_sig = ROOT.RooStats.SPlot('sData_sig', 'sData_sig', data_sig, model[SPLOT_FROM], sPlot_list)
data_sig_w = ROOT.RooDataSet(data_sig.GetName(), data_sig.GetTitle(), data_sig, data_sig.get(), '1 > 0', N_sig[SPLOT_FROM].GetName() + '_sw')
data_sig_w.SetName('sig_w')
hist_sig_weighted = ROOT.RooDataHist('hist_sig_weighted', 'hist_sig_weighted', ROOT.RooArgSet(var[SPLOT_TO]), data_sig_w) ### binning for this var was already previously set
#
mean_phi.setVal(1.01946); mean_phi.setConstant(1)
DE_2 = DataExplorer(label=SPLOT_TO, data=data_sig_w, model=model[SPLOT_TO])
fit_res_2 = DE_2.fit(is_sum_w2=True)
#
c_sPlot_2 = ROOT.TCanvas("c_sPlot_2", "c_sPlot_2", 800, 600); CMS_tdrStyle_lumi.CMS_lumi(c_sPlot_2, 2, 0);
frame_DE_2 = DE_2.plot_on_var(plot_params=plot_param[SPLOT_TO])
frame_DE_2.Draw()
#
chi2_results.update(DE_2.chi2_test())
# c_sPlot_2.Update(); c_sPlot_2.RedrawAxis(); # c_sPlot_2.GetFrame().Draw();
# c_sPlot_2.SaveAs('~/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/c_sPlot_1_' + MODE + refl_line + '.pdf')
#
# # file_out_data.write(str(N_sig[SPLOT_TO].getVal()) + ' ' + str(N_sig[SPLOT_TO].getError()) + '\n')

            #---------------#
            ##  sPlot III  ##
            #---------------#

mean[SPLOT_FROM].setConstant(1)
N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)
#
DE_3 = DataExplorer(label=SPLOT_FROM, data=data_side, model=model[SPLOT_FROM])
fit_res_3 = DE_3.fit(fix_float=bkgr_params[SPLOT_FROM], is_sum_w2=False)
#
# w3 = DE_3.prepare_workspace(poi=N_sig[SPLOT_FROM], nuisances=bkgr_params[SPLOT_FROM] + [mean[SPLOT_FROM], N_bkgr[SPLOT_FROM]])
# asympt_rrr = DE_3.asympt_signif(w=w3)
# asympt_rrr.Print()
#
c_sPlot_3 = ROOT.TCanvas("c_sPlot_3", "c_sPlot_3", 800, 600); CMS_tdrStyle_lumi.CMS_lumi(c_sPlot_3, 2, 0);
frame_DE_3 = DE_3.plot_on_var()
frame_DE_3.Draw()
#
chi2_results.update(DE_3.chi2_test())
# c_sPlot_3.Update(); c_sPlot_3.RedrawAxis(); # c_sPlot_3.GetFrame().Draw();
# c_sPlot_3.SaveAs('~/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/c_sPlot_3_' + MODE + refl_line + '.pdf')

# file_out_data.write(str(N_sig[SPLOT_FROM].getVal()) + ' ' + str(N_sig[SPLOT_FROM].getError()) + '\n')

            #--------------#
            ##  sPlot IV  ##
            #--------------#

mean[SPLOT_TO].setConstant(1)
#
sData_side = ROOT.RooStats.SPlot('sData_side', 'sData_side', data_side, model[SPLOT_FROM], sPlot_list)
data_side_w = ROOT.RooDataSet(data_side.GetName(), data_side.GetTitle(), data_side, data_side.get(), '1 > 0', N_sig[SPLOT_FROM].GetName() + '_sw')
data_side_w.SetName('side_w')
hist_side_weighted = ROOT.RooDataHist('hist_side_weighted', 'hist_side_weighted', ROOT.RooArgSet(var[SPLOT_TO]), data_side_w) ### binning for this var was already previously set
#
DE_4 = DataExplorer(label=SPLOT_TO, data=hist_side_weighted, model=model[SPLOT_TO])
DE_4.chi2_fit()
# #
# w4 = DE_4.prepare_workspace(poi = fr_model_phi, nuisances = bkgr_params[SPLOT_TO] + [mean[SPLOT_TO]])
# asympt_rrr = DE_4.asympt_signif(w = w4)
# asympt_rrr.Print()
# #
c_sPlot_4 = ROOT.TCanvas("c_sPlot_4", "c_sPlot_4", 800, 600); CMS_tdrStyle_lumi.CMS_lumi(c_sPlot_4, 2, 0);
frame_DE_4 = DE_4.plot_on_var()
frame_DE_4.Draw()
#
chi2_results.update(DE_4.chi2_test())
# c_sPlot_4.Update(); c_sPlot_4.RedrawAxis(); # c_sPlot_4.GetFrame().Draw();
# c_sPlot_4.SaveAs('~/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/c_sPlot_4_' + MODE + refl_line + '.pdf')

# file_out_data.write(str(N_sig[SPLOT_TO].getVal()) + ' ' + str(N_sig[SPLOT_TO].getError()) + '\n')
#
#             #--------------#
#             #   Writing   ##
#             #--------------#
#
# file_out_data.close()
# with open('./fit_validation/chis_' + MODE + '.txt', 'w') as file:
#     file.write(json.dumps(chi_dict))

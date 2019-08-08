from cuts_and_ranges import *
from DataExplorer import DataExplorer, fix_shapes
import CMS_tdrStyle_lumi

from math import sqrt
import json

CMS_tdrStyle_lumi.extraText = "Preliminary"
chi2_results = {}
N_sig_results = {}

if RUN == 2:
    file_data = ROOT.TFile('./lxplus_dir/X_RunII/X_RunII/BXP_v0_2035_of_2035_61ddc20.root')
elif RUN == 1:
    file_data = ROOT.TFile('new_2_with_more_B0_e3de87.root')
else:
    raise Exception(f'Don\'t have a file for Run = {RUN}')
# file_data = ROOT.TFile('~/BXP_v1_645_of_2035_.root')
data = ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp))
data = data.reduce(cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data + ' && ' + cuts_pipi[MODE]) # important to do reduce() instead of adding cuts to RooDataSet definition!

            #-------------------#
            ##  fixing shapes  ##
            #-------------------#

w_Bs = ROOT.TFile('workspace_' + MODE + '_Bs.root').Get('workspace')
w_psi = ROOT.TFile('workspace_psi_control.root').Get('workspace')
w_X = ROOT.TFile('workspace_X_control.root').Get('workspace')
w_phi = ROOT.TFile('workspace_' + MODE + '_phi.root').Get('workspace')
w_delta_phi = ROOT.TFile('workspace_' + MODE + '_delta_gen_phi_dRmatched_qM.root').Get('workspace')
w_dict = {'Bs': w_Bs, 'X': w_X, 'psi': w_psi, 'phi': w_phi, 'delta': w_delta_phi}
#
fix_shapes(workspaces_dict=w_dict, models_dict=signal_model_dict, var_ignore_list=[*var.values(), *mean.values()])
mean_delta.setVal(0.); mean_delta.setConstant(1)

            #---------------#
            ##  Inclusive  ##
            #---------------#

DE_inclus = DataExplorer(label=REGIONS_FROM, data=data, model=model[REGIONS_FROM])
if REGIONS_FROM == 'phi':
    DE_inclus.window = 0.01
    DE_inclus.distance_to_sdb = 0.005
else:
    DE_inclus.set_regions(num_of_sigma_window=3, num_of_sigma_to_sdb=2)
data_sig, data_side = DE_inclus.get_regions()
fit_res_inclus = DE_inclus.fit(is_sum_w2=False)
#
c_inclus = ROOT.TCanvas("c_inclus", "c_inclus", 800, 600)
frame_inclus = DE_inclus.plot_on_frame(plot_params=plot_param[REGIONS_FROM]);
frame_inclus_max = frame_inclus.GetMaximum(); coeffs = [0.75, 0.85, 0.95] if MODE == 'X' else [0.5, 0.62, 0.75]
y_sdb_left, y_sr, y_sdb_right = [coeff*frame_inclus_max for coeff in coeffs]
frame_inclus = DE_inclus.plot_regions(frame_inclus, y_sdb_left, y_sr, y_sdb_right)
frame_inclus.Draw()
CMS_tdrStyle_lumi.CMS_lumi(c_inclus, 2, 0)
#
chi2_results.update(DE_inclus.chi2_test(CHI2_PVALUE_THRESHOLD))
# c_inclus.Update(); c_inclus.RedrawAxis(); #c_inclus.GetFrame().Draw();
# c_inclus.SaveAs('~/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/c_inclus___' + MODE + REFL_LINE + '.pdf')

            #-------------#
            ##  sPlot I  ##
            #-------------#

if REFL_ON:
    N_B0_refl.setVal(100.); N_B0_refl.setConstant(0)
    refl_components = {'B0_refl_SR': [5.27, 5.47]}
else:
    N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)
    refl_components = {}

DE_1 = DataExplorer(label=SPLOT_FROM, data=data_sig, model=model[SPLOT_FROM])
fit_res_1 = DE_1.fit(is_sum_w2=False, fix_float=bkgr_params[SPLOT_FROM])
#
c_sPlot_1 = ROOT.TCanvas("c_sPlot_1", "c_sPlot_1", 800, 600)
frame_DE_1 = DE_1.plot_on_frame(plot_params=plot_param[SPLOT_FROM], **refl_components)
frame_DE_1.Draw()
CMS_tdrStyle_lumi.CMS_lumi(c_sPlot_1, 2, 0)
#
chi2_results.update(DE_1.chi2_test(CHI2_PVALUE_THRESHOLD))
N_sig_results.update({f'{DE_1.label}_{DE_1.data.GetName()}': (N_sig[SPLOT_FROM].getVal(), N_sig[SPLOT_FROM].getError(), DE_1.fit_status, DE_1.chi2_test_status)})
# c_sPlot_1.Update(); c_sPlot_1.RedrawAxis(); # c_sPlot_1.GetFrame().Draw();
# c_sPlot_1.SaveAs('~/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/c_sPlot_1_' + MODE + REFL_LINE + '.pdf')

            #--------------#
            ##  sPlot II  ##
            #--------------#

# ### Fixing model's parameters except for yields is needed according to sPlot tutorial (requires checking though)
# a1_Bs.setConstant(1); a2_Bs.setConstant(1); a3_Bs.setConstant(1); a4_Bs.setConstant(1);
# mean_Bs.setConstant(1); sigma_Bs.setConstant(1)

if SPLOT_FROM == 'Bs' and REFL_ON:
    sPlot_list = ROOT.RooArgList(N_sig[SPLOT_FROM], N_bkgr[SPLOT_FROM], N_B0_refl)
else:
    sPlot_list = ROOT.RooArgList(N_sig[SPLOT_FROM], N_bkgr[SPLOT_FROM])

sData_sig = ROOT.RooStats.SPlot('sData_sig', 'sData_sig', data_sig, model[SPLOT_FROM], sPlot_list)
data_sig_w = ROOT.RooDataSet(data_sig.GetName(), data_sig.GetTitle(), data_sig, data_sig.get(), '1 > 0', N_sig[SPLOT_FROM].GetName() + '_sw')
data_sig_w.SetName('SR_w')
DE_2 = DataExplorer(label=SPLOT_TO, data=data_sig_w, model=model[SPLOT_TO])
fit_res_2 = DE_2.fit(is_sum_w2=True, fix_float=bkgr_params[SPLOT_TO])
# #
# w2 = DE_2.prepare_workspace(poi=N_sig[SPLOT_TO], nuisances=bkgr_params[SPLOT_TO] + [mean[SPLOT_TO], N_bkgr[SPLOT_TO]])
# asympt_rrr = DE_2.asympt_signif(w=w2)
# asympt_rrr.Print()
# #
c_sPlot_2 = ROOT.TCanvas("c_sPlot_2", "c_sPlot_2", 800, 600)
frame_DE_2 = DE_2.plot_on_frame(plot_params=plot_param[SPLOT_TO])
frame_DE_2.Draw()
CMS_tdrStyle_lumi.CMS_lumi(c_sPlot_2, 2, 0)
#
chi2_results.update(DE_2.chi2_test(CHI2_PVALUE_THRESHOLD))
N_sig_results.update({f'{DE_2.label}_{DE_2.data.GetName()}': (N_sig[SPLOT_TO].getVal(), N_sig[SPLOT_TO].getError(), DE_2.fit_status, DE_2.chi2_test_status)})
# c_sPlot_2.Update(); c_sPlot_2.RedrawAxis(); # c_sPlot_2.GetFrame().Draw();
# c_sPlot_2.SaveAs('~/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/c_sPlot_1_' + MODE + REFL_LINE + '.pdf')
#
            #---------------#
            ##  sPlot III  ##
            #---------------#

N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)
mean[SPLOT_FROM].setConstant(1)
#
DE_3 = DataExplorer(label=SPLOT_FROM, data=data_side, model=model[SPLOT_FROM])
fit_res_3 = DE_3.fit(is_sum_w2=False, fix_float=bkgr_params[SPLOT_FROM])
#
c_sPlot_3 = ROOT.TCanvas("c_sPlot_3", "c_sPlot_3", 800, 600)
frame_DE_3 = DE_3.plot_on_frame(plot_params=plot_param[SPLOT_FROM])
frame_DE_3.Draw()
CMS_tdrStyle_lumi.CMS_lumi(c_sPlot_3, 2, 0)
#
chi2_results.update(DE_3.chi2_test(CHI2_PVALUE_THRESHOLD))
N_sig_results.update({f'{DE_3.label}_{DE_3.data.GetName()}': (N_sig[SPLOT_FROM].getVal(), N_sig[SPLOT_FROM].getError(), DE_3.fit_status, DE_3.chi2_test_status)})
# c_sPlot_3.Update(); c_sPlot_3.RedrawAxis(); # c_sPlot_3.GetFrame().Draw();
# c_sPlot_3.SaveAs('~/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/c_sPlot_3_' + MODE + REFL_LINE + '.pdf')

            #--------------#
            ##  sPlot IV  ##
            #--------------#

mean[SPLOT_TO].setConstant(1)
#
sData_side = ROOT.RooStats.SPlot('sData_side', 'sData_side', data_side, model[SPLOT_FROM], sPlot_list)
data_side_w = ROOT.RooDataSet(data_side.GetName(), data_side.GetTitle(), data_side, data_side.get(), '1 > 0', N_sig[SPLOT_FROM].GetName() + '_sw')
data_side_w.SetName('SdR_w')
#
DE_4 = DataExplorer(label=SPLOT_TO, data=data_side_w, model=model[SPLOT_TO])
fit_res_4 = DE_4.fit(is_sum_w2=True, fix_float=bkgr_params[SPLOT_TO])
#
c_sPlot_4 = ROOT.TCanvas("c_sPlot_4", "c_sPlot_4", 800, 600)
frame_DE_4 = DE_4.plot_on_frame(plot_params=plot_param[SPLOT_TO])
frame_DE_4.Draw()
CMS_tdrStyle_lumi.CMS_lumi(c_sPlot_4, 2, 0)
#
chi2_results.update(DE_4.chi2_test(CHI2_PVALUE_THRESHOLD))
N_sig_results.update({f'{DE_4.label}_{DE_4.data.GetName()}': (N_sig[SPLOT_TO].getVal(), N_sig[SPLOT_TO].getError(), DE_4.fit_status, DE_4.chi2_test_status)})
# c_sPlot_4.Update(); c_sPlot_4.RedrawAxis(); # c_sPlot_4.GetFrame().Draw();
# c_sPlot_4.SaveAs('~/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/c_sPlot_4_' + MODE + REFL_LINE + '.pdf')

#             #--------------#
#             #   Writing   ##
#             #--------------#
#
# with open(f'/home/yaourt/Study/Bs_resonances/fit_validation/chis_{MODE}.txt', 'w') as file_chi2:
#     json.dumps(chi_dict, file_chi2)
# with open(f'/home/yaourt/Study/Bs_resonances/{SPLOT_FROM}->{SPLOT_TO}/{MODE}_data_evtN.json', 'w') as file_evts:
#     json.dump(N_sig_results, file_evts)

# # with open('data.json', 'r') as fp:
# #     data = json.load(fp)

print('\n\n' + 65*'~' + '\n' + ' '*30 + 'NB:\n')
for fit_name, fit_params in N_sig_results.items():
    if N_sig_results[fit_name][2] == 1:
        print(f'Fit for {fit_name} did not converge!\n')
    if N_sig_results[fit_name][3] == 1:
        print(f'Fit for {fit_name} did not pass chi2 test! (p-value = {chi2_results[fit_name][-1]} < {CHI2_PVALUE_THRESHOLD})\n')
print(65*'~' + '\n\n')

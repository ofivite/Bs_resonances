from cuts_and_ranges import *
from DataExplorer import DataExplorer
from misc import fix_shapes
import CMS_tdrStyle_lumi
from math import sqrt
import json

CMS_tdrStyle_lumi.extraText = "Preliminary"
chi2_results = {}
N_sig_results = {}

if RUN == 2:
    file_data = ROOT.TFile('./lxplus_dir/X_RunII/X_RunII/BXP_2035_of_2035_B0M0.root')
    # file_data = ROOT.TFile('./lxplus_dir/X_RunII/X_RunII/BXP_v1_645_of_2035_.root')
elif RUN == 1:
    file_data = ROOT.TFile('new_2_with_more_B0_e3de87.root')
else:
    raise Exception(f'Don\'t have a file for Run = {RUN}')

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
w_dict = {'Bs': w_Bs, 'X': w_X, 'psi': w_psi, 'phi': w_phi}
fix_shapes(workspaces_dict=w_dict, models_dict=signal_model_dict, var_ignore_list=[*var.values(), *mean.values()])
mean_delta.setVal(0.); mean_delta.setConstant(1)

            #-----------------#
            ##  set regions  ##
            #-----------------#

DE_Bs = DataExplorer(label='Bs', data=data, model=model['Bs'])
DE_Bs.set_regions(num_of_sigma_window=3, num_of_sigma_to_sdb=2)
mean_Bs_val = mean['Bs'].getVal()
#
DE_control = DataExplorer(label=MODE, data=data, model=model[MODE])
DE_control.set_regions(num_of_sigma_window=3, num_of_sigma_to_sdb=2)
mean_control_val = mean[MODE].getVal()
#
DE_phi = DataExplorer(label='phi', data=data, model=model['phi'])
DE_phi.window = 0.01
DE_phi.distance_to_sdb = 0.005
mean_phi_val = mean['phi'].getVal()

#############################################################################################
# control variable

windows_control = f'TMath::Abs({var_discr.GetName()} - {mean_Bs_val}) < {DE_Bs.window} && TMath::Abs({PHI_mass_Cjp.GetName()} - {mean_phi_val}) < {DE_phi.window}'
DE_control.data = data.reduce(windows_control)
DE_control.fit(is_sum_w2=False, fix_float=bkgr_params[MODE])
#
c_control = ROOT.TCanvas("c_control", "c_control", 800, 600)
frame_control = DE_control.plot_on_frame(plot_params=plot_param[MODE])
frame_control.Draw()
CMS_tdrStyle_lumi.CMS_lumi(c_control, 2, 0)
#
chi2_results.update(DE_control.chi2_test(CHI2_PVALUE_THRESHOLD))
N_sig_results.update({f'{DE_control.label}_{DE_control.data.GetName()}': (N_sig[MODE].getVal(), N_sig[MODE].getError(), DE_control.fit_status, DE_control.chi2_test_status)})
#
# w_control = DE_control.prepare_workspace(poi=N_sig[MODE], nuisances=[*bkgr_params[MODE], mean[MODE], N_bkgr[MODE]])
# ar_control = DE_control.asympt_signif(w=w_control)
# ar_control.Print()
#
# c_control.SaveAs('~/Study/Bs_resonances/preliminary_look_plots/c_control_prelim_' + str(MODE) + '.pdf')

#############################################################################################
# Bs variable

windows_Bs = f'TMath::Abs({var_control.GetName()} - {mean_control_val}) < {DE_control.window} && TMath::Abs({PHI_mass_Cjp.GetName()} - {mean_phi_val}) < {DE_phi.window}'
DE_Bs.data = data.reduce(windows_Bs)
DE_Bs.fit(is_sum_w2=False, fix_float=bkgr_params['Bs'])
#
c_Bs = ROOT.TCanvas("c_Bs", "c_Bs", 800, 600)
frame_Bs = DE_Bs.plot_on_frame(plot_params=plot_param['Bs'])
frame_Bs.Draw()
CMS_tdrStyle_lumi.CMS_lumi(c_Bs, 2, 0)
#
chi2_results.update(DE_Bs.chi2_test(CHI2_PVALUE_THRESHOLD))
N_sig_results.update({f'{DE_Bs.label}_{DE_Bs.data.GetName()}': (N_sig['Bs'].getVal(), N_sig['Bs'].getError(), DE_Bs.fit_status, DE_Bs.chi2_test_status)})
#
# w_Bs = DE_Bs.prepare_workspace(poi=N_sig['Bs'], nuisances=[*bkgr_params['Bs'], mean['Bs'], N_bkgr['Bs']])
# ar_Bs = DE_Bs.asympt_signif(w=w_Bs)
# ar_Bs.Print()
#
# c_Bs.SaveAs('~/Study/Bs_resonances/preliminary_look_plots/c_Bs_prelim_' + str(MODE) + '.pdf')

############################################################################################
# phi variable

windows_phi = f'TMath::Abs({var_discr.GetName()} - {mean_Bs_val}) < {DE_Bs.window} && TMath::Abs({var_control.GetName()} - {mean_control_val}) < {DE_control.window}'
DE_phi.data = data.reduce(windows_phi)
DE_phi.fit(is_sum_w2=False, fix_float=bkgr_params['phi'])
#
c_phi = ROOT.TCanvas("c_phi", "c_phi", 800, 600)
frame_phi = DE_phi.plot_on_frame(plot_params=plot_param['phi'])
frame_phi.Draw()
CMS_tdrStyle_lumi.CMS_lumi(c_phi, 2, 0)
#
chi2_results.update(DE_phi.chi2_test(CHI2_PVALUE_THRESHOLD))
N_sig_results.update({f'{DE_phi.label}_{DE_phi.data.GetName()}': (N_sig['phi'].getVal(), N_sig['phi'].getError(), DE_phi.fit_status, DE_phi.chi2_test_status)})
#
# w_phi = DE_phi.prepare_workspace(poi=N_sig['phi'], nuisances=[*bkgr_params['phi'], mean['phi'], N_bkgr['phi']])
# ar_phi = DE_phi.asympt_signif(w=w_phi)
# ar_phi.Print()
#
# c_phi.SaveAs('~/Study/Bs_resonances/preliminary_look_plots/c_phi_prelim_' + str(MODE) + '.pdf')

############################################################################################

print('\n\n' + 65*'~' + '\n' + ' '*30 + 'NB:\n')
for fit_name, fit_params in N_sig_results.items():
    if N_sig_results[fit_name][2] != 0:
        print(f'Fit for {fit_name} did not converge! Fit status: {N_sig_results[fit_name][2]}\n')
    if N_sig_results[fit_name][3] != 0:
        print(f'Fit for {fit_name} did not pass chi2 test! (p-value = {chi2_results[fit_name][-1]} < {CHI2_PVALUE_THRESHOLD})\n')
print(65*'~' + '\n\n')

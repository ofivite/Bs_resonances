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

            #-------------------#
            ##  fixing shapes  ##
            #-------------------#

w_Bs, f_Bs = get_workspace('workspace_' + MODE + '_Bs.root', 'workspace')
w_psi, f_psi = get_workspace('workspace_psi_control.root', 'workspace')
w_X, f_X = get_workspace('workspace_X_control.root', 'workspace')
w_phi, f_phi = get_workspace('workspace_' + MODE + '_phi.root', 'workspace')
w_delta_phi, f_delta_phi = get_workspace('workspace_' + MODE + '_delta_gen_phi_dRmatched_qM.root', 'workspace')
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

            #-----------------#
            ##  set regions  ##
            #-----------------#

DE_Bs = DataExplorer(name='Bs', var=var['Bs'], data=data, model=model['Bs'], poi=N_sig['Bs'])
DE_Bs.set_regions()
#
DE_control = DataExplorer(name=MODE, var=var[MODE], data=data, model=model[MODE], poi=N_sig[MODE])
DE_control.set_regions()
#
DE_phi = DataExplorer(name='phi', var=var['phi'], data=data, model=model['phi'], poi=N_sig['phi'])
DE_phi.set_regions()

#############################################################################################
# control variable

# DE_control.data = data.reduce('TMath::Abs(BU_mass_Cjp - ' + str(mean['Bs'].getVal()) + ') < ' + str(DE_Bs.window) + ' && TMath::Abs(PHI_mass_Cjp - ' + str(mean['phi'].getVal()) + ') <' + str(DE_phi.window))
# DE_control.fit(is_sum_w2=False, fix_float=bkgr_params[MODE])
# c_control = ROOT.TCanvas("c_control", "c_control", 800, 600); CMS_tdrStyle_lumi.CMS_lumi( c_control, 2, 0 );
# frame_control = DE_control.plot_on_var()
# frame_control.Draw()
# #
# chi2_results.update(DE_control.chi2_test())
# #
# w_control = DE_control.prepare_workspace(nuisances=bkgr_params[MODE] + [mean[MODE], N_bkgr[MODE]])
# ar_control = DE_control.asympt_signif(w=w_control)
# ar_control.Print()
# #
# # fqResult_control = DE_control.toy_signif(w=w_control, n_toys = 30000, seed = 333)
# # # c_control.SaveAs('~/Study/Bs_resonances/preliminary_look_plots/c_control_prelim_' + str(mode) + '.pdf')

#############################################################################################
# Bs variable

DE_Bs.data = data.reduce('TMath::Abs(X_mass_Cjp - ' + str(mean[MODE].getVal()) + ') < ' + str(DE_control.window) + ' && TMath::Abs(PHI_mass_Cjp - ' + str(mean['phi'].getVal()) + ') < ' + str(DE_phi.window))
DE_Bs.fit(is_sum_w2=False, fix_float=bkgr_params['Bs'])
c_Bs = ROOT.TCanvas("c_Bs", "c_Bs", 800, 600); CMS_tdrStyle_lumi.CMS_lumi( c_Bs, 2, 0 );
frame_Bs = DE_Bs.plot_on_var()
frame_Bs.Draw()
#
chi2_results.update(DE_Bs.chi2_test())
#
w_Bs = DE_Bs.prepare_workspace(nuisances=bkgr_params['Bs'] + [mean['Bs'], N_bkgr['Bs']])
ar_Bs = DE_Bs.asympt_signif(w=w_Bs)
ar_Bs.Print()
#
# fqResult_Bs = DE_Bs.toy_signif(w=w_Bs, n_toys = 30000, seed = 333)
# # c_Bs.SaveAs('~/Study/Bs_resonances/preliminary_look_plots/c_Bs_prelim_' + str(mode) + '.pdf')

#############################################################################################
# phi variable

# DE_phi.data = data.reduce('TMath::Abs(BU_mass_Cjp - ' + str(mean['Bs'].getVal()) + ') < ' + str(DE_Bs.window) + ' && TMath::Abs(X_mass_Cjp - ' + str(mean[MODE].getVal()) + ') < ' + str(DE_control.window))
# DE_phi.fit(is_sum_w2=False, fix_float=bkgr_params['phi'])
# c_phi = ROOT.TCanvas("c_phi", "c_phi", 800, 600); CMS_tdrStyle_lumi.CMS_lumi( c_phi, 2, 0 );
# frame_phi = DE_phi.plot_on_var()
# frame_phi.Draw()
# #
# chi2_results.update(DE_phi.chi2_test())
# #
# w_phi = DE_phi.prepare_workspace(nuisances=bkgr_params['phi'] + [mean['phi'], N_bkgr['phi']])
# ar_phi = DE_phi.asympt_signif(w=w_phi)
# ar_phi.Print()
# #
# # fqResult_phi = DE_phi.toy_signif(w=w_phi, n_toys = 2, seed = 333)
# # # c_phi.SaveAs('~/Study/Bs_resonances/preliminary_look_plots/c_phi_prelim_' + str(mode) + '.pdf')

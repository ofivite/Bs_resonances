from RooSpace import *
from math import sqrt
import json
from DataExplorer import DataExplorer

CMS_tdrStyle_lumi.extraText = "Preliminary"
var_discr.setMin(left_discr_data); var_discr.setMax(right_discr_data); var_discr.setBins(nbins_discr_data)
PHI_mass_Cjp.setMin(left_phi_data); PHI_mass_Cjp.setMax(right_phi_data); PHI_mass_Cjp.setBins(nbins_phi_data)
var_control.setMin(left_control_data); var_control.setMax(right_control_data);  var_control.setBins(nbins_control_data)

file_data = ROOT.TFile('new_2_with_more_B0_e3de87.root')
data = ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp))
data = data.reduce(cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data + ' && ' + cuts_pipi[MODE])

            #------------------#
            ##  fixing shape  ##
            #------------------#

###
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

DE_inclus = DataExplorer(data, model[sPlot_cut], var[sPlot_cut], name = MODE)
DE_inclus.fit_data(is_extended = True, is_sum_w2 = False)
#
DE_inclus.make_regions()
data_sig, data_sideband = DE_inclus.get_regioned_data()
#
c_inclus = ROOT.TCanvas("c_inclus", "c_inclus", 800, 600); CMS_tdrStyle_lumi.CMS_lumi( c_inclus, 2, 0 );
frame_inclus = DE_inclus.plot_on_var()
frame_inclus.Draw()
# y_sdb_left, y_sr, y_sdb_right = (950, 1280, 1420) if MODE == 'X' else (1750, 2400, 2750)
# DE_inclus.draw_regions(y_sdb_left, y_sr, y_sdb_right)
# c_inclus.Update(); c_inclus.RedrawAxis(); #c_inclus.GetFrame().Draw();
# c_inclus.SaveAs('~/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/c_inclus___' + str(MODE) + refl_line + '.pdf')

            #-------------#
            ##  sPlot I  ##
            #-------------#

if REFL_ON and MODE == 'psi':  N_B0_refl.setVal(9.); N_B0_refl.setConstant(0)
else:        N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)
if sPlot_from == 'Bs' and MODE == 'X': mean[sPlot_from].setConstant(1)

DE_1 = DataExplorer(data = data_sig, model = model[sPlot_from], var = var[sPlot_from], name = sPlot_from)
DE_1.fit_data(fix_float = [a1, a2, a3, a4], is_extended = True, is_sum_w2 = False)
#
w1 = DE_1.prepare_workspace(poi = N[sPlot_from], nuisances = [a1, a2, mean_Bs, N_bkgr_Bs])
asympt_rrr = DE_1.asympt_signif(w = w1)
asympt_rrr.Print()
#
c_sPlot_1 = ROOT.TCanvas("c_sPlot_1", "c_sPlot_1", 800, 600); CMS_tdrStyle_lumi.CMS_lumi( c_sPlot_1, 2, 0 );
frame_DE_1 = DE_1.plot_on_var()
frame_DE_1.Draw()
# c_sPlot_1.Update(); c_sPlot_1.RedrawAxis(); # c_sPlot_1.GetFrame().Draw();
# c_sPlot_1.SaveAs('~/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/c_sPlot_1_' + str(MODE) + refl_line + '.pdf')

#
#             #--------------#
#             ##  sPlot II  ##
#             #--------------#
#
# ### Fixing model's parameters except for yields is needed according to sPlot tutorial
# # a1.setConstant(1); a2.setConstant(1); a3.setConstant(1); a4.setConstant(1);
# # mean_Bs.setConstant(1);
#
# sPlot_list = ROOT.RooArgList(N[sPlot_from], N_bkgr[sPlot_from], N_B0_refl) if sPlot_from == 'Bs' else ROOT.RooArgList(N[sPlot_from], N_bkgr[sPlot_from])
# sData_Bs_psi_sig = ROOT.RooStats.SPlot('sData_Bs_psi_sig', 'sData_Bs_psi_sig', data_sig, model[sPlot_from], sPlot_list)
# data_sig_weighted = ROOT.RooDataSet(data_sig.GetName(), data_sig.GetTitle(), data_sig, data_sig.get(), '1 > 0', N[sPlot_from].GetName() + '_sw') ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi
# data_sig_weighted.SetName('sig_w')
# # hist_sig_weighted = data_sig_weighted.binnedClone()
# hist_sig_weighted = ROOT.RooDataHist('h', 'h', ROOT.RooArgSet(PHI_mass_Cjp), data_sig_weighted)
#
# # currentlist = ROOT.RooLinkedList()
# # # cmd = RF.Save()
# # # currentlist.Add(cmd)
# # N_sig_phi_sw = ROOT.RooRealVar('N_sig_phi_sw', 'N_sig_phi_sw', -100000000, 100000000)
# # cmd = RF.YVar(N_sig_phi_sw)
# # currentlist.Add(cmd)
# # mean_phi.setVal(1.0196); N_sig_phi.setVal(130.); N_bkgr_phi.setVal(50.)
# # # aaa = model[sPlot_to].chi2FitTo(hist_sig_weighted) # RF.SumW2Error(ROOT.kTRUE)
#
# # model[sPlot_to].fitTo(data_sig_weighted, RF.SumW2Error(ROOT.kTRUE)) # RF.SumW2Error(ROOT.kTRUE)
# # model[sPlot_to].fitTo(data_sig_weighted, RF.SumW2Error(ROOT.kTRUE)) # RF.SumW2Error(ROOT.kTRUE)
# # model[sPlot_to].fitTo(data_sig_weighted, RF.SumW2Error(ROOT.kTRUE))
# # # a1.setConstant(1); a2.setConstant(1); a3.setConstant(1); a4.setConstant(1);
# # # a1_phi.setConstant(1); a2_phi.setConstant(1); a3_phi.setConstant(1); a4_phi.setConstant(1);
# # # a1_ext.setConstant(1); a2_ext.setConstant(1); a3_ext.setConstant(1); a4_ext.setConstant(1);
# # # rrr_sig = model[sPlot_to].chi2FitTo(hist_sig_weighted, RF.Save())
# # #
# # # a1.setConstant(0); a2.setConstant(0); a3.setConstant(0); a4.setConstant(0);
# # # a1_phi.setConstant(0); a2_phi.setConstant(0); a3_phi.setConstant(0); a4_phi.setConstant(0);
# # # a1_ext.setConstant(0); a2_ext.setConstant(0); a3_ext.setConstant(0); a4_ext.setConstant(0);
# # model[sPlot_to].fitTo(hist_sig_weighted, RF.SumW2Error(ROOT.kTRUE))
# # model[sPlot_to].fitTo(hist_sig_weighted, RF.SumW2Error(ROOT.kTRUE))
# # model[sPlot_to].fitTo(hist_sig_weighted, RF.SumW2Error(ROOT.kTRUE))
# # rrr_sig = model[sPlot_to].fitTo(hist_sig_weighted, RF.Save(), RF.SumW2Error(ROOT.kTRUE))
#


#     # Note that entries with zero bins are _not_ allowed
#     # for a proper chi^2 calculation and will give error
#     # messages
#     dsmall = d.reduce(ROOT.RooFit.EventRange(1, 100))
#     dhsmall = dsmall.binnedClone()
#     chi2_lowstat = ROOT.RooChi2Var("chi2_lowstat", "chi2", model, dhsmall)
# print chi2_lowstat.getVal()
#

# chi2 = ROOT.RooChi2Var("chi2","chi2", model[sPlot_to], hist_sig_weighted, extended = ROOT.kFALSE, nCPU = 2, RF.DataError(ROOT.RooAbsData.SumW2))
#
# # m = ROOT.RooMinuit(chi2)
# # m.migrad()
# # m.migrad()
# # m.migrad()
# # m.migrad()
#
# m = ROOT.RooMinimizer(chi2)
# m.setMinimizerType("Minuit2");
# m.setPrintLevel(3)
#
# m.minimize("Minuit2","minimize") ;
# m.minimize("Minuit2","minimize") ;
# m.hesse()
# r_chi2 = m.save()
# r_chi2.Print() ;
#
# ##########
#
# c_sPlot_2 = ROOT.TCanvas("c_sPlot_2", "c_sPlot_2", 800, 600)
#
# # # mean[sPlot_to].setConstant(1)
# # model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE)) # RF.SumW2Error(ROOT.kTRUE)
# # model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE)) # RF.SumW2Error(ROOT.kTRUE)
# # model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE))
# # a1.setConstant(1); a2.setConstant(1); a3.setConstant(1); a4.setConstant(1);
# # a1_phi.setConstant(1); a2_phi.setConstant(1); a3_phi.setConstant(1); a4_phi.setConstant(1);
# # a1_ext.setConstant(1); a2_ext.setConstant(1); a3_ext.setConstant(1); a4_ext.setConstant(1);
# # rrr_sig = model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE), RF.Save())
# #
# # a1.setConstant(0); a2.setConstant(0); a3.setConstant(0); a4.setConstant(0);
# # a1_phi.setConstant(0); a2_phi.setConstant(0); a3_phi.setConstant(0); a4_phi.setConstant(0);
# # a1_ext.setConstant(0); a2_ext.setConstant(0); a3_ext.setConstant(0); a4_ext.setConstant(0);
# # rrr_sig = model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE), RF.Save())
#
# # file_out_data.write(str(N[sPlot_to].getVal()) + ' ' + str(N[sPlot_to].getError()) + '\n')
# plot_on_frame(var[sPlot_to], data_sig_weighted, model[sPlot_to], ' ', left[sPlot_to], right[sPlot_to], nbins[sPlot_to], None, False, chi_dict)
# # plot_pull(var[sPlot_to], data_sig_weighted, model[sPlot_to], save = True)
# # plot_toys_pull(var[sPlot_to], model[sPlot_to], var_to_study = N_sig_phi,  N_toys = 1000, N_gen = int(data_sig_weighted.sumEntries()), save = True, label = data_sig_weighted.GetName())
#
# CMS_tdrStyle_lumi.CMS_lumi( c_sPlot_2, 2, 0 ); c_sPlot_2.Update(); c_sPlot_2.RedrawAxis();
# # c_sPlot_2.GetFrame().Draw();
# # c_sPlot_2.SaveAs('~/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/c_sPlot_2_' + str(MODE) + refl_line + '.pdf')





# ###--- plotting ll ---###
#
# nll = model[sPlot_to].createNLL(data_sig_weighted)
# pll = nll.createProfile(ROOT.RooArgSet(N[sPlot_to]))
#
# c_ll = ROOT.TCanvas("c_ll", "c_ll", 800, 600)
# frame_nll = N[sPlot_to].frame(RF.Bins(80), RF.Range(0, 160)) #N_sig_Bs.getVal() + 40
# frame_nll.SetTitle('')
#
# nll.plotOn(frame_nll, RF.ShiftToZero(), RF.LineColor(ROOT.kGreen))
# # nll.plotOn(frame_nll, RF.LineColor(ROOT.kGreen))
# pll.plotOn(frame_nll, RF.LineColor(ROOT.kRed))
#
# frame_nll.SetMaximum(280.)
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
# c_ll.SaveAs(MODE + '2_pll.pdf')



#
#
# # # ###-----###
#
# w = ROOT.RooWorkspace("w", True)
# Import = getattr(ROOT.RooWorkspace, 'import')
# Import(w, model[sPlot_to])
# mc = ROOT.RooStats.ModelConfig("ModelConfig",w)
# mc.SetPdf(w.pdf(model[sPlot_to].GetName()))
# mc.SetParametersOfInterest(ROOT.RooArgSet(w.var(N[sPlot_to].GetName())))
# # w.var("N_sig_X").setError(20.)
# mc.SetObservables(ROOT.RooArgSet(w.var(var[sPlot_to].GetName())))
# # mc.SetNuisanceParameters(ROOT.RooArgSet(w.var('a1_phi' if sPlot_to == 'phi' else 'a1'), w.var('a2_phi' if sPlot_to == 'phi' else 'a2'), w.var(N_bkgr_Bs.GetName()), w.var(mean_Bs.GetName())))
# mc.SetSnapshot(ROOT.RooArgSet(w.var(N[sPlot_to].GetName())))
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
# ac = ROOT.RooStats.AsymptoticCalculator(data_sig_weighted, sbModel, bModel)
# ac.SetOneSidedDiscovery(True)
# asResult = ac.GetHypoTest()
# print ('*' * 40, '\n\n\n\n\n\n', asResult.Print(), '\n\n\n\n\n\n', '*' * 40)
#
#
#
# a1.setConstant(0); a2.setConstant(0); a3.setConstant(0);
# a1_phi.setConstant(0); a2_phi.setConstant(0); a3_phi.setConstant(0);
# N[sPlot_to].setVal(0); N[sPlot_to].setConstant(1);
# model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE))
# rrr_null = model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE), RF.Save())
#
# nll_sig  = rrr_sig.minNll()
# nll_null = rrr_null.minNll()
# P = ROOT.TMath.Prob(2*(nll_null - nll_sig), 1) ## !!! Change delta of ndf appropriately
# # S = ROOT.TMath.ErfcInverse(P) * sqrt(2)
# S = ROOT.Math.gaussian_quantile_c(P, 1)
# print ('P=', P, ' nll_sig=', nll_sig, ' nll_null=', nll_null, '\n', 'S=', S)


#             #---------------#
#             ##  sPlot III  ##
#             #---------------#
#
# c_sPlot_3 = ROOT.TCanvas("c_sPlot_3", "c_sPlot_3", 800, 600)
# mean_Bs.setConstant(1); mean_phi.setConstant(1); mean_control[MODE].setConstant(1);
# N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)
#
# model[sPlot_from].fitTo(data_sideband, RF.Extended(ROOT.kTRUE))
# model[sPlot_from].fitTo(data_sideband, RF.Extended(ROOT.kTRUE))
# a1.setConstant(1); a2.setConstant(1); a3.setConstant(1); a4.setConstant(1);
# a1_phi.setConstant(1); a2_phi.setConstant(1); a3_phi.setConstant(1); a4_phi.setConstant(1);
# a1_ext.setConstant(1); a2_ext.setConstant(1); a3_ext.setConstant(1); a4_ext.setConstant(1);
# model[sPlot_from].fitTo(data_sideband, RF.Extended(ROOT.kTRUE))
# model[sPlot_from].fitTo(data_sideband, RF.Extended(ROOT.kTRUE))
#
# a1.setConstant(0); a2.setConstant(0); a3.setConstant(0); a4.setConstant(0);
# a1_phi.setConstant(0); a2_phi.setConstant(0); a3_phi.setConstant(0); a4_phi.setConstant(0);
# a1_ext.setConstant(0); a2_ext.setConstant(0); a3_ext.setConstant(0); a4_ext.setConstant(0);
#
# model[sPlot_from].fitTo(data_sideband, RF.Extended(ROOT.kTRUE))
#
# # file_out_data.write(str(N[sPlot_from].getVal()) + ' ' + str(N[sPlot_from].getError()) + '\n')
# plot_on_frame(var[sPlot_from], data_sideband, model[sPlot_from], '', left[sPlot_from], right[sPlot_from], nbins[sPlot_from], None, False, chi_dict)
# plot_pull(var[sPlot_from], data_sideband, model[sPlot_from], save=True)
# plot_toys_pull(var[sPlot_from], model[sPlot_from], var_to_study = N_sig_Bs,  N_toys = 1000, N_gen = int(data_sideband.sumEntries()), save = True, label = data_sideband.GetName())
#
# CMS_tdrStyle_lumi.CMS_lumi( c_sPlot_3, 2, 0 );
# c_sPlot_3.Update(); c_sPlot_3.RedrawAxis(); # c_sPlot_3.GetFrame().Draw();
# # c_sPlot_3.SaveAs('~/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/c_sPlot_3_' + str(MODE) + refl_line + '.pdf')
#
#
#             #--------------#
#             ##  sPlot IV  ##
#             #--------------#
#
# sData_Bs_psi_side = ROOT.RooStats.SPlot(
#     'sData_Bs_psi_side', 'sData_Bs_psi_side', data_sideband, model[sPlot_from],
#     sPlot_list
# )
# data_side_weighted = ROOT.RooDataSet(data_sideband.GetName(), data_sideband.GetTitle(), data_sideband, data_sideband.get(), '1 > 0', N[sPlot_from].GetName() + '_sw') ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi
# data_side_weighted.SetName('sideband_w')
# #
# c_sPlot_4 = ROOT.TCanvas("c_sPlot_4", "c_sPlot_4", 800, 600)
# model[sPlot_to].fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE))
# model[sPlot_to].fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE))
# model[sPlot_to].fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE))
# a1.setConstant(1); a2.setConstant(1); a3.setConstant(1); a4.setConstant(1);
# a1_phi.setConstant(1); a2_phi.setConstant(1); a3_phi.setConstant(1); a4_phi.setConstant(1);
# a1_ext.setConstant(1); a2_ext.setConstant(1); a3_ext.setConstant(1); a4_ext.setConstant(1);
# model[sPlot_to].fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE))
#
# # file_out_data.write(str(N[sPlot_to].getVal()) + ' ' + str(N[sPlot_to].getError()) + '\n')
# # file_out_data.close()
#
# # model_control.fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE))
# plot_on_frame(var[sPlot_to], data_side_weighted, model[sPlot_to], '', left[sPlot_to], right[sPlot_to], nbins[sPlot_to], None, False, chi_dict)
# # plot_pull(var[sPlot_to], data_side_weighted, model[sPlot_to], save=True)
#
# CMS_tdrStyle_lumi.CMS_lumi( c_sPlot_4, 2, 0 );
# c_sPlot_4.Update(); c_sPlot_4.RedrawAxis(); # c_sPlot_4.GetFrame().Draw();
# # c_sPlot_4.SaveAs('~/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/c_sPlot_4_' + str(MODE) + refl_line + '.pdf')
#
# a1.setConstant(0); a2.setConstant(0); a3.setConstant(0); a4.setConstant(0);
# a1_phi.setConstant(0); a2_phi.setConstant(0); a3_phi.setConstant(0); a4_phi.setConstant(0);
# a1_ext.setConstant(0); a2_ext.setConstant(0); a3_ext.setConstant(0); a4_ext.setConstant(0);
#
# with open('./fit_validation/chis_' + MODE + '.txt', 'w') as file:
#     file.write(json.dumps(chi_dict))

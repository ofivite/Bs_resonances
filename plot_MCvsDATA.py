from RooSpace import *
from cuts import *

ROOT.gStyle.SetOptStat(0)

f_d = ROOT.TFile('psi_data_sPlot_sig.root')
f_m = ROOT.TFile('psi_MC_sPlot_sig.root')

data = f_d.Get('data')
MC = f_m.Get('data')

# var_list = [mu_max_pt, mu_min_pt, mu_max_eta, mu_min_eta, K_max_pt, K_min_pt, K_max_eta, K_min_eta, pi_max_pt, pi_min_pt, pi_max_eta, pi_min_eta, BU_pt_Cjp, BU_eta_Cjp]
# var_name_list = ['mu_max_pt', 'mu_min_pt', 'mu_max_eta', 'mu_min_eta', 'K_max_pt', 'K_min_pt', 'K_max_eta', 'K_min_eta', 'pi_max_pt', 'pi_min_pt', 'pi_max_eta', 'pi_min_eta', 'BU_pt_Cjp', 'BU_eta_Cjp']
#
# mu_max_pt.setMax(40.); mu_min_pt.setMax(15.);
# K_max_pt.setMax(15.); K_min_pt.setMax(15.);
# pi_max_pt.setMax(10.); pi_min_pt.setMax(4.);
# BU_pt_Cjp.setMax(80.);
#
# mu_max_pt.setBins(40); mu_min_pt.setBins(40); mu_max_eta.setBins(50); mu_min_eta.setBins(50);
# K_max_pt.setBins(30); K_min_pt.setBins(30); K_max_eta.setBins(50); K_min_eta.setBins(50);
# pi_max_pt.setBins(40); pi_min_pt.setBins(40); pi_max_eta.setBins(50); pi_min_eta.setBins(50);
# BU_pt_Cjp.setBins(40); BU_eta_Cjp.setBins(50);


var_list = [mu_1_pt, mu_2_pt, mu_1_eta, mu_2_eta, K1_pt, K2_pt, K1_eta, K2_eta, PI1_pt, PI2_pt, PI1_eta, PI2_eta,
            BU_pt_Cjp, BU_eta_Cjp, BU_pvdistsignif2_Cjp, BU_pvcos2_Cjp, BU_vtxprob_Cjp,
            JP_pt, JP_eta, JPSI_pvdistsignif2_Cmumu, JPSI_pvcos2_Cmumu, JPSI_vtxprob_Cmumu, JPSI_mass_Cmumu,
            var_control, PIPI_mass_Cjp]
var_name_list = ['mu_1_pt', 'mu_2_pt', 'mu_1_eta', 'mu_2_eta', 'K1_pt', 'K2_pt', 'K1_eta', 'K2_eta', 'PI1_pt', 'PI2_pt', 'PI1_eta', 'PI2_eta',
                 'BU_pt_Cjp', 'BU_eta_Cjp', 'BU_pvdistsignif2_Cjp', 'BU_pvcos2_Cjp', 'BU_vtxprob_Cjp',
                 'JP_pt', 'JP_eta', 'JPSI_pvdistsignif2_Cmumu', 'JPSI_pvcos2_Cmumu', 'JPSI_vtxprob_Cmumu', 'JPSI_mass_Cmumu',
                 'psi_mass_Cjp', 'PIPI_mass_Cjp']

mu_1_pt.setMax(35.); mu_2_pt.setMax(35.);
K1_pt.setMax(15.); K2_pt.setMax(15.);
PI1_pt.setMax(8.); PI2_pt.setMax(8.);
BU_pt_Cjp.setMax(80.);

BU_pvdistsignif2_Cjp.setMax(300.); BU_pvcos2_Cjp.setMin(.999); BU_pvcos2_Cjp.setMax(1.);
JP_pt.setMax(70.); JPSI_pvdistsignif2_Cmumu.setMax(200.);
JPSI_mass_Cmumu.setMin(3.); JPSI_mass_Cmumu.setMax(3.2);
JPSI_pvcos2_Cmumu.setMin(.995); JPSI_pvcos2_Cmumu.setMax(1.);
var_control.setMin(3.67); var_control.setMax(3.7);
PIPI_mass_Cjp.setMin(.4); PIPI_mass_Cjp.setMax(.6);

mu_1_pt.setBins(35); mu_2_pt.setBins(35); mu_1_eta.setBins(50); mu_2_eta.setBins(50);
K1_pt.setBins(30); K2_pt.setBins(30); K1_eta.setBins(50); K2_eta.setBins(50);
PI1_pt.setBins(40); PI2_pt.setBins(40); PI1_eta.setBins(50); PI2_eta.setBins(50);
BU_pt_Cjp.setBins(40); BU_eta_Cjp.setBins(50);

BU_pvdistsignif2_Cjp.setBins(60); JP_pt.setBins(35); JP_eta.setBins(50);
JPSI_mass_Cmumu.setBins(40); JPSI_pvdistsignif2_Cmumu.setBins(40); var_control.setBins(30); BU_vtxprob_Cjp.setBins(50);
JPSI_vtxprob_Cmumu.setBins(50); PIPI_mass_Cjp.setBins(50);

for var, var_name in zip(var_list, var_name_list):
    c = ROOT.TCanvas("c", "c", 800, 600)
    hist_d = ROOT.TH1F('hist_d', ' ', var.getBins(), var.getMin(), var.getMax())
    hist_mc = ROOT.TH1F('hist_mc', ' ', var.getBins(), var.getMin(), var.getMax())
    data.fillHistogram(hist_d, ROOT.RooArgList(var));
    MC.fillHistogram(hist_mc, ROOT.RooArgList(var))
    hist_d.Scale( 1./data.sumEntries() ); hist_mc.Scale( 1./MC.sumEntries() )

    hist_d.SetLineColor(47);  hist_mc.SetLineColor(ROOT.kBlue-8)
    hist_d.SetLineWidth(3); hist_mc.SetLineWidth(3)
    hist_d.GetXaxis().SetTitle(var.GetTitle()); hist_mc.GetXaxis().SetTitle(var.GetTitle())
    hist_d.Draw('hist')
    hist_mc.Draw('hist same')

    leg = ROOT.TLegend(0.65, 0.75, 0.89, 0.89)
    leg.AddEntry(hist_mc, 'MC', 'l')
    leg.AddEntry(hist_d, 'Data, sPlot from SR', 'l')
    leg.Draw()

    c.SaveAs('MCvsDATA/' + var_name + '.pdf')

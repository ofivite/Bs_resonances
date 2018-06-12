from RooSpace import *
from cuts import *

ROOT.gStyle.SetOptStat(0)

f_d = ROOT.TFile('psi_PtEta_data.root')
f_m = ROOT.TFile('psi_PtEta_MC.root')

data = f_d.Get('data')
MC = f_m.Get('data_MC')
scale = MC.sumEntries() / data.sumEntries()

var_list = [mu_max_pt, mu_min_pt, mu_max_eta, mu_min_eta, K_max_pt, K_min_pt, K_max_eta, K_min_eta, pi_max_pt, pi_min_pt, pi_max_eta, pi_min_eta]
var_name_list = ['mu_max_pt', 'mu_min_pt', 'mu_max_eta', 'mu_min_eta', 'K_max_pt', 'K_min_pt', 'K_max_eta', 'K_min_eta', 'pi_max_pt', 'pi_min_pt', 'pi_max_eta', 'pi_min_eta']

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
    # frame = var.frame()
    # data.plotOn(frame, RF.Rescale(scale), RF.DrawOption('HIST B'), RF.LineColor(47))
    # MC.plotOn(frame, RF.DrawOption('HIST B'), RF.LineColor(ROOT.kBlue-8))
    # frame.Draw()
    c.SaveAs('MCvsDATA_Bs_psi/' + var_name + '.pdf')

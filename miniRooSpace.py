import os
import sys
from datetime import datetime

import ROOT
from ROOT import RooFit as RF
from cuts import *
import CMS_tdrStyle_lumi

# var_discr = ROOT.RooRealVar('BU_mass_Cjp', 'm(J/#psi#pi^{+}#pi^{#font[122]{\55}}K^{+}K^{#font[122]{\55}}) [GeV]', 5.1, 5.6)
# var_control = ROOT.RooRealVar('X_mass_Cjp', 'm(J/#psi#pi^{+}#pi^{#font[122]{\55}}) [GeV]', 3.4, 4.2)
# PIPI_mass_Cjp = ROOT.RooRealVar('PIPI_mass_Cjp', 'm(#pi^{+}#pi^{#font[122]{\55}}) [GeV]', 0.2, 1.2)
# PHI_mass_Cjp = ROOT.RooRealVar('PHI_mass_Cjp', 'm(K^{+}K^{#font[122]{\55}}) [GeV]', 0., 2.)
# SAMEEVENT = ROOT.RooRealVar('SAMEEVENT', 'SAMEEVENT', 0., 2.)
#
# mu_max_pt = ROOT.RooRealVar('mu_max_pt', 'p_{T}^{max}(#mu) [GeV]', 0., 400.)
# mu_min_pt = ROOT.RooRealVar('mu_min_pt', 'p_{T}^{min}(#mu) [GeV]', 0., 200.)
# mu_max_eta = ROOT.RooRealVar('mu_max_eta', '#eta^{max}(#mu)', -2.5, 2.5)
# mu_min_eta = ROOT.RooRealVar('mu_min_eta', '#eta^{min}(#mu)', -2.5, 2.5)
#
# K_max_pt = ROOT.RooRealVar('K_max_pt', 'p_{T}^{max}(K) [GeV]', 0., 150.)
# K_min_pt = ROOT.RooRealVar('K_min_pt', 'p_{T}^{min}(K) [GeV]', 0., 150.)
# K_max_eta = ROOT.RooRealVar('K_max_eta', '#eta^{max}(K)', -2.5, 2.5)
# K_min_eta = ROOT.RooRealVar('K_min_eta', '#eta^{min}(K)', -2.5, 2.5)
#
# pi_max_pt = ROOT.RooRealVar('pi_max_pt', 'p_{T}^{max}(#pi) [GeV]', 0., 100.)
# pi_min_pt = ROOT.RooRealVar('pi_min_pt', 'p_{T}^{min}(#pi) [GeV]', 0., 400.)
# pi_max_eta = ROOT.RooRealVar('pi_max_eta', '#eta^{max}(#pi)', -2.5, 2.5)
# pi_min_eta = ROOT.RooRealVar('pi_min_eta', '#eta^{min}(#pi)', -2.5, 2.5)
#
# BU_pt_Cjp = ROOT.RooRealVar('BU_pt_Cjp', 'p_{T}(B_{s}^{0}) [GeV]', 0, 800)
# BU_eta_Cjp = ROOT.RooRealVar('BU_eta_Cjp', '#eta(B_{s}^{0})', -2.5, 2.5)

#############################################################################################
# B0->psi(2S)K*0 reflection

# file_B0_refl_ws = ROOT.TFile('~/Study/Bs_resonances/file_B0_refl_ws_data_cuts_dR0p05_SC.root')
file_B0_refl_ws = ROOT.TFile('~/Study/Bs_resonances/file_B0_refl_dR0p05_from_a1c59b9.root')
w = file_B0_refl_ws.Get('w')

# B0_refl = w.pdf('B0_refl')
B0_refl = w.pdf('B0_refl_SR')
N_B0_refl = ROOT.RooRealVar('N_B0_refl', '', 990., 0., 1000.)


#
# plot_discr_param = ROOT.RooArgSet(mean_Bs, sigma_Bs_1, sigma_Bs_2, fr_Bs, N_sig_Bs, N_bkgr_Bs)
# plot_psi_param = ROOT.RooArgSet(mean_psi, sigma_psi_1, sigma_psi_2, fr_psi, N_sig_psi, N_bkgr_control)
# plot_phi_param = ROOT.RooArgSet(ROOT.RooArgSet(mean_phi), ROOT.RooArgSet(sigmaCB_phi_1, sigmaCB_phi_2, alpha_phi_1, alpha_phi_2, n_phi_1, n_phi_2, N_sig_phi, N_bkgr_phi, fr_phi))
# # plot_phi_param = ROOT.RooArgSet(mean_phi, gamma_BW_phi, sigma_phi_1, sigma_phi_2, sigmaCB_phi_1, sigmaCB_phi_2, alpha_phi_1, alpha_phi_2, n_phi_1, n_phi_2, N_sig_phi, N_bkgr_phi, fr_phi)
# plot_X_param = ROOT.RooArgSet(mean_X, sigma_X_1, sigma_X_2, fr_X, N_sig_X, N_bkgr_control)
# plot_control_param = {'X': plot_X_param, 'psi': plot_psi_param}

def plot_on_frame(roovar, data, model, title, left, right, nbins, plot_par, isMC):
    frame = ROOT.RooPlot(" ", title, roovar, left, right, nbins);
    # if SumW2 == 1:
    #     data.plotOn(frame, RF.DataError(ROOT.RooAbsData.SumW2))
    # else:
    #     data.plotOn(frame, RF.DataError(ROOT.RooAbsData.SumW2))
    data.plotOn(frame, RF.DataError(ROOT.RooAbsData.Auto))
    # model.paramOn(frame, RF.Layout(0.55, 0.96, 0.9), RF.Parameters(plot_par))
    # frame.getAttText().SetTextSize(0.053)
    model.plotOn(frame, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5)) #, RF.NormRange("full"), RF.Range('full')
    floatPars = model.getParameters(data).selectByAttrib('Constant', ROOT.kFALSE)
    print '\n\n' + 30*'<' + '\n\n         ndf = ' + str(floatPars.getSize()) + ';    chi2/ndf = ' + str(frame.chiSquare(floatPars.getSize())) + ' for ' + str(model.GetName()) + ' and ' + str(data.GetName()) + '         \n\n' + 30*'>' + '\n\n'

    model.plotOn(frame, RF.Components("model_bb_2D"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kGreen-2), RF.LineWidth(4) );
    model.plotOn(frame, RF.Components("model_bs_2D"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kAzure+3), RF.LineWidth(4));
    model.plotOn(frame, RF.Components("model_sb_2D"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
    model.plotOn(frame, RF.Components("model_ss_2D"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kOrange+7), RF.LineWidth(4) );
# , RF.Range(mean_phi.getValV() - 15 * gamma_BW_phi.getValV(), mean_phi.getValV() + 15 * gamma_BW_phi.getValV())
    model.plotOn(frame, RF.Components("sig_Bs_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    model.plotOn(frame, RF.Components("sig_Bs_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    model.plotOn(frame, RF.Components('sig_' + str(mode) + '_1'), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    model.plotOn(frame, RF.Components('sig_' + str(mode) + '_2'), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    # model_X.plotOn(frame_control, RF.Components("sig_X_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    # model_X.plotOn(frame_control, RF.Components("sig_X_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    # model.plotOn(frame_control, RF.Components("signal_X"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    model.plotOn(frame, RF.Components("bkgr_control"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
    model.plotOn(frame, RF.Components("bkgr_phi"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
    model.plotOn(frame, RF.Components("bkgr_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
    # model.plotOn(frame, RF.Components("signal_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 15 * sigma_Bs.getValV(), mean_Bs.getValV() + 15 * sigma_Bs.getValV()));
    model.plotOn(frame, RF.Components("signal_phi"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    if refl_ON: model.plotOn(frame, RF.Components("B0_refl_SR"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kGreen-5), RF.LineWidth(4), RF.Normalization(1.0), RF.Name('B0_refl_SR'), RF.Range(5.32, 5.44));
    data.plotOn(frame, RF.DataError(ROOT.RooAbsData.Auto))

    frame.GetYaxis().SetTitle('Candidates / ' + str(int((right - left) / nbins * 1000.)) + ' MeV')
    frame.GetXaxis().SetTitleSize(0.04)
    frame.GetYaxis().SetTitleSize(0.04)
    frame.GetXaxis().SetLabelSize(0.033)
    frame.GetYaxis().SetLabelSize(0.033)
    frame.GetXaxis().SetTitleOffset(1.05)
    frame.GetYaxis().SetTitleOffset(1.3)
    frame.Draw()


def _import(wsp, obj):
    getattr(wsp, 'import')(obj)

def get_timestamp(fmt='%Y-%m-%d-%a-%H-%M'):
    """Return formatted timestamp."""
    return datetime.strftime(datetime.today(), fmt)

def get_file(fname, mode='read'):
    """Open and return a ROOT file."""
    if os.path.exists(fname):
        return ROOT.TFile(fname, mode)
    else:
        raise IOError('File %s does not exist!' % fname)

def save_in_workspace(rfile, **argsets):
    """Save RooFit objects in workspace and persistify.
    Pass the different types of objects as a keyword arguments. e.g.
    save_in_workspace(pdf=[pdf1, pdf2], variable=[var1, var2])
    """

    # from rplot.fixes import ROOT
    import traceback
    # Persistify variables, PDFs and datasets
    workspace = ROOT.RooWorkspace('workspace', 'Workspace saved at %s' % get_timestamp())
    keys = argsets.keys()
    for key in keys:
        print 'Importing RooFit objects in %s list.' % key
        for arg in argsets[key]:
            try:
                _import(workspace, arg)
            except TypeError:
                print type(arg), arg
                traceback.print_exc()
    rfile.WriteTObject(workspace)
    print 'Saving arguments to file: %s' % rfile.GetName()


def get_workspace(fname, wname):
    """Read and return RooWorkspace from file."""
    ffile = get_file(fname, 'read')
    workspace = ffile.Get(wname)
    return workspace, ffile

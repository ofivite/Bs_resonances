# TODO: proper docstring for Functions, class implementation

import ROOT
from ROOT import RooFit as RF
from scipy.stats import chi2

class DataExplorer(object):
    """docstring for DataExplorer."""
    # def __init__(self, data, model, mode, var, poi):
        # super(DataExplorer, self).__init__()
        # self.data = data
        # self.model = model
        # self.mode = mode
        # self.var = var
        # self.poi = poi
        # self.is_fitted = False

    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)
        self.is_fitted = False
        self.chi_dict  = {}
        self.left  = self.var.getMin()
        self.right = self.var.getMax()
        self.nbins = self.var.numBins()


    def fit_data(self, is_extended, is_sum_w2, fix_float, **kwargs):
        """
        Fit some data distribution.
        NB: the corresponding model parameters will be updated after executing

        :param:
        :returns: None
        """
        self.model.fitTo(self.data, RF.Extended(is_extended), RF.SumW2Error(is_sum_w2))
        for param in fix_float:
            param.setConstant(1)
        #
        self.model.fitTo(self.data, RF.Extended(is_extended), RF.SumW2Error(is_sum_w2))
        for param in fix_float:
            param.setConstant(0)
        #
        self.model.fitTo(self.data, RF.Extended(is_extended), RF.SumW2Error(is_sum_w2))
        self.model.fitTo(self.data, RF.Extended(is_extended), RF.SumW2Error(is_sum_w2))
        self.is_fitted = True

    def prepare_workspace(self, poi, nuisances):
        """
        Create a worspace with the fitted to the data model and predefined POI and nuisance parameters

        :return: RooWorkspace
        """

        if not self.is_fitted:
            print('no workspace to be created: fit me to the data first')
            return

        w = ROOT.RooWorkspace("w", True)
        Import = getattr(ROOT.RooWorkspace, 'import') # special trick to make things not crush
        Import(w, self.model)
        mc = ROOT.RooStats.ModelConfig("ModelConfig", w)
        mc.SetPdf(w.pdf(self.model.GetName()))
        mc.SetParametersOfInterest(ROOT.RooArgSet(w.var(poi.GetName())))
        # w.var("N_sig_X").setError(20.)
        mc.SetObservables(ROOT.RooArgSet(w.var(self.var.GetName())))
        mc.SetNuisanceParameters(ROOT.RooArgSet(*[w.var(nui.GetName()) for nui in nuisances]))
        mc.SetSnapshot(ROOT.RooArgSet(w.var(poi.GetName())))
        Import(w, mc, 'ModelConfig')
        Import(w, self.data, 'data')
        self.w = w
        return w

    def asympt_signif(self, w):
        """
        Function to calculate one-sided significance for a given in the workspace s+b model using RooStats.AsymptoticCalculator

        :param: w: workspace to open
        :returns: GetHypoTest() object for printing with Print()
        """
        data = w.obj("data")
        #
        sbModel = w.obj("ModelConfig")
        sbModel.SetName("S+B_model")
        poi = sbModel.GetParametersOfInterest().first()
        #
        bModel = sbModel.Clone()
        bModel.SetName("B_only_model")
        oldval = poi.getVal()
        poi.setVal(0)
        bModel.SetSnapshot(ROOT.RooArgSet(poi))
        poi.setVal(oldval)
        #
        ac = ROOT.RooStats.AsymptoticCalculator(data, sbModel, bModel)
        ac.SetOneSidedDiscovery(True)
        as_result = ac.GetHypoTest()
        return as_result

    def plot_ll(self, poi, save = False):
        nll = self.model.createNLL(self.data)
        pll = nll.createProfile(ROOT.RooArgSet(poi))
        #
        c_ll = ROOT.TCanvas("c_ll", "c_ll", 800, 600); ll_left = 0; ll_right = 200
        frame_nll = poi.frame(RF.Bins(100), RF.Range(ll_left, ll_right))
        frame_nll.SetTitle('')
        #
        nll.plotOn(frame_nll, RF.ShiftToZero(), RF.LineColor(ROOT.kGreen))
        # nll.plotOn(frame_nll, RF.LineColor(ROOT.kGreen))
        pll.plotOn(frame_nll, RF.LineColor(ROOT.kRed))
        #
        frame_nll.SetMaximum(25.)
        frame_nll.SetMinimum(0.)
        frame_nll.Draw()
        #
        line_width = 4
        line_5sigma = ROOT.TLine(ll_left, 12.5, ll_right, 12.5)
        line_5sigma.SetLineWidth(line_width); line_5sigma.SetLineColor(47)
        line_5sigma.Draw();
        #
        CMS_tdrStyle_lumi.CMS_lumi( c_ll, 2, 0 );
        c_ll.Update(); c_ll.RedrawAxis(); # c_inclus.GetFrame().Draw();
        if save: c_ll.SaveAs(self.mode + '1_pll.pdf')


    def plot_var(self, title = ' ', plot_params = ROOT.RooArgSet()):
        """
        Plot the class model and data on the class variable's frame

        :title: Title for a RooPlot frame
        :plot_params: RooArgset with parameters to be shown on Legend

        :return: RooPlot frame
        """
        frame = ROOT.RooPlot(" ", title, self.var, self.left, self.right, self.nbins)
        self.data.plotOn(frame, RF.DataError(ROOT.RooAbsData.Auto))
        self.model.plotOn(frame, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5)) #, RF.NormRange('full'), RF.Range('full')
        self.model.paramOn(frame, RF.Layout(0.55, 0.96, 0.9), RF.Parameters(plot_params))
        frame.getAttText().SetTextSize(0.053)

        # Do chi2 GoF test
        nfloat = self.model.getParameters(self.data).selectByAttrib("Constant", ROOT.kFALSE).getSize()
        ndf = self.nbins - nfloat; chi = frame.chiSquare(nfloat) * ndf;
        pvalue = 1 - chi2.cdf(chi, ndf)
        self.chi_dict.update({self.model.GetName() + '_' + self.data.GetName(): [chi, ndf, pvalue]})

        # Loop over model components and plot'em
        iter = self.model.getComponents().iterator()
        iter_comp = iter.Next()
        while iter_comp:
            if 'sig' in iter_comp.GetName().split('_'):
                self.model.plotOn(frame, RF.Components(iter_comp.GetName()), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4))
            if 'bkgr' in iter_comp.GetName().split('_'):
                self.model.plotOn(frame, RF.Components(iter_comp.GetName()), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4))
            iter_comp = iter.Next()
        #
        if self.refl_ON: self.model.plotOn(frame, RF.Components("B0_refl_SR"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kGreen-5), RF.LineWidth(4), RF.Normalization(1.0), RF.Name('B0_refl_SR'), RF.Range(5.32, 5.44))
        self.data.plotOn(frame, RF.DataError(ROOT.RooAbsData.Auto)) # plotting data at the beginning once sometimes doesn't work
        #
        frame.GetYaxis().SetTitle('Candidates / ' + str(round((self.right - self.left) * 1000. / self.nbins, 1)) + ' MeV')
        frame.GetXaxis().SetTitleSize(0.04)
        frame.GetYaxis().SetTitleSize(0.04)
        frame.GetXaxis().SetLabelSize(0.033)
        frame.GetYaxis().SetLabelSize(0.033)
        frame.GetXaxis().SetTitleOffset(1.05)
        frame.GetYaxis().SetTitleOffset(1.3)
        #
        return frame

    def plot_pull(self, save = False):
        c_pulls = ROOT.TCanvas("c_pulls", "c_pulls", 800, 600)
        frame = self.var.frame()
        self.data.plotOn(frame)
        self.model.plotOn(frame)
        pull_hist = frame.pullHist()
        #
        frame2 = self.var.frame()
        frame2.addPlotable(pull_hist, 'P')
        frame2.Draw()
        if save: c_pulls.SaveAs('~/Study/Bs_resonances/fit_validation/'+ self.mode + '_' + self.data.GetName() + '.pdf')

    def plot_toys_pull(self, var_to_study, N_toys=100, N_gen = 1, label = '', save = False):
        width_N = 80 if self.mode == 'X' else 250
        err_upper = 30 if self.mode == 'X' else 400; err_nbins = 30
        var_lower = var_to_study.getVal() - width_N; var_upper = var_to_study.getVal() + width_N; var_nbins = 50
        #
        MC_manager = ROOT.RooMCStudy(self.model, ROOT.RooArgSet(self.var), RF.Extended(True), RF.FitOptions('mvl'))
        MC_manager.generateAndFit(N_toys, N_gen)
        #
        frame_var = var_to_study.frame(var_lower, var_upper, var_nbins);  MC_manager.plotParamOn(frame_var)
        frame_err = MC_manager.plotError(var_to_study)
        frame_pull = MC_manager.plotPull(var_to_study, -3, 3, 60, ROOT.kTRUE)
        #
        if save:
            c_var = ROOT.TCanvas("c_var", "c_var", 800, 600)
            frame_var.Draw()
            c_err = ROOT.TCanvas("c_err", "c_err", 800, 600)
            frame_err.Draw()
            c_pull = ROOT.TCanvas("c_pull", "c_pull", 800, 600)
            frame_pull.Draw()
            #
            c_var.SaveAs('~/Study/Bs_resonances/fit_validation/' + self.mode + '_' + self.var.GetName() + '_' + label + '.pdf')
            c_err.SaveAs('~/Study/Bs_resonances/fit_validation/' + self.mode + '_' + self.var.GetName() + '_' + label + '_err.pdf')
            c_pull.SaveAs('~/Study/Bs_resonances/fit_validation/'+ self.mode + '_' + self.var.GetName() + '_' + label + '_pull.pdf')

################################################################################################################################

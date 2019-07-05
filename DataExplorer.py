#
#   TODO
#
# proper docstring for Functions
# complex inherited classes (StatExplorer?)
# override chi2fit in StatExplorer with optional data
# exception handling
# private/protected items
# remove functions from the end of RooSpace.py (but study them firstly)
# are is_extended and is_sum_w2 necessary?
# make poi instance variable of StatExplorer, not DataExplorer

import ROOT
from ROOT import RooFit as RF
from scipy.stats import chi2
from math import sqrt
from pandas import DataFrame

class DataExplorer(object):
    """Base class exploring data-model relationship in Bs->X(3872)phi study"""

    def __init__(self, label, data, model):
        super(DataExplorer, self).__init__()
        assert (type(label) is str), 'label is not str'
        self.data = data
        self.model = model
        self.var = model.getObservables(data).iterator().Next()
        self.label = label
        self.is_fitted = False

    def set_regions(self):
        """Set signal region (SR) window and distance to sidebands (SdR)

        Parameters
        ---------

        Returns
        -------
        self, object
        """
        if self.label == 'phi':
            self.window = 0.01
            self.distance_to_sdb = 0.005
        else:
            fr      = self.model.getVariables().find(f'fr_{self.label}').getVal()
            sigma_1 = self.model.getVariables().find(f'sigma_{self.label}_1').getVal()
            sigma_2 = self.model.getVariables().find(f'sigma_{self.label}_2').getVal()
            sigma_eff = sqrt(fr*sigma_1**2 + (1-fr)*sigma_2**2)  ### effective sigma of sum of two gaussians with common mean
            #
            self.window = 3*sigma_eff
            self.distance_to_sdb = 2*sigma_eff
        return self

    def get_regions(self):
        """Reduce instance dataset with SR and SdR cuts
        NB: mind that mean might be pre- or post-fitted

        Returns
        -------
        data_sig, data_sideband: tuple of RooDataSet
            datasets corresponding to events in SR and SdR
        """
        mean = self.model.getParameters(self.data).find(f'mean_{self.label}').getVal()
        data_sig = self.data.reduce(f'TMath::Abs({self.var.GetName()} - {mean}) < {self.window}')
        data_sideband = self.data.reduce(f'TMath::Abs({self.var.GetName()} - {mean}) > {self.window + self.distance_to_sdb} && TMath::Abs({self.var.GetName()} -{mean}) < {2.*self.window + self.distance_to_sdb}')
        data_sig.SetName('sig')
        data_sideband.SetName('sideband')
        return data_sig, data_sideband

    def plot_regions(self, frame, y_sdb_left=0, y_sr=0, y_sdb_right=0, line_width=4):
        """Add vertical lines illustrating SR and SdR regions to the frame.
        NB: SR=|m-mean|<window;
            SdR=|m-mean|>window+distance_to_sdb &
                |m-mean|<2*window+distance_to_sdb

        Parameters
        ----------
        frame: RooPlot
            RooPlot frame to draw the lines on
        y_sdb_left: float, optional (default=0)
            y-coordinate for the left sideband region
        y_sr: float, optional (default=0)
            y-coordinate for the signal region
        y_sdb_right: float, optional (default=0)
            y-coordinate for the right sideband region

        Returns
        -------
        frame: RooPlot
        """
        mean = self.model.getParameters(self.data).find(f'mean_{self.label}').getVal()
        line_ll_sdb = (ROOT.TLine(mean - 2.*self.window - self.distance_to_sdb, 0, mean - 2.*self.window - self.distance_to_sdb, y_sdb_left),  ROOT.kBlue-8)
        line_lr_sdb = (ROOT.TLine(mean - self.window - self.distance_to_sdb,    0, mean - self.window - self.distance_to_sdb,    y_sdb_left),  ROOT.kBlue-8)
        line_rl_sdb = (ROOT.TLine(mean + 2.*self.window + self.distance_to_sdb, 0, mean + 2.*self.window + self.distance_to_sdb, y_sdb_right), ROOT.kBlue-8)
        line_rr_sdb = (ROOT.TLine(mean + self.window + self.distance_to_sdb   , 0, mean + self.window + self.distance_to_sdb,    y_sdb_right), ROOT.kBlue-8)
        line_l_sig  = (ROOT.TLine(mean - self.window,                           0, mean - self.window,                           y_sr)        , 47)
        line_r_sig  = (ROOT.TLine(mean + self.window,                           0, mean + self.window,                           y_sr)        , 47)
        lines = (line_ll_sdb, line_lr_sdb, line_rl_sdb, line_rr_sdb, line_l_sig, line_r_sig)
        #
        for line, color in lines:
            line.SetLineColor(color)
            line.SetLineWidth(line_width)
            frame.addObject(line)
        return frame

    def fit(self, is_sum_w2, fix_float=[]):
        """Fit instance data with instance model using fitTo() method. Set is_fitted=True.
        NB: the corresponding model parameters will be updated outside of the class instance after executing!

        Parameters
        ----------
        is_sum_w2: bool
            correct Hessian with data weights matrix to get correct errors, see RooFit tutorial rf403__weightedevts
        fix_float: list of RooRealVar, optional (default=[])
            variables from this list will be firstly setConstant(1) in the fit and then setConstant(0)

        Returns
        -------
        fit_results: RooFitResult
        """
        is_extended = self.model.canBeExtended()
        self.model.fitTo(self.data, RF.Extended(is_extended), RF.SumW2Error(is_sum_w2))
        for param in fix_float:
            param.setConstant(1)
        #
        self.model.fitTo(self.data, RF.Extended(is_extended), RF.SumW2Error(is_sum_w2))
        for param in fix_float:
            param.setConstant(0)
        #
        self.model.fitTo(self.data, RF.Extended(is_extended), RF.SumW2Error(is_sum_w2))
        fit_results = self.model.fitTo(self.data, RF.Extended(is_extended), RF.SumW2Error(is_sum_w2), RF.Save())
        self.is_fitted = True
        return fit_results

    def chi2_fit(self, data = None, fix_float=[], run_minos = False, poi = None, is_sum_w2 = 'auto'):
        """Fit the instance data with binned chi2 method
        NB: weights presence is taken care of automatically

        Parameters
        ----------

        //to be completed//

        run_minos: bool
            whether to calculate MINOS errors

        fix_float: list of RooRealVar, optional (default=[])
            variables from this list will be firstly setConstant(1) in the fit and then setConstant(0)

        Returns
        -------
        self, object

        """
        data_to_fit = self.data if data is None else data
        self.model.chi2FitTo(data_to_fit, ROOT.RooLinkedList())
        for param in fix_float:
            param.setConstant(1)
        self.model.chi2FitTo(data_to_fit, ROOT.RooLinkedList())
        for param in fix_float:
            param.setConstant(0)
        self.model.chi2FitTo(data_to_fit, ROOT.RooLinkedList()) # couldn't make it save RooFitResult
        self.is_fitted = True
        #
        if run_minos:
            is_extended = self.model.canBeExtended()
            chi = ROOT.RooChi2Var("chi","chi", self.model, data_to_fit, RF.Extended(is_extended), RF.DataError(ROOT.RooAbsData.Auto))
            m = ROOT.RooMinimizer(chi)
            m.setMinimizerType("Minuit2")
            m.setPrintLevel(3)
            m.minimize("Minuit2","minimize")
            m.minos(ROOT.RooArgSet(poi))
        return self

    def plot_on_var(self, title=' ', plot_params=ROOT.RooArgSet()):
        """Plot the instance model with all its components and data on the RooPlot frame

        Parameters
        ----------
        title: str, optional (default=' ')
            title for a RooPlot frame
        plot_params: RooArgSet, optional (default=RooArgSet)
            Set of parameters to be shown on the legend

        Returns
        -------
        frame: RooPlot
        """
        var_left  = self.var.getMin();
        var_right = self.var.getMax();
        var_nbins = self.var.numBins()
        #
        frame = ROOT.RooPlot(" ", title, self.var, var_left, var_right, var_nbins)  # frame.getAttText().SetTextSize(0.053)
        self.data.plotOn(frame, RF.DataError(ROOT.RooAbsData.Auto))
        self.model.plotOn(frame, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5)) #, RF.NormRange('full'), RF.Range('full')
        self.model.paramOn(frame, RF.Layout(0.55, 0.96, 0.9), RF.Parameters(plot_params))
        #
        iter = self.model.getComponents().iterator()
        iter_comp = iter.Next()
        while iter_comp:
            if 'sig' in iter_comp.GetName().split('_'):
                self.model.plotOn(frame, RF.Components(iter_comp.GetName()), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4))
            if 'bkgr' in iter_comp.GetName().split('_'):
                self.model.plotOn(frame, RF.Components(iter_comp.GetName()), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4))
            iter_comp = iter.Next()
        #
        self.model.plotOn(frame, RF.Components("B0_refl_SR"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kGreen-5), RF.LineWidth(4), RF.Normalization(1.0), RF.Name('B0_refl_SR'), RF.Range(5.32, 5.44))
        self.data.plotOn(frame, RF.DataError(ROOT.RooAbsData.Auto)) # plotting data at the beginning once sometimes doesn't work
        #
        frame.GetYaxis().SetTitle(f'Candidates / {round((var_right - var_left) * 1000. / var_nbins, 1)} MeV')
        frame.GetXaxis().SetTitleSize(0.04)
        frame.GetYaxis().SetTitleSize(0.04)
        frame.GetXaxis().SetLabelSize(0.033)
        frame.GetYaxis().SetLabelSize(0.033)
        frame.GetXaxis().SetTitleOffset(1.05)
        frame.GetYaxis().SetTitleOffset(1.3)
        return frame

    def prepare_workspace(self, poi, nuisances):
        """Create a workspace with the fitted to the data model, poi and nuisance parameters.

        Parameters
        ----------

        nuisances: list of RooRealVar
            nuisance parameters in statistical inference

        poi: RooRealVar
            parameter of interest in statistical inference

        Returns
        -------
        w: RooWorkspace
        """
        if not self.is_fitted:
            raise Exception('Model was not fitted to data, fit it first')

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
        return w

    @staticmethod
    def extract(w):
        """Extract data, signal+background and background-only models from a given RooWorkspace.
        Background-only model is taken from the s+b model by setting the parameter of interest to be 0.

        NB: naming conventions assume that data's name is 'data', and that the parameter of interest is the first one and corresponds to the signal yield.

        Parameters:
        -----------

        w, RooWorkspace
            workspace with saved data and s+b model to unpack

        Returns:
        --------
        data, model_sb, model_b: RooAbsData, RooAbsPdf, RooAbsPdf
            Tuple with data, s+b and b-only models
        """
        data = w.obj("data")
        #
        model_sb = w.obj("ModelConfig")
        model_sb.SetName("model_sb")
        poi = model_sb.GetParametersOfInterest().first()
        #
        model_b = model_sb.Clone()
        model_b.SetName("B_only_model")
        oldval = poi.getVal()
        poi.setVal(0)
        model_b.SetSnapshot(ROOT.RooArgSet(poi))
        poi.setVal(oldval)
        return data, model_sb, model_b

################################################################################################################################

    # def _asympt_signif_(self):
    #     """
    #     Function to calculate one-sided significance for a given in the workspace s+b model by bare hands
    #
    #     :param: w: workspace to open
    #     :returns: GetHypoTest() object for printing with Print()
    #     """
    #     N[sPlot_to].setVal(0); N[sPlot_to].setConstant(1);
    #     model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE))
    #     rrr_null = model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE), RF.Save())
    #
    #     nll_sig  = rrr_sig.minNll()
    #     nll_null = rrr_null.minNll()
    #     P = ROOT.TMath.Prob(2*(nll_null - nll_sig), 1) ## !!! should be always ndf = 1 = number of poi for this formula to work
    #     # S = ROOT.TMath.ErfcInverse(P) * sqrt(2)
    #     S = ROOT.Math.gaussian_quantile_c(P, 1)
    #     print ('P=', P, ' nll_sig=', nll_sig, ' nll_null=', nll_null, '\n', 'S=', S)

    def chi2_test(self):
        """Do chi2 goodness-of-fit test
        """
        if not self.is_fitted:
            raise Exception('Model was not fitted to data, fit it first')
        is_extended = self.model.canBeExtended()
        data_hist = ROOT.RooDataHist('data_hist', 'data_hist', ROOT.RooArgSet(self.var), self.data) # binning is taken from self.var definition
        nfloat = self.model.getParameters(self.data).selectByAttrib("Constant", ROOT.kFALSE).getSize()
        ndf = self.var.numBins() - nfloat
        chi = ROOT.RooChi2Var("chi","chi", self.model, data_hist, RF.Extended(is_extended), RF.DataError(ROOT.RooAbsData.Auto))
        chi = chi.getVal()
        pvalue = 1 - chi2.cdf(chi, ndf)
        return {f'{self.model.GetName()}_{self.data.GetName()}': [chi, ndf, pvalue]}

    @staticmethod
    def asympt_signif(w):
        """Function to calculate one-sided significance for a given in the workspace s+b model using RooStats.AsymptoticCalculator

        :param: w: workspace to open
        :returns: GetHypoTest() object for printing with Print()
        """
        data, model_sb, model_b = DataExplorer.extract(w)
        ac = ROOT.RooStats.AsymptoticCalculator(data, model_sb, model_b)
        ac.SetOneSidedDiscovery(True)
        as_result = ac.GetHypoTest()
        return as_result

    @staticmethod
    def toy_signif(w, n_toys = 1000, seed = 333):
        """
        // to be completed //
        """
        data, model_sb, model_b = DataExplorer.extract(w)
        fc = ROOT.RooStats.FrequentistCalculator(data, model_sb, model_b)
        fc.SetToys(n_toys, n_toys/10); # fc.SetNToysInTails(500, 100)
        profll = ROOT.RooStats.ProfileLikelihoodTestStat(model_sb.GetPdf())
        profll.SetOneSidedDiscovery(True)
        toymcs = ROOT.RooStats.ToyMCSampler(fc.GetTestStatSampler())
        toymcs.SetTestStatistic(profll)
        #
        if not model_sb.GetPdf().canBeExtended():
            toymcs.SetNEventsPerToy(1)
            print ('adjusting for non-extended formalism')
        #
        fqResult = fc.GetHypoTest()
        fqResult.Print()
        #
        c = ROOT.TCanvas()
        plot = ROOT.RooStats.HypoTestPlot(fqResult)
        plot.SetLogYaxis(True)
        plot.Draw()
        c.Draw()
        c.SaveAs(f'./toy_signif_{model_sb.GetPdf().GetName()}.pdf')
        return

    def toy_tstat(self, n_toys = 1000, seed = 333, save=False):
        ROOT.RooRandom.randomGenerator().SetSeed(seed)
        t_list = []
        #
        self.poi.setVal(0); self.poi.setConstant(1);
        self.chi2_fit() ### assuming the data to be RooDataHist()
        data_TH1 = self.data.createHistogram(self.var.GetName())
        max_error = max([data_TH1.GetBinError(i) for i in range(1, data_TH1.GetNbinsX() + 1)])

        for i_toy in range(n_toys):
            self.poi.setVal(0); self.poi.setConstant(1);
            toy_data = self.model.generate(ROOT.RooArgSet(self.var), self.data.sumEntries())
            toy_roohist = ROOT.RooDataHist('toy_TH1', 'toy_TH1', ROOT.RooArgSet(self.var), toy_data)
            toy_TH1 = toy_roohist.createHistogram(self.var.GetName())
            for i in range(1, toy_TH1.GetNbinsX()+1):
                toy_TH1.SetBinError(i, max_error)
            toy_hist = ROOT.RooDataHist('toy_hist', 'toy_hist', ROOT.RooArgList(self.var), RF.Import(toy_TH1))
            #
            self.chi2_fit(data=toy_hist)
            chi2_null = ROOT.RooChi2Var("chi2_null","chi2_null", self.model, toy_hist, RF.Extended(False), RF.DataError(ROOT.RooAbsData.Auto))
            chi2_null = chi2_null.getVal()
            #
            if save:
                c_null = ROOT.TCanvas("c_null", "c_null", 800, 600);
                frame_null = self.var.frame()
                toy_hist.plotOn(frame_null, RF.DataError(ROOT.RooAbsData.SumW2))
                self.model.plotOn(frame_null)
                frame_null.Draw()
                c_null.SaveAs(f'./tnull_toys/null_{i_toy}.pdf')
            #
            self.poi.setConstant(0);
            self.chi2_fit(data=toy_hist)
            chi2_sb = ROOT.RooChi2Var("chi2_sb","chi2_sb", self.model, toy_hist, RF.Extended(False), RF.DataError(ROOT.RooAbsData.Auto))
            chi2_sb = chi2_sb.getVal()
            t_list.append([chi2_null - chi2_sb, chi2_null, chi2_sb])

        if save:
            c_sb = ROOT.TCanvas("c_sb", "c_sb", 800, 600);
            frame_sb = self.var.frame()
            toy_hist.plotOn(frame_sb, RF.DataError(ROOT.RooAbsData.SumW2))
            self.model.plotOn(frame_sb)
            frame_sb.Draw()
            c_sb.SaveAs(f'./tnull_toys/sb_{i_toy}.pdf')

        df = DataFrame(t_list, columns=['t', 'chi2_null', 'chi2_sb'])
        df.to_pickle('t_.pkl')
        return df

    def plot_ll(self, save=False, save_prefix = ''):
        nll = self.model.createNLL(self.data)
        pll = nll.createProfile(ROOT.RooArgSet(self.poi))
        #
        frame_nll = self.poi.frame(RF.Bins(100), RF.Range(ll_left, ll_right))
        frame_nll.SetTitle('')
        #
        nll.plotOn(frame_nll, RF.ShiftToZero(), RF.LineColor(ROOT.kGreen))
        pll.plotOn(frame_nll, RF.LineColor(ROOT.kRed))
        #
        frame_nll.SetMaximum(25.)
        frame_nll.SetMinimum(0.)
        if save:
            c_ll = ROOT.TCanvas("c_ll", "c_ll", 800, 600); ll_left = 0; ll_right = 200
            frame_nll.Draw()
            #
            line_width = 4
            line_5sigma = ROOT.TLine(ll_left, 12.5, ll_right, 12.5)
            line_5sigma.SetLineWidth(line_width); line_5sigma.SetLineColor(47)
            line_5sigma.Draw();
            #
            c_ll.SaveAs(f'{save_prefix}1_pll.pdf')
        return frame_nll

    def plot_pull(self, save=False, save_path='./fit_validation/', save_prefix = ''):
        frame = self.var.frame()
        self.data.plotOn(frame)
        self.model.plotOn(frame)
        pull_hist = frame.pullHist()
        #
        frame_pull = self.var.frame()
        frame_pull.addPlotable(pull_hist, 'P')
        if save:
            c_pull = ROOT.TCanvas("c_pull", "c_pull", 800, 600)
            frame_pull.Draw()
            c_pull.SaveAs(f'{save_path}{save_prefix}_{self.data.GetName()}.pdf')
        return frame_pull

    def plot_toys_pull(self, var_to_study, N_toys=100, N_gen=1, save=False, save_path='./fit_validation/', save_prefix = ''):
        """Make bias checks in fitted model parameter var_to_study by generating toys with RooMCStudy()
        """
        if not self.is_fitted:
            raise Exception('Model was not fitted to data, fit it first')

        # width_N = 80 if self.mode == 'X' else 250
        # err_upper = 30 if self.mode == 'X' else 400; err_nbins = 30
        # var_lower = var_to_study.getVal() - width_N; var_upper = var_to_study.getVal() + width_N; var_nbins = 50
        #
        MC_manager = ROOT.RooMCStudy(self.model, ROOT.RooArgSet(self.var), RF.Extended(True), RF.FitOptions('mvl'))
        MC_manager.generateAndFit(N_toys, N_gen)
        #
        frame_var = var_to_study.frame() #var_lower, var_upper, var_nbins
        MC_manager.plotParamOn(frame_var)
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
            c_var. SaveAs(f'{save_path}{save_prefix}_{self.var.GetName()}.pdf')
            c_err. SaveAs(f'{save_path}{save_prefix}_{self.var.GetName()}err.pdf')
            c_pull.SaveAs(f'{save_path}{save_prefix}_{self.var.GetName()}pull.pdf')
        return MC_manager

################################################################################################################################

print('\n\n         ~~~' + '\n\n')

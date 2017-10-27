from ROOT import *; import glob, numpy as n; from array import array
from variables import *
isMC = 0

#__aa = 0;       __bb =  50 ;
__aa = 0;       __bb =  14000;
# __aa = 0;       __bb =  6000 ; ## 
# __aa = 6000;    __bb =  14000 ; ## 

_fileOUT = ('sim/' if isMC else '') + 'SimpleFile' + ('MC' if isMC else '') + '_Bs_to_Xphi_b715_preselection_test7_NoMultCandRemoval_%i_%i.root'%(__aa, __bb);
 

MyFileNamesMC = glob.glob( MCpath(1) + "*.root")
MyFileNamesDA = glob.glob("/afs/cern.ch/user/r/rchistov/XbFrame/crab_projects_Bfinder_Rtest_b715/crab_Bfinder*/results/*.root")[__aa: __bb] ## 1

MyFileNames = (MyFileNamesMC if isMC else MyFileNamesDA); ch = TChain('mkcands/ntuple');
for fName in  MyFileNames:
    ii = ch.Add(fName);

print 'get ', len(MyFileNames), 'files from', __aa,'to',__bb,';  chain created'

fileOUT  = TFile (_fileOUT, "recreate");    mytree = TTree("mytree","mytree");

nEvt = ch.GetEntries(); print "entries: from", 0, 'to', nEvt-1; 
H_cuts = TH1F("H_cuts", "H_cuts", 40, 0, 20)

###  declaration and connecting to the branches of my new variables {{{1
NOUT, NOUT_evt, BBB, ibs = [int(0) for i in range(4)];
PV, PVE, JPV, JPVE, JPP3, BUV_Cjp, BUP3_Cjp, BUVE_Cjp, _TV3zero = [TVector3() for i in range(9)]
BUP4_Cjp, MU1P4, MU2P4, MU1P4_Cjp, MU2P4_Cjp, K1P4, K1P4_Cjp, PI1reflP4_Cjp, K1reflP4_Cjp, PI1P4, PI2P4, PI3P4, XP4, PIPIP4, PI1P4_Cjp, PI2P4_Cjp, PI3P4_Cjp, XP4_Cjp, PIPIP4_Cjp, KPIPIP4, KPIPIP4_Cjp = [TLorentzVector() for i in range(21)];
_TV3zero  = TVector3(0,0,0)

_MY_VARS_ = [
"K1_pt", "K1_ips", "K2_pt", "PI1_pt", "PI2_pt", ##"K1_trchi2ndf", "K1_pixhit", "K1_hit", 
"X_mass", "X_mass_Cjp", "PIPI_mass_Cjp",
"PHI_mass_Cjp", "PHIPIPIP4_mass_Cjp",
"BU_mass_Cjp", "BU_reflmass1_Cjp", "BU_reflmass2_Cjp",
"BU_pt_Cjp", "BU_pvdistsignif2_Cjp", "BU_pvdistsignif3_Cjp",
"BU_pvcos2_Cjp", "BU_vtxprob_Cjp",
# "BU_p_Cjp", "BU_pvdist_Cjp", 
# "BU_properLT_Cjp", "BU_properLTxy_Cjp",
# "BU_chi2ndf_Cjp", "BU_pvcossignif3_Cjp",
"JPSI_mass_Cmumu",
# "JPSI_masc_Cmumu", "JPSI_vtxprob_Cmumu", "JPSI_pvcos2_Cmumu", "JPSI_pvdistsignif2_Cmumu", 
"SAMEEVENT"]
_MC_VARS = ["MC_mu", "MC_k1"];
if isMC: _MY_VARS_ += _MC_VARS

for _var_ in _MY_VARS_:
    exec(_var_ + ' = n.zeros(1, dtype=float)')

for _var_ in _MY_VARS_:
    #print 'executing ' + 'mytree.Branch("' + _var_ + '"' + ' '*(25-len(_var_)) + ',' + _var_ + ' '*(25-len(_var_)) + ', "'+ _var_ + '/D")'
    exec('mytree.Branch("' + _var_ + '"' + ' '*(25-len(_var_)) + ',' + _var_ + ' '*(25-len(_var_)) + ', "'+ _var_ + '/D")')

###  declaration and connecting to the branches of my new variables }}}1

for evt in range(0, nEvt):
    ##
    if (ch.GetEntry(evt) <= 0) : break;
    BInfo_size  = ch.nB
    if len(ch.B_kaon_px1) != BInfo_size :continue
    
    for Bj in range(BInfo_size):
        ##
        ibs = Bj
        #
        K1P4        .SetXYZM(ch.B_kaon_px1[ibs], ch.B_kaon_py1[ibs], ch.B_kaon_pz1[ibs], PDG_KAON_MASS)
        K1P4_Cjp    .SetXYZM(ch.B_kaon_px1_cjp[ibs], ch.B_kaon_py1_cjp[ibs], ch.B_kaon_pz1_cjp[ibs], PDG_KAON_MASS)
        K1reflP4_Cjp    .SetXYZM(ch.B_kaon_px1_cjp[ibs], ch.B_kaon_py1_cjp[ibs], ch.B_kaon_pz1_cjp[ibs], PDG_PION_MASS)
        #
        K1_pt[0]        = K1P4.Pt() 
######################
        if K1_pt[0]  < 0.7 :continue
        #
        if ch.mumAngT[ibs]==0 or ch.mupAngT[ibs]==0 : ## soft muon
            H_cuts.Fill(1)
            continue
        #
        if ch.mumNPHits[ibs] < 1.0 or ch.mumNHits[ibs] < 6.0 or ch.mumdz[ibs] > 20. or ch.mumdxy[ibs] > 0.3:
            H_cuts.Fill(2)
            continue
        #
        if ch.mupNPHits[ibs] < 1.0 or ch.mupNHits[ibs] < 6.0 or ch.mupdz[ibs] > 20. or ch.mupdxy[ibs] > 0.3:
            H_cuts.Fill(3)
            continue
        #
        if (not 'HLT_DoubleMu4_Jpsi_Displaced' in ch.triggersMuPL[ibs]) or (not 'HLT_DoubleMu4_Jpsi_Displaced' in ch.triggersMuML[ibs]) :continue
        #
        # K1_eta[0]       = K1P4.Eta()
        # K1_ip[0]        = ch.kaon1_dxy[ibs]
        K1_ips[0]       = abs( ch.kaon1_dxy[ibs] / (0.00001 + ch.kaon1_dxyE[ibs]) )
        if ch.kaon1_trackchi2[ibs] > 2.5 or ch.kaon1_PHits[ibs] < 1.0 or ch.kaon1_Hits[ibs] < 6.0 :
            H_cuts.Fill(4)
            continue
	PI1P4       .SetXYZM  (ch.B_pi1_px1[ibs], ch.B_pi1_py1[ibs], ch.B_pi1_pz1[ibs], PDG_KAON_MASS)
	PI2P4       .SetXYZM  (ch.B_pi2_px1[ibs], ch.B_pi2_py1[ibs], ch.B_pi2_pz1[ibs], PDG_PION_MASS)
	PI3P4       .SetXYZM  (ch.B_pi3_px1[ibs], ch.B_pi3_py1[ibs], ch.B_pi3_pz1[ibs], PDG_PION_MASS)
	PI1reflP4_Cjp   .SetXYZM  (ch.B_pi1_px1_cjp[ibs], ch.B_pi1_py1_cjp[ibs], ch.B_pi1_pz1_cjp[ibs], PDG_PION_MASS)
	PI1P4_Cjp   .SetXYZM  (ch.B_pi1_px1_cjp[ibs], ch.B_pi1_py1_cjp[ibs], ch.B_pi1_pz1_cjp[ibs], PDG_KAON_MASS)
	PI2P4_Cjp   .SetXYZM  (ch.B_pi2_px1_cjp[ibs], ch.B_pi2_py1_cjp[ibs], ch.B_pi2_pz1_cjp[ibs], PDG_PION_MASS)
	PI3P4_Cjp   .SetXYZM  (ch.B_pi3_px1_cjp[ibs], ch.B_pi3_py1_cjp[ibs], ch.B_pi3_pz1_cjp[ibs], PDG_PION_MASS)

        K2_pt[0]        = PI1P4.Pt() 
        PI1_pt[0]        = PI2P4.Pt() 
        PI2_pt[0]        = PI3P4.Pt() 

#        if(K1_pt[0] < PI1_pt[0]) :continue
#        if(K1_pt[0] < PI2_pt[0]) :continue
#        if(K2_pt[0] < PI1_pt[0]) :continue
#        if(K2_pt[0] < PI2_pt[0]) :continue



	PIPIP4_Cjp  = PI3P4_Cjp+PI2P4_Cjp
	PIPI_mass_Cjp[0] = PIPIP4_Cjp.M() 

	PHIP4_Cjp = PI1P4_Cjp+K1P4_Cjp
	PHI_mass_Cjp[0] = PHIP4_Cjp.M()

        PHIPIPIP4_Cjp = PIPIP4_Cjp + PHIP4_Cjp
        PHIPIPIP4_mass_Cjp[0] = PHIPIPIP4_Cjp.M()

#        if PHI_mass_Cjp[0] > 1.035 :continue
#        if PHI_mass_Cjp[0] < 1.005 :continue

#        if PIPI_mass_Cjp[0]   <   0.4    :continue
#        if PIPI_mass_Cjp[0]   >   0.78    :continue
##            H_cuts.Fill(16)
##	    continue
        BUP4_Cjp    .SetXYZM  ( ch.B_px[ibs], ch.B_py[ibs], ch.B_pz[ibs], ch.B_mass[ibs])
        #
        BUV_Cjp     = TVector3(ch.B_DecayVtxX[ibs],  ch.B_DecayVtxY[ibs],  ch.B_DecayVtxZ[ibs]   )
        BUVE_Cjp    = TVector3( sqrt(ch.B_DecayVtxXE[ibs]), sqrt(ch.B_DecayVtxYE[ibs]), sqrt(ch.B_DecayVtxZE[ibs])  )
        BUP3_Cjp    = BUP4_Cjp.Vect()
        #
        PV          = TVector3( ch.PV_bestBang_RF_X[ibs],   ch.PV_bestBang_RF_Y[ibs],   ch.PV_bestBang_RF_Z[ibs]    )
        PVE         = TVector3( sqrt(ch.PV_bestBang_RF_XE[ibs]),  sqrt(ch.PV_bestBang_RF_YE[ibs]),  sqrt(ch.PV_bestBang_RF_ZE[ibs])  )
        #
        BU_mass_Cjp[0]          = ch.B_mass[ibs]

        if BU_mass_Cjp[0]   >   5.6    :continue
#        if BU_mass_Cjp[0]   <   5.35    :continue

#        if BU_mass_Cjp[0]   >   4.6    :continue
#        if BU_mass_Cjp[0]   <   4.4    :continue
#        if BU_mass_Cjp[0]   <   bmin    :continue
#        if BU_mass_Cjp[0]   >   bmax    :continue
#        BU_mass_C0[0]           = ch.B_mass_c0[ibs]
#        BU_mass_0C[0]           = ch.B_mass_0c[ibs]
        #
        BU_pt_Cjp[0]            = BUP4_Cjp.Pt()
        if BU_pt_Cjp[0] <   15.0    :continue
        # BU_p_Cjp[0]             = BUP4_Cjp.Vect().Mag()
        BU_pvdistsignif2_Cjp[0] = DetachSignificance2( BUV_Cjp - PV, PVE, BUVE_Cjp)
        if BU_pvdistsignif2_Cjp[0] < 5. :continue
	BU_pvdistsignif3_Cjp[0] = DetachSignificance3( BUV_Cjp - PV, PVE, BUVE_Cjp)
        # BU_pvdist_Cjp[0]        = (BUV_Cjp-PV).Mag()
        BU_pvcos2_Cjp[0]        = DirectionCos2 ( BUV_Cjp - PV, BUP3_Cjp ) 
        if BU_pvcos2_Cjp[0] < 0.999 :continue
#            H_cuts.Fill(9)
#            continue
        #
        BU_vtxprob_Cjp[0]       = ch.B_Prob[ibs]
        if BU_vtxprob_Cjp[0] < 0.10 :
#            H_cuts.Fill(10)
            continue
        #
        MU1P4   .SetXYZM(ch.B_mu_px1[ibs], ch.B_mu_py1[ibs], ch.B_mu_pz1[ibs], PDG_MUON_MASS)
        MU2P4   .SetXYZM(ch.B_mu_px2[ibs], ch.B_mu_py2[ibs], ch.B_mu_pz2[ibs], PDG_MUON_MASS)
        MU1P4_Cjp   .SetXYZM(ch.B_mu_px1_cjp[ibs], ch.B_mu_py1_cjp[ibs], ch.B_mu_pz1_cjp[ibs], PDG_MUON_MASS)
        MU2P4_Cjp   .SetXYZM(ch.B_mu_px2_cjp[ibs], ch.B_mu_py2_cjp[ibs], ch.B_mu_pz2_cjp[ibs], PDG_MUON_MASS)
        JPV     = TVector3( ch.B_J_DecayVtxX[ibs],  ch.B_J_DecayVtxY[ibs],  ch.B_J_DecayVtxZ[ibs]   )
        JPVE    = TVector3( sqrt(ch.B_J_DecayVtxXE[ibs]), sqrt(ch.B_J_DecayVtxYE[ibs]), sqrt(ch.B_J_DecayVtxZE[ibs])  )
        JPP3    = TVector3( ch.B_J_px[ibs],         ch.B_J_py[ibs],         ch.B_J_pz[ibs])

#	BU_reflmass_Cjp     = MU1P4_Cjp + MU2P4_Cjp + K1reflP4_Cjp + PI1P4_Cjp + PI3P4_Cjp + PI2P4_Cjp
        BU_reflmass1_Cjp[0] = (MU1P4_Cjp + MU2P4_Cjp + K1reflP4_Cjp + PI1P4_Cjp + PI3P4_Cjp + PI2P4_Cjp).M()
        BU_reflmass2_Cjp[0] = (MU1P4_Cjp + MU2P4_Cjp + K1P4_Cjp + PI1reflP4_Cjp + PI3P4_Cjp + PI2P4_Cjp).M()
	XP4_Cjp     = MU1P4_Cjp + MU2P4_Cjp + PI3P4_Cjp + PI2P4_Cjp
	X_mass_Cjp[0]  		= XP4_Cjp.M()
#        if X_mass_Cjp[0] > 3.7    :continue 
#        if X_mass_Cjp[0] < 3.67   :continue    
	X_mass[0]  		= XP4.M()

        if MU1P4.Pt() < 4.0 or MU2P4.Pt() < 4.0:
            H_cuts.Fill(11)
            continue
        #
        if sqrt (ch.B_J_px[ibs]**2 + ch.B_J_py[ibs]**2) < 7.0:
            H_cuts.Fill(12)
            continue
        #
        if ch.B_J_Prob[ibs] < 0.1:
            H_cuts.Fill(13)
            continue
        #
        JPSI_mass_Cmumu[0]          = ch.B_J_mass[ibs]
        if JPSI_mass_Cmumu[0]   <   3.04    :continue
        if JPSI_mass_Cmumu[0]   >   3.15    :continue
        # JPSI_vtxprob_Cmumu[0]       = ch.B_J_Prob[ibs]
        # JPSI_masc_Cmumu[0]          = (MU2P4 + MU1P4).M()
        JPSI_pvcos2_Cmumu_va        = DirectionCos2 ( JPV - PV, JPP3 )
        JPSI_pvdistsignif2_Cmumu_va = DetachSignificance2( JPV - PV, PVE, JPVE)
        if JPSI_pvcos2_Cmumu_va < 0.9:
            H_cuts.Fill(14)
            continue
        #
        if JPSI_pvdistsignif2_Cmumu_va < 3.0:
            H_cuts.Fill(15)
            continue
        #
        _mctr = 0
        if isMC:
            _mctr   =   1 if abs(ch.MCID_k1[ibs])==321      else 0;
            _mctr   +=  2 if abs(ch.MCID_pk1[ibs])==521     else 0;
            MC_k1[0] =  _mctr
            _mctr   =   1 if (abs(ch.MCID_mu1[ibs])==13     and abs(ch.MCID_mu2[ibs])==13)      else 0;
            _mctr   +=  2 if (abs(ch.MCID_pmu1[ibs])==443   and abs(ch.MCID_pmu2[ibs])==443)    else 0;
            _mctr   +=  4 if (abs(ch.MCID_ppmu1[ibs])==521  and abs(ch.MCID_ppmu2[ibs])==521)   else 0;
            MC_mu[0] = _mctr
        #
        SAMEEVENT[0] = 0;
        if (BBB > -1) : 
            SAMEEVENT[0] = 1
            NOUT_evt -= 1;
        #
        mytree.Fill(); NOUT += 1; NOUT_evt +=1; BBB = Bj; 
   
    BBB = -1
    if (evt % 2000 == 0) :    ## printout progress
        _perc = str(TMath.Nint(100*(evt+1)/(nEvt+0.0)));
        print "["+_perc+(' ' * (3 - len(_perc)))+"%];evt",evt,' '*(6-len(str(evt))),";saved ["+str(__aa)+":"+str(__bb)+"]", NOUT, ' ', NOUT_evt

fileOUT.Write();
print NOUT, ' ', NOUT_evt


#cc = TCanvas('cc', 'cc', 800, 600)
#mytree.Draw('BU_mass_Cjp', 'K1_pt > 0.8 && BU_pvcos2_Cjp > 0.98 && BU_pvdistsignif2_Cjp > 5')
#cc.SaveAs('pica.gif')

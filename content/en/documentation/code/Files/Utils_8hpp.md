---
title: "file ColliderBit/Utils.hpp"

description: "[No description available]"

---

# file ColliderBit/Utils.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::ColliderBit](/documentation/code/namespaces/namespacegambit_1_1colliderbit/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::ColliderBit::jet_collection_settings](/documentation/code/classes/structgambit_1_1colliderbit_1_1jet__collection__settings/)** <br>Struct of different jet collection settings.  |

## Detailed Description


**Author**: 

  * Andy Buckley ([andy.buckley@glasgow.ac.uk](mailto:andy.buckley@glasgow.ac.uk)) 
  * Abram Krislock ([a.m.b.krislock@fys.uio.no](mailto:a.m.b.krislock@fys.uio.no)) 
  * Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 
  * Pat Scott ([pat.scott@uq.edu.au](mailto:pat.scott@uq.edu.au)) 
  * Tomas Gonzalo ([gonzalo@physk.rwth-aachen.de](mailto:gonzalo@physk.rwth-aachen.de)) 


**Date**: 

  * 2019 Oct
  * 2016 Mar
  * 2020 Jun
  * 2020 Jan
  * 2021 Jul


Util variables and functions for ColliderBit



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
///  \file
///
///  Util variables and functions for ColliderBit
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Andy Buckley
///          (andy.buckley@glasgow.ac.uk)
///  \date 2019 Oct
///
///  \author Abram Krislock
///          (a.m.b.krislock@fys.uio.no)
///  \date 2016 Mar
///
///  \author Anders Kvellestad
///          (anders.kvellestad@fys.uio.no)
///  \date 2020 Jun
///
///  \author Pat Scott
///          (pat.scott@uq.edu.au)
///  \date 2020 Jan
///
///  \author Tomas Gonzalo
///          (gonzalo@physk.rwth-aachen.de)
///  \date 2021 Jul
///
///  *********************************************

#pragma once

#include <functional>
#include <memory>
#include <cfloat>

#include "HEPUtils/MathUtils.h"
#include "HEPUtils/BinnedFn.h"
#include "HEPUtils/Event.h"
#include "HEPUtils/FastJet.h"

#include "gambit/ColliderBit/mt2_bisect.h"

namespace Gambit
{

  namespace ColliderBit
  {

    /// Unit conversions (multiply to construct in standard units, divide to decode to that unit)
    static const double GeV = 1, MeV = 1e-3, TeV = 1e3;

    /// Struct of different jet collection settings
    struct jet_collection_settings
    {
      std::string key;
      std::string algorithm;
      double R;
      std::string recombination_scheme;
      std::string strategy;
    };

    /// Storage of different FastJet methods
    FJNS::JetAlgorithm FJalgorithm_map(std::string);
    FJNS::Strategy FJstrategy_map(std::string);
    FJNS::RecombinationScheme FJRecomScheme_map(std::string);

    /// Use the HEPUtils Event without needing namespace qualification
    using HEPUtils::Event;
    /// Use the HEPUtils Particle without needing namespace qualification
    using HEPUtils::Particle;
    /// Use the HEPUtils Jet without needing namespace qualification
    using HEPUtils::Jet;
    /// Use the HEPUtils P4 four-vector without needing namespace qualification
    using HEPUtils::P4;

    /// Use the HEPUtils add_quad function without needing namespace qualification
    using HEPUtils::add_quad;

    /// Typedef for a vector of Particle pointers
    typedef std::vector<const HEPUtils::Particle*> ParticlePtrs;

    /// Typedef for a vector of Jet pointers
    typedef std::vector<const HEPUtils::Jet*> JetPtrs;

    /// @name Particle IDs
    //@{

    /// Identifier for jets true
    inline bool amIaJet(const HEPUtils::Jet *jet) { (void)jet; return true; }

    /// Indentifier for b-jets true
    inline bool amIaBJet(const HEPUtils::Jet *jet) { return jet->btag(); }

    /// Identifier for jets false
    inline bool amIaJet(const HEPUtils::Particle *part) { (void)part; return false; }

    /// Identifier for b-jets true
    inline bool amIaBJet(const HEPUtils::Particle *part) { (void)part; return true; }

    /// Identifier for electrons
    inline bool amIanElectron(const HEPUtils::Particle *part) { return part->abspid() == 11; }

    /// Identifier for muons
    inline bool amIaMuon(const HEPUtils::Particle *part) { return part->abspid() == 13; }

    /// Identifier for taus
    inline bool amIaTau(const HEPUtils::Particle *part) { return part->abspid() == 15; }

    //@}

    /// @name Particle-list filtering by cuts
    //@{

    /// Convenience combination of remove_if and erase
    template <typename CONTAINER, typename RMFN>
    inline void iremoveerase(CONTAINER& c, const RMFN& fn) {
      auto newend = std::remove_if(c.begin(), c.end(), fn);
      c.erase(newend, c.end());
    }

    /// In-place filter a supplied particle vector by rejecting those which fail a supplied cut
    inline void ifilter_reject(ParticlePtrs& particles,
                               std::function<bool(const Particle*)> rejfn, bool do_delete=true) {
      iremoveerase(particles, [&](const Particle* p) {
          const bool rm = rejfn(p);
          if (rm && do_delete) delete p;
          return rm;
        });
    }

    /// In-place filter a supplied particle vector by keeping those which pass a supplied cut
    inline void ifilter_select(ParticlePtrs& particles,
                               std::function<bool(const Particle*)> selfn, bool do_delete=true) {
      ifilter_reject(particles, [&](const Particle* p) { return !selfn(p); }, do_delete);
    }


    /// Filter a supplied particle vector by rejecting those which fail a supplied cut
    /// @todo Optimise by only copying those which are selected (filter_select is canonical)
    inline ParticlePtrs filter_reject(const ParticlePtrs& particles,
                                      std::function<bool(const Particle*)> rejfn, bool do_delete=true) {
      ParticlePtrs rtn = particles;
      ifilter_reject(rtn, rejfn, do_delete);
      return rtn;
    }

    /// Filter a supplied particle vector by keeping those which pass a supplied cut
    inline ParticlePtrs filter_select(const ParticlePtrs& particles,
                                      std::function<bool(const Particle*)> selfn, bool do_delete=true) {
      return filter_reject(particles, [&](const Particle* p) { return !selfn(p); }, do_delete);
    }

    //@}



    /// @name Jet-list filtering by cuts
    //@{

    /// In-place filter a supplied jet vector by rejecting those which fail a supplied cut
    inline void ifilter_reject(JetPtrs& jets,
                               std::function<bool(const Jet*)> rejfn, bool do_delete=true) {
      iremoveerase(jets, [&](const Jet* j) {
          const bool rm = rejfn(j);
          if (rm && do_delete) delete j;
          return rm;
        });
    }

    /// In-place filter a supplied jet vector by keeping those which pass a supplied cut
    inline void ifilter_select(JetPtrs& jets,
                               std::function<bool(const Jet*)> selfn, bool do_delete=true) {
      ifilter_reject(jets, [&](const Jet* j) { return !selfn(j); }, do_delete);
    }


    /// Filter a supplied particle vector by rejecting those which fail a supplied cut
    /// @todo Optimise by only copying those which are selected (filter_select is canonical)
    inline JetPtrs filter_reject(const JetPtrs& jets,
                                 std::function<bool(const Jet*)> rejfn, bool do_delete=true) {
      JetPtrs rtn = jets;
      ifilter_reject(rtn, rejfn, do_delete);
      return rtn;
    }

    /// Filter a supplied particle vector by keeping those which pass a supplied cut
    inline JetPtrs filter_select(const JetPtrs& jets,
                                 std::function<bool(const Jet*)> selfn, bool do_delete=true) {
      return filter_reject(jets, [&](const Jet* j) { return !selfn(j); }, do_delete);
    }

    //@}



    /// @todo Provide random selection functors from const, 1D map, 2D map, and eff functor



    /// @name Random booleans sampled from efficiency maps
    //@{

    /// Return a random true/false at a success rate given by a number
    bool random_bool(double eff);

    /// Return a random true/false at a success rate given by a 1D efficiency map
    inline bool random_bool(const HEPUtils::BinnedFn1D<double>& effmap, double x) {
      return random_bool( effmap.get_at(x) );
    }

    /// Return a random true/false at a success rate given by a 2D efficiency map
    inline bool random_bool(const HEPUtils::BinnedFn2D<double>& effmap, double x, double y) {
      return random_bool( effmap.get_at(x, y) );
    }

    //@}


    /// @name Random filtering by efficiency
    //@{

    /// Utility function for filtering a supplied particle vector by sampling wrt an efficiency scalar
    void filtereff(std::vector<const HEPUtils::Particle*>& particles, double eff, bool do_delete=false);

    /// Utility function for filtering a supplied particle vector by sampling an efficiency returned by a provided function object
    void filtereff(std::vector<const HEPUtils::Particle*>& particles, std::function<double(const HEPUtils::Particle*)> eff_fn, bool do_delete=false);

    /// Utility function for filtering a supplied particle vector by sampling wrt a binned 1D efficiency map in pT
    void filtereff_pt(std::vector<const HEPUtils::Particle*>& particles, const HEPUtils::BinnedFn1D<double>& eff_pt, bool do_delete=false);

    /// Utility function for filtering a supplied particle vector by sampling wrt a binned 2D efficiency map in |eta| and pT
    void filtereff_etapt(std::vector<const HEPUtils::Particle*>& particles, const HEPUtils::BinnedFn2D<double>& eff_etapt, bool do_delete=false);

    //@}


    /// @name Tagging
    //@{

    /// Randomly get a tag result (can be anything) from a 2D |eta|-pT efficiency map
    /// @todo Also need 1D? Sampling in what variable?
    inline bool has_tag(const HEPUtils::BinnedFn2D<double>& effmap, double eta, double pt) {
      try {
        return random_bool(effmap, fabs(eta), pt);
      } catch (...) {
        return false; // No tag if outside lookup range... be careful!
      }
    }

    /// Return a map<Jet*,bool> containing a generated b-tag for every jet in the input vector
    inline std::map<const HEPUtils::Jet*,bool> generateBTagsMap(const std::vector<const HEPUtils::Jet*>& jets, 
                                                                double bTagEff, double cMissTagEff, double otherMissTagEff,
                                                                double pTmin = 0., double absEtaMax = DBL_MAX)
    {
      std::map<const HEPUtils::Jet*,bool> bTagsMap;
      for (const HEPUtils::Jet* j : jets)
      {
        bool genBTag = false;
        if((j->pT() > pTmin) && (j->abseta() < absEtaMax))
        {
          if(j->btag()) 
          { 
            if(random_bool(bTagEff)) { genBTag = true; }
          }
          else if(j->ctag()) 
          { 
            if(random_bool(cMissTagEff)) { genBTag = true; }
          }
          else
          { 
            if(random_bool(otherMissTagEff)) { genBTag = true; }
          }
        }
        bTagsMap[j] = genBTag;
      }
      return bTagsMap;
    }


    template <typename NUM1, typename NUM2>
    inline size_t binIndex(NUM1 val, const std::vector<NUM2>& binedges, bool allow_overflow=false) {
      if (val < binedges.front()) return -1; ///< Below/out of histo range
      if (val >= binedges.back()) return allow_overflow ? int(binedges.size())-1 : -1; ///< Above/out of histo range
      return std::distance(binedges.begin(), --std::upper_bound(binedges.begin(), binedges.end(), val));
    }


    /// Make a vector of central bin values from a vector of bin edge values using linear interpolation
    inline std::vector<double> mk_bin_values(const std::vector<double>& binEdgeValues) {
      std::vector<double> results;
      results.reserve(binEdgeValues.size()-1);
      for (size_t i = 0; i < binEdgeValues.size()-1; ++i)
        results.push_back( (binEdgeValues[i] + binEdgeValues[i+1])/2.0 );
      return results;
    }
    /// Alias
    inline std::vector<double> makeBinValues(const std::vector<double>& binEdgeValues) {
      return mk_bin_values(binEdgeValues);
    }


    /// Run jet clustering from any P4-compatible momentum type
    template <typename MOM>
    inline std::vector<std::shared_ptr<HEPUtils::Jet>> get_jets(const std::vector<MOM*>& moms, double R,
                                                double ptmin=0*GeV, FJNS::JetAlgorithm alg=FJNS::antikt_algorithm) {
      // Make PseudoJets
      std::vector<FJNS::PseudoJet> constituents;
      for (const MOM* p : moms) constituents.push_back(HEPUtils::mk_pseudojet(*p));
      // Run clustering
      std::vector<FJNS::PseudoJet> jets = HEPUtils::get_jets(constituents, R, ptmin, alg);
      // Make newly-allocated Jets
      std::vector<std::shared_ptr<HEPUtils::Jet>> rtn;
      for (const FJNS::PseudoJet& j : jets) rtn.push_back(std::make_shared<HEPUtils::Jet>(HEPUtils::mk_p4(j)));
      return rtn;
    }


    /// Check if there's a physics object above ptmin in an annulus rmin..rmax around the given four-momentum p4
    inline bool object_in_cone(const HEPUtils::Event& e, std::string jetcollection, const HEPUtils::P4& p4, double ptmin, double rmax, double rmin=0.05) {
      for (const HEPUtils::Particle* p : e.visible_particles())
        if (p->pT() > ptmin && HEPUtils::in_range(HEPUtils::deltaR_eta(p4, *p), rmin, rmax)) return true;
      for (const HEPUtils::Jet* j : e.jets(jetcollection))
        if (j->pT() > ptmin && HEPUtils::in_range(HEPUtils::deltaR_eta(p4, *j), rmin, rmax)) return true;
      return false;
    }


    /// Overlap removal -- discard from first list if within deltaRMax of any from the second list
    /// Optional arguments:
    ///  - use_rapidity = use rapidity instead of psedurapidity to compute deltaR. Defaults to False
    ///  - pTmax = only discard from first list with pT < pTmax. Defaults to DBL_MAX
    ///  - btageff = do not discard jets that have a b-tagging efficiency lower than btageff. Defaults to 0
    template<typename MOMPTRS1, typename MOMPTRS2>
    void removeOverlap(MOMPTRS1& momstofilter, const MOMPTRS2& momstocmp, double deltaRMax, bool use_rapidity=false, double pTmax = DBL_MAX, double btageff = 0)
    {
      ifilter_reject(momstofilter, [&](const typename MOMPTRS1::value_type& mom1)
      {
        for (const typename MOMPTRS2::value_type& mom2 : momstocmp) {
          const double dR = (use_rapidity) ? deltaR_rap(mom1->mom(), mom2->mom()) : deltaR_eta(mom1->mom(), mom2->mom());
          if (dR < deltaRMax && mom1->pT() < pTmax && ( !amIaBJet(mom1) || !random_bool(btageff) ) ) return true;
        }
        return false;
      }, false);
    }

    /// Overlap removal -- discard from first list if within deltaRmax of any from the second list.
    /// Overload of previous function where deltaRmax is a function of the pT of the first list
    /// Optional arguments:
    ///  - use_rapidity = use rapidity instead of psedurapidity to compute deltaR. Defaults to False
    ///  - pTmax = only discard from first list with pT < pTmax. Defaults to DBL_MAX
    ///  - btageff = do not discard jets that have a b-tagging efficiency lower than btageff. Defaults to 0
    template<typename MOMPTRS1, typename MOMPTRS2>
    void removeOverlap(MOMPTRS1& momstofilter, const MOMPTRS2& momstocmp, double (*deltaRMax)(const double), bool use_rapidity=false, double pTmax = DBL_MAX, double btageff = 0)
    {
      ifilter_reject(momstofilter, [&](const typename MOMPTRS1::value_type& mom1)
      {
        for (const typename MOMPTRS2::value_type& mom2 : momstocmp) {
          const double dR = (use_rapidity) ? deltaR_rap(mom1->mom(), mom2->mom()) : deltaR_eta(mom1->mom(), mom2->mom());
          if (dR < deltaRMax(mom1->pT()) && mom1->pT() < pTmax && ( !amIaBJet(mom1) || !random_bool(btageff) ) ) return true;
        }
        return false;
      }, false);
    }

    /// Overlap removal for checking against b-jets -- discard from first list if within deltaRMax of a b-jet in the second list
    /// Optional arguments:
    ///  - use_rapidity = use rapidity instead of psedurapidity to compute deltaR. Defaults to False
    ///  - pTmax = only discard from first list with pT < pTmax. Defaults to DBL_MAX
    template<typename MOMPTRS1>
    void removeOverlapIfBjet(MOMPTRS1& momstofilter, std::vector<const HEPUtils::Jet*>& jets, double deltaRMax, bool use_rapidity=false, double pTmax = DBL_MAX)
    {
      ifilter_reject(momstofilter, [&](const typename MOMPTRS1::value_type& mom1)
      {
        for (const HEPUtils::Jet* jet : jets) {
          const double dR = (use_rapidity) ? deltaR_rap(mom1->mom(), jet->mom()) : deltaR_eta(mom1->mom(), jet->mom());
          if (dR < deltaRMax && mom1->pT() < pTmax && jet->btag() ) return true;
        }
        return false;
      }, false);
    }


    /// Non-iterator version of std::all_of
    template <typename CONTAINER, typename FN>
    inline bool all_of(const CONTAINER& c, const FN& f) {
      return std::all_of(std::begin(c), std::end(c), f);
    }

    /// Non-iterator version of std::any_of
    template <typename CONTAINER, typename FN>
    inline bool any_of(const CONTAINER& c, const FN& f) {
      return std::any_of(std::begin(c), std::end(c), f);
    }

    /// Non-iterator version of std::none_of
    template <typename CONTAINER, typename FN>
    inline bool none_of(const CONTAINER& c, const FN& f) {
      return std::none_of(std::begin(c), std::end(c), f);
    }


    /// Utility function for returning a collection of same-flavour, oppsosite-sign particle pairs
    std::vector<std::vector<const HEPUtils::Particle*>> getSFOSpairs(std::vector<const HEPUtils::Particle*> particles);

    /// Utility function for returning a collection of oppsosite-sign particle pairs
    std::vector<std::vector<const HEPUtils::Particle*>> getOSpairs(std::vector<const HEPUtils::Particle*> particles);

    /// Utility function for returning a collection of same-sign particle pairs
    std::vector<std::vector<const HEPUtils::Particle*>> getSSpairs(std::vector<const HEPUtils::Particle*> particles);

    /// Utility function for returning a collection of b-tagged jets
    std::vector<std::vector<const HEPUtils::Jet*>> getBJetPairs(std::vector<const HEPUtils::Jet*> bjets);


    /// @name Sorting
    //@{

    /// Particle-sorting function
    inline void sortBy(ParticlePtrs& particles, std::function<bool(const Particle*, const Particle*)> cmpfn) {
      std::sort(particles.begin(), particles.end(), cmpfn);
    }

    /// Comparison function to give a particles sorting order decreasing by pT
    inline bool cmpParticlesByPt(const HEPUtils::Particle* lep1, const HEPUtils::Particle* lep2) { return lep1->pT() > lep2->pT(); }

    // Sort a particles list by decreasing pT
    inline void sortByPt(ParticlePtrs& particles) { sortBy(particles, cmpParticlesByPt); }


    /// Jet-sorting function
    inline void sortBy(JetPtrs& jets, std::function<bool(const Jet*, const Jet*)> cmpfn) {
      std::sort(jets.begin(), jets.end(), cmpfn);
    }

    /// Comparison function to give a jets sorting order decreasing by pT
    inline bool cmpJetsByPt(const HEPUtils::Jet* jet1, const HEPUtils::Jet* jet2) { return jet1->pT() > jet2->pT(); }

    // Sort a jets list by decreasing pT
    inline void sortByPt(JetPtrs& jets) { sortBy(jets, cmpJetsByPt); }

    // Sort a list of pairs by how close their invariant mass is to their parent mass
    inline void sortByParentMass(std::vector<std::vector<const Particle *> > &pairs, double mP)
    {
      auto compfn = [&](std::vector<const Particle *> pair1, std::vector<const Particle *> pair2)
      {
        return std::abs((pair1.at(0)->mom() + pair1.at(1)->mom()).m() - mP) < std::abs((pair2.at(0)->mom() + pair2.at(1)->mom()).m() - mP);
      };
      std::sort(pairs.begin(), pairs.end(), compfn);
    }

    //@}

    /// Remove pairs with already used leptons, assumes some order
    //@{
    inline void uniquePairs(std::vector<std::vector<const Particle *> > &pairs)
    {
      for(auto it = pairs.begin(); it != pairs.end(); ++it)
      {
        for(auto it2 = std::next(it); it2 != pairs.end(); ++it2)
        {
          if(it2->at(0) == it->at(0) or
             it2->at(1) == it->at(0) or
             it2->at(0) == it->at(1) or
             it2->at(1) == it->at(1))
          {
            it2--;
            pairs.erase(it2+1);
          }
        }
      }
    }
    //@}

    /// @name Counting
    //@{

    /// Count number of particles that have pT > pTlim
    inline int countPt(const std::vector<const Particle*>& particles, double pTlim)
    {
        int sum = 0;
        for (const Particle* p : particles)
        {
          if (p->pT() > pTlim) { sum++; }
        }
        return sum;
    }

    /// Count number of jets that have pT > pTlim
    inline int countPt(const std::vector<const Jet*>& jets, double pTlim)
    {
        int sum = 0;
        for (const Jet* j : jets)
        {
          if (j->pT() > pTlim) { sum++; }
        }
        return sum;
    }
    
    //@}


    /// @name Summing pT
    //@{

    /// Scalar sum pT of particles with pT > pTlim (default pTlim = 0)
    inline double scalarSumPt(const std::vector<const Particle*>& particles, double pTlim=0.)
    {
        double sum = 0.;
        for (const Particle* p : particles)
        { 
          if (p->pT() > pTlim) { sum += p->pT(); } 
        }
        return sum;
    }

    /// Scalar sum pT of jets
    inline double scalarSumPt(const std::vector<const Jet*>& jets, double pTlim=0.)
    {
        double sum = 0.;
        for (const Jet* j : jets)
        { 
          if (j->pT() > pTlim) { sum += j->pT(); } 
        }
        return sum;
    }
    
    //@}

    /// @name Transverse masses
    //@{

    /// Faster way to compute stransverse mass
    inline double get_mT2(const Particle *part1, const Particle *part2, P4 pTmiss, double mass)
    {

      double p1[3] = {part1->mass(), part1->mom().px(), part1->mom().py()};
      double p2[3] = {part2->mass(), part2->mom().px(), part2->mom().py()};
      double pMiss[3] = {0., pTmiss.px(), pTmiss.py() };
      double mn = mass;

      mt2_bisect::mt2 mt2_calc;
      mt2_calc.set_momenta(p1,p2,pMiss);
      mt2_calc.set_mn(mn);

      return  mt2_calc.get_mt2();

    }

    /// Faster way to compute stransverse mass, from the momenta
    inline double get_mT2(P4 mom1, P4 mom2, P4 pTmiss, double mass)
    {

      double p1[3] = {mom1.m(), mom1.px(), mom1.py()};
      double p2[3] = {mom2.m(), mom2.px(), mom2.py()};
      double pMiss[3] = {0., pTmiss.px(), pTmiss.py() };
      double mn = mass;

      mt2_bisect::mt2 mt2_calc;
      mt2_calc.set_momenta(p1,p2,pMiss);
      mt2_calc.set_mn(mn);

      return  mt2_calc.get_mt2();

    }

    // Transverse mass of a single particle system
    inline double get_mT(const Particle *part, P4 pTmiss)
    {
      return sqrt( 2 * pTmiss.pT() * part->pT()*(1 - cos(part->phi() - pTmiss.phi())) );
    }

    // Transverse mass of a single particle system, given the 4-momentum
    inline double get_mT(P4 mom, P4 pTmiss)
    {
      return sqrt( 2 * pTmiss.pT() * mom.pT()*(1 - cos(mom.phi() - pTmiss.phi())) );
    }

    // Transverse mass of a two-particle system
    inline double get_mT(const Particle *part1, const Particle *part2, P4 pTmiss)
    {
      P4 p2mom = part1->mom() + part2->mom();
      return get_mT(p2mom, pTmiss);
    }

    // Transverse mass of a three-particle system
    inline double get_mT(const Particle *part1, const Particle *part2, const Particle *part3, P4 pTmiss)
    {
      P4 p3mom = part1->mom() + part2->mom() + part3->mom();
      return get_mT(p3mom, pTmiss);
    }

    //@}

    /// @name Particle sign helper functions
    //@{
    
    /// Have two particles the same sign?
    inline bool sameSign(const Particle *P1, const Particle *P2)
    {
      return P1->pid() * P2->pid() > 0;
    }

    /// Have two particles the opposite sign?
    inline bool oppositeSign(const Particle *P1, const Particle *P2)
    {
      return P1->pid() * P2->pid() < 0;
    }

    //@}
  }

}
```


-------------------------------

Updated on 2025-02-12 at 16:10:35 +0000

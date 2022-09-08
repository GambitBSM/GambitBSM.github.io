---
title: "file Models/models.hpp"

description: "[No description available]"

---

# file Models/models.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Models](/documentation/code/namespaces/namespacegambit_1_1models/)** <br>Forward declaration of [Models::ModelFunctorClaw]() class for use in constructors.  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/)**  |

## Detailed Description


Model helper declarations.

Duties: Activate primary_model_functors according to the model(s) being scanned.



------------------


# Authors

(add name and date if you modify)

Ben Farmer ([benjamin.farmer@monash.edu.au](mailto:benjamin.farmer@monash.edu.au)) 

2013 July 17

Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 

2013 Aug 

2014 Mar



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Model helper declarations.
///  
///  Duties:
///    Activate primary_model_functors according 
///    to the model(s) being scanned.
///
///  *********************************************
///
///  Authors
///  =======
///
///  (add name and date if you modify)
///
///  \author Ben Farmer
///          (benjamin.farmer@monash.edu.au)
///  \date 2013 July 17
///
///  \author Pat Scott
///          (patscott@physics.mcgill.ca)
///  \date 2013 Aug
///  \date 2014 Mar
///
///  *********************************************


#ifndef __models_hpp__
#define __models_hpp__

#include <string>
#include <vector>
#include <set>
#include <map>

//#include "gambit/Elements/functors.hpp"
//#include "gambit/Utils/util_types.hpp"
//#include "gambit/Utils/standalone_error_handlers.hpp"

namespace Gambit
{
  class primary_model_functor;

  namespace Models
  {
     
    typedef std::string str;
    typedef std::vector<primary_model_functor*> primodel_vec;
    typedef std::map<str, primary_model_functor *> activemodel_map;

    /// Models object that performs initialisation and checking operations
    /// on a primary_model_functor list.
    class ModelFunctorClaw
    {

      private:

        /// Function pointer type
        typedef bool (*LineageFunction)(const str, const ModelFunctorClaw*);

        /// Internal record of the active models
        std::set<str> activemodels;         

        /// \name Private lineage/ancestry/friends databases
        /// @{
        std::set<str> allmodelnames;
        std::map<str, str> myParentsDB;
        std::map<str, std::vector<str> > myLineageDB;
        std::map<str, std::vector<str> > myDescendantsDB;
        std::map<str, LineageFunction  > myIsDescendantOfDB;
        std::map<str, std::set<str> > myFriendsDB;
        std::map<str, std::set<str> > myBestFriendsDB;
        /// @}

      public:

        /// Constructor
        ModelFunctorClaw(){}
        /// Destructor
        ~ModelFunctorClaw(){}
        
        /// Model activation function
        ///
        /// Returns a vector of primary_model_functors to be activated, according to the model(s) being scanned
        primodel_vec getPrimaryModelFunctorsToActivate (std::set<str>, const primodel_vec&);
       
        /// Searches primary model functor list for specified model
        primary_model_functor* getPrimaryModelFunctor(const std::string modelname, const primodel_vec&) const;
  
        /// Active model functor "usefulness" checker
        ///
        /// Checks that all the active primary model functors are actually used 
        /// for something in the dependency tree. If not throws an error to warn
        /// the user.
        void checkPrimaryModelFunctorUsage(const activemodel_map&) const;
        
        /// Add a new model to the model database.
        void declare_model (const str&, const str&);

        /// Add a friend, and all its friends and ancestors, to a model's list of friends
        void add_friend (const str &model, const str &newfriend);

        /// Indicate whether a model is recognised by GAMBIT or not
        bool model_exists (const str &) const; 

        /// List all the models recognised by GAMBIT
        str list_models() const;

        /// Verify that a string matches a model recognised by GAMBIT, crash otherwise
        void verify_model(const str&) const;

        /// Return set of all models recognised by GAMBIT
        const std::set<str>& get_allmodels() const;

        /// Return the set of active models;
        std::set<str> get_activemodels() const;

        /// Retrieve the lineage for a given model
        std::vector<str> get_lineage (const str &) const;

        /// Retrieve the friends for a given model
        std::set<str> get_friends (const str &model) const;

        /// Retrieve the best friends for a given model
        std::set<str> get_best_friends (const str &model) const;

        /// Retrieve the descendants for a given model
        std::vector<str> get_descendants (const str &) const;
        
        /// Retrieve the parent model for a given model
        str get_parent (const str&) const;

        /// Check if model 1 is descended from model 2
        bool descended_from (const str &, const str &) const;

        /// Check if model 1 is an ancestor of model 2
        bool ancestor_of (const str &, const str &) const;

        /// Check if model 1 exists somewhere downstream of (and can be therefore be interpreted as a) model 2
        bool downstream_of (const str&, const str&) const;

        /// Check if model 1 exists somewhere upstream of model 2, allowing model 2 to be interpreted as model 1
        bool upstream_of (const str&, const str&) const;

    };
 
  }

}

#endif
```


-------------------------------

Updated on 2022-09-08 at 02:23:03 +0000

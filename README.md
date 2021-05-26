# MC-miniAODext-processor_UL
Code to process Monte Carlo simulation (UL Run 2)


# 1. Installation

Run the following set of commands to install the repo
```
scram p CMSSW CMSSW_10_6_20
cd CMSSW_10_6_20/src
eval `scram runtime -sh`
cmsenv


git clone https://github.com/longlivedpeople/MC-miniAODext-processor_UL.git
```



# 2. Details about the era processing


## 2.1 2016 (pre-VFP)




## 2.2 2016 (post-VFP)

Run from 2016-postVFP dir:
```
cd Run2016-postVFP
```

To launch each background production, you must set your storage site in the crab cfg crab_backgroun*.py e.g. /store/user/fernance.

To submit each background, just type:
```
voms-proxy-init --voms cms
cmsenv
crab submit crab_*.py 
```

Further details, the configuration of these config files was set to:
```
--python_filename MC-RunIISummer20UL16MiniAODextended_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:RunIISummer20UL16MiniAODextended.root --conditions 106X_mcRun2_asymptotic_v13 --step PAT --geometry DB:Extended --filein file:input.root --era Run2_2016 --runUnscheduled --no_exec --mc -n 10
```

## 2.3 2018

Run from Run2018 dir:
```
cd Run2018
```

To launch each background production, you must set your storage site in the crab cfg crab_backgroun*.py e.g. /store/user/fernance.

To submit each background, just type:
```
voms-proxy-init --voms cms
cmsenv
crab submit crab_*.py
```






import CRABClient
from CRABClient.UserUtilities import config

config = config()

# All output/log files go in directory workArea/requestName/
#config.General.workArea = 'crab_projects'

config.General.requestName = 'crab_TTTo2L2Nu'

config.General.transferOutputs = True
config.General.transferLogs = True
config.General.instance = 'prod'

# Set pluginName = Analysis if you are reading a dataset, or to PrivateMC if not (so you are generating events)
config.JobType.pluginName = 'Analysis'
# CMSSW cfg file you wish to run
config.JobType.psetName = 'MC-RunIISummer20UL18MiniAODv2ext_cfg.py'
# Increase virtual memory limit (sum needed by all threads) from default of 2000 MB.
config.JobType.maxMemoryMB = 2500
# Number of threads to use.
#config.JobType.numCores = 2
# To allow use of SL7 CMSSW versions that were SL6 at time of original DATA/MC production.
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2/AODSIM'
config.Data.inputDBS = 'global'


# Units of "totalUnits" and "unitsPerJob" (e.g. files, events, lumi sections)
config.Data.splitting = 'FileBased'
# Total number of these units to be processed.
#config.Data.totalUnits = NTOTAL
# Requested number in each subjob.
config.Data.unitsPerJob = 20
config.Data.outLFNDirBase = ## write user storage e.g. '/store/user/fernance/'
config.Data.publication = True

config.Data.outputDatasetTag = 'extended_RunIISummer20UL18MiniAOD'

config.Site.storageSite = 'T2_ES_IFCA'


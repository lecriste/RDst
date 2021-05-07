# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/RDst-InclusiveHbToDstMu-no-acceptance-fragment.py --fileout file:RDst-InclusiveHbToDstMu-no-acceptance.root --mc --eventcontent RAWSIM --datatier GEN --conditions 106X_upgrade2018_realistic_v11_L1v1 --beamspot Realistic25ns13TeVEarly2018Collision --step GEN --geometry DB:Extended --era Run2_2018 --python_filename RDst-InclusiveHbToDstMu-no-acceptance_cfg.py --no_exec cmsDriver.py Configuration/GenProduction/python/RDst-InclusiveHbToDstMu-no-acceptance-fragment-pythia.py --fileout file:RDst-InclusiveHbToDstMu-no-acceptance-pythia.root --mc --eventcontent RAWSIM --datatier GEN --conditions 106X_upgrade2018_realistic_v11_L1v1 --beamspot Realistic25ns13TeVEarly2018Collision --step GEN --geometry DB:Extended --era Run2_2018 --python_filename RDst-InclusiveHbToDstMu-no-acceptance-pythia_cfg.py --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('GEN',Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2018Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500000)
)
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/RDst-InclusiveHbToDstMu-no-acceptance-fragment.py nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:RDst-InclusiveHbToDstMu-no-acceptance-pythia.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v11_L1v1', '')

process.DstFromBhadronFilter = cms.EDFilter("PythiaFilterMultiAncestor",
    DaughterIDs = cms.untracked.vint32(421, 211),
    DaughterMaxEtas = cms.untracked.vdouble(1000000000.0, 1000000000.0),
    DaughterMaxPts = cms.untracked.vdouble(1000000000.0, 1000000000.0),
    DaughterMinEtas = cms.untracked.vdouble(-1000000000.0, -1000000000.0),
    DaughterMinPts = cms.untracked.vdouble(-1.0, -1.0),
    MaxEta = cms.untracked.double(99.0),
    MinEta = cms.untracked.double(-99.0),
    MinPt = cms.untracked.double(-1.0),
    MotherIDs = cms.untracked.vint32(5),
    ParticleID = cms.untracked.int32(413)
)


process.DstMuMaxMassFilter = cms.EDFilter("MCParticlePairFilter",
    MaxEta = cms.untracked.vdouble(1000000000.0, 1000000000.0),
    MaxInvMass = cms.untracked.double(8.0),
    MinEta = cms.untracked.vdouble(-1000000000.0, -1000000000.0),
    MinPt = cms.untracked.vdouble(-1.0, -1.0),
    ParticleCharge = cms.untracked.int32(0),
    ParticleID1 = cms.untracked.vint32(413),
    ParticleID2 = cms.untracked.vint32(13),
    Status = cms.untracked.vint32(2, 1)
)


process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            convertPythiaCodes = cms.untracked.bool(False),
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            list_forced_decays = cms.vstring(
                'MyD*+', 
                'MyD*-'
            ),
            operates_on_particles = cms.vint32(),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
            user_decay_embedded = cms.vstring('\nAlias      MyD0        D0\nAlias      Myanti-D0   anti-D0\nAlias      MyD*-       D*-\nAlias      MyD*+       D*+\n\nChargeConj MyD0   Myanti-D0\nChargeConj MyD*-  MyD*+\n\nDecay MyD0\n1.000       K-  pi+           PHSP;\nEnddecay\nCDecay Myanti-D0\n\nDecay MyD*-\n1.000       Myanti-D0 pi-     VSS;\nEnddecay\nCDecay MyD*+\n\nEnd\n')
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings', 
            'pythia8CP5Settings', 
            'processParameters'
        ),
        processParameters = cms.vstring(
            'SoftQCD:nonDiffractive = on', 
            'PTFilter:filter = on', 
            'PTFilter:quarkToFilter = 5', 
            'PTFilter:scaleToFilter = 5.0'
        ),
        pythia8CP5Settings = cms.vstring(
            'Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.03344', 
            'MultipartonInteractions:bProfile=2', 
            'MultipartonInteractions:pT0Ref=1.41', 
            'MultipartonInteractions:coreRadius=0.7634', 
            'MultipartonInteractions:coreFraction=0.63', 
            'ColourReconnection:range=5.176', 
            'SigmaTotal:zeroAXB=off', 
            'SpaceShower:alphaSorder=2', 
            'SpaceShower:alphaSvalue=0.118', 
            'SigmaProcess:alphaSvalue=0.118', 
            'SigmaProcess:alphaSorder=2', 
            'MultipartonInteractions:alphaSvalue=0.118', 
            'MultipartonInteractions:alphaSorder=2', 
            'TimeShower:alphaSorder=2', 
            'TimeShower:alphaSvalue=0.118', 
            'SigmaTotal:mode = 0', 
            'SigmaTotal:sigmaEl = 21.89', 
            'SigmaTotal:sigmaTot = 100.309', 
            'PDF:pSet=LHAPDF6:NNPDF31_nnlo_as_0118'
        ),
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'
        )
    ),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0)
)


process.D0ToKpiFromDstFilter = cms.EDFilter("PythiaFilterMultiAncestor",
    DaughterIDs = cms.untracked.vint32(-321, 211),
    DaughterMaxEtas = cms.untracked.vdouble(1000000000.0, 1000000000.0),
    DaughterMaxPts = cms.untracked.vdouble(1000000000.0, 1000000000.0),
    DaughterMinEtas = cms.untracked.vdouble(-1000000000.0, -1000000000.0),
    DaughterMinPts = cms.untracked.vdouble(-1.0, -1.0),
    MaxEta = cms.untracked.double(99.0),
    MinEta = cms.untracked.double(-99.0),
    MinPt = cms.untracked.double(-1.0),
    MotherIDs = cms.untracked.vint32(413),
    ParticleID = cms.untracked.int32(421)
)


process.ProductionFilterSequence = cms.Sequence(process.generator+process.DstFromBhadronFilter+process.D0ToKpiFromDstFilter+process.DstMuMaxMassFilter)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.ProductionFilterSequence)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

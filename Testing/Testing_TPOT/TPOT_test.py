from tpot import TPOTClassifier
from DataExtraction import DataSetExtraction as DSE
from Testing_TPOT import PipelineSelection as PS

data_names = ['MicroOrganisms']#,'RSCTC']
selection_types = ['regular_selection', 'FS_selection']
algorithm_types = ['regular_algorithms', 'FS_algorithms']

PS.create_experiment_tpot(data_names, selection_types, algorithm_types, train_size=0.9, max_opt_time=720, n_gen=10, pop_size=20)
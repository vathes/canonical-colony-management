import datajoint as dj
import inspect
from djutils.pipeline import Pipeline
from .subject import *


required_table_names = ('Lab', 'User', 'Source', 'Protocol')

_subj_tables = (Strain, Sequence, Allele, Line,
                Subject, SubjectDeath, SubjectCullMethod,
                BreedingPair, Litter, Weaning, SubjectLitter,
                Cage, SubjectCaging,
                GenotypeTest, Zygosity)

pipeline = Pipeline(_subj_tables, required_table_names)

import datajoint as dj
from djlab import pipeline as lab_pipeline
from djsubject import pipeline as subj_pipeline

lab_schema = dj.schema('u24_lab_')
subj_schema = dj.schema('u24_subject_')

# initiate lab pipeline
lab_tables = lab_pipeline.init_pipeline(lab_schema)

requirements = {'Lab': lab_tables['Lab'],
                'User': lab_tables['User'],
                'Source': lab_tables['Source'],
                'Protocol': lab_tables['Protocol']}

subject_tables = subj_pipeline.init_pipeline(
    subj_schema, requirements, add_here=True)

import datajoint as dj
from djlab import schema_template as lab
from djsubject import schema_template as subject


# initiate lab pipeline
lab.declare_tables(dj.schema('u24_lab_'))

subject.declare_tables(
    dj.schema('u24_subject_'),
    requirements = {'Lab': lab.Lab,
                    'User': lab.User,
                    'Source': lab.Source,
                    'Protocol': lab.Protocol},
    add_here=True)

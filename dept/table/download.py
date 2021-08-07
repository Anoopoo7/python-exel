from .models import Dpt_model
import pandas as pd 


def convert():
    model = Dpt_model.objects.all()


    df = pd.read_csv("../table.csv")
    head = df[['name','subject']].values

    ec = ""
    mech = ""
    it = ""
    for i in  model:
        if i.department == 'ec':
            ec = ec + "  " + i.faculties

        elif i.department == 'Mech':
            mech = mech + "  " + i.faculties

        elif i.department == 'IT':
            it = it + "  " + i.faculties

    df.loc[df['name'] == 'ec' , 'subject'] = ec
    df.loc[df['name'] == 'Mech' , 'subject'] = mech
    df.loc[df['name'] == 'IT' , 'subject'] = it
    print(df)
    df.to_csv("../table.csv")
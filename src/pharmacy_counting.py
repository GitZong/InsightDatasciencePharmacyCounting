#!/usr/bin/python
import pandas as pd
import sys
infile=sys.argv[1]
outfile=sys.argv[2]
df=pd.read_csv(infile,sep=",")
def medical_record(df):
    df['name']=df[['prescriber_last_name','prescriber_first_name']].apply(lambda x: " ".join(x),axis=1)
    grouped_df=df.groupby(['drug_name'])
    medical_record=[]
    for group in grouped_df:
        drug_name=group[0]
        total_cost=group[1].drug_cost.sum()
        number_prescriber=pd.Series(pd.unique(group[1]['name'])).count()
        medical_record.append([drug_name,number_prescriber,total_cost])
    medical_record=pd.DataFrame(medical_record,columns=['drug_name','num_prescriber','total_cost']
                               )

    medical_record=medical_record.sort_values(by='total_cost',ascending=False)
    return medical_record
medical_record(df).to_csv(outfile,index=False)

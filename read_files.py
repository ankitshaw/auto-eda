import pandas as pd

def get_dataset(filename, sep, header=0):
    df = None
    if filename != '' and not filename.endswith(('.csv')):
        df = pd.read_csv(filename,sep=sep,index_col=None)
    elif filename != '' and filename.endswith(('xlsx','xls')):
        df = pd.read_excel(filename, header=header)
    else:
        print('DOOMED! Not able to read the dataset file.')
    
    return df


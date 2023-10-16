import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Invoice:

    def __init__(self, filepath = '../data/Invoices-with-Merged-Categories-and-Merged-Amounts.csv'):
        self.url = filepath
        self.sql_url = ''#put elephant sql postgresql url link for your project

    def wrangle(self):
        self.df = pd.read_csv(self.url)
        l = len(self.df)
        #print(l)
        self.df.columns = self.df.columns.str.lower().str.strip().str.replace(' ', '_')
        new_cat = [self.df['category'][index].split(sep='|') for index in range(len(df))]
        new_prices = [self.df['amount'][index].split(sep='|') for index in range(len(df))]
        order_ids = list(self.df['order_id'])
        c = 0
        for l1, l2 in zip(new_cat, new_prices):
            #print(l1, l2)
            for cat, price in zip(l1,l2):
                #print(f"{order_ids[c]}, {cat}, {price}")
                self.df.loc[len(df.index)] = [order_ids[c], cat.strip(), price.strip()]
            c += 1
        return self.df[l:].reset_index(drop=True)
    
    def creat_vis(self, cat='category'):
        sns.histplot(data=self.df, y = cat)
        return plt.savefig(f'histogram_of_the_{cat}_column.png')
    
    def create_sql(self, df:pd.DataFrame):
        df.to_sql('invoices', con=self.sql_url, if_exists='replace')

    def creat_csv(self, df: pd.DataFrame, filename:str):
        df.to_csv(f'data/{filename}.csv', index=False)
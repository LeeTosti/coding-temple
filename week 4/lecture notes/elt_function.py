import pandas as pd

def wrangle(filepath):
    df = pd.read_csv(filepath)
    l = len(df)
    #print(l)
    df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')
    new_cat = [df['category'][index].split(sep='|') for index in range(len(df))]
    new_prices = [df['amount'][index].split(sep='|') for index in range(len(df))]
    order_ids = list(df['order_id'])
    c = 0
    for l1, l2 in zip(new_cat, new_prices):
        #print(l1, l2)
        for cat, price in zip(l1,l2):
            #print(f"{order_ids[c]}, {cat}, {price}")
            df.loc[len(df.index)] = [order_ids[c], cat.strip(), price.strip()]
        c += 1
    return df[l:].reset_index(drop=True)
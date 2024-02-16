import pandas as pd
import os
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
import concurrent.futures

## calculate the distance between beads from the 3D chromatin chains data 

def make_dir(d):
    '''Utility for making a directory if not existing.'''
    if not os.path.exists(d):
        os.makedirs(d)
        

### load position data
dist_df_output_path = '../sample_data/chain_dist_df/'
make_dir(dist_df_output_path)

posi_data_path = '../sample_data/3D_chromatin_chains/GM12878_chr2.230805000.231690000/'
posi_data_list = os.listdir(posi_data_path)
all_posi_data = []

### calculate the dist_df for each chain
for chain in posi_data_list:
    position_data = np.loadtxt(posi_data_path+chain)
    dist_arr = pairwise_distances(X = position_data, metric = 'euclidean', n_jobs = 10)
    dist_df = pd.DataFrame(dist_arr)
    dist_df.to_csv(dist_df_output_path+chain+'.csv',index=False)
    
    dist_df_melted = dist_df.melt(var_name='j', value_name=chain, ignore_index=False).reset_index().rename(columns={'index': 'i'})
    all_posi_data.append(dist_df_melted)    
all_posi_df = all_posi_data[0]

### merge chain dist data
for df in all_posi_data[1:]:
    all_posi_df = all_posi_df.merge(df, on=['i','j'])
all_posi_df.to_csv(dist_df_output_path+'all_dist_df.csv',index=False)
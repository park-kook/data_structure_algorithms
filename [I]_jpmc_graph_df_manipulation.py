
import pandas as pd
import numpy as np

'''
Graph Nodes and Edges
'''

nodes_df = (
  pd.DataFrame(
    [
      [1, np.random.rand(16), np.random.rand(16)],
      [2, np.random.rand(16), np.random.rand(16)],
      [3, np.random.rand(16), np.random.rand(16)]
    ],
    columns = ['id', 'emb1', 'emb2']
  )
)

rel_df = (
  pd.DataFrame([[1,2],[1,3],[2,3]], columns = ['src','dst'])
)

mask = [False, True]

'''
Applying mask to nodes_df results in a dataframe that looks like:

'''

(
  pd.DataFrame(
    [
      [1,[0]*16, np.random.rand(16)],
      [2,[0]*16, np.random.rand(16)],
      [3,[0]*16, np.random.rand(16)]
    ],
    columns = ['id', 'emb1', 'emb2']

  )
)


mask = [False, True]


nodes_df.iloc[:,1] = pd.Series([[0]*dimension]*len(nodes_df), index = nodes_df.index)]
nodes_df.iloc[1:2:,1] = pd.Series([[0]*dimension], index = nodes_df.index[[0]])]

def graph(nodes_df, mask):
  dimension = len(nodes_df.iloc[0,1])
  for i in range(len(mask)):
    if not mask[i]:
      nodes_df.iloc[:i+1] = pd.Series([[0]*dimension]*len(nodes_df), index = nodes_df.index)
  return nodes_df
  
graph(nodes_df,  mask)


def graph(nodes_df, mask):
  dimension = len(nodes_df.iloc[0,1])
  for i in range(len(mask)):
    if not mask[i]:
      nodes_df.iloc[:i+1] = list(zip([[0]*dimension]*len(nodes_df)))
  return nodes_df
  
graph(nodes_df,  mask)


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

	id	emb1	emb2
0	1	[0.3901972315844553, 0.30596920389626114, 0.94...	[0.0038704251071560725, 0.4431299367779896, 0....
1	2	[0.0917034166028049, 0.27870550303429387, 0.10...	[0.5010994291474486, 0.1730234465036311, 0.135...
2	3	[0.9549118418713086, 0.35884874493755947, 0.88...	[0.9431234372194536, 0.08075168114399955, 0.92...


mask = [False, True]

dimension = len(nodes_df.iloc[0,1])
nodes_df.iloc[:,1] = pd.Series([[0]*dimension]*len(nodes_df), index = nodes_df.index)
	id	emb1	emb2
0	1	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]	[0.0038704251071560725, 0.4431299367779896, 0....
1	2	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]	[0.5010994291474486, 0.1730234465036311, 0.135...
2	3	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]	[0.9431234372194536, 0.08075168114399955, 0.92...

         

         
nodes_df.iloc[1:2,1] = pd.Series([[0]*dimension], index = nodes_df.index[[0]])
	id	emb1	emb2
0	1	[0.3901972315844553, 0.30596920389626114, 0.94...	[0.0038704251071560725, 0.4431299367779896, 0....
1	2	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]	[0.5010994291474486, 0.1730234465036311, 0.135...
2	3	[0.9549118418713086, 0.35884874493755947, 0.88...	[0.9431234372194536, 0.08075168114399955, 0.92...

         
def graph(nodes_df, mask):
  dimension = len(nodes_df.iloc[0,1])
  for i in range(len(mask)):
    if not mask[i]:
      nodes_df.iloc[:,i+1] = pd.Series([[0]*dimension]*len(nodes_df), index = nodes_df.index)
  return nodes_df
  
graph(nodes_df,  mask)


def graph(nodes_df, mask):
  dimension = len(nodes_df.iloc[0,1])
  for i in range(len(mask)):
    if not mask[i]:
      nodes_df.iloc[:,i+1] = list(zip([[0]*dimension]*len(nodes_df)))
  return nodes_df
  
graph(nodes_df,  mask)

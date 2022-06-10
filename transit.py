import pandas as pd
from pyvis.network import Network

transitEdges = pd.read_csv('C:/Users/Kate/Desktop/transits.csv')


#condense the data for faster/smaller graph
transitEdgesCond = transitEdges[transitEdges['total'] > 50]

print(len(transitEdgesCond))

transit_net = Network(height='750px', width='70%', bgcolor='#222222', font_color='white')

# set the physics layout of the network
transit_net.force_atlas_2based()

sources = transitEdgesCond['origin']
targets = transitEdgesCond['destination']
weights = transitEdgesCond['total']

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    transit_net.add_node(src, src, title=src)
    transit_net.add_node(dst, dst, title=dst)
    transit_net.add_edge(src, dst, value=w)

neighbor_map = transit_net.get_adj_list()

# add neighbor data to node hover data
for node in transit_net.nodes:
    node['title'] += '\nNeighbors:\n' + '\n'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])

#transit_net.show_buttons()

transit_net.show('C:/Users/Kate/Desktop/transitCond.html')

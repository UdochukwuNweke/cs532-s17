import igraph


def setEdgeProps(graph, color):
	
	for edges in graph.es:
		edges['edge_color'] = color
		graph.es["edge_width"] = 1

	return graph

def GirvinNewmanAlg(graph, maxClusterCount):
		
	vertex_colors = {0: 'black', 1: 'light blue', 2: 'red', 
	3: 'green', 4: 'pink', 5: 'brown'}
	clusters = graph.clusters('weak')
	clusterCount = len(clusters)
	iterationCounter = 1
	
	while graph.ecount() > 0 and clusterCount < maxClusterCount:

		clusters = graph.clusters('weak')
		clusterCount = len(clusters)

		for cluster in clusters:
			for vertex_index in cluster:
				graph.vs[vertex_index]['vertex_color'] = 0
		
		style = {}
		style['vertex_color'] = [vertex_colors[node['vertex_color']] 
		for node in graph.vs]

		
		edgeBetweenness = graph.edge_betweenness()

	
		indexOfEdgeWithMaximumBetweenness = max(xrange(len(edgeBetweenness)),
	    key = edgeBetweenness.__getitem__)

		
		graph.es[indexOfEdgeWithMaximumBetweenness]['edge_color'] = 'gold'
		graph.es[indexOfEdgeWithMaximumBetweenness]['edge_width'] = 5
		drawGraph(graph, vertex_colors, str(iterationCounter)+ '-' + 
	    str(clusterCount) + '.pdf' )

		
		graph.delete_edges(indexOfEdgeWithMaximumBetweenness)
		iterationCounter = iterationCounter + 1

def drawGraph(graph, vertex_colors, outfilename):

	style = {}

	layout = graph.layout('rt')
	style['layout'] = layout
	style['margin'] = 25

	style["vertex_color"] = [vertex_colors[node['Faction']] for node in graph.vs]
	style['edge_color'] = [edgeColor for edgeColor in graph.es['edge_color']]
	style['edge_width'] = [edgeWidth for edgeWidth in graph.es['edge_width']]
	style['vertex_label'] = graph.vs['name']

	igraph.plot(graph,'./graph_plots/' + outfilename, **style)

karateClub = igraph.Graph.Read_GraphML('karate.graphml')
karateClub = setEdgeProps(karateClub, 'black')

drawGraph(karateClub, {1.0: 'pink', 2.0: 'pink'}, 'karateClub.beforesplit.pdf')
drawGraph(karateClub, {1.0: 'light blue', 2.0: 'red'},
 'karateClub.postsplit.pdf')
GirvinNewmanAlg(karateClub, 5)
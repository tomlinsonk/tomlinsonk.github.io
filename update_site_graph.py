import os

NODE_SNIPPET = 'nodes = new vis.DataSet([{'
EDGE_SNIPPET = 'edges = new vis.DataSet([{'


with open('site.html', 'r') as f:
	lines = f.readlines()

node_line = next(line for line in lines if NODE_SNIPPET in line)
edge_line = next(line for line in lines if EDGE_SNIPPET in line)

with open('content/graph/_index.md', 'r') as f:
	lines = f.readlines()

node_edit_count = 0
edge_edit_count = 0

for i in range(len(lines)):
	if NODE_SNIPPET in lines[i]:
		lines[i] = node_line
		node_edit_count += 1
	elif EDGE_SNIPPET in lines[i]:
		lines[i] = edge_line
		edge_edit_count += 1

assert node_edit_count == 1
assert edge_edit_count == 1

with open('content/graph/_index.md', 'w') as f:
	f.writelines(lines)
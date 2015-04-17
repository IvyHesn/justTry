from lxml import etree

def create_tree(path):
	tree=etree.parse(path)
	return tree
tree=create_tree('levelProperty.xml')



root=tree.getroot()
root.findall('levels/id')
print (root.findall('/levels/id'))



if 0:
	tree=create_tree('levelProperty.xml')
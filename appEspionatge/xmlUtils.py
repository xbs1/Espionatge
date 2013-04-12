from xml.dom import minidom
from xml.dom.minidom import getDOMImplementation

def link_node(document, link):
	node = document.createElement("link")
	text = document.createTextNode(link)
	node.appendChild(text)

	return node

def xml_list_all_links(model, path, request):
	impl = getDOMImplementation()

	document = impl.createDocument(None, path, None)

	for instance in model.objects.all():
		link = link_node(document, instance.get_path(request))
		document.documentElement.appendChild(link)

	return document.toxml()
	
def xml_show_content(instance, path, request):
	impl = getDOMImplementation()
	document = impl.createDocument(None, path, None)
	
	data = instance.show_content(path, request)
	
	i = 0
	for key in data.keys():
		value = data[key]
		node = document.createElement(key)
		
		if isinstance(value, list):
			for link in value:
				linkNode = document.createElement("link")
				text = document.createTextNode(link)
				linkNode.appendChild(text)
				node.appendChild(linkNode)
		else:
			node.appendChild(document.createTextNode(str(value)))
	
		document.documentElement.appendChild(node)
		i += 1
    	 
	return document.toxml()
	

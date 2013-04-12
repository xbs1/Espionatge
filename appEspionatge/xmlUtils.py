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
	

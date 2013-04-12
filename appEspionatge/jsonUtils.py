from django.utils import simplejson

def json_list_all_links(model, path, request):

	paths = []
	
	for instance in model.objects.all():
		paths.append(instance.get_path(request))

	data = simplejson.dumps({
	'links': paths
	})
	
	return data
	

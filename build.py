import yaml, pystache, codecs, jsonschema, markdown, datetime, os

#configuration via defaults and config.yaml
defaults = {
	'template_directory':'./templates',
	'template_file_extension': 'tpl',
	'output_directory': './static/'
}
cfg = dict(defaults.items() + yaml.load(open('config.yaml')).items())

#pystache renders mustache templates
stache = pystache.Renderer(search_dirs=cfg['template_directory'], file_extension=cfg['template_file_extension'])

def validateYaml(f):
	""" post validation schema is defined in cfg['post_schema'] """
	if os.path.isfile(f) and f.endswith('.yaml'):
		try:
			jsonschema.validate(yaml.load(open(f)), cfg['post_schema'])
			return True
		except Exception, e:
			print ("Error loading post %s: %s" % (f,e))[0:240] + "...\n"
	return False

#get posts directory
posts = [yaml.load(open(os.path.join('posts', f))) for f in os.listdir('posts') if validateYaml(os.path.join('posts', f))]

#additional runtime metadata
cfg['general'] = dict(cfg['general'].items() + {
	'pagecount':	len(posts),
	'rundate':		datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
}.items())

#flush directory
for old_file in os.listdir(defaults['output_directory']):
    if os.path.isfile(os.path.join(defaults['output_directory'], old_file)) and old_file.endswith('.html'):
    	os.unlink(os.path.join(defaults['output_directory'], old_file))

#generate post html - see template syntax explanation in readme
for post in posts:
	#convert any fields specified in cfg['markdown_fields'] to markdown
	if 'markdown_fields' in cfg:
		for field in cfg['markdown_fields']:
			if field in post:
				post[field] = markdown.markdown(post[field])

	#output in utf8
	out = codecs.open(defaults['output_directory'] + post['slug'] + ".html", 'w', encoding='utf-8')
	out.write(stache.render_name('post', dict(cfg['general'].items() + post.items())))
	out.close()

out = codecs.open(defaults['output_directory'] + 'index.html', 'w', encoding='utf-8')
out.write(stache.render_name('index', dict(cfg['general'].items() + {'posts':posts}.items())))
out.close()

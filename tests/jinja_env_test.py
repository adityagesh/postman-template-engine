from jinja2 import Environment
import postmanrenderer.jinja_env as jinja_env

def test_enabled_filters():
    # file_loader = FileSystemLoader(APP.root_dir + APP.template_dir)
    env = Environment()
    jinja_env.init(env)
    assert env.filters["to_json"]


def test_to_json():
    l = ['abc', 'xyz' ,  'efg']
    assert jinja_env.to_json(l) == '["abc", "xyz", "efg"]'
    
import sys
import json
from collections.abc import Mapping, Sequence
from collections import OrderedDict
import ruamel.yaml

# if you instantiate a YAML instance as yaml, you have to explicitly import the error
from ruamel.yaml.error import YAMLError
from ruamel.yaml.comments import CommentedMap


yaml = ruamel.yaml.YAML()  # this uses the new API
# if you have standard indentation, no need to use the following
yaml.indent(sequence=4, offset=2)

input_file = 'input.json'
output_file = 'xx.yaml'

def json_2_yaml(in_file, out_file):
    with open(in_file, 'r') as stream:
        try:
            datamap = json.load(stream, object_pairs_hook=CommentedMap)
            # if you need to "restore" literal style scalars, etc.
            # walk_tree(datamap)
            with open(out_file, 'w') as output:
                yaml.dump(datamap, output)
        except yaml.YAMLError as exc:
            print(exc)
            return False
    return True


json_2_yaml(input_file, output_file)
with open(output_file) as fp:
    sys.stdout.write(fp.read())

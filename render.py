#!/usr/bin/env python3

import argparse
import io
import os
import sys
from jinja2 import Template, Environment, FileSystemLoader, PackageLoader, select_autoescape
from yamlreader import yaml_load

# Parse command line
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
    Renders a set of Jinja templates with a set of YAML dictionaries to the output dir
        Notes:
            - Templates must end with '.j2' extension
            - YAML dictionaries are loaded lexically, with the last key taking precedence.
            - Output dir is created idempotically (mkdir -p </foo/bar/non-existent/output)
    ''')
parser.add_argument('-d', '--dictionaries', default='./examples/dictionaries',
                    help="Folder containing yaml dictionaries")
parser.add_argument('-t', '--templates', default='./examples/templates',
                    help="Folder containing templates to be rendered")
parser.add_argument('-o', '--output', default='./output',
                    help="Folder to write rendered templates")
args = parser.parse_args()

templates = args.templates
dicts = args.dictionaries
outdir = args.output

# Create output dir
os.makedirs(outdir, exist_ok=True)

# Load templates
env = Environment(loader=FileSystemLoader(templates), autoescape=select_autoescape())

# Load and flatten yaml dictionaries lexically
dict = yaml_load(dicts)

# Render templates
files = [f for f in os.listdir(templates) if os.path.isfile(os.path.join(templates, f))]
for f in files:
    renderedFile = env.get_template(f).render(dict)
    outfile = os.path.splitext(f)[0] #template.yaml.j2 --> template.yaml
    with open(os.path.join(outdir, outfile), "w") as of:
        of.write(renderedFile)

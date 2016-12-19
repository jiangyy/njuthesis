#!/usr/bin/python

import yaml, os, re, sys

yfile = 'thesis.yaml' if len(sys.argv) == 1 else sys.argv[1]
meta = yaml.load(open(yfile))

os.system("rm -rf build/*; mkdir -p build/")
os.system("cp frontmatter/*.lyx build/; cp thesis.layout build/")

def gen(fname):
    with open("build/%s" % fname) as fp:
        contents = fp.read().decode('utf-8')
        
    def repl(m):
        key = m.group(1).strip()
        if key in meta:
            return unicode(meta[key])
        else:
            return "\\textcolor{red}{Undefined (%s)}" % key
        
    contents = re.sub(r'-\{\{-(.*?)-\}\}-', repl, contents)

    with open("build/%s" % fname, "w") as fp:
        fp.write(contents.encode('utf-8'))

gen('thesis.layout')
gen('titlepage.lyx')
gen('abstract.lyx')
gen('frontmatter.lyx')

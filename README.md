# mksite

mksite is a web site generator for tiny web sites for college courses

## Why mksite?

1. I'm aware of static site generators like Jekyll and Hugo. They seem to be targeting blogs and graphic-intensive marketing material. Their approaches seem pretty heavyweight for my needs.
1. mksite is intended to support more information-dense static web
sites for college courses, and to support quick and easy updates with the instructional material covered today.

## What does mksite do?

1. mksite translates [markdown](https://python-markdown.github.io/) pages into HTML, using [mustache](https://github.com/noahmorrison/chevron) templates
if specified.
1. mksite can catenate fragments of markdown into rows of a markdown
table, to use as a timeline of a course. For example, `Timeline.rows/`
might contain `week1.toml`, `week2.toml`, etc.
1. mksite can publish the output of these translation steps, and your static assets, to a network location you specify.

## How to use mksite
1. Clone this repo into a new directory 
1. Edit your `.bashrc` (or `.zshrc`) to add:
	1. `MKSITE_DIR=~/mksite` or wherever you cloned it
	1. `export PATH=$MKSITE_DIR:$PATH`
	1. After exiting your editor, `source .bashrc`
1. `pip3 install -r requirements.txt`
1. Create a new directory for your site, `cd` into it, and `mksite init` to copy some default files from mksite's directory into your site directory. Those assets can bootstrap your site, and you can modify them freely after initialization.
	1. Note the `mksite.toml` file, which contains config settings for your site.
	1. The page layout specified in `index.html` is primitive, but you can change it, or perhaps more sophisticated layouts can be added later.
1. `mksite build` iterates the files and directories found in your site
directory, translating them as described below, and outputting the resulting HTML files to the `build/` directory

	1. All `.md` files will be translated from markdown to HTML
	1. Source code fragments will get [syntax highlighting](https://python-markdown.github.io/extensions/code_hilite/).
	1. All `.mustache` files will get their templates resolved, and generate
	a file without the `.mustache` extension. So `foo.md.mustache` will
	generate `foo.md` and `foo.html.mustache` will generate `foo.html`
	1. Directories ending in `.rows` will be iterated, and their contents
	combined to form an HTML table. The rows will be sorted by file mod date, in newest-to-oldest order.
	1. All files ending in `.css`, `.js`, or `.png` will be copied to 
	`build/assets`
	1. You must add links in markdown format for your HTML files to `sidebar.md`. Could auto-generate this but maybe it's better to manually choose the names and order of the links?
1. `mksite publish` will use publish the contents of the `build/` directory to the network location you specify in the `[publish]` section of `mksite.toml`
	1. For rsync, specify `method = "rsync"` and `destination = "you@yourhost.edu:~you/site/"`
	1. For git, specify `method = "git"` and  `destination = "git@github.com:/your-org/site"` 

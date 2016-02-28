
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1"><a href="#Essentials-of-IPython/Jupyter-Notebooks">Essentials of IPython/Jupyter Notebooks</a></div><div class="lev2"><a href="#Introduction">Introduction</a></div><div class="lev3"><a href="#What-is-the-Jupyter-Notebook?">What is the Jupyter Notebook?</a></div><div class="lev3"><a href="#Components">Components</a></div><div class="lev3"><a href="#Kernels">Kernels</a></div><div class="lev3"><a href="#Notebook-documents">Notebook documents</a></div><div class="lev3"><a href="#Installation-and-Upgrade">Installation and Upgrade</a></div><div class="lev3"><a href="#Access">Access</a></div><div class="lev2"><a href="#Notebook">Notebook</a></div><div class="lev3"><a href="#Modal-Editor">Modal Editor</a></div><div class="lev4"><a href="#Edit-mode">Edit mode</a></div><div class="lev4"><a href="#Command-mode">Command mode</a></div><div class="lev3"><a href="#Keyboard-Shortcuts-(Command-mode)">Keyboard Shortcuts (Command mode)</a></div><div class="lev4"><a href="#Notebooks">Notebooks</a></div><div class="lev4"><a href="#Navigation">Navigation</a></div><div class="lev4"><a href="#Cell-types">Cell types</a></div><div class="lev4"><a href="#Cell-creation">Cell creation</a></div><div class="lev3"><a href="#Keyboard-Shortcuts-(Edit-mode)">Keyboard Shortcuts (Edit mode)</a></div><div class="lev4"><a href="#Text">Text</a></div><div class="lev4"><a href="#Code">Code</a></div><div class="lev3"><a href="#Large-Outputs">Large Outputs</a></div><div class="lev3"><a href="#Raw-Cells">Raw Cells</a></div><div class="lev3"><a href="#Markdown-Cells">Markdown Cells</a></div><div class="lev2"><a href="#Kernel">Kernel</a></div><div class="lev3"><a href="#Cell-Magics">Cell Magics</a></div><div class="lev4"><a href="#Timing-code-execution">Timing code execution</a></div><div class="lev4"><a href="#Capturing-stdout/err">Capturing <code>stdout/err</code></a></div><div class="lev4"><a href="#Writing-contents-to-a-file">Writing contents to a file</a></div><div class="lev4"><a href="#Running-code-under-other-interpreters">Running code under other interpreters</a></div><div class="lev3"><a href="#Rich-Output">Rich Output</a></div><div class="lev4"><a href="#Display-imports">Display imports</a></div><div class="lev4"><a href="#Images">Images</a></div><div class="lev4"><a href="#HTML">HTML</a></div><div class="lev4"><a href="#JavaScript">JavaScript</a></div><div class="lev4"><a href="#LaTeX">LaTeX</a></div><div class="lev4"><a href="#Audio">Audio</a></div><div class="lev4"><a href="#Video">Video</a></div><div class="lev4"><a href="#External-sites">External sites</a></div><div class="lev4"><a href="#Links-to-local-files">Links to local files</a></div><div class="lev4"><a href="#Rich-output,-security,-and-nbviewer">Rich output, security, and nbviewer</a></div><div class="lev3"><a href="#Plotting-with-Matplotlib">Plotting with Matplotlib</a></div><div class="lev2"><a href="#Interactive-Widgets">Interactive Widgets</a></div><div class="lev3"><a href="#Using-interact">Using interact</a></div><div class="lev2"><a href="#Extensions">Extensions</a></div>

# # Essentials of IPython/Jupyter Notebooks

# **References:**
# 
# - [IPython Documentation (official)](http://ipython.readthedocs.org/en/stable/index.html)
# - [IPython Documentation (nbviewer)](http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Index.ipynb)
# - [IPython Cookbook](https://github.com/ipython/ipython/wiki?path=Cookbook)
# - [Markdown Specification](http://daringfireball.net/projects/markdown/)
# - [MathJax TeX and LaTeX Support](http://docs.mathjax.org/en/latest/tex.html#tex-support)
# - [Jupyter Notebook Users Manual (Bryn Mawr College Computer Science)](http://jupyter.cs.brynmawr.edu/hub/dblank/public/Jupyter%20Notebook%20Users%20Manual.ipynb)
# - [Jupyter Notebook Extensions](https://github.com/ipython-contrib/IPython-notebook-extensions)

# ## Introduction

# ### What is the Jupyter Notebook?

# The [IPython/Jupyter Notebook](http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb) is a **web-based interactive computing system** that enables users to author notebook documents that include:
# 
# - Sections with different levels of headings
# - Narrative text (plain text, supporting the [Markdown](http://daringfireball.net/projects/markdown/) markup language, HTML, and $\LaTeX$)
# - Live code, supporting multiple languages
# - Equations, inline and environments, using $\LaTeX$ syntax in Markdown and rendered in-browser by [MathJax](http://www.mathjax.org/)
# - Plots
# - HTML
# - Interactive widgets
# - Media (images, audio, and video)
# - Websites 
# 
# The notebook documents contain a **complete and self-contained record of a computation** that can be exported to various formats and shared easily with others using email, Dropbox, version control systems (like git/[GitHub](http://github.com/)), or  [nbviewer.ipython.org](http://nbviewer.ipython.org/).

# ### Components
# 
# The Jupyter Notebook combines three components:
# 
# - **Notebook web application**: An interactive *web* application for writing and running code interactively and authoring notebook documents.
# 
# - **Kernels**: Separate processes started by the notebook web application to run users' code in a given language and return output back to the notebook web application. Kernels also handle computations for interactive widgets, tab completion, and introspection.
# 
# - **Notebook documents**: Self-contained documents that contain a representation of all content visible in the notebook web application, including inputs and outputs of the computations, narrative text, equations, images, and rich media representations of objects. Each notebook document has its own kernel.

# ### Kernels
# 
# The Jupyter Notebook allows code to be run in a range of different programming languages. For each notebook document that a user opens, the web application starts a *kernel* that runs the code for that notebook. Each kernel is capable of running code in a single programming language, including:
# 
# Language | Link
# -------- | ----
# Python | https://github.com/ipython/ipython (*default*)
# R | https://github.com/takluyver/IRkernel
# Ruby | https://github.com/minrk/iruby
# node.js | https://gist.github.com/Carreau/4279371
# Haskell | https://github.com/gibiansky/IHaskell
# Scala | https://github.com/Bridgewater/scala-notebook
# Julia | https://github.com/JuliaLang/IJulia.jl
# Go | https://github.com/takluyver/igo
# 
# See [IPython kernels](https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages) for a complete list of all available kernels and supported languages.

# ### Notebook documents
# 
# Notebook documents are just files with a **`.ipynb`** extension on the local filesystem. Hence, they can be organized into folders and subfolders and shared with others, just like any other common file.
# 
# Notebooks consist of a linear sequence of *cells*. There are four basic cell types:
# 
# - **Heading cells**: 6 levels of hierarchical organization and formatting
# - **Markdown cells**: narrative text with embedded LaTeX equations
# - **Code cells**: input and output of live code that is run in the kernel
# - **Raw cells**: unformatted text that is included, without modification, when notebooks are converted to different formats using `nbconvert`
# 
# Internally, notebook documents are [JSON](http://en.wikipedia.org/wiki/JSON) data with binary values [base64](http://en.wikipedia.org/wiki/Base64) encoded. This allows them to be **read and manipulated programmatically** by any programming language. Because JSON is a text format, notebook documents are version control friendly.
# 
# Notebooks can be **exported** to the following static formats using Jupyter's `nbconvert` utility: 
# - Python (`.py`)
# - Markdown (`.md`)
# - reStructuredText (reST) (`.rst`)
# - HTML (`.html`)
# - PDF via LaTeX (`.pdf`)
# - Slide shows ([reveal.js](http://lab.hakim.se/reveal-js/#/))
# 
# Any notebook document available from a public URL on or GitHub can be **shared** via [nbviewer](http://nbviewer.ipython.org/). This service loads the notebook document from the URL and renders it as a static web page. The resulting web page may be shared with others and seen without requiring a Python installation.

# ### Installation and Upgrade
# 
# The easiest way to have Python and Jupyter on your system is by installing [Anaconda](https://www.continuum.io/downloads). Anaconda is a completely free Python distribution that conveniently installs Python, the Jupyter Notebook, and other commonly used packages for science, math, engineering, and data analysis.
# 
# If disk space is an issue, [Miniconda](http://conda.pydata.org/miniconda.html) can be installed instead. Miniconda contains only conda and Python. Individual packages can be installed as needed through the `conda` command.
# 
# A Jupyter installation can be upgraded using:
# 
# - `pip install -U jupyter`, if using pip, or
# - `conda update jupyter`, if using Anaconda.

# ### Access
# 
# Assuming Anaconda was installed in the "C:\Python" Windows directory, the Jupyter Notebook environment can be launched using the following Windows shortcuts:
# 
# - Anaconda Launcher:
# 
# 
#     C:\Python\node-webkit\nw.exe "C:\Python/node-webkit/launcher"
#     
# 
# - Notebook:
# 
# 
#     C:\Python\python.exe "C:\Python\Scripts/jupyter-script.py" notebook
# 
# Additionally, the environment can be launched from the Terminal (Mac/Linux) or Command Prompt (Windows) through the following command:
# 
#     jupyter notebook

# ## Notebook

# ### Modal Editor

# #### Edit mode
# 
# - *green* cell border
# - To enable:
#     - select a cell and press <kbd>enter</kbd>,
#     - double-click *on* a cell, or
#     - click *on* a cell's editor area

# #### Command mode
# 
# - *grey* cell border
# - To exit *Edit mode* and enable *Command mode*:
#     - press <kbd>esc</kbd>,
#     - press <kbd>ctrl+m</kbd>, or 
#     - click *outside* a cell's editor area

# ### Keyboard Shortcuts (Command mode)
# 
# The following are the most useful keyboard shortcuts in *Command mode*:

# #### Notebooks
# 
# Action | Command
# ------ | -------
# open the command palette | <kbd>ctrl+shift+P</kbd>
# show all keyboard shortcuts | <kbd>h</kbd>
# find and replace text | <kbd>f</kbd>
# save notebook | <kbd>s</kbd>
# toggle output | <kbd>o</kbd>

# #### Navigation
# 
# Action | Command
# ------ | -------
# scroll notebook up | <kbd>shift+space</kbd>
# scroll notebook down | <kbd>space</kbd>
# select cell above | <kbd>pgup</kbd> / <kbd>k</kbd>
# select cell below | <kbd>pgdn</kbd> / <kbd>j</kbd>

# #### Cell types
# 
# Action | Command
# ------ | 
# raw cell | <kbd>r</kbd>
# Code cell | <kbd>y</kbd>
# Markdown cell | <kbd>m</kbd> + <kbd>1</kbd>...<kbd>6</kbd> (Headings) 

# #### Cell creation
# 
# Action | Command
# ------ | -------
# insert new cell above | <kbd>a</kbd>
# insert new cell below | <kbd>b</kbd>
# cut cell | <kbd>x</kbd>
# copy cell | <kbd>c</kbd>
# paste cell below | <kbd>v</kbd>
# delete selected cell | <kbd>d d</kbd>
# undo cell deletion | <kbd>z</kbd>
# merge cells (current + below) | <kbd>shift+m</kbd>

# ### Keyboard Shortcuts (Edit mode)
# 
# The following are the most useful keyboard shortcuts in *Edit mode*:

# #### Text
# 
# Action | Command
# ------ | -------
# code completion / indent | <kbd>tab</kbd>
# toogle comment | <kbd>alt+c</kbd>
# indent | <kbd>ctrl+]</kbd>
# dedent | <kbd>ctrl+[</kbd>
# delete word after | <kbd>ctrl+delete</kbd>
# delete word before | <kbd>ctrl+backspace</kbd>
# select all | <kbd>ctrl+a</kbd>
# undo   | <kbd>ctrl+z</kbd>
# redo   | <kbd>ctrl+y</kbd>
# split cell | <kbd>ctrl+shift-</kbd>

# #### Code
# 
# Action | Command
# ------ | -------
# run current cell and enter Command mode | <kbd>ctrl+enter</kbd>
# run current cell and move to the next | <kbd>shift+enter</kbd>
# run current cell and insert new cell below | <kbd>alt+enter</kbd>

# ### Large Outputs
# 
# To better handle large outputs, the output area can be collapsed. After running a cell, single- or double- click on the active area to the left of the output. If the output is too large, beyond a certain point, output will scroll automatically.

# In[1]:

for i in range(25):
    print(i)


# ### Raw Cells
# 
# Raw cells have no input-output distinction and cannot be rendered into anything. When running all notebook cells, raw  cells will remain exactly as is and the notebook will automatically select the cell directly below it. Raw cells have no options to bold, italicize, or enlarge any text or characters in the cell.
# 
# Because they have no rendered form, raw cells can be used to include text or code not meant to be formatted or executed. This is useful, for example, to illustrate Markdown or code syntax in unrendered form without showing any output.
<pre>
This is a raw cell
```python
def f(x):
    return x**2
```
</pre>
# ### Markdown Cells
# 
# Text can be added to Jupyter Notebooks using Markdown cells. [Markdown](http://daringfireball.net/projects/markdown/) is a popular markup language that is a superset of HTML. Markdown does not automatically hard-wrap text in paragraphs. If this is required, insert paragraph breaks by ending the line with two spaces and pressing Enter.

# - **Add headings**
                <pre>
                # Heading 1
                # Heading 2
                ## Heading 2.1
                ### Heading 2.1.1
                #### Heading 2.1.1.1
                </pre>
# - **Format text**
# 
#     *italics*  
#     **bold**  
#     ***both***  
#     ~~strikethrough~~  
#     <kbd>boxed</kbd>   
#     <pre>```raw ----```</pre>
                <pre>
                *italics*  
                **bold**  
                ***both***  
                ~~strikethrough~~  
                [kbd]boxed[/kbd] (replace [] with angle brackets)
                [pre]```raw ----```[/pre] (replace [] with angle brackets)
                </pre>
# - **Build nested itemized lists**
# 
# 
# - One
#     - Item
#     - Item
#         - Subitem
#     - Item
# - Two
                <pre>
               - One
                   - Item
                   - Item
                       - Subitem
                   - Item
               - Two
               </pre>
# - **Build nested enumerated lists**
# 
# 
# 1. One
#     1. Item A
#     1. Item B
# 2. Two
            <pre>
            1. One
                1. Item A
                1. Item B
            2. Two
            </pre>
# - **Add horizontal rules**
# 
#     ----
                <pre>
                ----
                </pre>
# - **Add blockquotes**
#     
# > This is a
# > blockquote
# 
# ...
# 
# > This is a
# >> nested
# >> blockquote
                <pre>
                > This is a
                > blockquote

                ...

                > This is a
                >> nested
                >> blockquote
                </pre>
# - **Add inline code:**
# 
#     Inline `code` has `back-ticks` around it.
                <pre>
                Inline `code` has `back-ticks` around it.
                </pre>
# - **Add Github flavored markdown (GFM) code blocks meant for illustration instead of execution**
#     
#     Github flavored markdown allows the use of triple backticks (`  ```language...`) to create fenced code blocks that support syntax highlighting:
# 
#     ```python
#     # Python
#     def f(x):
#         """Docstring"""
#         return x ** 2
#     ```
#     
#     ```java
#     //Java
#     public class HelloWorld {
#         public static void main(String[] args) {
#             // print to the terminal window
#             System.out.println("Hello, World");
#         }
#     }
#     ```
# 
#     ```javascript
#     //Javascript
#     console.log("Hello World")
#     ```
                <pre>
                ```python
                # Python
                def f(x):
                    """Docstring"""
                    return x ** 2
                ```
                </pre>
# - **Add mathematical (LaTeX) equations**
# 
#     inline equations such as $e^{i\pi} + 1 = 0$ and displayed equations such as:
#     $$e^x= \sum_{i=0}^\infty \frac{1}{i!}x^i$$
                <pre>
                inline equations such as $e^{i\pi} + 1 = 0$ and displayed equations such as:
                $$e^x= \sum_{i=0}^\infty \frac{1}{i!}x^i$$
                </pre>
# - **Add tables**
# 
# Tables are part of GFM and support inline Markdown.
# 
# Function | Description
# -------- | -----------
# `abs(x)` | Return the absolute value of `x`
#          | `...`
# `len(s)` | Return the length of an object. 
                <pre>
                Function | Description
                -------- | -----------
                `abs(x)` | Return the absolute value of `x`
                         | ...
                `len(s)` | Return the length of an object.
                </pre>
# Colons can be used to align columns:

#    | left-aligned | centered | right-alined
# -- | ------------ | :------: | -----------:
# A  | `$1,000` | `$1,000` | `$1,000`
# B  | `$100` | `$100` | `$100`
# C  | `$10` | `$10` | `$10`
# D  | `$1` | `$1` | `$1`
                <pre>
                   | left-aligned | centered | right-alined
                -- | ------------ | :------: | -----------:
                A  | `$1,000` | `$1,000` | `$1,000`
                B  | `$100` | `$100` | `$100`
                C  | `$10` | `$10` | `$10`
                D  | `$1` | `$1` | `$1`
                </pre>
# - **Add links**
# 
#     - external: [IPython's website](http://ipython.org)
#     - external with mouse-over titles: [IPython's website](http://ipython.org "Homepage")
#     - reference: This is an [external reference link] [reflink]. It was defined in a separate [line][1].
#     - internal to notebook headings: e.g., see [Markdown Cells](#Markdown-Cells) for more information...
#     - internal to notebook files: [xf_test_jupyter](input/xf_test_jupyter.ipynb)
#     - internal to local files: <img src="images/python_logo.png\" />
# 
# [reflink]: http://ipython.org "Homepage"
# [1]: http://ipython.org "Numbers can also be used as reference"
        <pre>
        - external: [IPython's website](http://ipython.org)
            - external with mouse-over titles: [IPython's website](http://ipython.org "Homepage")
            - reference: This is an [external reference link] [reflink]. It was defined in a separate [line][1].
            - internal to notebook headings: e.g., see [Markdown Cells](#Markdown-Cells) for more information...
            - internal to notebook files: [xf_test_jupyter](input/xf_test_jupyter.ipynb)
            - internal to local files: <img src="images/python_logo.png\" />

        [reflink]: http://ipython.org "Homepage"
        [1]: http://ipython.org "Numbers can also be used as reference"
        </pre>
# ## Kernel
# 
# Jupyter provides extensions to the Python programming language that make working interactively convenient and efficient. These extensions are implemented in the [IPython/Jupyter Kernel](http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/IPython%20Kernel/Index.ipynb)
#  and are available in all of the Jupyter frontends (Notebook, Terminal, Console and Qt Console) when running this kernel.

# ### Cell Magics
# 
# Jupyter has a system of commands called **magics** which provide a *mini command language*. Such a language is  orthogonal to the syntax of Python and is extensible by the user with new commands. Magics are meant to be typed interactively so they use command-line conventions, such as using *whitespace* for separating arguments, *dashes* for options, and other conventions typical of a command-line environment.
# 
# Magics come in two kinds:
# 
# - **Line magics:** these are commands prepended by one **`%`** character and whose arguments only extend to the end of the current line.
# 
# - **Cell magics:** these use two percent characters as a marker (**`%%`**), and they receive as argument *both* the current line where they are declared and the whole body of the cell. Note that cell magics can *only* be used as the first line in a cell, and as a general principle they can't be 'stacked' (i.e. you can only use one cell magic per cell). However, there are a few of them that can be stacked because of how they operate.

# Use **`%lsmagic`** to list all available magics, both line and cell magics currently defined:

# In[2]:

get_ipython().magic('lsmagic')


# First, import some necessary modules:

# In[3]:

get_ipython().magic('matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# #### Timing code execution
# 
# Use **`%timeit`** or **`%%timeit`** to time the execution of code. They exist both in line and in cell form.

# In[4]:

get_ipython().magic('timeit np.linalg.eigvals(np.random.rand(100,100))')


# In[5]:

get_ipython().run_cell_magic('timeit', 'a = np.random.rand(100, 100)', 'np.linalg.eigvals(a)')


# #### Capturing `stdout/err`
# 
# Use **`%%capture`** to capture the `stdout/err` of any block of python code, either to discard it or to store it in a variable for later use.

# In[6]:

get_ipython().run_cell_magic('capture', 'capt', 'L = [1, 2, 3]\nprint(L)')


# In[7]:

capt.stdout


# In[8]:

capt.show()


# #### Writing contents to a file
# 
# - Use **`%%writefile`** to write cell contents as a named file.
# - Use **`%run`** to run the file created with `%%writefile`.

# In[9]:

get_ipython().run_cell_magic('writefile', '"output/xf_test_writefile_magic.py"', 'print("Hello world")')


# In[10]:

get_ipython().magic('run "output/xf_test_writefile_magic.py"')


# #### Running code under other interpreters
# 
# - Use **`%%script`** to run a cell in a subprocess of any interpreter in your system, such as bash, ruby, perl, R, etc.
# - Use `--out var_name` and `--err var_name` to capture the `stdout/err` from these processes into Python variables.

# In[11]:

get_ipython().run_cell_magic('script', 'R --no-save --out output --err error', 'a <- 2\na * 4')


# In[12]:

print(output)


# In[13]:

print(error)


# ### Rich Output
# 
# In Python, objects can declare their textual representation using the `__repr__` method. Jupyter allows objects to declare other, rich representations including:
# 
# - HTML
# - JSON
# - PNG
# - JPEG
# - SVG
# - LaTeX
# 
# A single object can declare some or all of these representations; all are handled by IPython's `display` system, which can be used to incorporate a broad range of content into the notebooks.

# #### Display imports
# 
# The **`display`** function is a general purpose tool for displaying different representations of objects. It functions as `print` for these rich representations.

# In[14]:

from IPython.display import display


# There are also specific functions to display a particular representation:

# In[15]:

from IPython.display import (
    display_pretty,
    display_html,
    display_json,
    display_png,
    display_jpeg,
    display_svg,
    display_latex,
)


# #### Images
# 
# Use the **`Image`** class to work with images (JPEG, PNG). By default, image data is embedded in the notebook document so that the images can be viewed offline. However it is also possible to tell the `Image` class to only store a link to the image.

# In[16]:

from IPython.display import Image


# In[17]:

img = Image(filename='images/ipython_logo.png')
display(img)  # also, simply img


# SVG images are also supported out of the box.

# In[18]:

from IPython.display import SVG
SVG(filename='images/python_logo.svg')


# An image can also be displayed from raw data or a URL.

# In[19]:

Image(url='http://python.org/images/python-logo.gif')


# #### HTML
# 
# Python objects can declare HTML representations that will be displayed in the notebook. Use the **`HTML`** class to display some HTML.

# In[20]:

from IPython.display import HTML


# In[21]:

table = """
<table>
<tr>
<th>Header 1</th>
<th>Header 2</th>
</tr>
<tr>
<td>11</td>
<td>12</td>
</tr>
<tr>
<td>21</td>
<td>22</td>
</tr>
</table>"""

h = HTML(table)
display(h)


# The same thing can be accomplished using the **`%%html`** cell magic:

# In[22]:

get_ipython().run_cell_magic('html', '', '<table>\n<tr>\n<th>Header 1</th>\n<th>Header 2</th>\n</tr>\n<tr>\n<td>11</td>\n<td>12</td>\n</tr>\n<tr>\n<td>21</td>\n<td>22</td>\n</tr>\n</table>')


# #### JavaScript
# 
# The notebook also enables objects to declare a JavaScript representation.

# In[23]:

from IPython.display import Javascript


# In[24]:

# uncomment to run
# jsmssg = Javascript('alert("Hello world!")');  
# display(jsmssg)


# #### LaTeX
# 
# The IPython display system also has builtin support for the display of mathematical expressions typeset in $\LaTeX$, which is rendered in the browser using [MathJax](http://mathjax.org/). Raw LaTeX text can be passed as a string to the `Math` object:

# In[25]:

from IPython.display import Math


# In[26]:

Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx')


# The delimiters can be included with the `Latex` class, so other $\LaTeX$ modes such as `eqnarray` can also be used:

# In[27]:

from IPython.display import Latex
Latex(r"""\begin{eqnarray}
\nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} 
& = \frac{4\pi}{c}\vec{\mathbf{j}} \\
\nabla \cdot \vec{\mathbf{E}} 
& = 4 \pi \rho \\
\nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} 
& = \vec{\mathbf{0}} \\
\nabla \cdot \vec{\mathbf{B}} 
& = 0 
\end{eqnarray}""")


# The same thing can be accomplished using the **`%%latex`** cell magic:

# In[28]:

get_ipython().run_cell_magic('latex', '', '\\begin{align}\n\\nabla \\times \\vec{\\mathbf{B}} -\\, \\frac1c\\, \\frac{\\partial\\vec{\\mathbf{E}}}{\\partial t} \n& = \\frac{4\\pi}{c}\\vec{\\mathbf{j}} \\\\\n\\nabla \\cdot \\vec{\\mathbf{E}} \n& = 4 \\pi \\rho \\\\\n\\nabla \\times \\vec{\\mathbf{E}}\\, +\\, \\frac1c\\, \\frac{\\partial\\vec{\\mathbf{B}}}{\\partial t} \n& = \\vec{\\mathbf{0}} \\\\\n\\nabla \\cdot \\vec{\\mathbf{B}} \n& = 0\n\\end{align}')


# #### Audio
# 
# Use the **`Audio`** display class to create an audio control that is embedded in the notebook. The interface is analogous to the interface of the `Image` display class. All audio formats supported by the browser can be used; however, no single format is presently supported in all browsers.

# In[29]:

from IPython.display import Audio
Audio(url="http://www.nch.com.au/acm/8k16bitpcm.wav")


# #### Video
# 
# More objects can also be displayed in the notebook, as long as their representation supports the IPython `display` protocol. For example, videos hosted externally on YouTube are easy to load:

# In[30]:

from IPython.display import YouTubeVideo
YouTubeVideo('sjfsUzECqK0')


# #### External sites
# 
# An entire page from another site can be embedded in an `IFrame`.

# In[31]:

from IPython.display import IFrame
IFrame('http://jupyter.org', width='100%', height=350)


# #### Links to local files
# 
# IPython provides built-in display classes for generating links to local files. 
# 
# - Use the **`FileLink`** object to create a link to a single file. 
# - Alternatively, use `FileLinks('.')` to generate links to all of the files in the current working directory and all its sub-directories, if any.

# In[32]:

from IPython.display import FileLink, FileLinks
FileLink('input/xf_test_jupyter.ipynb')


# #### Rich output, security, and nbviewer
# 
# The Jupyter Notebook allows arbitrary code execution in both the Jupyter kernel and in the browser, through HTML and JavaScript output. More importantly, because Jupyter has a JavaScript API for running code in the browser, HTML and JavaScript output can actually trigger code to be run in the kernel. This poses a significant security risk as it would allow Jupyter notebooks to execute arbitrary code on your computer.
# 
# To protect against these risks, the Jupyter Notebook has a [security model](http://ipython.org/ipython-doc/dev/notebook/security.html) that specifies how dangerous output is handled. Here is a short summary:
# 
# - When running code in the notebook, all rich output is displayed.
# - When opening a notebook, rich output is only displayed if it doesn't contain security vulnerabilities or if the notebook is a trusted notebook.
# 
# Much of the power of the notebook is that it enables users to share notebooks with each other using http://nbviewer.ipython.org, without installing Jupyter locally. As of IPython/Jupyter 2.0, notebooks rendered on nbviewer will display all output, including HTML and JavaScript. Furthermore, to provide a consistent JavaScript environment on the live notebook and nbviewer, the [jQuery](http://jquery.com/) and [RequireJS](http://requirejs.org/) JavaScript libraries are loaded onto the `nbviewer` page, before the notebook and its output is displayed.

# ### Plotting with Matplotlib
# 
# Jupyter works with the [Matplotlib](http://matplotlib.org/) plotting library, which integrates Matplotlib with IPython's `display` system and event loop handling.
# 
# Use the **`%matplotlib`** magic command to enable plotting in the current notebook:
# - Use `%matplotlib inline` to embed plots inside the notebook.
# - Use `%matplotlib notebook` to get interactive panning and zooming of matplotlib figures in the browser.

# In[33]:

get_ipython().magic('matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# In[34]:

x = np.linspace(0, 3*np.pi, 500)
plt.plot(x, np.sin(x**2))
plt.title('A simple chirp');


# In[35]:

# %matplotlib notebook


# In[36]:

plt.figure()
x = np.linspace(0, 5 * np.pi, 1000)
for n in range(1, 4):
    plt.plot(np.sin(n * x))
plt.show()


# ## Interactive Widgets
# 
# Jupyter includes an architecture for [interactive widgets](http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Interactive%20Widgets/Index.ipynb) that tie together Python code running in the kernel and JavaScript/HTML/CSS running in the browser. These widgets enable users to explore their code and data interactively.

# ### Using interact
# 
# The **`interact`** function (from `ipywidgets`) automatically creates user interface (UI) controls for exploring code and data interactively. It is the easiest way to get started using IPython's widgets.

# In[37]:

from ipywidgets import interact, interactive, fixed, widgets


# At the most basic level, `interact` autogenerates UI controls for function arguments, and then calls a user-defined  function with those arguments when manipulating the controls interactively to explore the function.

# In[38]:

def f(x):
    print('x^2: {}'.format(x**2))


# When passing this function as the first argument to interact along with an integer keyword argument (x=10), a slider is generated and bound to the function. When the slider is moved, the function is called and the current value of `x` is printed.

# In[39]:

interact(f, x=10);


# `interact` can also be used as a decorator to make it possible to define a function and interact with it in a single shot.

# In[40]:

@interact(x=5, y=1.0)
def g(x, y):
    print('x*y: {}'.format(x*y))


# One or more of the function arguments can also be fixed to specific values. In this case, a slider is only produced for the variables that are not fixed.

# In[41]:

interact(g, x=20, y=fixed(5.0));


# Use the **`IntSlider`/`FloatSlider`** widgets as keyword arguments for a given function parameter to specify values for the parameter's `min`, `max`, `step`, and `initial` values.

# In[42]:

interact(f, x=widgets.IntSlider(min=-50,max=50,step=1,value=0));


# The same thing can be accomplished by passing a tuple containing `(min,max,step)` values to the desired parameters.

# In[43]:

interact(g, x=(0,8,2), y=(-10.0,10.0,1.0));


# A decorator can also be used to simplify notation and set an initial value for the widget.

# In[44]:

@interact(x=(0.0,20.0,0.5))
def h(x=5.5):
    print(x)


# Pass a dictionary to obtain a dropdown menu that passes non-string values to the Python function. The dictionary keys are used for the names in the dropdown menu UI and the values are the arguments that are passed to the underlying Python function.

# In[45]:

interact(f, x={'one': 10, 'two': 20});


# If a string is passed, `interact` will generate a text area or a dropdown menu, depending on how many string arguments are passed.

# In[46]:

def first_letter(S):
    return S[0]

interact(first_letter, S=('apples','oranges'));


# ## Extensions

# The Jupyter Notebook extensions repository contains a collection of extensions that add functionality to the Jupyter environment. These extensions are mostly written in Javascript and are loaded locally in your browser.
# 
# The easiest way to install the collection of Jupyter extensions is using `pip`, from the current master. In the command line, enter
# 
# ---
# 
# `pip install https://github.com/ipython-contrib/IPython-notebook-extensions/archive/master.zip --user` *(or use* `--upgrade` *to upgrade)*
# 
# ---
# 
# When using the Anaconda Python installation (highly recommended), you can install the package using 
# 
# ---
# 
# `conda install -c https://conda.binstar.org/juhasch nbextensions`
# 
# ---
# 
# After installation, simply go to the `/nbextensions/` page in the notebook to activate/deactivate individual extensions (e.g., `http://localhost:8888/nbextensions/`).
# 
# For more information, go to [IPython-notebook-extensions
# ](https://github.com/ipython-contrib/IPython-notebook-extensions) on GitHub or refer to the local [`nbextensions` `readme.md`](http://localhost:8889/nbextensions/config/rendermd/nbextensions/config/readme.md) file.

# In[ ]:




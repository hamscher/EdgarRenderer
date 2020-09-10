"""
:mod:`EdgarRenderer.Brel`
~~~~~~~~~~~~~~~~~~~
Edgar(tm) Renderer was created by staff of the U.S. Securities and Exchange Commission.
Data and content created by government employees within the scope of their employment 
are not subject to domestic copyright protection. 17 U.S.C. 105.
"""
"""
Brel: simple minded Abstract XBRL instance + DTS Interface
Initial Implementation via lxml + arelle

"""
"""
replacements for lxml.etree
"""
import lxml

iterparse = lxml.etree.iterparse
parse = lxml.etree.parse
treeToString = lxml.etree.tostring

Comment = lxml.etree.Comment
Element = lxml.etree.Element
LxmlError = lxml.etree.LxmlError
HTML = lxml.etree.HTML
QName = lxml.etree.QName
SubElement = lxml.etree.SubElement
XSLT = lxml.etree.XSLT
XSLTError = lxml.etree.XSLTError

ElementDepthFirstIterator = lxml.etree.ElementDepthFirstIterator

"""
replacements for arelle
"""


"""
is the class even needed?
"""
class brel(object):
    def __init__(self):
        pass

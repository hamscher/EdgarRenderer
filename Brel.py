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
import arelle
from arelle import (XbrlConst)

# name spaces
xbrli = arelle.XbrlConst.xbrli
link = arelle.XbrlConst.link
xlink = arelle.XbrlConst.xlink

# arc roles
summationItem = arelle.XbrlConst.summationItem
parentChild = arelle.XbrlConst.parentChild
conceptLabel = arelle.XbrlConst.conceptLabel
conceptReference = arelle.XbrlConst.conceptReference

# roles
defaultLinkRole = arelle.XbrlConst.defaultLinkRole
documentationLabel = arelle.XbrlConst.documentationLabel

# q names
qnIXbrl11Hidden = arelle.XbrlConst.qnIXbrl11Hidden
qnXbrliIdentifier = arelle.XbrlConst.qnXbrliIdentifier

"""
is the class even needed?
"""
class brel(object):
    def __init__(self):
        pass

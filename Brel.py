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
#from arelle import (XbrlConst)

"""
replacements for arelle.XbrlConst
"""
# name spaces
xbrli = arelle.XbrlConst.xbrli
link = arelle.XbrlConst.link
xlink = arelle.XbrlConst.xlink
xhtml = arelle.XbrlConst.xhtml
ixbrl11 = arelle.XbrlConst.ixbrl11
xsd = arelle.XbrlConst.xsd
ixbrlAll = arelle.XbrlConst.ixbrlAll

# arc roles
summationItem = arelle.XbrlConst.summationItem
parentChild = arelle.XbrlConst.parentChild
conceptLabel = arelle.XbrlConst.conceptLabel
conceptReference = arelle.XbrlConst.conceptReference
dimensionDefault = arelle.XbrlConst.dimensionDefault
dimensionDomain = arelle.XbrlConst.dimensionDomain

# roles
defaultLinkRole = arelle.XbrlConst.defaultLinkRole
documentationLabel = arelle.XbrlConst.documentationLabel

# Clark notations
cnXbrliIdentifier = "{"+xbrli+"}xbrli:identifier"

# q names
qnIXbrl11Hidden = arelle.XbrlConst.qnIXbrl11Hidden
qnXbrliIdentifier = arelle.ModelObject.qname(cnXbrliIdentifier)
qnLinkPresentationArc = arelle.XbrlConst.qnLinkPresentationArc
qnLinkPresentationLink = arelle.XbrlConst.qnLinkPresentationLink

"""
replacements for arelle.ModelDocument
"""

load = arelle.ModelDocument.load
LoadingException = arelle.ModelDocument.LoadingException

class Type:
    UnknownXML = arelle.ModelDocument.Type.UnknownXML
    UnknownNonXML = arelle.ModelDocument.Type.UnknownNonXML
    UnknownTypes = arelle.ModelDocument.Type.UnknownTypes  # to test if any unknown type, use <= Type.UnknownTypes
    firstXBRLtype = arelle.ModelDocument.Type.firstXBRLtype
    SCHEMA = arelle.ModelDocument.Type.SCHEMA
    LINKBASE = arelle.ModelDocument.Type.LINKBASE
    INSTANCE = arelle.ModelDocument.Type.INSTANCE
    INLINEXBRL = arelle.ModelDocument.Type.INLINEXBRL
    lastXBRLtype = arelle.ModelDocument.Type.lastXBRLtype
    DTSENTRIES = arelle.ModelDocument.Type.DTSENTRIES
    INLINEXBRLDOCUMENTSET = arelle.ModelDocument.Type.INLINEXBRLDOCUMENTSET
    VERSIONINGREPORT = arelle.ModelDocument.Type.VERSIONINGREPORT
    TESTCASESINDEX = arelle.ModelDocument.Type.TESTCASESINDEX
    TESTCASE = arelle.ModelDocument.Type.TESTCASE
    REGISTRY = arelle.ModelDocument.Type.REGISTRY
    REGISTRYTESTCASE = arelle.ModelDocument.Type.REGISTRYTESTCASE
    XPATHTESTSUITE = arelle.ModelDocument.Type.XPATHTESTSUITE
    RSSFEED = arelle.ModelDocument.Type.RSSFEED
    ARCSINFOSET = arelle.ModelDocument.Type.ARCSINFOSET
    FACTDIMSINFOSET = arelle.ModelDocument.Type.FACTDIMSINFOSET
    
    TESTCASETYPES = (TESTCASESINDEX, TESTCASE, REGISTRY, REGISTRYTESTCASE, XPATHTESTSUITE)


"""
replacements for arelle.ModelDts
"""
ModelConcept = arelle.ModelDtsObject.ModelConcept
ModelResource = arelle.ModelDtsObject.ModelResource


"""
replacements for arelle.ModelValue
"""

QName = arelle.ModelValue.QName

"""
Miscellaneous replacements
"""

referencedFiles = arelle.ValidateFilingText.referencedFiles

collapseWhitespace = arelle.XmlUtil.collapseWhitespace
descendantAttr = arelle.XmlUtil.descendantAttr

VALID = arelle.XmlValidate.VALID
VALID_NO_CONTENT = arelle.XmlValidate.VALID_NO_CONTENT

Cntlr = arelle.Cntlr.Cntlr

FileSource = arelle.FileSource

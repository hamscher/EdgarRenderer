"""
:mod:`EdgarRenderer.Brel`
~~~~~~~~~~~~~~~~~~~
Edgar(tm) Renderer was created by staff of the U.S. Securities and Exchange Commission.
Data and content created by government employees within the scope of their employment 
are not subject to domestic copyright protection. 17 U.S.C. 105.
"""
from builtins import object
"""
Brel: simple minded Abstract XBRL instance + DTS Interface
Initial Implementation via lxml + arelle
"""
"""
replacements for lxml.etree
"""
import lxml

iterparse = lxml.etree.iterparse # function
parse = lxml.etree.parse # function
treeToString = lxml.etree.tostring # function

Comment = lxml.etree.Comment # factory
Element = lxml.etree.Element # factory
LxmlError = lxml.etree.LxmlError # exception class
HTML = lxml.etree.HTML # function
QName = lxml.etree.QName # wrapper function
SubElement = lxml.etree.SubElement # factory
XSLT = lxml.etree.XSLT # function
XSLTError = lxml.etree.XSLTError # exception class

ElementDepthFirstIterator = lxml.etree.ElementDepthFirstIterator # Element method

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

#  QNames
qnIXbrl11Hidden = arelle.XbrlConst.qnIXbrl11Hidden
qnXbrliIdentifier = arelle.ModelObject.qname(cnXbrliIdentifier)
qnLinkPresentationArc = arelle.XbrlConst.qnLinkPresentationArc
qnLinkPresentationLink = arelle.XbrlConst.qnLinkPresentationLink

"""
replacements for arelle.ModelDocument
"""

load = arelle.ModelDocument.load # function
LoadingException = arelle.ModelDocument.LoadingException # Exception
openFileSource = arelle.FileSource.openFileSource # function

class FileSource (arelle.FileSource.FileSource):
    pass


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
replacements for arelle.ModelObject
"""
def isModelObject(o):
    return isinstance(o,arelle.ModelDtsObject.ModelObject)

class ModelObject (arelle.ModelObject.ModelObject):
    pass

"""
replacements for arelle.ModelDts
"""
def isModelConcept(o):
    return isinstance(o,arelle.ModelDtsObject.ModelConcept)

class ModelConcept (arelle.ModelDtsObject.ModelConcept):
    pass


def isModelResource(o):
    return isinstance(o,arelle.ModelDtsObject.ModelResource)

class ModelResource (arelle.ModelDtsObject.ModelResource):
    pass


def isDimensionItem(o):
    return isinstance(o,arelle.ModelDtsObject.ModelConcept) and o.isDimensionItem

"""
replacements for arelle.ModelValue
"""

def isQName (o):
    return isinstance(o,arelle.ModelValue.QName)

class QName (arelle.ModelValue.QName):
    pass

def isIsoDuration (o):
    return isinstance(o,arelle.ModelValue.IsoDuration)

class IsoDuration (arelle.ModelValue.IsoDuration):
    pass

qname = arelle.ModelValue.qname # function


"""
Miscellaneous replacements
"""

class Cntlr (arelle.Cntlr.Cntlr):
    pass

referencedFiles = arelle.ValidateFilingText.referencedFiles # function

collapseWhitespace = arelle.XmlUtil.collapseWhitespace # function
descendantAttr = arelle.XmlUtil.descendantAttr # function

VALID = arelle.XmlValidate.VALID # enum int
VALID_NO_CONTENT = arelle.XmlValidate.VALID_NO_CONTENT # enum int

"""
gsed -r -n 's/.*((model[A-Z][a-zA-Z0-9_]*|fact|context|unit|qname|controller)\.[a-zA-Z0-9_]*[\.\[\(]?).*/\1/gp' *.py | sort -u

context.
context.dimsHash
context.endDatetime
context.entityIdentifier
context.entityIdentifier[
context.id
context.isForeverPeriod
context.period.
context.qnameDims.
context.scenario
context.scenario.
controller.ErrorMsgs
controller.VERSION
controller.auxMetadata
controller.cntlr.
controller.createdFolders
controller.debugMode
controller.entrypoint
controller.entrypointFolder
controller.excelXslt
controller.factCubeCount
controller.factCubeCount[
controller.factHasHtmlAnchor
controller.formatLogMessage(
controller.includeLogsInSummary
controller.inlineList
controller.instanceList
controller.instanceSummaryList
controller.logDebug(
controller.logError(
controller.logInfo(
controller.logTrace(
controller.nextBarChartFileNum
controller.nextFileNum
controller.nextUncategorizedFileNum
controller.noEquity
controller.originalProcessingFolder
controller.otherXbrlList
controller.processInZip
controller.processingFolder
controller.renderedFiles.
controller.reportFormat
controller.reportFormat.
controller.reportXslt
controller.reportXsltDissem
controller.reportZip
controller.reportZip.
controller.reportsFolder
controller.roleHasHtmlAnchor
controller.roleHasHtmlAnchor[
controller.sourceDict
controller.summaryHasLogEntries
controller.summaryXslt
controller.supplementList
controller.supplementalFileList
controller.validatedForEFM
controller.writeFile(
controller.xlWriter
fact.
fact.ancestorQnames
fact.concept
fact.concept.
fact.context
fact.contextID
fact.decimals
fact.decimals.
fact.document
fact.isNil
fact.isNumeric
fact.isTuple
fact.iterancestors(
fact.modelXbrl
fact.prefixedName
fact.qname
fact.sValue
fact.sourceline
fact.unit
fact.unitID
fact.unitSymbol(
fact.utrEntries.
fact.value
fact.value.
fact.xValid
fact.xValue
fact.xmlLang
fact.xsiNil
modelDocument.basename
modelDocument.filepath
modelDocument.filepathdir
modelDocument.referencesDocument.
modelDocument.relativeUri(
modelDocument.targetDocumentPreferredFilename
modelDocument.targetDocumentSchemaRefs
modelDocument.type
modelDocument.uri
modelManager.abortOnMajorError
modelManager.cntlr.
modelManager.disclosureSystem
modelManager.formulaOptions.
modelManager.showStatus(
modelManager.validate(
modelManager.validateDisclosureSystem
modelRelationshipsFrom.items(
modelRelationshipsFrom.keys(
modelRelationshipsTo.keys(
modelType.qnameDerivedFrom
modelXbrl.arelleUnitTests
modelXbrl.arelleUnitTests[
modelXbrl.contexts.
modelXbrl.debug(
modelXbrl.duplicateFactSet
modelXbrl.efmOptions
modelXbrl.error(
modelXbrl.errors
modelXbrl.extractedInlineInstance
modelXbrl.facts
modelXbrl.factsByQname.
modelXbrl.factsByQname[
modelXbrl.fileSource
modelXbrl.fileSource.
modelXbrl.info(
modelXbrl.ixdsHtmlElements
modelXbrl.log(
modelXbrl.logger.
modelXbrl.modelDocument
modelXbrl.nameConcepts[
modelXbrl.namespaceDocs.
modelXbrl.prefixedNamespaces[
modelXbrl.profileActivity(
modelXbrl.profileStat(
modelXbrl.qnameConcepts
modelXbrl.qnameConcepts.
modelXbrl.qnameConcepts[
modelXbrl.qnameTypes
modelXbrl.qnameTypes[
modelXbrl.relationshipSet(
modelXbrl.relationshipSets.
modelXbrl.roleTypeName(
modelXbrl.roleTypes[
modelXbrl.units
modelXbrl.urlDocs.
modelXbrl.warning(
qname.clarkNotation
qname.localName
qname.localName.
qname.localname
qname.namespace
qname.namespaceURI
unit.
unit.id
unit.isSingleMeasure
unit.measures[
unit.sourceline
unit.value


"""
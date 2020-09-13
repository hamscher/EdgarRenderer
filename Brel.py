"""
:mod:`EdgarRenderer.Brel`
~~~~~~~~~~~~~~~~~~~
Edgar(tm) Renderer was created by staff of the U.S. Securities and Exchange Commission.
Data and content created by government employees within the scope of their employment 
are not subject to domestic copyright protection. 17 U.S.C. 105.
"""
#from builtins import object
from colorsys import _v
"""
Brel: simple minded Abstract XBRL instance + DTS Interface
Initial Implementation via lxml + arelle
"""

""" BREL COMMON """
from typing import List #@UnusedImport

class IModelObject:
        
    def __getattr__(self,name):
        try:
            return self.__dict__[name]
        except Exception as e:
            if '_realObject' in self.__dict__:
                _v = getattr(self._realObject,name)
                setattr(self,name,_v)
                return _v
            else:
                raise e
            
def isModelObject(o):
    return issubclass(type(o),IModelObject)
"""
Xbrl
Document
Unit
Fact
Context
Footnote
Period
Concept
Type
Link
Resource
Relationship

These should have abstract methods (signatures) declared.
"""

class IModelXbrl(IModelObject):
    pass

def isModelXbrl(o):
    return issubclass(type(o),IModelXbrl)
###

class IModelDocument(IModelObject):
    pass

def isModelDocument(o):
    return issubclass(type(o),IModelDocument)
###

class IModelUnit(IModelObject):
    pass

def isModelUnit(o):
    return issubclass(type(o),IModelUnit)
###

class IModelFact(IModelObject):
    pass

def isModelFact(o):
    return issubclass(type(o),IModelFact)
###

class IModelContext(IModelObject):
    pass

def isModelContext(o):
    return issubclass(type(o),IModelContext)
###

class IModelConcept(IModelObject):
    pass

def isModelConcept(o):
    return issubclass(type(o),IModelConcept)
###

class IModelType(IModelObject):
    pass

def isModelType(o):
    return issubclass(type(o),IModelType)
###

class IModelLink(IModelObject):
    pass

def isModelLink(o):
    return issubclass(type(o),IModelLink)
###

class IModelResource(IModelObject):
    pass

def isModelResource(o):
    return issubclass(type(o),IModelResource)
###

class IModelRelationship(IModelObject):
    pass

def isModelRelationship(o):
    return issubclass(type(o),IModelRelationship)

""" BREL IN LXML + ARELLE """

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

class ModelObject (IModelObject):
    pass

"""
replacements for arelle.ModelDts.*
"""

class ModelContext(IModelContext):
    """
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
    """
    proxy = {} # class variable
    @staticmethod
    def of(context): 
        assert isinstance(context,arelle.ModelInstanceObject.ModelContext)
        try: return ModelContext.proxy[context]
        except: return ModelContext(context)
        
    def __init__(self,context):
        assert isinstance(context,arelle.ModelInstanceObject.ModelContext)
        self.proxy[context] = self
        self._realObject = context
        self.document = self.modelDocument = ModelDocument.of(context.document)
        self.modelXbrl = ModelXbrl.of(context.modelXbrl)
        return

class ModelConcept(IModelConcept):
    proxy = {} # class variable
    @staticmethod
    def of(concept): 
        assert isinstance(concept,arelle.ModelDtsObject.ModelConcept)
        try: return ModelConcept.proxy[concept]
        except: return ModelConcept(concept)

    def __init__(self,concept):
        assert isinstance(concept,arelle.ModelDtsObject.ModelConcept)
        self.proxy[concept] = self 
        self._realObject = concept
        

class ModelLink (IModelLink):
    proxy = {} # class variable
    @staticmethod
    def of(link): 
        assert isinstance(link,arelle.ModelDtsObject.ModelLink)
        try: return ModelLink.proxy[link]
        except: return ModelLink(link)
    def __init__(self,link):
        assert isinstance(link,arelle.ModelDtsObject.ModelLink)
        self.proxy[link] = self
        self._realObject = link
    pass

class ModelResource (IModelResource):
    proxy = {} # class variable
    @staticmethod
    def of(resource): 
        assert isinstance(resource,arelle.ModelDtsObject.ModelResource)
        try: return ModelFact.proxy[resource]
        except: return ModelFact(resource)
    def __init__(self,resource):
        assert isinstance(resource,arelle.ModelDtsObject.ModelResource)
        self.proxy[resource] = self
        self._realObject = resource
    pass

class ModelRelationship (IModelRelationship):
    proxy = {} # class variable
    @staticmethod
    def of(relationship): 
        assert isinstance(relationship,arelle.ModelDtsObject.ModelRelationship)
        try: return ModelFact.proxy[relationship]
        except: return ModelFact(relationship)
    def __init__(self,relationship):
        assert isinstance(relationship,arelle.ModelDtsObject.ModelRelationship)
        self.proxy[relationship] = self
        self._realObject = relationship
    pass

class ModelType (IModelType):
    proxy = {} # class variable
    @staticmethod
    def of(modelType): 
        assert isinstance(modelType,arelle.ModelDtsObject.ModelType)
        try: return ModelFact.proxy[modelType]
        except: return ModelFact(modelType)
    def __init__(self,modelType):
        assert isinstance(modelType,arelle.ModelDtsObject.ModelType)
        self.proxy[modelType] = self
        self._realObject = modelType
    pass

class ModelUnit (IModelUnit):
    proxy = {} # class variable
    @staticmethod
    def of(unit): 
        assert isinstance(unit,arelle.ModelInstanceObject.ModelUnit)
        try: return ModelUnit.proxy[unit]
        except: return ModelUnit(unit)
    def __init__(self,unit):
        assert isinstance(unit,arelle.ModelInstanceObject.ModelUnit)
        self.proxy[unit] = self
        self._realObject = unit
    pass


class ModelDocument (IModelDocument):
    proxy = {} # class variable
    @staticmethod
    def of(document): 
        assert isinstance(document,arelle.ModelDocument.ModelDocument)
        try: return ModelDocument.proxy[document]
        except: return ModelDocument(document)
        
    def __init__(self,document):
        assert isinstance(document,arelle.ModelDocument.ModelDocument)
        self.proxy[document] = self
        self._realObject = document
        self.modelXbrl = ModelXbrl.of(document.modelXbrl)
        self.idObjects = {}
        for k,v in document.idObjects.items():        
            self.idObjects[k] = v
            try: 
                fn = maker[type(v)]
                self.idObjects[k] = fn(v)
            except KeyError as e: #@UnusedVariable
                pass
    pass

"""fact.
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
fact.iter -- an lxml function
fact.iterancestors(   -- an lxml function
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
fact.xsiNil"""

class ModelFact(IModelFact):
    proxy = {} # class variable
    @staticmethod
    def of(fact): 
        assert isinstance(fact,arelle.ModelInstanceObject.ModelFact)
        try: return ModelFact.proxy[fact]
        except: return ModelFact(fact)
    
    def __init__(self,fact):
        assert isinstance(fact,arelle.ModelInstanceObject.ModelFact)
        self.proxy[fact] = self
        self._realObject = fact
        self.concept = ModelConcept.of(fact.concept)
        self.context = ModelContext.of(fact.context)
        if getattr(fact,'unit',None) is not None:
            self.unit = _u = ModelUnit.of(fact.unit)
        # footnote
        

class ModelXbrl(IModelXbrl): 
    proxy = {} # class variable
    @staticmethod
    def of(modelXbrl): 
        assert isinstance(modelXbrl,arelle.ModelXbrl.ModelXbrl)
        try: return ModelXbrl.proxy[modelXbrl]
        except: return ModelXbrl(modelXbrl)
    
    def __init__(self,modelXbrl):
        self.proxy[modelXbrl] = self
        self._realObject = modelXbrl
        # Contexts
        self.contexts = {}
        for k,v in modelXbrl.contexts.items():
            self.contexts[k] = ModelContext.of(v)
        # Facts
        self.facts = []
        for v in modelXbrl.facts:
            _v = ModelFact.of(v)
            self.facts.append(_v)

maker = {arelle.ModelInstanceObject.ModelFact : ModelFact.of
           ,arelle.ModelInstanceObject.ModelContext : ModelContext.of
           ,arelle.ModelInstanceObject.ModelUnit : ModelUnit.of 
           ,arelle.ModelDtsObject.ModelConcept : ModelConcept.of
           ,arelle.ModelDtsObject.ModelType : ModelType.of
           ,arelle.ModelDtsObject.ModelLink : ModelLink.of
           ,arelle.ModelDtsObject.ModelRelationship : ModelRelationship.of
           ,arelle.ModelDtsObject.ModelResource : ModelResource.of
           ,arelle.ModelXbrl.ModelXbrl : ModelXbrl.of
            }

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


def mainFunHook(modelXbrl,**kwargs): #@UnusedVariable
        # occurs upon <?arelle-unit-test location="EdgarRenderer/Filing.py#mainFun" action="AssertionError"?>
    if "EdgarRenderer/Filing.py#mainFun" in modelXbrl.arelleUnitTests:
        action = modelXbrl.arelleUnitTests["EdgarRenderer/Filing.py#mainFun"]
        objectConstructor = __dict__[action]
        raise objectConstructor("EdgarRenderer/Filing.py#mainFun")




        

 
"""
gsed -r -n 's/.*((model[A-Z][a-zA-Z0-9_]*|fact|context|unit|qname|controller)\.[a-zA-Z0-9_]*[\.\[\(]?).*/\1/gp' *.py | sort -u

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
"""
"""
:mod:`EdgarRenderer.Brel`
~~~~~~~~~~~~~~~~~~~
Edgar(tm) Renderer was created by staff of the U.S. Securities and Exchange Commission.
Data and content created by government employees within the scope of their employment 
are not subject to domestic copyright protection. 17 U.S.C. 105.
"""
#from builtins import object
from collections import defaultdict
from builtins import list

"""
Brel: simple minded Abstract XBRL instance + DTS Interface
Initial Implementation via lxml + arelle
"""

""" BREL COMMON """
from typing import List, Final #@UnusedImport

class IModelObject:
        
    def __getattr__(self,name):
        try:
            return self.__dict__[name]
        except Exception as e:
            if '_realObject' in self.__dict__:
                _v = getattr(self._realObject,name)
                if hasattr(self,'props'): # collect key misses
                    self.props.add(name)
                # setattr(self,name,_v) # this screws up when name is a defined method
                return _v
            else:
                raise e

    def __del__(self):
        try:
            del self.proxy[self._realObject]
        except Exception:
            pass
    
    def __str__(self):
        return 'B!'+str(self._realObject)

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

class IModelInlineFact(IModelFact): # n.b.
    pass

def isModelInlineFact(o):
    return issubclass(type(o),IModelInlineFact)
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

###

class IModelRelationshipSet(IModelObject):
    pass

def isModelRelationshipSet(o):
    return issubclass(type(o),IModelRelationshipSet)

###

class IModelDimensionValue(IModelObject):
    pass

def isModelDimensionValue(o):
    return issubclass(type(o),IModelDimensionValue)

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
    proxy = {} # class variable containing universe of instances
    props = set() # class variable containing all properties used
    # set: {'id', 'endDatetime', 'startDatetime', 'iter', 'entityIdentifier', 'scenario', 'instantDatetime', 'segDimValues', 'isForeverPeriod', 'qnameDims'}
    @staticmethod
    def of(context): 
        assert isinstance(context,arelle.ModelInstanceObject.ModelContext)
        try: return ModelContext.proxy[context]
        except: return ModelContext(context)
        
    def __init__(self,context):
        assert isinstance(context,arelle.ModelInstanceObject.ModelContext)
        self.proxy[context] = self
        self._realObject = context
        for a in ['document','modelXbrl','qnameDims']:
            try:
                _value = getattr(context,a)
                setattr(self,a,getProxy(_value))
            except AttributeError:
                pass
        return

    
    @property
    def id(self):
        return self._realObject.id
    
    @property
    def isForeverPeriod(self):
        return self._realObject.isForeverPeriod
    
    @property
    def instantDatetime(self):
        return self._realObject.instantDatetime
    
    @property
    def startDatetime(self):
        return self._realObject.startDatetime
    
    @property
    def endDatetime(self):
        return self._realObject.endDatetime



class ModelConcept(IModelConcept):
    proxy = {} # class variable containing universe of instances
    props = set() # class variable containing all properties used
    # set: {'isMonetary', 'typeQname', 'label', 'type', 'isShares', 'isTextBlock'}
    @staticmethod
    def of(concept): 
        assert isinstance(concept,arelle.ModelDtsObject.ModelConcept)
        try: return ModelConcept.proxy[concept]
        except: return ModelConcept(concept)

    def __init__(self,concept):
        assert isinstance(concept,arelle.ModelDtsObject.ModelConcept)
        self.proxy[concept] = self 
        self._realObject = concept
        for a in ['type']:
            try:
                _value = getattr(concept,a)
                setattr(self,a,getProxy(_value))
            except AttributeError:
                pass

    def label(self,**kwargs):
        return self._realObject.label(**kwargs)
    
    @property
    def typeQname(self):
        return self._realObject.typeQname
    
    @property
    def id(self):
        return self._realObject.id



class ModelLink (IModelLink):
    proxy = {} # class variable containing universe of instances
    props = set() # class variable containing all properties used
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
    proxy = {} # class variable containing universe of instances
    props = set() # class variable containing all properties used
    @staticmethod
    def of(resource): 
        assert isinstance(resource,arelle.ModelDtsObject.ModelResource)
        try: return ModelResource.proxy[resource]
        except: return ModelResource(resource)
    def __init__(self,resource):
        assert isinstance(resource,arelle.ModelDtsObject.ModelResource)
        self.proxy[resource] = self
        self._realObject = resource
    pass

class ModelRelationship (IModelRelationship):
    proxy = {} # class variable containing universe of instances
    props = set() # class variable containing all properties used
    @staticmethod
    def of(relationship): 
        assert isinstance(relationship,arelle.ModelDtsObject.ModelRelationship)
        try: return ModelRelationship.proxy[relationship]
        except: return ModelRelationship(relationship)
    def __init__(self,relationship):
        assert isinstance(relationship,arelle.ModelDtsObject.ModelRelationship)
        self.proxy[relationship] = self
        self._realObject = relationship
        for a in ['toModelObject','fromModelObject']:
            try:
                _value = getattr(relationship,a)
                setattr(self,a,getProxy(_value))
            except AttributeError:
                pass

class ModelRelationshipSet (IModelRelationshipSet):
    proxy = {} # class variable containing universe of instances
    props = set() # class variable containing all properties used
    @staticmethod
    def of(relationshipSet): 
        assert isinstance(relationshipSet,arelle.ModelRelationshipSet.ModelRelationshipSet)
        try: return ModelRelationshipSet.proxy[relationshipSet]
        except: return ModelRelationshipSet(relationshipSet)
    def __init__(self,relationshipSet):
        assert isinstance(relationshipSet,arelle.ModelRelationshipSet.ModelRelationshipSet)
        self.proxy[relationshipSet] = self
        self._realObject = relationshipSet
        for a in ['rootConcepts','modelXbrl','modelRelationships','modelConceptRoots']:
            try:
                _value = getattr(relationshipSet,a)
                setattr(self,a,getProxy(_value))
            except AttributeError:
                pass

    def loadModelRelationshipsTo(self):
        self._realObject.loadModelRelationshipsTo()
    
    def loadModelRelationshipsFrom(self):
        self._realObject.loadModelRelationshipsFrom()
    
    @property
    def modelRelationshipsTo(self):
        try:
            return self._modelRelationshipsTo
        except AttributeError:
            self._modelRelationshipsTo = getProxy(self._realObject.modelRelationshipsTo)
            return self._modelRelationshipsTo
    
    @property
    def modelRelationshipsFrom(self):
        try: 
            return self._modelRelationshipsFrom
        except AttributeError:
            self._modelRelationshipsFrom = getProxy(self._realObject.modelRelationshipsFrom)
            return self._modelRelationshipsFrom
    
    @property
    def linkRoleUris(self) -> List[str]:
        return self._realObject.linkRoleUris

    def toModelObject(self,o) -> List[ModelObject]:
        dest = None
        try:
            dest = o._realObject
            result = getProxy(self._realObject.toModelObject(dest))
            return result
        except AttributeError as e:
            raise e
    
    def fromModelObject(self,o) -> List[ModelObject]:
        src = None
        try:
            src = o._realObject
            result = getProxy(self._realObject.fromModelObject(src))
            return result
        except AttributeError as e:
            raise e


class ModelType (IModelType):
    proxy = {} # class variable containing universe of instances
    props = set() # class variable containing all properties used
    @staticmethod
    def of(modelType): 
        assert isinstance(modelType,arelle.ModelDtsObject.ModelType)
        try: return ModelType.proxy[modelType]
        except: return ModelType(modelType)
    def __init__(self,modelType):
        assert isinstance(modelType,arelle.ModelDtsObject.ModelType)
        self.proxy[modelType] = self
        self._realObject = modelType
        for a in []:
            try:
                _value = getattr(modelType,a)
                setattr(self,a,getProxy(_value))
            except AttributeError:
                pass

class ModelUnit (IModelUnit):
    proxy = {} # class variable containing universe of instances
    props = set() # class variable containing all properties used
    # set: {'id', 'isSingleMeasure', 'measures', 'value', 'sourceline'}
    @staticmethod
    def of(unit): 
        assert isinstance(unit,arelle.ModelInstanceObject.ModelUnit)
        try: return ModelUnit.proxy[unit]
        except: return ModelUnit(unit)
    def __init__(self,unit):
        assert isinstance(unit,arelle.ModelInstanceObject.ModelUnit)
        self.proxy[unit] = self
        self._realObject = unit
        for a in []:
            try:
                _value = getattr(unit,a)
                setattr(self,a,getProxy(_value))
            except AttributeError:
                pass
    @property
    def id(self):
        return self._realObject.id
    


class ModelDocument (IModelDocument):
    proxy = {} # class variable containing universe of instances
    props = set() # class variable containing all properties used
    @staticmethod
    def of(document): 
        assert isinstance(document,arelle.ModelDocument.ModelDocument)
        try: return ModelDocument.proxy[document]
        except: return ModelDocument(document)
        
    def __init__(self,document):
        assert isinstance(document,arelle.ModelDocument.ModelDocument)
        self.proxy[document] = self
        self._realObject = document
        for a in ['modelXbrl','idObjects']:
            try:
                _value = getattr(document,a)
                setattr(self,a,getProxy(_value))
            except AttributeError:
                pass
    pass

class ModelDimensionValue (IModelDimensionValue):
    proxy = {} # class variable containing universe of instances
    props = set() # class variable containing all properties used
    @staticmethod
    def of(dimensionValue): 
        assert isinstance(dimensionValue,arelle.ModelInstanceObject.ModelDimensionValue)
        try: return ModelDimensionValue.proxy[dimensionValue]
        except: return ModelDimensionValue(dimensionValue)
        
    def __init__(self,dimensionValue):
        assert isinstance(dimensionValue,arelle.ModelInstanceObject.ModelDimensionValue)
        self.proxy[dimensionValue] = self
        self._realObject = dimensionValue
        for a in ['dimension','member']:
            try:
                _value = getattr(dimensionValue,a)
                setattr(self,a,getProxy(_value))
            except AttributeError:
                pass
    pass

class ModelFact(IModelFact):
    proxy = dict() # class variable
    props = set() # class variable
    # set: {'utrEntries', 'decimals', 'qname', 'document', 'xValid', 'isNil', 'unit', 'xmlLang', 'unitID', 'value', 'ancestorQnames', 'contextID', 'iter', 'iterancestors', 'isNumeric', 'xsiNil', 'modelXbrl'}
    @staticmethod
    def of(fact):
        if isinstance(fact,(arelle.ModelInstanceObject.ModelInlineFact)):
            return ModelInlineFact.of(fact)
        else:
            assert isinstance(fact,arelle.ModelInstanceObject.ModelFact)
            try:
                return ModelFact.proxy[fact]
            except KeyError:
                return ModelFact(fact)

    def __init__(self,fact):
        assert isinstance(fact,arelle.ModelInstanceObject.ModelFact)
        self.proxy[fact] = self
        self._realObject = fact
        for a in ['concept','context','unit']:
            try:
                _value = getattr(fact,a)
                setattr(self,a,getProxy(_value))
            except AttributeError:
                pass

    def anchorsInTextBlock(self):
        result = []
        for e in self.iter('*'): # for some reason iter('a') does not work.
            if e.localName=='a' and not 'href' in e.attrib and ('id' in e.attrib  or 'name' in e.attrib):
                atts = e.elementAttributesStr
                line = e.sourceLine
                result += [(atts,line)]
        return result
    
    def unitSymbol(self): # method must exist on the fact and access the utr if needed.
        """(str) -- utr symbol for this fact and unit"""
        if self.unit is not None and self.concept is not None:
            return self.unit._realObject.utrSymbol(self.concept._realObject.type)
        return ""
    
    @property
    def isNil(self):
        return self._realObject.isNil
    
    @property
    def isNumeric(self):
        return self._realObject.isNumeric
    
    @property
    def decimals(self):
        return self._realObject.decimals
    
    @property
    def xmlLang(self):
        return self._realObject.xmlLang
    
    @property
    def isTuple(self):
        return self._realObject.isTuple
    
    @property
    def contextId(self):
        return self._realObject.contextId
    
    @property
    def sourceline(self):
        return self._realObject.sourceline
    
    @property
    def qname(self):
        return self._realObject.qname
    
    @property
    def unitId(self):
        return self._realObject.unitId
    

class ModelInlineFact(IModelInlineFact):
    proxy = dict() # class variable
    props = set() # class variable
    @staticmethod
    def of(fact): 
        assert isinstance(fact,arelle.ModelInstanceObject.ModelInlineFact)
        try: return ModelInlineFact.proxy[fact]
        except: return ModelInlineFact(fact)
    
    def __init__(self,fact):
        assert isinstance(fact,arelle.ModelInstanceObject.ModelInlineFact)
        self.proxy[fact] = self
        self._realObject = fact
        self._realObject = fact
        for a in ['concept','context','unit']:
            try:
                _value = getattr(fact,a)
                setattr(self,a,getProxy(_value))
            except AttributeError:
                pass

class ModelXbrl(IModelXbrl): 
    proxy = {} # class variable
    props = set() # class variable
    
    """arelleUnitTests
    baseSets
    debug
    errors
    factsByQname
    fileSource
    labelroles
    langs
    matchSubstitutionGroup
    modelDocument
    modelManager
    modelObjects
    nameConcepts
    namespaceDocs
    profileActivity
    qnameConcepts
    relationshipSet
    relationshipSets
    roleTypes
    schemaDocsToValidate
    skipDTS
    units
    urlDocs
    urlUnloadableDocs"""

    @staticmethod
    def of(modelXbrl): 
        assert isinstance(modelXbrl,arelle.ModelXbrl.ModelXbrl)
        try: return ModelXbrl.proxy[modelXbrl]
        except: return ModelXbrl(modelXbrl)
    
    def __init__(self,modelXbrl):
        self.proxy[modelXbrl] = self
        self._realObject = modelXbrl
        for a in ['contexts','facts','factsByQname','qnameConcepts']:
            try:
                _value = getattr(modelXbrl,a)
                setattr(self,a,getProxy(_value))
            except AttributeError:
                pass

                        
    def relationshipSet(self, arcrole, linkrole=None, linkqname=None, arcqname=None, includeProhibits=False):
        # TODO: rewrite as iterator with a predicate filter instead of curious tokens like arcrole='XBRL-footnote'
        return ModelRelationshipSet.of(self._realObject.relationshipSet(
            arcrole
            ,linkrole=linkrole
            ,linkqname=linkqname
            ,arcqname=arcqname
            ,includeProhibits=includeProhibits))


# Constant
maker = {arelle.ModelInstanceObject.ModelFact : ModelFact.of
           ,arelle.ModelInstanceObject.ModelInlineFact : ModelInlineFact.of
           ,arelle.ModelInstanceObject.ModelContext : ModelContext.of
           ,arelle.ModelInstanceObject.ModelUnit : ModelUnit.of 
           ,arelle.ModelDtsObject.ModelConcept : ModelConcept.of
           ,arelle.ModelDtsObject.ModelType : ModelType.of
           ,arelle.ModelDtsObject.ModelLink : ModelLink.of
           ,arelle.ModelDtsObject.ModelRelationship : ModelRelationship.of
           ,arelle.ModelDtsObject.ModelResource : ModelResource.of
           ,arelle.ModelXbrl.ModelXbrl : ModelXbrl.of
           ,arelle.ModelDocument.ModelDocument : ModelDocument.of
           ,arelle.ModelInstanceObject.ModelDimensionValue : ModelDimensionValue.of
           ,str : (lambda x: x)
           ,int : (lambda x: x)
           ,float : (lambda x: x)
           ,arelle.ModelValue.QName : (lambda x : x)
           }

def getProxy(obj):
    result = obj
    try:
        result = maker[type(obj)](obj)
    except KeyError:
        if type(obj) in [list]:
            result = [getProxy(o) for o in obj]
        elif type(obj) in [defaultdict]:
            result = defaultdict(obj.default_factory,{getProxy(k) : getProxy(v) for k,v in obj.items()})
        elif type(obj) in [dict]:
            result = {getProxy(k) : getProxy(v) for k,v in obj.items()}
        elif type(obj) in [set]:
            result = {getProxy(o) for o in obj}
        elif obj == None:
            pass
        else: 
            raise "What is this? {} {}".format(type(obj),obj)
    return result

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
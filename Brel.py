"""
:mod:`EdgarRenderer.Brel`
~~~~~~~~~~~~~~~~~~~
Edgar(tm) Renderer was created by staff of the U.S. Securities and Exchange Commission.
Data and content created by government employees within the scope of their employment 
are not subject to domestic copyright protection. 17 U.S.C. 105.
"""
# from builtins import object
from collections import defaultdict
from builtins import list
from datetime import datetime
from re import sub

"""
Brel: simple minded Abstract XBRL instance + DTS Interface
Initial Implementation via lxml + arelle
"""

""" BREL COMMON """
from typing import Dict, List, Tuple, Generator, Any


class IModelObject:

    def __getattr__(self, name):
        try:
            return self.__dict__[name]
        except Exception as e:
            if 'realObject' in self.__dict__:
                _v = getattr(self.realObject, name)  # later we'll rename this _realObject
                if hasattr(self, '_props'):  # collect key misses
                    self._props.add(name)
                # setattr(self,name,_v) # this screws up when name is a defined method
                return _v
            else:
                raise e

    def __del__(self):
        try:
            del self._proxy[self.realObject]
        except Exception:
            pass

    def __str__(self):
        return 'B!' + str(self.realObject)


def isModelObject(o):
    return issubclass(type(o), IModelObject)
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
    return issubclass(type(o), IModelXbrl)
# ##


class IModelDocument(IModelObject):
    pass


def isModelDocument(o):
    return issubclass(type(o), IModelDocument)
# ##


class IModelUnit(IModelObject):
    pass


def isModelUnit(o):
    return issubclass(type(o), IModelUnit)
# ##


class IModelFact(IModelObject):
    pass


def isModelFact(o):
    return issubclass(type(o), IModelFact)
# ##


class IModelInlineFact(IModelFact):  # n.b.
    pass


def isModelInlineFact(o):
    return issubclass(type(o), IModelInlineFact)
# ##


class IModelContext(IModelObject):
    pass


def isModelContext(o):
    return issubclass(type(o), IModelContext)
# ##


class IModelConcept(IModelObject):
    pass


def isModelConcept(o):
    return issubclass(type(o), IModelConcept)
# ##


class IModelType(IModelObject):
    pass


def isModelType(o):
    return issubclass(type(o), IModelType)
# ##


class IModelLink(IModelObject):
    pass


def isModelLink(o):
    return issubclass(type(o), IModelLink)
# ##


class IModelResource(IModelObject):
    pass


def isModelResource(o):
    return issubclass(type(o), IModelResource)
# ##


class IModelRelationship(IModelObject):
    pass


def isModelRelationship(o):
    return issubclass(type(o), IModelRelationship)

# ##


class IModelRelationshipSet(IModelObject):
    pass


def isModelRelationshipSet(o):
    return issubclass(type(o), IModelRelationshipSet)

# ##


class IModelDimensionValue(IModelObject):
    pass


def isModelDimensionValue(o):
    return issubclass(type(o), IModelDimensionValue)


""" BREL IN LXML + ARELLE """

"""
replacements for lxml.etree
"""
import lxml

iterparse = lxml.etree.iterparse  # function
parse = lxml.etree.parse  # function
treeToString = lxml.etree.tostring  # function

Comment = lxml.etree.Comment  # factory
Element = lxml.etree.Element  # factory
LxmlError = lxml.etree.LxmlError  # exception class
HTML = lxml.etree.HTML  # function
QName = lxml.etree.QName  # wrapper function
SubElement = lxml.etree.SubElement  # factory
XSLT = lxml.etree.XSLT  # function
XSLTError = lxml.etree.XSLTError  # exception class

ElementDepthFirstIterator = lxml.etree.ElementDepthFirstIterator  # Element method

"""
replacements for arelle
"""
import arelle

UNVALIDATED = arelle.XmlValidate.UNVALIDATED
UNKNOWN = arelle.XmlValidate.UNKNOWN
INVALID = arelle.XmlValidate.INVALID
NONE = arelle.XmlValidate.NONE
VALID = arelle.XmlValidate.VALID
VALID_ID = arelle.XmlValidate.VALID_ID
VALID_NO_CONTENT = arelle.XmlValidate.VALID_NO_CONTENT 

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
cnXbrliIdentifier = "{" + xbrli + "}xbrli:identifier"

#  QNames
qnIXbrl11Hidden = arelle.XbrlConst.qnIXbrl11Hidden
qnXbrliIdentifier = arelle.ModelObject.qname(cnXbrliIdentifier)
qnLinkPresentationArc = arelle.XbrlConst.qnLinkPresentationArc
qnLinkPresentationLink = arelle.XbrlConst.qnLinkPresentationLink

"""
replacements for arelle.ModelDocument
"""

LoadingException = arelle.ModelDocument.LoadingException  # Exception
openFileSource = arelle.FileSource.openFileSource  # function


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
    """    
    """
    _proxy = {}  # class variable containing universe of instances
    _props = set()  # class variable containing all properties used

    @staticmethod
    def of(obj): 
        assert isinstance(obj, arelle.ModelObject.ModelObject)
        try: return ModelObject._proxy[obj]
        except: return ModelObject(obj)

    def __init__(self, obj):
        assert isinstance(obj, arelle.ModelObject.ModelObject)
        self._proxy[obj] = self
        self.realObject = obj
        for a in ['modelXbrl']:
            try:
                _value = getattr(obj, a)
                setattr(self, a, getProxy(_value))
            except AttributeError:
                pass

    def iter(self, *args, **kwargs) -> Generator[Any, None, None]:
        for _value in self.realObject.iter(*args, **kwargs):
            result = getProxy(_value)
            yield result

    def iterancestors(self, *args, **kwargs) -> Generator[Any, None, None]:
        for _value in self.realObject.iterancestors(*args, **kwargs):
            result = getProxy(_value)
            yield result

    def iterchildren(self, *args, **kwargs) -> Generator[Any, None, None]:
        for _value in self.realObject.iterchildren(*args, **kwargs):
            result = getProxy(_value)
            yield result

    @property
    def qname(self) -> QName:
        return self.realObject.qname

    @property
    def text(self) -> str:
        return self.realObject.text

    @property
    def tag(self) -> str:
        return self.realObject.tag

    @property
    def xValue(self) -> str:
        return self.realObject.xValue

    @property
    def localName(self) -> str:
        return self.realObject.localName

    @property
    def isValid(self) -> bool:
        try:
            return self._isValid
        except AttributeError:
            result = (VALID <= self.realObject.xValid)
            self._isValid = result
            return result

    @property
    def isValidOrValidID(self) -> bool:
        try:
            return self._isValidOrValidID
        except AttributeError:
            result = (VALID <= self.realObject.xValid < VALID_NO_CONTENT)
            self._isValidOrValidID = result
            return result

"""
replacements for arelle.ModelDts.*
"""


class ModelContext(IModelContext, ModelObject):
    """
    set: {'entityIdentifier', 'segDimValues', 'iter', 'scenario'}
    """
    _proxy = {}  # class variable containing universe of instances
    _props = set()  # class variable containing all properties used

    # set: {'iter','scenario', 'segDimValues'}
    @staticmethod
    def of(context): 
        assert isinstance(context, arelle.ModelInstanceObject.ModelContext)
        try: return ModelContext._proxy[context]
        except: return ModelContext(context)

    def __init__(self, context):
        assert isinstance(context, arelle.ModelInstanceObject.ModelContext)
        self._proxy[context] = self
        self.realObject = context
        for a in ['document', 'modelXbrl', 'qnameDims']:
            try:
                _value = getattr(context, a)
                setattr(self, a, getProxy(_value))
            except AttributeError:
                pass
        return

    @property
    def dimensionValues(self) -> Generator[IModelDimensionValue, None, None]:
        qnameDims = self.realObject.qnameDims
        for d in qnameDims.values():
            yield getProxy(d)

    @property
    def segDimValues(self) -> Dict[IModelConcept, IModelDimensionValue]:
        try: return self._segDimValues
        except AttributeError:
            result = getProxy(self.realObject.segDimValues)
            self._segDimValues = result
            return result

    @property
    def entityIdentifier(self) -> (str, str):
        return self.realObject.entityIdentifier

    @property
    def id(self) -> str:
        return self.realObject.id

    @property
    def isForeverPeriod(self) -> bool:
        return self.realObject.isForeverPeriod

    @property
    def isStartEndPeriod(self) -> bool:
        return self.realObject.isStartEndPeriod

    @property
    def isInstancePeriod(self) -> bool:
        return self.realObject.isStartEndPeriod

    @property
    def instantDatetime(self) -> datetime:
        return self.realObject.instantDatetime

    @property
    def startDatetime(self) -> datetime:
        return self.realObject.startDatetime

    @property
    def endDatetime(self) -> datetime:
        return self.realObject.endDatetime

    @property
    def scenario(self) -> ModelObject:
        return getProxy(self.realObject.scenario)


class ModelConcept(IModelConcept, ModelObject):
    _proxy = {}  # class variable containing universe of instances
    _props = set()  # class variable containing all properties used
    """
    """

    @staticmethod
    def of(concept): 
        assert isinstance(concept, arelle.ModelDtsObject.ModelConcept)
        try: return ModelConcept._proxy[concept]
        except: return ModelConcept(concept)

    def __init__(self, concept):
        assert isinstance(concept, arelle.ModelDtsObject.ModelConcept)
        self._proxy[concept] = self 
        self.realObject = concept
        for a in ['type']:
            try:
                _value = getattr(concept, a)
                setattr(self, a, getProxy(_value))
            except AttributeError:
                pass

    def label(self, **kwargs) -> str:
        return self.realObject.label(**kwargs)

    @property
    def name(self) -> str:
        return self.realObject.name

    @property
    def substitutionGroup(self) -> IModelConcept:
        result = self.realObject.substitutionGroup
        return result

    @property
    def typeQname(self) -> QName:
        return self.realObject.typeQname

    @property
    def id(self) -> str:
        return self.realObject.id

    @property
    def balance(self) -> str:
        result = self.realObject.balance
        return result

    @property
    def isTypedDimension(self) -> bool:
        result = self.realObject.isTypedDimension
        return result

    @property
    def isDimensionItem(self) -> bool:
        result = self.realObject.isDimensionItem
        return result

    @property
    def isTextBlock(self) -> bool:
        result = self.realObject.isTextBlock
        return result

    @property
    def isItem(self) -> bool:
        result = self.realObject.isItem
        return result

    @property
    def isAbstract(self) -> bool:
        result = self.realObject.isAbstract
        return result

    @property
    def isMonetary(self) -> bool:
        result = self.realObject.isMonetary
        return result

    @property
    def isShares(self) -> bool:
        result = self.realObject.isShares
        return result

    @property
    def modelXbrl(self) -> IModelXbrl:
        result = self.realObject.modelXbrl
        return result

    @property
    def baseXsdType(self) -> str:  # local name of base XML Schema type
        result = self.realObject.baseXsdType
        return result

    @property
    def periodType(self) -> str:  # instant or duration
        result = self.realObject.periodType
        return result

# ##


class ModelLink (IModelLink, ModelObject):
    _proxy = {}  # class variable containing universe of instances
    _props = set()  # class variable containing all properties used

    @staticmethod
    def of(link): 
        assert isinstance(link, arelle.ModelDtsObject.ModelLink)
        try: return ModelLink._proxy[link]
        except: return ModelLink(link)

    def __init__(self, link):
        assert isinstance(link, arelle.ModelDtsObject.ModelLink)
        self._proxy[link] = self
        self.realObject = link

###


class ModelResource (IModelResource, ModelObject):
    _proxy = {}  # class variable containing universe of instances
    _props = set()  # class variable containing all properties used
    """
    set: {'text', 'iterchildren', 'xmlLang', 'role'}
    """

    @staticmethod
    def of(resource): 
        assert isinstance(resource, arelle.ModelDtsObject.ModelResource)
        try: return ModelResource._proxy[resource]
        except: return ModelResource(resource)

    def __init__(self, resource):
        assert isinstance(resource, arelle.ModelDtsObject.ModelResource)
        self._proxy[resource] = self
        self.realObject = resource

    @property
    def xmlLang(self) -> str:
        result = self.realObject.xmlLang
        return result

    @property
    def role(self) -> str:
        result = self.realObject.role
        return result

    @property
    def text(self) -> str:
        result = self.realObject.text
        return result


class ModelRelationship (IModelRelationship, ModelObject):
    _proxy = {}  # class variable containing universe of instances
    _props = set()  # class variable containing all properties used
    """

    """

    @staticmethod
    def of(relationship): 
        assert isinstance(relationship, arelle.ModelDtsObject.ModelRelationship)
        try: return ModelRelationship._proxy[relationship]
        except: return ModelRelationship(relationship)

    def __init__(self, relationship):
        assert isinstance(relationship, arelle.ModelDtsObject.ModelRelationship)
        self._proxy[relationship] = self
        self.realObject = relationship
        for a in ['toModelObject', 'fromModelObject']:
            try:
                _value = getattr(relationship, a)
                setattr(self, a, getProxy(_value))
            except AttributeError:
                pass

    @property
    def linkrole(self) -> str:
        result = self.realObject.linkrole
        return result

    @property
    def order(self) -> float:
        result = self.realObject.linkrole
        return result

    @property
    def weight(self) -> float:
        result = self.realObject.weight
        return result

    @property
    def preferredLabel(self) -> str:  # The role of the preferred role, not the preferred label.
        result = self.realObject.preferredLabel
        return result

###

class ModelRelationshipSet (IModelRelationshipSet, ModelObject):
    _proxy = {}  # class variable containing universe of instances
    _props = set()  # class variable containing all properties used
    """
    set: set()
    """

    @staticmethod
    def of(relationshipSet): 
        assert isinstance(relationshipSet, arelle.ModelRelationshipSet.ModelRelationshipSet)
        try: return ModelRelationshipSet._proxy[relationshipSet]
        except: return ModelRelationshipSet(relationshipSet)

    def __init__(self, relationshipSet):
        assert isinstance(relationshipSet, arelle.ModelRelationshipSet.ModelRelationshipSet)
        self._proxy[relationshipSet] = self
        self.realObject = relationshipSet
        for a in ['rootConcepts', 'modelXbrl', 'modelRelationships', 'modelConceptRoots']:
            try:
                _value = getattr(relationshipSet, a)
                setattr(self, a, getProxy(_value))
            except AttributeError:
                pass

    def loadModelRelationshipsTo(self):
        self.realObject.loadModelRelationshipsTo()

    def loadModelRelationshipsFrom(self):
        self.realObject.loadModelRelationshipsFrom()

    @property
    def modelRelationshipsTo(self):
        try:
            return self._modelRelationshipsTo
        except AttributeError:
            self._modelRelationshipsTo = getProxy(self.realObject.modelRelationshipsTo)
            return self._modelRelationshipsTo

    @property
    def modelRelationshipsFrom(self):
        try: 
            return self._modelRelationshipsFrom
        except AttributeError:
            self._modelRelationshipsFrom = getProxy(self.realObject.modelRelationshipsFrom)
            return self._modelRelationshipsFrom

    @property
    def linkRoleUris(self) -> List[str]:
        return self.realObject.linkRoleUris

    def toModelObject(self, o) -> List[ModelObject]:
        dest = None
        try:
            dest = o.realObject
            result = getProxy(self.realObject.toModelObject(dest))
            return result
        except AttributeError as e:
            raise e

    def fromModelObject(self, o) -> List[ModelObject]:
        src = None
        try:
            src = o.realObject
            result = getProxy(self.realObject.fromModelObject(src))
            return result
        except AttributeError as e:
            raise e

###

class ModelType (IModelType, ModelObject):
    _proxy = {}  # class variable containing universe of instances
    _props = set()  # class variable containing all properties used
    """set: {'name'}"""

    @staticmethod
    def of(modelType): 
        assert isinstance(modelType, arelle.ModelDtsObject.ModelType)
        try: return ModelType._proxy[modelType]
        except: return ModelType(modelType)

    def __init__(self, modelType):
        assert isinstance(modelType, arelle.ModelDtsObject.ModelType)
        self._proxy[modelType] = self
        self.realObject = modelType
        for a in []:
            try:
                _value = getattr(modelType, a)
                setattr(self, a, getProxy(_value))
            except AttributeError:
                pass

    @property
    def name(self) -> str:
        result = self.realObject.name
        return result

###

class ModelUnit (IModelUnit, ModelObject):
    _proxy = {}  # class variable containing universe of instances
    _props = set()  # class variable containing all properties used
    """
    set: {'value', 'sourceline', 'measures', 'isSingleMeasure'}
    """

    @staticmethod
    def of(unit): 
        assert isinstance(unit, arelle.ModelInstanceObject.ModelUnit)
        try: return ModelUnit._proxy[unit]
        except: return ModelUnit(unit)

    def __init__(self, unit):
        assert isinstance(unit, arelle.ModelInstanceObject.ModelUnit)
        self._proxy[unit] = self
        self.realObject = unit
        for a in []:
            try:
                _value = getattr(unit, a)
                setattr(self, a, getProxy(_value))
            except AttributeError:
                pass

    @property
    def id(self) -> str:
        return self.realObject.id

    @property
    def sourceline(self) -> int:
        result = self.realObject.sourceline
        return result

    @property
    def isSingleMeasure(self) -> bool:
        return self.realObject.isSingleMeasure

    @property
    def measures(self) -> (List[QName], List[QName]):
        return self.realObject.measures

    @property
    def value(self) -> str:
        result = self.realObject.value
        return result

###

class ModelDocument (IModelDocument, ModelObject):
    _proxy = {}  # class variable containing universe of instances
    _props = set()  # class variable containing all properties used
    """
    """

    @staticmethod
    def of(document): 
        assert isinstance(document, arelle.ModelDocument.ModelDocument)
        try: return ModelDocument._proxy[document]
        except: return ModelDocument(document)

    def __init__(self, document):
        assert isinstance(document, arelle.ModelDocument.ModelDocument)
        self._proxy[document] = self
        self.realObject = document
        for a in ['modelXbrl', 'idObjects']:
            try:
                _value = getattr(document, a)
                setattr(self, a, getProxy(_value))
            except AttributeError:
                pass

    @property
    def targetDocumentPreferredFilename(self) -> str:
        result =self.realObject.targetDocumentPreferredFilename
        return result

    @property
    def targetDocumentSchemaRefs(self) -> {str}:
        result = self.realObject.targetDocumentSchemaRefs
        return result

    @property
    def basename(self) -> str:
        result = self.realObject.basename
        return result

    def type(self) -> Type:
        result = self.realObject.type
        return result

###
###

class ModelDimensionValue (IModelDimensionValue, ModelObject):
    _proxy = {}  # class variable containing universe of instances
    _props = set()  # class variable containing all properties used
    """
    set: {'memberQname'}
    """

    @staticmethod
    def of(dimensionValue): 
        assert isinstance(dimensionValue, arelle.ModelInstanceObject.ModelDimensionValue)
        try: return ModelDimensionValue._proxy[dimensionValue]
        except: return ModelDimensionValue(dimensionValue)

    def __init__(self, dimensionValue):
        assert isinstance(dimensionValue, arelle.ModelInstanceObject.ModelDimensionValue)
        self._proxy[dimensionValue] = self
        self.realObject = dimensionValue
        for a in ['dimension', 'member']:
            try:
                _value = getattr(dimensionValue, a)
                setattr(self, a, getProxy(_value))
            except AttributeError:
                pass

    @property
    def isTyped(self):
        return self.realObject.isTyped

    @property
    def isExplicit(self):
        return self.realObject.isExplicit

    @property
    def typedMember(self):
        try:
            return self._typedMember
        except AttributeError:
            _v = self.realObject.typedMember
            result = getProxy(_v)
            self._typedMember = result
            return result

    @property
    def memberQname(self):
        if not self.isExplicit:
            Exception("error",_("{} is not an explicit dimension").format(self))
        return self.member.realObject.qname

    @property
    def dimensionQname(self):
        return self.dimension.realObject.qname

###

class ModelFact(IModelFact, ModelObject):
    _proxy = dict()  # class variable
    _props = set()  # class variable
    """
    {'contextID', 'text', 'utrEntries', 'ancestorQnames'}
    """

    @staticmethod
    def of(fact):
        if isinstance(fact, (arelle.ModelInstanceObject.ModelInlineFact)):
            return ModelInlineFact.of(fact)
        else:
            assert isinstance(fact, arelle.ModelInstanceObject.ModelFact)
            try:
                return ModelFact._proxy[fact]
            except KeyError:
                return ModelFact(fact)

    def __init__(self, fact):
        assert isinstance(fact, arelle.ModelInstanceObject.ModelFact)
        self._proxy[fact] = self
        self.realObject = fact
        for a in ['concept', 'context', 'unit']:
            try:
                _value = getattr(fact, a)
                setattr(self, a, getProxy(_value))
            except AttributeError:
                pass

    @property
    def ancestorQnames(self) -> Generator[QName, None, None]:
        for q in self.realObject.ancestorQnames:
            yield q

    @property
    def utrEntries(self) -> Generator[Any, None, None]:
        for utrEntry in self.realObject.utrEntries:
            yield utrEntry

    def anchorsInTextBlock(self) -> Generator[Tuple[str, int], None, None]:
        tree = None
        try:
            s = sub(">[^<]+<", "><", self.text)
            s = sub(".[a-z]+=\"[^\"]*\"", "", s)
            s = sub(".[a-z]+=\'[^\']*'", "", s)
            tree = lxml.etree.fromstring(s)
        except:
            return 
        for e in tree.iter(tag='a'):
            if not 'href' in e.attrib and ('id' in e.attrib  or 'name' in e.attrib):
                atts = e.elementAttributesStr
                line = e.sourceLine
                yield (atts, line)

    def unitSymbol(self) -> str:  # method must exist on the fact and access the utr if needed.
        """(str) -- utr symbol for this fact and unit"""
        if self.unit is not None and self.concept is not None:
            return self.unit.realObject.utrSymbol(self.concept.realObject.type)
        return ""

    @property
    def document(self) -> IModelDocument:
        return self.realObject.document

    @property
    def modelXbrl(self) -> IModelXbrl:
        return self.realObject.modelXbrl

    @property
    def xsiNil(self) -> str:
        return self.realObject.xsiNil

    @property
    def isNil(self) -> bool:
        return self.realObject.isNil

    @property
    def isNumeric(self) -> bool:
        return self.realObject.isNumeric

    @property
    def decimals(self):
        return self.realObject.decimals

    @property
    def xmlLang(self) -> str:
        return self.realObject.xmlLang

    @property
    def isTuple(self) -> bool:
        return self.realObject.isTuple

    @property
    def contextID(self) -> str:
        return self.realObject.contextID

    @property
    def sourceline(self) -> int:
        return self.realObject.sourceline

    @property
    def unitID(self) -> str:
        return self.realObject.unitID

    @property
    def text(self) -> str:
        return self.realObject.text

    @property
    def value(self):
        return self.realObject.value


###

class ModelInlineFact(IModelInlineFact, ModelFact):
    _proxy = dict()  # class variable
    _props = set()  # class variable
    """set()"""

    @staticmethod
    def of(fact): 
        assert isinstance(fact, arelle.ModelInstanceObject.ModelInlineFact)
        try: return ModelInlineFact._proxy[fact]
        except: return ModelInlineFact(fact)

    def __init__(self, fact):
        assert isinstance(fact, arelle.ModelInstanceObject.ModelInlineFact)
        self._proxy[fact] = self
        self.realObject = fact
        self.realObject = fact
        for a in ['concept', 'context', 'unit']:
            try:
                _value = getattr(fact, a)
                setattr(self, a, getProxy(_value))
            except AttributeError:
                pass

    @property
    def contextID(self) -> str:
        result = self.realObject.contextID
        assert type(result) == str
        return result

    @property
    def unitID(self) -> str:
        result = self.realObject.unitID
        assert type(result) == str
        return result

###

class ModelXbrl(IModelXbrl, ModelObject): 
    _proxy = {}  # class variable
    _props = set()  # class variable

    """set: {'labelroles', 'langs', 'urlUnloadableDocs', 'nameConcepts', 'roleTypes', 'schemaDocsToValidate', 'errors', 'arelleUnitTests', 'baseSets', 'units', 'matchSubstitutionGroup', 'skipDTS', 'debug', 'modelObjects', 'modelManager', 'urlDocs', 'fileSource', 'profileActivity', 'namespaceDocs', 'relationshipSets', 'modelDocument'}"""

    @staticmethod
    def of(modelXbrl): 
        assert isinstance(modelXbrl, arelle.ModelXbrl.ModelXbrl)
        try: return ModelXbrl._proxy[modelXbrl]
        except: return ModelXbrl(modelXbrl)

    def __init__(self, modelXbrl):
        self._proxy[modelXbrl] = self
        self.realObject = modelXbrl
        for a in ['contexts', 'facts', 'factsByQname', 'nameConcepts', 'qnameConcepts','modelDocument']:
            try:
                _value = getattr(modelXbrl, a)
                setattr(self, a, getProxy(_value))
            except AttributeError:
                pass

    @property
    def units(self) -> Generator[str, None, None]:
        for u in self.realObject.units:
            yield u

    def relationshipSet(self, arcrole, linkrole=None, linkqname=None, arcqname=None, includeProhibits=False):
        # TODO: rewrite as iterator with a predicate filter instead of curious tokens like arcrole='XBRL-footnote'
        return ModelRelationshipSet.of(self.realObject.relationshipSet(
            arcrole
            , linkrole=linkrole
            , linkqname=linkqname
            , arcqname=arcqname
            , includeProhibits=includeProhibits))

    @property
    def relationshipSets(self) -> Dict[Tuple[str],ModelRelationshipSet]:        
        _value = self.realObject.relationshipSets
        result = {k : getProxy(v) for k,v in _value.items()}
        return result

    @property
    def xValue(self):
        return None

    def load(self,uri,**kwargs) -> None:
        return arelle.ModelDocument.load(self.realObject,uri,**kwargs)

    @property
    def namespaces(self) -> Generator[str, None, None]:
        namespaceSet = None 
        try:
            namespaceSet = self._namespaceSet
        except AttributeError:
            namespaceSet = {k for k in self.realObject.namespaceDocs.keys()}
        for namespace in namespaceSet:
            yield namespace

    @property
    def fileSource(self) -> arelle.FileSource.FileSource:
        result = self.realObject.fileSource
        assert type(result) == arelle.FileSource.FileSource
        return result

    def profileActivity(self,**kwargs):
        self.realObject.profileActivity(**kwargs)

    @property
    def errors(self) -> List[Any]:
        result = self.realObject.errors
        assert type(result) == list
        return result

    @property
    def urlDocs(self) -> Dict[str, ModelDocument]:
        result = self.realObject.urlDocs
        assert type(result) == dict
        return result

    @property
    def roleTypes(self) -> Dict[str, List[ModelObject]]:
        result = self.realObject.roleTypes
        assert type(result) == dict
        return result

    @property
    def modelManager(self) -> Any:
        result = self.realObject.modelManager
        assert type(result) == arelle.ModelManager.ModelManager
        return result

    @property
    def arelleUnitTests(self) -> Dict[str,str]:
        result = self.realObject.arelleUnitTests
        assert type(result) == dict
        return result

    def trace(self, codes, msg, **args) -> None:
        self.realObject.trace(codes,msg,**args)

    def debug(self, codes, msg, **args) -> None:
        self.realObject.debug(codes,msg,**args)

    def info(self, codes, msg, **args) -> None:
        self.realObject.info(codes,msg,**args)        

    def warn(self, codes, msg, **args) -> None:
        self.realObject.warn(codes,msg,**args)

    def error(self, codes, msg, **args) -> None:
        self.realObject.error(codes,msg,**args)




def identity(x):
    return x

# Constant
maker = {arelle.ModelInstanceObject.ModelFact : ModelFact.of
           , arelle.ModelInstanceObject.ModelInlineFact : ModelInlineFact.of
           , arelle.ModelInstanceObject.ModelContext : ModelContext.of
           , arelle.ModelInstanceObject.ModelUnit : ModelUnit.of 
           , arelle.ModelDtsObject.ModelConcept : ModelConcept.of
           , arelle.ModelDtsObject.ModelType : ModelType.of
           , arelle.ModelDtsObject.ModelLink : ModelLink.of
           , arelle.ModelDtsObject.ModelRelationship : ModelRelationship.of
           , arelle.ModelRelationshipSet.ModelRelationshipSet : ModelRelationshipSet.of
           , arelle.ModelDtsObject.ModelResource : ModelResource.of
           , arelle.ModelXbrl.ModelXbrl : ModelXbrl.of
           , arelle.ModelDocument.ModelDocument : ModelDocument.of
           , arelle.ModelInstanceObject.ModelDimensionValue : ModelDimensionValue.of
           , arelle.ModelObject.ModelObject : ModelObject.of
           , arelle.ModelValue.QName : identity
           , str : identity
           , int : identity
           , float : identity
           , list : (lambda obj: [getProxy(o) for o in obj])
           , defaultdict : (lambda obj: defaultdict(obj.default_factory, {getProxy(k) : getProxy(v) for k, v in obj.items()}))
           , dict : (lambda obj: {getProxy(k) : getProxy(v) for k, v in obj.items()})
           , set : (lambda obj: {getProxy(o) for o in obj})
           }


def getProxy(obj):
    result = obj
    try:
        result = maker[type(obj)](obj)
    except KeyError:
        if obj == None:
            pass
        else: 
            raise Exception("error", "Cannot get proxy for {} {}".format(type(obj), obj))
    return result


def isDimensionItem(o) -> bool:
    return isinstance(o, arelle.ModelDtsObject.ModelConcept) and o.isDimensionItem

"""
replacements for arelle.ModelValue
"""


def isQName (o) -> bool:
    return isinstance(o, arelle.ModelValue.QName)


class QName (arelle.ModelValue.QName):
    pass


def isIsoDuration (o) -> bool:
    return isinstance(o, arelle.ModelValue.IsoDuration)


class IsoDuration (arelle.ModelValue.IsoDuration):
    pass


qname = arelle.ModelValue.qname  # function

"""
Miscellaneous replacements
"""


class Cntlr (arelle.Cntlr.Cntlr):
    pass


referencedFiles = arelle.ValidateFilingText.referencedFiles  # function

collapseWhitespace = arelle.XmlUtil.collapseWhitespace  # function
descendantAttr = arelle.XmlUtil.descendantAttr  # function

VALID = arelle.XmlValidate.VALID  # enum int
VALID_NO_CONTENT = arelle.XmlValidate.VALID_NO_CONTENT  # enum int


def mainFunHook(modelXbrl, **ignore): 
    # occurs upon <?arelle-unit-test location="EdgarRenderer/Filing.py#mainFun" action="AssertionError"?>
    if "EdgarRenderer/Filing.py#mainFun" in modelXbrl.arelleUnitTests:
        action = modelXbrl.arelleUnitTests["EdgarRenderer/Filing.py#mainFun"]
        objectConstructor = getattr(modelXbrl,action,eval(action))
        raise objectConstructor("EdgarRenderer/Filing.py#mainFun")

"""
"ModelDocument {'type', 'basename'}",
 "ModelObject {'get'}",
 "ModelXbrl {'profileActivity', 'modelManager', 'relationshipSets', 'errors', 'arelleUnitTests',
 'debug', 'roleTypes', 'fileSource', 'namespaceDocs', 'urlDocs'}"]
 
 """

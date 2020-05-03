# eXtensible Markup Language

>**Clone the repository: [Click Here](https://github.com/ahnafpie/Working-with-web-data-.xml-in-python3.git)**


### XML Basic Element

* **Start Tag**
* **End Tag**
* **Text Content**
* **Attribute**
* **Self Closing Tag**

**Example of the XML element:**
```xml
<person>
    <name>Chuck</name>
    <phone type='intl'>
    0123456789
    </phone>
    <email hide='yes'/>
</person>
```
### XML Terminology

* ***Tags*** indicate the beginning and ending of elements.
* ***Attributes*** Keyword/value pairs on the opening tag of XML.
* ***Serialize / De-Serialize*** Converting data into a common format that can be stored/transsmitted between systems in a programming language-independent manner.

### XML Schema

* Description of the *'legal'* format of an **XML** document.
* Expressed in terms of constraints on the structure and content of documents
* Often used to specify a *'Contract'* between systems - "My system will only accept XML that conforms to this particular Schema."
* If a particular piece of XML meets the specification of the Schema - it is said to *'validate'*

### XML Scema Languages

* **Document Type Definition (DTD)**
* **Standard Generalized Markup Language (ISO 8879:1986 SGML)**
* **XML Schema from W3C-(XSD)**

>We will focus on the XSD

### XSD Structure

```xsd
xs:element
xs:sequence
xs:complexType
```

### XSD Data Types

```xsd
xs:string
xs:date
xs:dateTime
xs:decimal
xs: integer
```

### Schema Example:


### **XML: **
```xml
<?xml version="1.0" encoding="UTF-8"?>

<shiporder orderid="889923"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:noNamespaceSchemaLocation="shiporder.xsd">
  <orderperson>John Smith</orderperson>
  <shipto>
    <name>Ola Nordmann</name>
    <address>Langgt 23</address>
    <city>4000 Stavanger</city>
    <country>Norway</country>
  </shipto>
  <item>
    <title>Empire Burlesque</title>
    <note>Special Edition</note>
    <quantity>1</quantity>
    <price>10.90</price>
  </item>
  <item>
    <title>Hide your heart</title>
    <quantity>1</quantity>
    <price>9.90</price>
  </item>
</shiporder>

```

### **Schema: **
```xsd
<?xml version="1.0" encoding="UTF-8" ?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

<xs:simpleType name="stringtype">
  <xs:restriction base="xs:string"/>
</xs:simpleType>

<xs:simpleType name="inttype">
  <xs:restriction base="xs:positiveInteger"/>
</xs:simpleType>

<xs:simpleType name="dectype">
  <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="orderidtype">
  <xs:restriction base="xs:string">
    <xs:pattern value="[0-9]{6}"/>
  </xs:restriction>
</xs:simpleType>

<xs:complexType name="shiptotype">
  <xs:sequence>
    <xs:element name="name" type="stringtype"/>
    <xs:element name="address" type="stringtype"/>
    <xs:element name="city" type="stringtype"/>
    <xs:element name="country" type="stringtype"/>
  </xs:sequence>
</xs:complexType>

<xs:complexType name="itemtype">
  <xs:sequence>
    <xs:element name="title" type="stringtype"/>
    <xs:element name="note" type="stringtype" minOccurs="0"/>
    <xs:element name="quantity" type="inttype"/>
    <xs:element name="price" type="dectype"/>
  </xs:sequence>
</xs:complexType>

<xs:complexType name="shipordertype">
  <xs:sequence>
    <xs:element name="orderperson" type="stringtype"/>
    <xs:element name="shipto" type="shiptotype"/>
    <xs:element name="item" maxOccurs="unbounded" type="itemtype"/>
  </xs:sequence>
  <xs:attribute name="orderid" type="orderidtype" use="required"/>
</xs:complexType>

<xs:element name="shiporder" type="shipordertype"/>

</xs:schema>
```
>The restriction element indicates that the datatype is derived from a W3C XML Schema namespace datatype. So, the following fragment means that the value of the element or attribute must be a string value:
```xsd
<xs:restriction base="xs:string">
```
>The restriction element is more often used to apply restrictions to elements. Look at the following lines from the schema above:

```xsd
<xs:simpleType name="orderidtype">
  <xs:restriction base="xs:string">
    <xs:pattern value="[0-9]{6}"/>
  </xs:restriction>
</xs:simpleType>
```
>This indicates that the value of the element or attribute must be a string, it must be exactly six characters in a row, and those characters must be a number from 0 to 9.



# Parsing XML

>**Get Exercise Code with Result: [Click Here](https://github.com/ahnafpie/Working-with-web-data-.xml-in-python3/blob/master/exercise_xml.ipynb)**

>**Get Assignment: [Click Here](https://github.com/ahnafpie/Working-with-web-data-.xml-in-python3/blob/master/Assignment_xml.ipynb)**

>**Get Py3 file: [Click Here](https://github.com/ahnafpie/Working-with-web-data-.xml-in-python3/commit/def54ddc8cc53254074f84fc78790163c83d0ad6)**

Here is a simple application that parses some XML and extracts some data elements
from the XML:

```python3
import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
```
Using an XML parser such as ElementTree has the advantage that while the XML in this example is quite simple, it turns out there are many rules regarding valid XML, and using ```ElementTree``` allows us to extract data from XML without worrying about the rules of XML syntax.

### Looping through nodes:

Often the XML has multiple nodes and we need to write a loop to process all of
the nodes. In the following program, we loop through all of the user nodes:
```python3
import xml.etree.ElementTree as ET


input = '''
<stuff>
<users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>
            </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
```

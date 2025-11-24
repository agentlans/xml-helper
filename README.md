# XML Helper

```python
from xml_helper import (
    XMLValidator,
    extract_xml,
    xml_wrap,
    xml_unwrap,
)

# 1. Extract XML from a markdown-style message
message = """
```xml
<note><msg>Hello!</msg></note>
```"""
xml_content = extract_xml(message)
print("Extracted XML:", xml_content)

# 2. Validate the extracted XML against an XSD schema
validator = XMLValidator("schema.xsd")
if validator.validate(xml_content):
    print("XML is valid!")
else:
    print("XML is NOT valid.")

# 3. Wrap plain text in XML
wrapped = xml_wrap("Hello World", "message")
print("Wrapped XML:", wrapped)

# 4. Unwrap XML back to plain text
text = xml_unwrap(wrapped, tag="message")
print("Unwrapped text:", text)
```

### Output (example)

```
Extracted XML: <note><msg>Hello!</msg></note>
XML is valid!
Wrapped XML: <message>Hello World</message>
Unwrapped text: Hello World
```

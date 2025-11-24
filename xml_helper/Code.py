import re
from lxml import etree
import xml.etree.ElementTree as ET

class XMLValidator:
    """Validate XML strings using an XSD schema."""

    def __init__(self, xsd_path: str):
        self.schema = self._load_schema(xsd_path)

    def _load_schema(self, path: str) -> etree.XMLSchema:
        try:
            with open(path, "rb") as f:
                schema_doc = etree.parse(f)
            return etree.XMLSchema(schema_doc)
        except Exception as e:
            raise RuntimeError(f"Failed to load XSD '{path}': {e}")

    def validate(self, xml: str) -> bool:
        if not xml.strip():
            return False
        try:
            doc = etree.fromstring(xml.encode("utf-8"))
            self.schema.assertValid(doc)
            return True
        except (etree.DocumentInvalid, etree.XMLSyntaxError):
            return False


_XML_BLOCK_REGEX = re.compile(
    r"```(?:xml)?\s*\n(.*?)\n```",
    re.DOTALL | re.IGNORECASE
)

def extract_xml(text: str) -> str:
    """Extract XML from a fenced code block."""
    match = _XML_BLOCK_REGEX.search(text)
    return match.group(1).strip() if match else text

def xml_wrap(text: str, tag: str) -> str:
    """Wrap plain text in a simple XML element."""
    root = ET.Element(tag)
    root.text = text or ""
    return ET.tostring(root, encoding="unicode")

def xml_unwrap(xml: str, tag: str | None = None) -> str:
    """Extract text from a single-element XML wrapper."""
    try:
        root = ET.fromstring(xml)
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML: {e}")

    if tag and root.tag != tag:
        raise ValueError(f"Expected <{tag}>, got <{root.tag}>")

    if list(root):
        raise ValueError("XML contains nested elements, expected pure text.")

    return root.text or ""


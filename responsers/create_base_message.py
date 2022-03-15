import xml.etree.ElementTree as ET

def provide_ribs():
    root = ET.Element('Envelope')
    bod = ET.SubElement(root,'Body')
    return root, bod

def create_full(root):
    return bytes.decode(ET.tostring(root), 'utf-8')
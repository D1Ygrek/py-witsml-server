import xml.etree.ElementTree as ET

from .create_base_message import provide_ribs, create_full

def return_from_store(param):
    envelop, body = provide_ribs()
    res = ET.SubElement(body,'Result')
    res.text = '1'
    return create_full(envelop)
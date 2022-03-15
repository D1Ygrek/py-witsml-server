import xml.etree.ElementTree as ET

def what_do_you_need(asked_xml):
    print(asked_xml)
    root = ET.fromstring(asked_xml)
    el = root.find('{http://schemas.xmlsoap.org/soap/envelope/}Body')
    for funcTag in el:
        #print(f'<----{funcTag.tag}---->')
        return(funcTag.tag.split('WMLS_')[-1],funcTag)

    
    #for child in root:
    #    print(child.tag.split('}')[-1] == 'Body')
    #    print(child.tag.split('}')[-1])
    #    print(child.tag)
        
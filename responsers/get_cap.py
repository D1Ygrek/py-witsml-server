import xml.etree.ElementTree as ET

from .create_base_message import provide_ribs, create_full

capServerData = """
<capServers xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.4.1">
    <capServer apiVers="1.4.1">
        <contact>
            <name>Customer Support North America</name>
            <email>rto@halliburton.com</email>
            <phone>1-877-263-6071</phone>
        </contact>
        <description>RTS WITSML Server</description>
        <name>RTS WITSML</name>
        <vendor>Halliburton</vendor>
        <version>13.0</version>
        <schemaVersion>1.4.1.1</schemaVersion>
        <changeDetectionPeriod>60</changeDetectionPeriod>
        <growingTimeoutPeriod dataObject="log">3600</growingTimeoutPeriod>
        <growingTimeoutPeriod dataObject="trajectory">3600</growingTimeoutPeriod>
        <growingTimeoutPeriod dataObject="mudLog">3600</growingTimeoutPeriod>
        <maxRequestLatestValues>500</maxRequestLatestValues>
        <cascadedDelete>false</cascadedDelete>
        <supportUomConversion>false</supportUomConversion>
        <compressionMethod>gzip</compressionMethod>
        <function name="WMLS_GetCap">
            <dataObject>capServer</dataObject>
        </function>
        <function name="WMLS_GetVersion"/>
        <function name="WMLS_GetBaseMsg"/>
        <function name="WMLS_GetFromStore">
            dataObject>well</dataObject>
            <dataObject>wellbore</dataObject>
            <dataObject maxDataNodes="10000" maxDataPoints="3000000">trajectory</dataObject>
            <dataObject maxDataNodes="10000" maxDataPoints="3000000">log</dataObject>
            <dataObject maxDataNodes="10000" maxDataPoints="3000000">mudLog</dataObject>
            <dataObject>tubular</dataObject>
            <dataObject>bhaRun</dataObject>
            <dataObject>changeLog</dataObject>
            <dataObject>fluidsReport</dataObject>
            <dataObject>wbGeometry</dataObject>
            <dataObject>formationMarker</dataObject>
            <dataObject>rig</dataObject>
        </function>
    </capServer>
</capServers>
"""

def return_cap(params):
    root, bod = provide_ribs()
    gcr = ET.SubElement(bod, 'WMLS_GetCapResponse')
    res = ET.SubElement(gcr, 'Result')
    co = ET.SubElement(gcr,'CapabilitiesOut')
    smo = ET.SubElement(gcr, 'SuppMsgOut')
    res.text = '1'
    co.text = capServerData
    return create_full(root)

    
def return_version(params):
    #print(params)
    data = """<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
                    xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
                    xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" 
                    xmlns:tns="http://www.witsml.org/wsdl/120" 
                    xmlns:types="http://www.witsml.org/wsdl/120/encodedTypes" 
                    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                    <soap:Body soap:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
                        <q2:WMLS_GetVersionResponse xmlns:q2="http://www.witsml.org/message/120">
                          <Result xsi:type="xsd:string">1.4.1.1</Result>
                        </q2:WMLS_GetVersionResponse>
                    </soap:Body>
                </soap:Envelope>
    """
    return data
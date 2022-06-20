import xml.etree.ElementTree as ET

data = """
<person>
    <name>Kevin</name>
    <phone type>"intl">
        +1 123 456 7890
    </phone>
    <email hide="yes/>
</person>
"""

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))



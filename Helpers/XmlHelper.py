import xml.etree.ElementTree as ET


class XmlHelper(object):
    """helps in doing xml parsing"""

    def get_xml_file(self, path, child_index=None):
        ''' 
           int child index , int grand child index, int great grand child index
        '''
        tree = ET.parse(path)
        print(type(tree))
        root = tree.getroot()
        if child_index is None:
            return root
        else:
            return root[child_index]

    def extract_xml_root(self, root, return_parent=False):
        for child in root:
            if return_parent is True:
                return child
            print(child.tag, child.attrib)

    def update_xml(self, root, key, value):
        for child in root.iter(key):
            child.text = str(value)
            print("Updated value = " + child.text)

    def convert_xml_to_string(self, root):
        return ET.tostring(root, encoding='utf-8', method='xml')

    def convert_to_xml_from_string(self, str_value):
        return ET.fromstring(str_value)

    def get_element_value(self, root, element_name):
        child_element_values = list()
        for child in root.iter(element_name):
            child_element_values.append(child.text)
        return child_element_values

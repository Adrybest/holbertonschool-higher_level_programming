#!/usr/bin/env python3
"""Serialization and deserialization using XML as an alternative format to JSON"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file"""
    root_element = ET.Element("data")

    for i, j in dictionary.items():
        child_element = ET.SubElement(root_element, i)
        child_element.text = str(j)

    tree = ET.ElementTree(root_element)

    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize data from an XML file"""
    tree = ET.parse(filename)
    root_element = tree.getroot()

    dictio = {}

    for child in root_element:
        dictio[child.tag] = child.text

    return dictio

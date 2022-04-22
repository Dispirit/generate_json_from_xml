#!/usr/bin/env python

import json
import xml.etree.ElementTree as ET
import sys


def get_version(file_xml) -> None:
    root = ET.parse(file_xml).getroot()
    value_list = []
    for type_tag in root.findall('versioning/versions/version'):
        value = type_tag.text
        value_list.append(value)
    value_list.reverse()
    write_json(value_list)


def write_json(get_list) -> json:
    key_value = {'options': []}

    for element in get_list:
        key_value['options'].append({
            "key": element,
            "value": element,
            "enabled": 1
        })

    project = 0

    if project == 0:
        json_name = "versions.json"
    elif project == 1:
        json_name = "versions_r.json"

    with open(json_name, 'w') as outfile:
        json.dump(key_value, outfile, indent=4)


if __name__ == '__main__':
    # xml_file = sys.argv[1]
    xml_file = "maven-metadata.xml"
    get_version(xml_file)

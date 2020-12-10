import xml.etree.ElementTree as ET


def add_color(letter, color):
    svg_tree = ET.parse('images/' + letter + '.svg')
    svg_root = svg_tree.getroot()

    for child in svg_root:
        if child.tag.endswith('g') or child.tag.endswith('path'):
            child.attrib['fill'] = color

    svg_var = ET.tostring(svg_root, encoding='unicode', method='xml')
    with open('images/' + letter + '.svg', 'w') as dest:
        dest.write(svg_var)
import xml.etree.ElementTree as ET
import os
package_base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

def add_color(letter, color):
    if letter == '-':
        return
    svg_tree = ET.parse(f'{package_base_path}/../images/{letter}.svg')
    svg_root = svg_tree.getroot()

    for child in svg_root:
        if child.tag.endswith('g') or child.tag.endswith('path'):
            child.attrib['fill'] = color

    svg_var = ET.tostring(svg_root, encoding='unicode', method='xml')
    with open(f'{package_base_path}/../images/{letter}.svg') as dest:
        dest.write(svg_var)


def calculate_ratio(parsed_sequences):
    ratio = []
    seq_length = parsed_sequences[0].get('seq_length')
    seq_num = len(parsed_sequences)
    possible_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for i in range(0, seq_length):
        letter_count = dict()
        for seq_obj in parsed_sequences:
            current_letter = seq_obj.get('seq')[i]
            letter_count[current_letter] = letter_count.get(current_letter, 0) + 1

        ratio_of_pos = dict()
        for letter in possible_letters:
            ratio_of_pos[letter] = letter_count.get(letter, 0)/seq_num

        ratio.append({k: ratio_of_pos[k] for k in sorted(ratio_of_pos, key=ratio_of_pos.get, reverse=True)})

    return ratio

def get_base_path():
    return package_base_path

from bioviz.colorMaps import get_colormap, get_all_color_map_names


def test_get_colormap_names():
    expected_result = ['clustal', 'macClade', 'gcat', 'purinePyrimidine', 'translation', 'annotation', 'nucleotide', 'proteinClustal', 'proteinZappo', 'proteinTaylor', 'proteinHydrophobicity', 'proteinHelixPropensity', 'proteinStrandPropensity', 'proteinTurnPropensity', 'proteinBuriedIndex']
    actual_result = get_all_color_map_names()
    assert expected_result == actual_result


def test_get_colormap_undefined():
    expected_result = "Invalid color theme"
    actual_result = get_colormap('asd')
    assert expected_result == actual_result


def test_get_colormap_clustal():
    expected_result = {
        "A": "red",
        "C": "blue",
        "G": "orange",
        "T": "green",
        "U": "green"
    }
    actual_result = get_colormap('clustal')
    assert expected_result == actual_result


def test_get_colormap_mac_clade():
    expected_result = {
        "A": "red",
        "C": "green",
        "G": "yellow",
        "T": "blue",
        "U": "blue"
    }
    actual_result = get_colormap('macClade')
    assert expected_result == actual_result


def test_get_colormap_gcat():
    expected_result = {
        "A": "red",
        "C": "orange",
        "G": "orange",
        "T": "red",
        "U": "red"
    }
    actual_result = get_colormap('gcat')
    assert expected_result == actual_result


def test_get_colormap_purine_pyrimidine():
    expected_result = {
        "A": "pink",
        "C": "blue",
        "G": "pink",
        "T": "blue",
        "U": "blue"
    }
    actual_result = get_colormap('purinePyrimidine')
    assert expected_result == actual_result


def test_get_colormap_translation():
    expected_result = {
        "A": "red",
        "C": "red",
        "G": "red",
        "T": "green",
        "U": "green"
    }
    actual_result = get_colormap('translation')
    assert expected_result == actual_result


def test_get_colormap_annotation():
    expected_result = {
        "A": "yellow",
        "C": "yellow",
        "G": "black",
        "T": "green",
        "U": "green"
    }
    actual_result = get_colormap('annotation')
    assert expected_result == actual_result


def test_get_colormap_nucleotide():
    expected_result = {
        "A": "#64F73F",
        "C": "#FFB340",
        "G": "#EB413C",
        "T": "#3C88EE",
        "U": "#3C88EE"
    }
    actual_result = get_colormap('nucleotide')
    assert expected_result == actual_result


def test_get_colormap_protein_clustal():
    expected_result = {
        "A": "#80a0f0",
        "R": "#f01505",
        "N": "#00ff00",
        "D": "#c048c0",
        "C": "#f08080",
        "Q": "#00ff00",
        "E": "#c048c0",
        "G": "#f09048",
        "H": "#15a4a4",
        "I": "#80a0f0",
        "L": "#80a0f0",
        "K": "#f01505",
        "M": "#80a0f0",
        "F": "#80a0f0",
        "P": "#ffff00",
        "S": "#00ff00",
        "T": "#00ff00",
        "W": "#80a0f0",
        "Y": "#15a4a4",
        "V": "#80a0f0",
        "B": "black",
        "X": "black",
        "Z": "black"
    }
    actual_result = get_colormap('proteinClustal')
    assert expected_result == actual_result


def test_get_colormap_protein_zappo():
    expected_result = {
        "A": "#ffafaf",
        "R": "#6464ff",
        "N": "#00ff00",
        "D": "#ff0000",
        "C": "#ffff00",
        "Q": "#00ff00",
        "E": "#ff0000",
        "G": "#ff00ff",
        "H": "#6464ff",
        "I": "#ffafaf",
        "L": "#ffafaf",
        "K": "#6464ff",
        "M": "#ffafaf",
        "F": "#ffc800",
        "P": "#ff00ff",
        "S": "#00ff00",
        "T": "#00ff00",
        "W": "#ffc800",
        "Y": "#ffc800",
        "V": "#ffafaf",
        "B": "black",
        "X": "black",
        "Z": "black"
    }
    actual_result = get_colormap('proteinZappo')
    assert expected_result == actual_result


def test_get_colormap_protein_taylor():
    expected_result = {
        "A": "#ccff00",
        "R": "#0000ff",
        "N": "#cc00ff",
        "D": "#ff0000",
        "C": "#ffff00",
        "Q": "#ff00cc",
        "E": "#ff0066",
        "G": "#ff9900",
        "H": "#0066ff",
        "I": "#66ff00",
        "L": "#33ff00",
        "K": "#6600ff",
        "M": "#00ff00",
        "F": "#00ff66",
        "P": "#ffcc00",
        "S": "#ff3300",
        "T": "#ff6600",
        "W": "#00ccff",
        "Y": "#00ffcc",
        "V": "#99ff00",
        "B": "black",
        "X": "black",
        "Z": "black"
    }
    actual_result = get_colormap('proteinTaylor')
    assert expected_result == actual_result


def test_get_colormap_protein_hydrophobicity():
    expected_result = {
        "A": "#ad0052",
        "R": "#0000ff",
        "N": "#0c00f3",
        "D": "#0c00f3",
        "C": "#c2003d",
        "Q": "#0c00f3",
        "E": "#0c00f3",
        "G": "#6a0095",
        "H": "#1500ea",
        "I": "#ff0000",
        "L": "#ea0015",
        "K": "#0000ff",
        "M": "#b0004f",
        "F": "#cb0034",
        "P": "#4600b9",
        "S": "#5e00a1",
        "T": "#61009e",
        "W": "#5b00a4",
        "Y": "#4f00b0",
        "V": "#f60009",
        "B": "#0c00f3",
        "X": "#680097",
        "Z": "#0c00f3"
    }
    actual_result = get_colormap('proteinHydrophobicity')
    assert expected_result == actual_result


def test_get_colormap_protein_helix_propensity():
    expected_result = {
        "A": "#e718e7",
        "R": "#6f906f",
        "N": "#1be41b",
        "D": "#778877",
        "C": "#23dc23",
        "Q": "#926d92",
        "E": "#ff00ff",
        "G": "#00ff00",
        "H": "#758a75",
        "I": "#8a758a",
        "L": "#ae51ae",
        "K": "#a05fa0",
        "M": "#ef10ef",
        "F": "#986798",
        "P": "#00ff00",
        "S": "#36c936",
        "T": "#47b847",
        "W": "#8a758a",
        "Y": "#21de21",
        "V": "#857a85",
        "B": "#49b649",
        "X": "#758a75",
        "Z": "#c936c9"
    }
    actual_result = get_colormap('proteinHelixPropensity')
    assert expected_result == actual_result


def test_get_colormap_protein_strand_propensity():
    expected_result = {
        "A": "#5858a7",
        "R": "#6b6b94",
        "N": "#64649b",
        "D": "#2121de",
        "C": "#9d9d62",
        "Q": "#8c8c73",
        "E": "#0000ff",
        "G": "#4949b6",
        "H": "#60609f",
        "I": "#ecec13",
        "L": "#b2b24d",
        "K": "#4747b8",
        "M": "#82827d",
        "F": "#c2c23d",
        "P": "#2323dc",
        "S": "#4949b6",
        "T": "#9d9d62",
        "W": "#c0c03f",
        "Y": "#d3d32c",
        "V": "#ffff00",
        "B": "#4343bc",
        "X": "#797986",
        "Z": "#4747b8"
    }
    actual_result = get_colormap('proteinStrandPropensity')
    assert expected_result == actual_result


def test_get_colormap_protein_turn_propensity():
    expected_result = {
        "A": "#2cd3d3",
        "R": "#708f8f",
        "N": "#ff0000",
        "D": "#e81717",
        "C": "#a85757",
        "Q": "#3fc0c0",
        "E": "#778888",
        "G": "#ff0000",
        "H": "#708f8f",
        "I": "#00ffff",
        "L": "#1ce3e3",
        "K": "#7e8181",
        "M": "#1ee1e1",
        "F": "#1ee1e1",
        "P": "#f60909",
        "S": "#e11e1e",
        "T": "#738c8c",
        "W": "#738c8c",
        "Y": "#9d6262",
        "V": "#07f8f8",
        "B": "#f30c0c",
        "X": "#7c8383",
        "Z": "#5ba4a4"
    }
    actual_result = get_colormap('proteinTurnPropensity')
    assert expected_result == actual_result


def test_get_colormap_protein_buried_index():
    expected_result = {
        "A": "#00a35c",
        "R": "#00fc03",
        "N": "#00eb14",
        "D": "#00eb14",
        "C": "#0000ff",
        "Q": "#00f10e",
        "E": "#00f10e",
        "G": "#009d62",
        "H": "#00d52a",
        "I": "#0054ab",
        "L": "#007b84",
        "K": "#00ff00",
        "M": "#009768",
        "F": "#008778",
        "P": "#00e01f",
        "S": "#00d52a",
        "T": "#00db24",
        "W": "#00a857",
        "Y": "#00e619",
        "V": "#005fa0",
        "B": "#00eb14",
        "X": "#00b649",
        "Z": "#00f10e"
    }
    actual_result = get_colormap('proteinBuriedIndex')
    assert expected_result == actual_result

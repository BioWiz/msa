from bioviz import msa
from diffimg import diff


def test_dendrogram_visualization_from_parsed_alignment():
    expected_result = 'example_data/example_dendrogram.png'
    d = msa.draw_dendrogram('example_data/example.dnd')
    msa.export_image(d, 'png')
    actual_result = 'example_dendrogram.png'
    df = diff(expected_result, actual_result, delete_diff_file=True)
    assert df == 0.0

from bioviz import msa, parser
from diffimg import diff


def test_msa_visualization_from_file():
    expected_result = 'example_data/example_clustal_alignment.png'
    v = msa.draw_alignment_from_file(file='example_data/example_clustal.clustal',
                                     color_scheme="clustal", dest_file='example_clustal_alignment.html')
    msa.export_image(v, 'png')
    actual_result = 'example_clustal_alignment.png'
    assert diff(expected_result, actual_result, delete_diff_file=True) == 0.0


def test_msa_visualization_from_parsed_alignment():
    expected_result = 'example_data/example_clustal_alignment.png'
    parsed_seq = parser.parse_file('example_data/example_clustal.clustal')
    v = msa.draw_alignment_from_parsed_seq(parsed_seq=parsed_seq,
                                           color_scheme="clustal", dest_file='example_clustal_alignment.html')
    msa.export_image(v, 'png')
    actual_result = 'example_clustal_alignment.png'
    assert diff(expected_result, actual_result, delete_diff_file=True) == 0.0

from bioviz import msa, parser
from diffimg import diff


def test_sequence_logo_visualization_from_file():
    expected_result = 'example_data/example_clustal_seqLogo.png'
    sl = msa.draw_seqlogo_from_file(file='example_data/example_clustal.clustal',
                                    color_scheme='clustal', dest_file='example_clustal_seqLogo.html', web=False)
    msa.export_image(sl, 'png')
    actual_result = 'example_clustal_seqLogo.png'
    df = diff(expected_result, actual_result, delete_diff_file=True)
    assert df < 0.001


def test_sequence_logo_visualization_from_parsed_alignment():
    parsed_seq = parser.parse_file('example_data/example_clustal.clustal')
    expected_result = 'example_data/example_clustal_seqLogo.png'
    sl = msa.draw_seqlogo_from_parsed_seq(parsed_sequences=parsed_seq,
                                          color_scheme='clustal', dest_file='example_clustal_seqLogo.html')
    msa.export_image(sl, 'png')
    actual_result = 'example_clustal_seqLogo.png'
    df = diff(expected_result, actual_result, delete_diff_file=True)
    assert df < 0.001

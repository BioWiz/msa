from bioviz.seqLogo import SeqLogo
from bioviz import parser
from diffimg import diff


def test_sequence_logo_visualization_from_file():
    expected_result = 'example_data/example_clustal_seqLogo.png'
    sl = SeqLogo()
    sl.dest_file = 'example_clustal_seqLogo.html'
    parsed_seq = parser.parse_file('example_data/example_clustal.clustal')
    sl.export_image(sl.draw(parsed_seq, 'clustal'), 'png')
    actual_result = 'example_clustal_seqLogo.png'
    df = diff(expected_result, actual_result, delete_diff_file=True)
    assert df == 0.0

"""
def test_sequence_logo_visualization_from_parsed_alignment():
    expected_result = <image of a sequence logo visualization using our test data>
    actual_result = sequence_logo(already parsed alignment)
    diff = diff(expected_result, acutal result)# you can use the diff shell tool in a subprocess to get the diff of the two images as files,
    #or use this https://github.com/nicolashahn/diffimg
    assert diff == 0 or None # whichever the diff returns if there is no difference between the two files / images
"""
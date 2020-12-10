from bioviz.msa import MSA
from bioviz import parser
from diffimg import diff


def test_msa_visualization_from_file():
    expected_result = 'example_data/example_clustal_msa.png'
    v = MSA()
    v.dest_file = 'example_clustal_msa.html'
    parsed = parser.parse_file('example_data/example_clustal.clustal')
    v.export_image(v.draw(parsed, 'clustal'), 'png')
    actual_result = 'example_clustal_msa.png'
    assert diff(expected_result, actual_result, delete_diff_file=True) == 0.0


"""
def test_msa_visualization_from_parsed_alignment():
    expected_result = <image of a msa visualization using our test data>
    actual_result = msa(already parsed alignment)
    diff = diff(expected_result, acutal result)# you can use the diff shell tool in a subprocess to get the diff of the two images as files,
    #or use this https://github.com/nicolashahn/diffimg
    assert diff == 0 or None # whichever the diff returns if there is no difference between the two files / images
"""
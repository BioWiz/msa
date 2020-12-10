from bioviz.parser import parse_file


def test_parsing_sequences():
    expected_result = []
    actual_result = parse_file('example_data/example_clustal.clustal')
    assert expected_result == actual_result

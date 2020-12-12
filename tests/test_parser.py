from bioviz.parser import parse_file
from Bio.Seq import Seq


def test_parsing_sequences():
    expected_ids = ['LC006775.1', 'LC006829.1', 'LC006802.1', 'LC006811.1', 'LC006784.1', 'LC006757.1', 'LC006748.1',
                    'LC006766.1']
    expected_seqs = [Seq('GTCGACAAAAAGGTCCGTGACGGCCAAGCTCTCGACAACCACCAGGCCACCGCCGTCGCT'),
                     Seq('GTCGACAAAAAGGTCCGTGACGGCCAAGCTCTCGACAACCACCAGGCCACCGCCGTCGCT'),
                     Seq('GTCGACAAAAAGGTCCGTGACGGCCAAGCTCTCGACAACCACCAGGCCACCGCCGTCACT'),
                     Seq('GTCGACAAAAAGGTCCGTGACGGCCAAGCTCTCGACAACCACCAGGCCACCGCCGTCGCC'),
                     Seq('GTCGACAAAAAGGTCCGTGACGGCCAAGCTCTCGACAACCACCAGGCCACCGCCGTCGCC'),
                     Seq('GTCGACAAAAAGGTCCGTGACGGCCAAGCTCTCGACAACCACCAGGCCACCGCCGTCGCC'),
                     Seq('GTCGACAAAAAGGTCCGTGACGGCCAAGCTCTCGACAACCACCAGGCCACCGCCGTCGCC'),
                     Seq('GTCGACAAAAAGATCCGTGACGGCCAAGCTCTCGACAACCACCAGGCCACCGCCGTCGCC')]
    expected_length = 60
    expected_result = []
    for id, seq in zip(expected_ids, expected_seqs):
        expected_result.append({
            'id': id,
            'seq': seq,
            'seq_length': expected_length
        })
    actual_result = parse_file('example_data/example_clustal.clustal')
    assert expected_result == actual_result

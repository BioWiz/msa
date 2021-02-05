from Bio import SeqIO
import logging

# This parser requires a file and returns a Seq.
def parse_file(file):
    file_name = file
    file_format = file_name.split('.')[-1]

    # Handle clustal_num file format as clustal format
    if '_' in file_format:
        file_format = file_format.split('_')[0]

    sequences = []

    try:
        for seq_record in SeqIO.parse(file_name, file_format):
            sequences.append({
                'id': seq_record.id,
                'seq': seq_record.seq,
                'seq_length': len(seq_record)
                }
            )
        return sequences
    except Exception as ex:
        logging.error(ex)
        return ex
    
    

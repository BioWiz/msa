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

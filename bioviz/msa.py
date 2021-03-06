from bioviz import dendrogram, alignment, seqLogo, parser, colorMaps
import logging
from bioviz.exceptions import InvalidColorMapException, InvalidFileFormatException

file_formats = ['clustal', 'clustal_num', 'msf', 'fasta']
color_maps = colorMaps.get_all_color_map_names()


def draw_seqlogo_from_file(file, color_scheme, web=False, plot_width=20, plot_height=160, steps=5, dest_file=''):
    """ Gets a multiple sequence alignment file and draws the plot into an html file.

    :param file: The path to the clustal / clustal_num / msf / fasta file.
    :type file: str
    :param color_scheme: The name of the color scheme.
    :type color_scheme: str
    :param plot_width: An integer number for the width of the plot. Default is 20px.
    :type plot_width: int
    :param plot_height: An integer number for the height of the plot. Default is 160px.
    :type plot_height: int
    :param steps: An integer number to use as the step size of the 'x' axis. Default is 5.
    :type steps: int
    :param dest_file: The filename the html output should be saved as. Default is seqLogo_<timestamp>.html
    :type dest_file: str
    :return: A SeqLogo object.
    :rtype: SeqLogo
    """
    if file.split('.')[-1] not in file_formats:
        logging.error("File format must be clustal / clustal_num / msf / fasta!")
        return InvalidFileFormatException(f'{file} is not valid for this diagram type. Please use files with clustal msf or fasta extension.' )
    if color_scheme not in color_maps:
        logging.error("Invalid color map name. See get_all_color_map_names function for available names.")
        return  InvalidColorMapException(f'{color_scheme} is not a valid color scheme name.')
    sl = seqLogo.SeqLogo(plot_width, plot_height, steps, dest_file)
    parsed_sequences = parser.parse_file(file)
    if isinstance(parsed_sequences, Exception):
        return f'Drawing alignment failed with the following error: {parsed_sequences}'
    sl.draw(parsed_sequences, color_scheme, web)
    return sl


def draw_seqlogo_from_parsed_seq(parsed_sequences, color_scheme, plot_width=20, plot_height=160, steps=5, dest_file=''):
    """ Gets the parsed sequences and draws the plot into an html file.

    :param parsed_sequences: Array of the parsed sequences.
    :type parsed_sequences: list
    :param color_scheme: The name of the color scheme.
    :type color_scheme: str
    :param plot_width: An integer number for the width of the plot. Default is 20px.
    :type plot_width: int
    :param plot_height: An integer number for the height of the plot. Default is 160px.
    :type plot_height: int
    :param steps: An integer number to use as the step size of the 'x' axis. Default is 5.
    :type steps: int
    :param dest_file: The filename the html output should be saved as. Default is seqLogo_<timestamp>.html
    :type dest_file: str
    :return: A SeqLogo object.
    :rtype: SeqLogo
    """
    if color_scheme not in color_maps:
        logging.error("Invalid color map name. See get_all_color_map_names function for available names.")
        return  InvalidColorMapException(f'{color_scheme} is not a valid color scheme name.')
    sl = seqLogo.SeqLogo(plot_width, plot_height, plot_height, dest_file)
    sl.draw(parsed_sequences, color_scheme)
    return sl


def draw_alignment_from_file(file, color_scheme, plot_width=100, dest_file=''):
    """ Gets a multiple sequence alignment file and draws the plot into an html file.

    :param file: The path to the clustal / clustal_num / msf / fasta file.
    :type file: str
    :param color_scheme: The name of the color scheme.
    :type color_scheme: str
    :param plot_width: An integer number for the width of the plot. Default is 100px.
    :type plot_width: int
    :param dest_file: The filename the html output should be saved as. Default is alignment_<timestamp>.html
    :type dest_file: str
    :return: An Alignment object, or the exception object if an error occured.
    :rtype: Alignment
    """
    if color_scheme not in color_maps:
        logging.error("Invalid color map name. See get_all_color_map_names function for available names.")
        return  InvalidColorMapException(f'{color_scheme} is not a valid color scheme name.')
    if file.split('.')[-1] not in file_formats:
        logging.error("File format must be clustal / clustal_num / msf / fasta!")
        return InvalidFileFormatException(f'{file} is not valid for this diagram type. Please use files with clustal msf or fasta extension.' )
    logo = alignment.Alignment(plot_width, dest_file)
    parsed_seq = parser.parse_file(file)
    if isinstance(parsed_seq, Exception):
        return parsed_seq
    logo.draw(parsed_seq, color_scheme)
    return logo


def draw_alignment_from_parsed_seq(parsed_seq, color_scheme, plot_width=100, dest_file=''):
    """ Gets the parsed sequences and draws the plot into an html file.

    :param parsed_seq: Array of the parsed sequences.
    :type parsed_seq: list
    :param color_scheme: The name of the color scheme.
    :type color_scheme: str
    :param plot_width: An integer number for the width of the plot. Default is 100px.
    :type plot_width: int
    :param dest_file: The filename the html output should be saved as. Default is alignment_<timestamp>.html
    :type dest_file: str
    :return: An Alignment object.
    :rtype: Alignment
    """
    if color_scheme not in color_maps:
        logging.error("Invalid color map name. See get_all_color_map_names function for available names.")
        return  InvalidColorMapException(f'{color_scheme} is not a valid color scheme name.')
    logo = alignment.Alignment(plot_width, dest_file)
    logo.draw(parsed_seq, color_scheme)
    return logo


def draw_dendrogram(dnd_file, name_label_size=7, length_label_size=6, plot_width=500, plot_height=500, dest_file=''):
    """ Gets a dnd file and draws the plot into an html file.

    :param dnd_file: Path to the dnd file.
    :type dnd_file: str
    :param name_label_size: An integer for the label size of the displayed names. Default is 7px.
    :type name_label_size: int
    :param length_label_size: An integer for the label size of the displayed lengths. Default is 6px.
    :type length_label_size: int
    :param plot_width: An integer number for the width of the plot. Default is 500px.
    :type plot_width: int
    :param plot_height: An integer number for the height of the plot. Default is 500px.
    :type plot_height: int
    :param dest_file: The filename the html output should be saved as. Default is <input file name>_dendrogram.html
    :type dest_file: str
    :return: A Dendrogram object.
    :rtype: Dendrogram
    """
    if dnd_file.split('.')[-1] != 'dnd':
        logging.error("File format must be dnd!")
        return InvalidFileFormatException(f'{file} is not valid for this diagram type. Please use files with dnd extension.' )
    d = dendrogram.Dendrogram(name_label_size, length_label_size, plot_width, plot_height, dest_file)
    d.draw(dnd_file)
    return d


def show(logo):
    """Opens the default browser and opens the html containing the logo.

    :param logo: A SeqLogo / Alignment / Dendrogram object.
    """
    if not isinstance(logo, dendrogram.Dendrogram) and not isinstance(logo, seqLogo.SeqLogo) and not isinstance(logo, alignment.Alignment):
        logging.error("The logo parameter should be the type of Dendrogram / SeqLogo / Alignment.")
        return
    logo.show()

def save(logo):
    """Save the html file containing the interactive logo without opening it in the browser.
    
    :param logo: A SeqLogo / Alignment / Dendrogram object.
    """
    if not isinstance(logo, dendrogram.Dendrogram) and not isinstance(logo, seqLogo.SeqLogo) and not isinstance(logo, alignment.Alignment):
        logging.error("The logo parameter should be the type of Dendrogram / SeqLogo / Alignment.")
        return
    resultFilename = logo.save()
    return resultFilename


def export_image(logo, img_type, transparent=False):
    """Saves the image the same name as the html file.

    :param logo: A SeqLogo / Alignment / Dendrogram object.
    :param img_type: "png" or "svg"
    :type img_type: str
    :param transparent: Default is False.
    :type transparent: bool
    """
    if not isinstance(logo, dendrogram.Dendrogram) and not isinstance(logo, alignment.Alignment) and not isinstance(logo, seqLogo.SeqLogo):
        logging.error("The logo parameter should be the type of Dendrogram, Alignment or Sequence Logo.")
        return
    if img_type != 'png' and img_type != 'svg':
        logging.error("Image type should be png or svg.")
        return
    return logo.export_image(img_type, transparent)


def get_all_color_map_names():
    """
    :return: List of all available color maps.
    :rtype: list
    """
    return colorMaps.get_all_color_map_names()


def get_nucleotide_color_map_names():
    """
    :return: List of all available color maps for nucleotides.
    :rtype: list
    """
    return colorMaps.get_nucleotide_color_map_names()


def get_protein_color_map_names():
    """
    :return: List of all available color maps for proteins.
    :rtype: list
    """
    return colorMaps.get_protein_color_map_names()

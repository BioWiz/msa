import argparse
import sys
from bioviz import msa

class NoAction(argparse.Action):
    def __init__(self, **kwargs):
        kwargs.setdefault('default', argparse.SUPPRESS)
        kwargs.setdefault('nargs', 0)
        super(NoAction, self).__init__(**kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        pass

parser = argparse.ArgumentParser(prog="bioviz", description="BioViz - Python library for visualizing Bio Data.")
parser.register('action', 'none', NoAction)


parser.add_argument( '--file', '-f', metavar='INPUT', nargs=1, type=str, required=not('--colors?' in sys.argv or '-c?' in sys.argv),
    help="Path to the file to used as input.")

parser.add_argument( '--type', '-t', metavar='TYPE', nargs=1, type=str, required=not('--colors?' in sys.argv or '-c?' in sys.argv),
    choices=['alignment', 'dendogram','seqlogo'], help="Define what type of figure should be created.")

parser.add_argument('--colors?', '-c?', action='store_true', dest="colors_help", help='List available color schemes.' )

parser.add_argument('--width', '-w', type=int, metavar="PLOT_WIDTH", help="For alignment and sequence logo figures defines the width in number of residues,"+
        "for the dendogram it defines plot width in pixels.")

parser.add_argument( '--color', '-c', metavar='COLOR_SCHEME', nargs=1, type=str,
    help="Color scheme to use for the residues. Defaults to clustal")

parser.add_argument('--save', '-s', action='store_true', help="Only save the html file containing the fiugre, and do not automatically open it.")

parser.add_argument('--output', '-o', type=str, nargs=1, help="The name or full path including the file name to save the result.")

parser.add_argument('--export', '-e', metavar='EXPORT_FILE_TYPE', type=str, choices=['png', 'svg'],help='Export the logo as PNG or SVG. SVG is not available for the sequence logo.')


type_group = parser.add_argument_group(title='Diagram types')
type_group.add_argument('alignment', action='none', help="Display the MSA file as plain sequence aligment.")
type_group.add_argument('dendogram',action='none', help="Create a dendogram from a dnd file")
type_group.add_argument('seqlogo', action='none', help="Create a sequence logo from the alignment.")



color_group_nucleotide = parser.add_argument_group(title="Nucleotide color schemes")
color_group_protein = parser.add_argument_group(title="Protein color schemes")

nucleotide_colors = msa.get_nucleotide_color_map_names()
protein_colors = msa.get_protein_color_map_names()

for color in nucleotide_colors:
    color_group_nucleotide.add_argument(color, help=f'{color} color scheme.', action='none')

for color in protein_colors:
    color_group_protein.add_argument(color, help=f'{color} color scheme.', action='none')



args = parser.parse_args()
print(args)

if args.colors_help:
    print("Available color schemes:")
    print('\nFor nucleotide sequences:\n')
    for color in nucleotide_colors:
        print(color)
    
    print('\nFor protein sequences:\n')
    for color in protein_colors:
        print(color)
    exit(0)



if args.type[0] == 'alignment':
    logo = msa.draw_alignment_from_file(args.file[0], (args.color[0]), plot_width=args.width[0] if args.width != None else 100,
        dest_file=(args.output[0] if args.output != None else '' ))
elif args.type[0] == 'seqlogo':
    logo = msa.draw_seqlogo_from_file(args.file[0], (args.color[0]), plot_width=args.width[0] if args.width != None else 100,
        dest_file=(args.output[0] if args.output != None else '' ))
else:
    logo = msa.draw_dendrogram(args.file[0], plot_width=args.width[0] if args.width != None else 500, 
        dest_file=(args.output[0] if args.output != None else '' ))

if args.save:
    print(f'Result saved to {msa.save(logo)}')
else:
    msa.show(logo)

if args.export :
    print(f'Figure exported to {msa.export_image(logo, args.export)}')
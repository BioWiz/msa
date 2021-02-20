Python 3.7 and Bokeh based visualization for Multiple Sequence Alignments

usage: bioviz [-h] --file INPUT --type TYPE [--colors?] [--width PLOT_WIDTH]
              [--color COLOR_SCHEME] [--save] [--output OUTPUT]
              [--export EXPORT_FILE_TYPE]

optional arguments:
  -h, --help            show this help message and exit
  --file INPUT, -f INPUT
                        Path to the file to used as input.
  --type TYPE, -t TYPE  Define what type of figure should be created.
  --colors?, -c?        List available color schemes.
  --width PLOT_WIDTH, -w PLOT_WIDTH
                        For alignment and sequence logo figures defines the
                        width in number of residues,for the dendogram it
                        defines plot width in pixels.
  --color COLOR_SCHEME, -c COLOR_SCHEME
                        Color scheme to use for the residues. Defaults to
                        clustal
  --save, -s            Only save the html file containing the fiugre, and do
                        not automatically open it.
  --output OUTPUT, -o OUTPUT
                        The name or full path including the file name to save
                        the result.
  --export EXPORT_FILE_TYPE, -e EXPORT_FILE_TYPE
                        Export the logo as PNG or SVG. SVG is not available
                        for the sequence logo.

Diagram types:
  alignment             Display the MSA file as plain sequence aligment.
  dendogram             Create a dendogram from a dnd file
  seqlogo               Create a sequence logo from the alignment.

Nucleotide color schemes:
  clustal               clustal color scheme.
  macClade              macClade color scheme.
  gcat                  gcat color scheme.
  purinePyrimidine      purinePyrimidine color scheme.
  translation           translation color scheme.
  annotation            annotation color scheme.
  nucleotide            nucleotide color scheme.

Protein color schemes:
  proteinClustal        proteinClustal color scheme.
  proteinZappo          proteinZappo color scheme.
  proteinTaylor         proteinTaylor color scheme.
  proteinHydrophobicity
                        proteinHydrophobicity color scheme.
  proteinHelixPropensity
                        proteinHelixPropensity color scheme.
  proteinStrandPropensity
                        proteinStrandPropensity color scheme.
  proteinTurnPropensity
                        proteinTurnPropensity color scheme.
  proteinBuriedIndex    proteinBuriedIndex color scheme.

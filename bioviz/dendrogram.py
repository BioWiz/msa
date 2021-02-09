import copy
from Bio import Phylo
from bokeh.io import export_png, export_svgs
from bokeh.models import ColumnDataSource, LabelSet, Range1d
from bokeh.plotting import figure, output_file, show, save


class Dendrogram(object):

    def __init__(self,name_label_size,length_label_size, plot_width, plot_height, dest_file):
        self.name_label_size = name_label_size
        self.length_label_size = length_label_size
        self.plot_width = plot_width
        self.plot_height = plot_height
        self.dest_file = dest_file
        self.p = figure()

    def draw(self, file):
        if self.dest_file is '':
            self.dest_file = file.split('/')[-1].split('.')[0] + '_dendrogram.html'
        elif self.dest_file.split('.')[-1] != 'html':
            self.dest_file += ".html"
        output_file(self.dest_file)

        # Constants
        tree = Phylo.read(file, "newick")
        tree.ladderize()
        terminal_count = tree.count_terminals()
        terminals = tree.get_terminals()

        # Variables:
        # x_coords: list of list consisting of x coordinates of each line (from root to terminal)
        # names: list of terminal names
        # terminal_lengths: list of lengths / x coordinates of terminals (will be displayed)
        # label_x and label_y: lists of x and y coordinates of labels
        # unique_x_lines: list of lists containing x coordinate pairs (from-to) which can be separately drawn
        # draw_x and draw_y: lists of lists containing x and y pairs to be drawn eg. [[start_x, finish_x]..]
        x_coords = []
        names = []
        terminal_lengths = []
        label_x = []
        label_y = []
        unique_x_lines = []
        draw_x = []
        draw_y = []

        # Get all lines from root to terminal.
        for terminal, i in zip(terminals, range(1, terminal_count + 1)):
            actual_line_x_coords = []
            length = 0
            trace = tree.trace(start=tree.root, finish=terminal)
            # print(trace)
            for clade in trace:
                if clade.branch_length:
                    length += clade.branch_length
                actual_line_x_coords.append(length)
                if clade is terminal:
                    terminal_lengths.append(round(length, 5))
                    names.append(clade.name)
                    label_x.append(length)
                    label_y.append(i)
            x_coords.append(actual_line_x_coords)

        # Split length arrays into a list of unique lines "from-to" on x axis.
        for line in x_coords:
            if len(line) is 2 and line not in unique_x_lines:
                unique_x_lines.append(line)
            else:
                # Split the line into pairs.
                segments_of_two = []
                for i in range(0, len(line)-1):
                    segments_of_two.append([line[i], line[i+1]])
                # Check each pair, add if unique.
                for segment in segments_of_two:
                    if segment not in unique_x_lines:
                        unique_x_lines.append(segment)

        # If x coord is a terminal, add the correct y coord.
        for xline in unique_x_lines:
            occurrences = [i for i, val in enumerate(label_x) if val == xline[1]]
            if len(occurrences) is 1:
                draw_x.append(xline)
                draw_y.append([xline[0], label_y[occurrences[0]]])
            # If there are more than one terminal of the same length.
            elif len(occurrences) > 1:
                for i in occurrences:
                    # Recheck whether line goes to a terminal.
                    if x_coords[i][-2] == xline[0]:
                        draw_x.append(xline)
                        draw_y.append([xline[0], label_y[i]])
            else:
                draw_x.append(xline)
                draw_y.append(copy.deepcopy(xline))

        # Compute the correct y coords of inner clades.
        clade_y = dict() # helper dict to pair x and y coords
        for yline in reversed(draw_y):
            siblings = []
            x = yline[1]
            # If line ends in a terminal, do nothing.
            if x in label_x:
                continue
            for line in draw_y:
                if line[0] == x:
                    siblings.append(line[1])
            if siblings:
                clade_y[x] = (max(siblings)+min(siblings))/2
                for line in draw_y:
                    for i in range(0, len(line)):
                        if line[i] in clade_y:
                            line[i] = clade_y[line[i]]

        # Compute the first y coord to be at center.
        starters = [line[1] for line in draw_y if line[0] == 0]
        start_y = sum(starters) / len(starters)
        draw_y = [[start_y, line[1]] if line[0] == 0 else [line[0], line[1]] for line in draw_y]

        # Draw plot
        self.p = figure(plot_width=self.plot_width, height=self.plot_height)

        # Set plot width for labels to be visible.
        longest = max(label_x)
        self.p.x_range = Range1d(-0.01, longest + len(max(names)) * longest * 0.02)

        # Don't show y axis.
        self.p.yaxis.visible = False

        # Draw lines
        for xline, yline in zip(draw_x, draw_y):
            # print(xline, yline)
            self.p.step(xline, yline, line_width=2, mode="before", color="black")

        source = ColumnDataSource(data=dict(x=label_x, y=label_y, labels=names))
        name_labels = LabelSet(x='x', y='y', text='labels', level='glyph',
                               text_font_size=str(self.name_label_size)+"pt",
                               x_offset=5, y_offset=0, source=source, render_mode='canvas')
        self.p.add_layout(name_labels)

        source = ColumnDataSource(data=dict(x=label_x, y=label_y, labels=terminal_lengths))
        length_labels = LabelSet(x='x', y='y', text='labels', level='glyph',
                                 text_font_size=str(self.length_label_size)+"pt",
                                 x_offset=5, y_offset=-14, source=source, render_mode='canvas')
        self.p.add_layout(length_labels)

        return self.p

    def show(self):
        show(self.p)

    def save(self):
        resultFileName = save(self.p,filename=self.dest_file, title='BioViz Dendogram')
        return resultFileName
        
    def export_image(self, img_type, transparent=False):
        if transparent:
            self.p.background_fill_color = None
            self.p.border_fill_color = None
        if img_type is "png":
            return export_png(self.p, filename=self.dest_file.split(".")[0] + ".png")
        elif img_type is "svg":
            self.p.output_backend = "svg"
            export_svgs(self.p, filename=self.dest_file.split(".")[0] + ".svg")
        else:
            return print("Possible image types are 'svg' and 'png'.")

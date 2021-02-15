import math
from bioviz import colorMaps, utils
from bokeh.io import output_file, show, save
from bokeh.io.export import export_png, export_svgs
from bokeh.models import ColumnDataSource, Plot, LinearAxis, Grid, Range1d
from bokeh.models.glyphs import ImageURL, Image
from bokeh.layouts import column
from datetime import datetime

#from bokeh.plotting import Figure

base_path = utils.get_base_path()

class SeqLogo(object):
    
    def __init__(self,plot_width, plot_height,steps,dest_file):
        self.plots = []
        self.plot_width = plot_width
        self.plot_height = plot_height
        # Steps of the ticker on the x axis
        self.steps = steps
        self.dest_file = dest_file


    def draw(self, parsed_sequences, color_scheme, web):
        if self.dest_file is '':
            timestamp = datetime.now().strftime("%y%m%d%H%M%S%f")
            self.dest_file = 'seqLogo_' + timestamp + '.html'
        elif self.dest_file.split('.')[-1] != 'html':
            self.dest_file += ".html"
        output_file(self.dest_file)

        ratio = utils.calculate_ratio(parsed_sequences)
        seq_length = len(ratio)
        # data numbering starts at 1 -> so should the ratio
        ratio.insert(0, {})

        #color_map = colorMaps.get_colormap(color_scheme)
        #for letter, color in color_map.items():
        #    utils.add_color(letter, color)

        # Each subplot should be plot_width letter 'long' at max.
        subplot_count = math.ceil(seq_length / self.plot_width)

        # Create subplots.
        for k in range(0, subplot_count):
            x_start = 1 + self.plot_width * k

            if k == subplot_count - 1:
                x_end = seq_length + 1
                self.plot_width = (x_end - x_start)
            else:
                x_end = self.plot_width + 1 + self.plot_width * k

            # x and y have the values of the axes of the plot - same for every sequence
            x = range(x_start, x_end)
            y = [0] * (x_end - x_start)
            source_seq = ColumnDataSource(dict(x=x, y=y))

            subplot = Plot(title=None, plot_width=int(80 * self.plot_width), plot_height=self.plot_height,
                           x_range=Range1d(start=x_start - 1, end=x_end),
                           y_range=Range1d(start=0, end=1),
                           min_border_top=10, toolbar_location=None,
                           )

            _sum = 0
            for position in range(x_start, x_end):
                for letter, rat in ratio[position].items():                      
                    remainder = 0
                    if not rat == 1.0:
                        remainder = _sum % 1
                        
                    _sum += rat
                    if not rat == 0.0:
                        #print(f'{letter}:ratio:{rat}, {remainder}')
                        if web:
                            image = ImageURL(name=letter, url=dict(value=f'http://localhost:8080//img/{color_scheme}_{letter}.svg'), x=position, y=remainder,
                                         w=1, h=rat, anchor="bottom_center")
                            subplot.add_glyph(source_seq, image)
                        else:
                            image = ImageURL(name=letter, url=dict(value=f'{base_path}/../images/{color_scheme}_{letter}.svg'), x=position, y=remainder,
                                         w=1, h=rat, anchor="bottom_center")
                            subplot.add_glyph(source_seq, image)
                _sum = 0

            xaxis = LinearAxis(axis_label="Position")
            xaxis.bounds = (x_start, x_end)
            xaxis.ticker = [x_start] + (list(range(x_start + self.steps - 1, x_end, self.steps)))
            subplot.add_layout(xaxis, 'below')

            subplot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
            self.plots.append(subplot)      
        return self.plots

    def show(self):
        show(column(self.plots))
    
    def save(self):
        resultFileName = save(column(self.plots),filename=self.dest_file, title='BioViz Sequence Logo')
        return resultFileName
        
    def export_image(self, img_type, transparent=False):
        if transparent:
            for plot in self.plots:
                plot.background_fill_color = None
                plot.border_fill_color = None
        if img_type == "png":
            return export_png(column(self.plots), filename=self.dest_file.split(".")[0] + ".png")
            # image = get_screenshot_as_png(column(plots), height=self.plot_height, width=self.plot_width)
            # return image.save("seqlogo.png")
        elif img_type == "svg":
            for plot in self.plots:
                plot.output_backend = "svg"
            return export_svgs(column(self.plots), filename=self.dest_file.split(".")[0] + ".svg")[0]
        else:
            return print("Possible image types are 'svg' and 'png'.")

import math
import os

from bioviz import calcRatio, colorMaps, utils
from bokeh.io import output_file, show
from bokeh.io.export import get_screenshot_as_png
from bokeh.models import ColumnDataSource, Plot, LinearAxis, Grid, Range1d
from bokeh.models.glyphs import ImageURL
from bokeh.layouts import column
from datetime import datetime
from selenium import webdriver


class SeqLogo(object):
    plot_width = 20
    plot_height = 160
    # Steps of the ticker on the x axis
    steps = 5
    _root_path = os.path.realpath(os.getcwd())
    dest_file = ''

    def draw(self, parsed_sequences, color_scheme):
        if self.dest_file is '':
            timestamp = datetime.now().strftime("%y%m%d%H%M%S%f")
            self.dest_file = 'seqLogo_' + timestamp + '.html'
        output_file(self.dest_file)

        ratio = calcRatio.calculate_ratio(parsed_sequences)
        seq_length = len(ratio)
        # data numbering starts at 1 -> so should the ratio
        ratio.insert(0, {})

        color_map = colorMaps.get_colormap(color_scheme)
        for letter, color in color_map.items():
            utils.add_color(letter, color)

        # Each subplot should be plot_width letter 'long' at max.
        subplot_count = math.ceil(seq_length / self.plot_width)
        plots = []

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
                           min_border_top=10, toolbar_location=None)

            sum = 0
            for r in range(x_start, x_end):
                for letter, rat in ratio[r].items():
                    remainder = 0
                    if not rat == 1.0:
                        remainder = sum % 1
                    sum += rat
                    if not rat == 0.0:
                        image = ImageURL(name=letter, url=dict(value=self._root_path + "/images/" + letter + ".svg"), x=r, y=remainder,
                                         w=1, h=rat, anchor="bottom_center")
                        subplot.add_glyph(source_seq, image)
                sum = 0

            xaxis = LinearAxis(axis_label="Position")
            xaxis.bounds = (x_start, x_end)
            xaxis.ticker = [x_start] + (list(range(x_start + self.steps - 1, x_end, self.steps)))
            subplot.add_layout(xaxis, 'below')

            subplot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
            plots.append(subplot)

            return plots

    def show(self, plots):
        show(column(plots))

    def export_image(self, plots, img_type, transparent=False):
        _options = webdriver.ChromeOptions()
        _options.add_argument('--disable-web-security')
        _webd = webdriver.Chrome(options=_options)
        if transparent:
            for plot in plots:
                plot.background_fill_color = None
                plot.border_fill_color = None
        if img_type is "png":
            image = get_screenshot_as_png(column(plots), driver=_webd)
            return image.save("seqLogo.png")
        else:
            return print("Possible image type is 'png'.")

import sys

try:
    from charts.chart_line import ChartLine
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - chart_line.py not found.")
    sys.exit()

try:
    from charts.chart_bar import ChartBar
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - chart_bar.py not found.")
    sys.exit()

try:
    from charts.chart_pie import ChartPie
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - chart_pie.py not found.")
    sys.exit()

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Errors.py not found.")
    sys.exit()

try:
    from charts.calc_chart_data import CalcData
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - calc_chart_data.py not found.")
    sys.exit()

import charts.calc_chart_data as calc

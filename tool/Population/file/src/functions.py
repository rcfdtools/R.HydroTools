# https://github.com/rcfdtools/R.HydroTools/tree/main/tool/Population
# -*- coding: UTF-8 -*-


# Function for print and show results in a log file
def print_log(file_log, txt_print, on_screen=False, center_div=False):
    # div50 is use for show 2 plots in the same line
    if on_screen:
        print(txt_print)
    if center_div:
        file_log.write('\n<div align="center">\n' + '\n')
    file_log.write(txt_print)
    if center_div:
        file_log.write('\n\n</div>\n' + '\n')

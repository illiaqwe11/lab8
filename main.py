from sea_level_predictor import *

sea_level_plot = predict_sea_level()

sea_level_plot.savefig('sea_level_plot.png')

sea_level_plot.show()

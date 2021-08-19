
import numpy as np
import pandas as pd
import keras



data = [{'epoch': '1574617329', 'max_deflection': '0.025276', 'axis_ratio': '0.357335', 'p2p_azimuth_unwrapped': '304.42751', 'wind_speed_3': '3.6666666666666665', 'wind_dir_3_corr': '142.1233333333333', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617332', 'max_deflection': '0.052946', 'axis_ratio': '0.238828', 'p2p_azimuth_unwrapped': '298.749567', 'wind_speed_3': '4.266666666666667', 'wind_dir_3_corr': '148.44333333333333',
'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617335', 'max_deflection': '0.047497', 'axis_ratio': '0.021875', 'p2p_azimuth_unwrapped': '293.351226', 'wind_speed_3': '4.733333333333333', 'wind_dir_3_corr': '148.05666666666664', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617338', 'max_deflection': '0.047497', 'axis_ratio': '0.021875', 'p2p_azimuth_unwrapped': '293.351226', 'wind_speed_3': '4.7', 'wind_dir_3_corr': '141.02', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617341', 'max_deflection': '0.042657', 'axis_ratio': '0.168554', 'p2p_azimuth_unwrapped': '288.677158', 'wind_speed_3': '6.2', 'wind_dir_3_corr': '143.9466666666667', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617344', 'max_deflection': '0.040712', 'axis_ratio': '0.029131', 'p2p_azimuth_unwrapped': '294.785483', 'wind_speed_3': '6.8', 'wind_dir_3_corr': '148.61333333333334',
'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617347', 'max_deflection': '0.040712', 'axis_ratio': '0.029131', 'p2p_azimuth_unwrapped': '294.785483', 'wind_speed_3': '7.333333333333333', 'wind_dir_3_corr': '150.9466666666667', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617350', 'max_deflection': '0.045294', 'axis_ratio': '0.130746', 'p2p_azimuth_unwrapped': '309.203365', 'wind_speed_3': '6.8', 'wind_dir_3_corr': '152.48', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617353', 'max_deflection': '0.029547', 'axis_ratio': '0.245575', 'p2p_azimuth_unwrapped': '311.190918', 'wind_speed_3': '5.033333333333333', 'wind_dir_3_corr': '145.08666666666667', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617356', 'max_deflection': '0.029547', 'axis_ratio': '0.245575', 'p2p_azimuth_unwrapped': '311.190918', 'wind_speed_3': '5.0', 'wind_dir_3_corr': '138.08', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617359', 'max_deflection': '0.018251', 'axis_ratio': '0.468303', 'p2p_azimuth_unwrapped': '272.437893', 'wind_speed_3': '4.233333333333333', 'wind_dir_3_corr': '131.81333333333333', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617362', 'max_deflection': '0.016303', 'axis_ratio': '0.257437', 'p2p_azimuth_unwrapped': '215.635508', 'wind_speed_3': '3.6', 'wind_dir_3_corr': '151.14666666666668', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617365', 'max_deflection': '0.014708', 'axis_ratio': '0.284403', 'p2p_azimuth_unwrapped': '177.488255', 'wind_speed_3': '4.266666666666667', 'wind_dir_3_corr': '153.08', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617368', 'max_deflection': '0.014708', 'axis_ratio': '0.284403', 'p2p_azimuth_unwrapped': '177.488255', 'wind_speed_3': '5.033333333333333', 'wind_dir_3_corr': '147.21333333333334', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617371', 'max_deflection': '0.027707', 'axis_ratio': '0.138521', 'p2p_azimuth_unwrapped': '151.176809', 'wind_speed_3': '5.9', 'wind_dir_3_corr': '143.89333333333337', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617374', 'max_deflection': '0.042297', 'axis_ratio': '0.390051', 'p2p_azimuth_unwrapped': '141.512019', 'wind_speed_3': '6.333333333333333', 'wind_dir_3_corr': '147.04666666666665', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617377', 'max_deflection': '0.042297', 'axis_ratio': '0.390051', 'p2p_azimuth_unwrapped': '141.512019', 'wind_speed_3': '6.3', 'wind_dir_3_corr': '146.76666666666668', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617380', 'max_deflection': '0.062314', 'axis_ratio': '0.345797', 'p2p_azimuth_unwrapped': '139.005068', 'wind_speed_3': '6.766666666666667', 'wind_dir_3_corr': '145.86', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617383', 'max_deflection': '0.066662', 'axis_ratio': '0.189328', 'p2p_azimuth_unwrapped': '137.882096', 'wind_speed_3': '5.966666666666666', 'wind_dir_3_corr': '154.48333333333335', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617386', 'max_deflection': '0.066662', 'axis_ratio': '0.189328', 'p2p_azimuth_unwrapped': '137.882096', 'wind_speed_3': '5.833333333333333', 'wind_dir_3_corr': '143.75333333333333', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617389', 'max_deflection': '0.0829', 'axis_ratio': '0.130326', 'p2p_azimuth_unwrapped': '130.718576', 'wind_speed_3': '4.633333333333333', 'wind_dir_3_corr': '139.88', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617392', 'max_deflection': '0.087383', 'axis_ratio': '0.120721', 'p2p_azimuth_unwrapped': '127.64886', 'wind_speed_3': '5.366666666666667', 'wind_dir_3_corr': '137.52', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617395', 'max_deflection': '0.087383', 'axis_ratio': '0.120721', 'p2p_azimuth_unwrapped': '127.64886', 'wind_speed_3': '7.733333333333333', 'wind_dir_3_corr': '127.62', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617398', 'max_deflection': '0.101926', 'axis_ratio': '0.050802', 'p2p_azimuth_unwrapped': '127.737035', 'wind_speed_3': '7.666666666666667', 'wind_dir_3_corr': '120.46666666666664', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617401', 'max_deflection': '0.09209', 'axis_ratio': '0.069128', 'p2p_azimuth_unwrapped': '124.341488', 'wind_speed_3': '7.033333333333334', 'wind_dir_3_corr': '122.74333333333334', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617404', 'max_deflection': '0.088706', 'axis_ratio': '0.206277', 'p2p_azimuth_unwrapped': '129.031963', 'wind_speed_3': '7.033333333333334', 'wind_dir_3_corr': '120.22', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch':
'1574617407', 'max_deflection': '0.088706', 'axis_ratio': '0.206277', 'p2p_azimuth_unwrapped': '129.031963', 'wind_speed_3': '6.8', 'wind_dir_3_corr': '119.92666666666666', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617410', 'max_deflection': '0.113769', 'axis_ratio': '0.031599', 'p2p_azimuth_unwrapped': '136.972528', 'wind_speed_3': '5.8', 'wind_dir_3_corr': '121.21333333333332', 'Dirp': '0.0437777777777777', 'TSea':
'0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617413', 'max_deflection': '0.101917', 'axis_ratio': '0.211231', 'p2p_azimuth_unwrapped': '136.260781', 'wind_speed_3': '7.166666666666667', 'wind_dir_3_corr': '122.21333333333332', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617416', 'max_deflection': '0.101917', 'axis_ratio': '0.211231', 'p2p_azimuth_unwrapped': '136.260781', 'wind_speed_3': '8.566666666666668', 'wind_dir_3_corr': '130.74666666666667', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617419', 'max_deflection': '0.094098', 'axis_ratio': '0.399637', 'p2p_azimuth_unwrapped': '132.043156', 'wind_speed_3': '9.533333333333331', 'wind_dir_3_corr': '133.58', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095',
'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617422', 'max_deflection': '0.093638', 'axis_ratio': '0.422638', 'p2p_azimuth_unwrapped': '127.984458', 'wind_speed_3': '9.233333333333333', 'wind_dir_3_corr': '130.48', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617425', 'max_deflection': '0.093638', 'axis_ratio': '0.422638', 'p2p_azimuth_unwrapped': '127.984458', 'wind_speed_3': '7.8', 'wind_dir_3_corr': '127.94666666666669', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617428', 'max_deflection': '0.080389', 'axis_ratio': '0.46163', 'p2p_azimuth_unwrapped': '126.487152', 'wind_speed_3': '8.033333333333333', 'wind_dir_3_corr': '129.85333333333332', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617431', 'max_deflection': '0.06001', 'axis_ratio': '0.459857', 'p2p_azimuth_unwrapped': '125.488946', 'wind_speed_3': '8.6', 'wind_dir_3_corr': '123.85666666666668', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617434', 'max_deflection': '0.06001', 'axis_ratio': '0.459857', 'p2p_azimuth_unwrapped': '125.488946', 'wind_speed_3': '7.866666666666667', 'wind_dir_3_corr': '125.31', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617437', 'max_deflection': '0.051303', 'axis_ratio': '0.48962', 'p2p_azimuth_unwrapped': '120.533999', 'wind_speed_3': '7.133333333333333', 'wind_dir_3_corr': '127.05333333333334', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617440', 'max_deflection': '0.048917', 'axis_ratio': '0.461496', 'p2p_azimuth_unwrapped': '93.947313', 'wind_speed_3': '6.8', 'wind_dir_3_corr': '124.64666666666666', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617443', 'max_deflection': '0.046923', 'axis_ratio': '0.266373', 'p2p_azimuth_unwrapped': '95.601589', 'wind_speed_3': '7.266666666666667', 'wind_dir_3_corr': '125.21333333333332', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617446', 'max_deflection': '0.046923', 'axis_ratio': '0.266373', 'p2p_azimuth_unwrapped': '95.601589', 'wind_speed_3': '7.433333333333334', 'wind_dir_3_corr': '124.48', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617449', 'max_deflection': '0.037378', 'axis_ratio': '0.168468', 'p2p_azimuth_unwrapped': '122.733648', 'wind_speed_3': '7.066666666666666', 'wind_dir_3_corr': '123.12333333333332', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617452', 'max_deflection': '0.066545', 'axis_ratio': '0.050011', 'p2p_azimuth_unwrapped': '141.457286', 'wind_speed_3': '6.166666666666667', 'wind_dir_3_corr': '117.46666666666664', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617455', 'max_deflection': '0.066545', 'axis_ratio': '0.050011', 'p2p_azimuth_unwrapped': '141.457286', 'wind_speed_3': '5.733333333333333', 'wind_dir_3_corr': '121.70666666666666', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617458', 'max_deflection': '0.056123', 'axis_ratio': '0.244481', 'p2p_azimuth_unwrapped': '144.491304', 'wind_speed_3': '6.266666666666667', 'wind_dir_3_corr': '123.19666666666669', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617461', 'max_deflection': '0.047253', 'axis_ratio': '0.030347', 'p2p_azimuth_unwrapped': '153.002107', 'wind_speed_3': '7.0', 'wind_dir_3_corr': '128.76333333333335', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617464', 'max_deflection': '0.047253', 'axis_ratio': '0.030347', 'p2p_azimuth_unwrapped': '153.002107', 'wind_speed_3': '7.266666666666667', 'wind_dir_3_corr': '127.88', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617467', 'max_deflection': '0.056352', 'axis_ratio': '0.045659', 'p2p_azimuth_unwrapped': '163.87994', 'wind_speed_3': '7.3', 'wind_dir_3_corr': '126.15000000000002', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617470', 'max_deflection': '0.065982', 'axis_ratio': '0.287275', 'p2p_azimuth_unwrapped': '162.596109', 'wind_speed_3': '7.733333333333333', 'wind_dir_3_corr': '125.62666666666668', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617473', 'max_deflection': '0.067253', 'axis_ratio': '0.236346', 'p2p_azimuth_unwrapped': '162.467144', 'wind_speed_3': '7.566666666666666', 'wind_dir_3_corr': '122.71333333333332', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617476', 'max_deflection': '0.067253', 'axis_ratio': '0.236346', 'p2p_azimuth_unwrapped': '162.467144', 'wind_speed_3': '7.733333333333333', 'wind_dir_3_corr': '127.58', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617479', 'max_deflection': '0.072179', 'axis_ratio': '0.158162', 'p2p_azimuth_unwrapped': '173.083129', 'wind_speed_3': '8.633333333333333', 'wind_dir_3_corr': '125.36', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617482', 'max_deflection': '0.085216', 'axis_ratio': '0.181058', 'p2p_azimuth_unwrapped': '167.428047', 'wind_speed_3': '7.899999999999999', 'wind_dir_3_corr': '119.06333333333332', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617485', 'max_deflection': '0.085216', 'axis_ratio': '0.181058', 'p2p_azimuth_unwrapped': '167.428047', 'wind_speed_3': '7.266666666666667', 'wind_dir_3_corr': '115.29666666666668', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617488', 'max_deflection': '0.090764', 'axis_ratio': '0.317516', 'p2p_azimuth_unwrapped': '165.206019', 'wind_speed_3': '6.3', 'wind_dir_3_corr': '122.88666666666666', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617491', 'max_deflection': '0.097818', 'axis_ratio': '0.342115', 'p2p_azimuth_unwrapped': '173.213454', 'wind_speed_3': '6.9', 'wind_dir_3_corr': '127.68', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617494', 'max_deflection': '0.097818', 'axis_ratio': '0.342115', 'p2p_azimuth_unwrapped': '173.213454', 'wind_speed_3': '7.266666666666667', 'wind_dir_3_corr': '125.05', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617497', 'max_deflection': '0.107395', 'axis_ratio': '0.456921', 'p2p_azimuth_unwrapped': '168.193844', 'wind_speed_3': '6.6000000000000005', 'wind_dir_3_corr': '127.48000000000002', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617500', 'max_deflection': '0.106947', 'axis_ratio': '0.448652', 'p2p_azimuth_unwrapped': '166.158813', 'wind_speed_3': '5.833333333333333', 'wind_dir_3_corr': '133.88', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617503', 'max_deflection': '0.106947', 'axis_ratio': '0.448652', 'p2p_azimuth_unwrapped': '166.158813', 'wind_speed_3': '6.033333333333334', 'wind_dir_3_corr': '131.91333333333333', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617506', 'max_deflection': '0.095038', 'axis_ratio': '0.493897', 'p2p_azimuth_unwrapped': '168.921264', 'wind_speed_3': '5.333333333333333', 'wind_dir_3_corr': '125.21333333333332', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617509', 'max_deflection': '0.091908', 'axis_ratio': '0.59676', 'p2p_azimuth_unwrapped': '159.90498', 'wind_speed_3': '4.633333333333334', 'wind_dir_3_corr': '137.88', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617512', 'max_deflection': '0.092962', 'axis_ratio': '0.464975', 'p2p_azimuth_unwrapped': '163.425802', 'wind_speed_3': '4.6000000000000005', 'wind_dir_3_corr': '140.38', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617515', 'max_deflection': '0.092962', 'axis_ratio': '0.464975', 'p2p_azimuth_unwrapped': '163.425802', 'wind_speed_3': '6.166666666666667', 'wind_dir_3_corr': '131.94666666666666', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617518', 'max_deflection': '0.082552', 'axis_ratio': '0.608198', 'p2p_azimuth_unwrapped': '157.390524', 'wind_speed_3': '6.533333333333334', 'wind_dir_3_corr': '135.6266666666667', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617521', 'max_deflection': '0.062386', 'axis_ratio': '0.839131', 'p2p_azimuth_unwrapped': '94.627329', 'wind_speed_3': '6.599999999999999', 'wind_dir_3_corr': '133.69', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617524', 'max_deflection': '0.062386', 'axis_ratio': '0.839131', 'p2p_azimuth_unwrapped': '94.627329', 'wind_speed_3': '6.8', 'wind_dir_3_corr': '133.41', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617527', 'max_deflection': '0.062654', 'axis_ratio': '0.812063', 'p2p_azimuth_unwrapped': '27.966355', 'wind_speed_3': '6.7', 'wind_dir_3_corr': '128.08', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617530', 'max_deflection': '0.062654', 'axis_ratio': '0.812063', 'p2p_azimuth_unwrapped': '27.966355', 'wind_speed_3': '5.8', 'wind_dir_3_corr': '123.44666666666669', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617533', 'max_deflection': '0.070624', 'axis_ratio': '0.632816', 'p2p_azimuth_unwrapped': '8.228645', 'wind_speed_3': '6.2', 'wind_dir_3_corr': '117.15666666666668', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617536', 'max_deflection': '0.061703', 'axis_ratio': '0.89605', 'p2p_azimuth_unwrapped': '-70.987767', 'wind_speed_3': '5.366666666666667', 'wind_dir_3_corr': '126.02333333333335', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617539', 'max_deflection': '0.061703', 'axis_ratio': '0.89605', 'p2p_azimuth_unwrapped': '-70.987767', 'wind_speed_3': '3.6666666666666665', 'wind_dir_3_corr': '120.51333333333332', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617542', 'max_deflection': '0.068981', 'axis_ratio': '0.375669', 'p2p_azimuth_unwrapped': '-143.545846', 'wind_speed_3': '3.9333333333333336', 'wind_dir_3_corr': '131.04666666666665', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617545', 'max_deflection': '0.068981', 'axis_ratio': '0.375669', 'p2p_azimuth_unwrapped': '-143.545846', 'wind_speed_3': '4.466666666666666', 'wind_dir_3_corr': '137.74666666666667', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617548', 'max_deflection': '0.079783', 'axis_ratio': '0.387363', 'p2p_azimuth_unwrapped': '-170.166431', 'wind_speed_3': '4.866666666666666', 'wind_dir_3_corr': '141.1233333333333', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617551', 'max_deflection': '0.078098', 'axis_ratio': '0.451894', 'p2p_azimuth_unwrapped': '-158.901268', 'wind_speed_3': '4.7', 'wind_dir_3_corr': '142.95333333333335', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617554', 'max_deflection': '0.071379', 'axis_ratio': '0.261267', 'p2p_azimuth_unwrapped': '-145.10893', 'wind_speed_3': '4.133333333333333', 'wind_dir_3_corr': '142.51333333333332', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617557', 'max_deflection': '0.071379', 'axis_ratio': '0.261267', 'p2p_azimuth_unwrapped': '-145.10893', 'wind_speed_3': '4.933333333333334', 'wind_dir_3_corr': '127.14666666666668', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617560', 'max_deflection': '0.087098', 'axis_ratio': '0.198512', 'p2p_azimuth_unwrapped': '-142.903441', 'wind_speed_3': '5.5', 'wind_dir_3_corr': '128.74666666666667', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav':
'0.0023666666666666'}, {'epoch': '1574617563', 'max_deflection': '0.070407', 'axis_ratio': '0.207153', 'p2p_azimuth_unwrapped': '-140.893006', 'wind_speed_3': '5.833333333333333', 'wind_dir_3_corr': '134.83666666666667', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222',
'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617566', 'max_deflection': '0.070407', 'axis_ratio': '0.207153', 'p2p_azimuth_unwrapped': '-140.893006', 'wind_speed_3': '5.333333333333333', 'wind_dir_3_corr': '142.42333333333332', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617569', 'max_deflection': '0.062332', 'axis_ratio': '0.201935', 'p2p_azimuth_unwrapped': '-122.897102', 'wind_speed_3': '5.9', 'wind_dir_3_corr': '135.54333333333332', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617572', 'max_deflection': '0.06568', 'axis_ratio': '0.026964', 'p2p_azimuth_unwrapped': '-101.038239', 'wind_speed_3': '5.766666666666666', 'wind_dir_3_corr': '132.18666666666667', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617575', 'max_deflection': '0.06568', 'axis_ratio': '0.026964', 'p2p_azimuth_unwrapped': '-101.038239', 'wind_speed_3': '5.666666666666667', 'wind_dir_3_corr': '137.71', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617578', 'max_deflection': '0.074982', 'axis_ratio': '0.331546', 'p2p_azimuth_unwrapped': '-91.115161', 'wind_speed_3': '6.0',
'wind_dir_3_corr': '140.49333333333334', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617581', 'max_deflection': '0.076039', 'axis_ratio': '0.56425', 'p2p_azimuth_unwrapped': '-94.717487', 'wind_speed_3': '6.2', 'wind_dir_3_corr': '137.76', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617584', 'max_deflection': '0.076039', 'axis_ratio': '0.56425', 'p2p_azimuth_unwrapped': '-94.717487', 'wind_speed_3': '6.7', 'wind_dir_3_corr': '133.15333333333334', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617587', 'max_deflection': '0.061903', 'axis_ratio': '0.744827', 'p2p_azimuth_unwrapped': '-83.168312', 'wind_speed_3': '6.066666666666666', 'wind_dir_3_corr': '131.35333333333332', 'Dirp': '0.0437777777777777',
'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617590', 'max_deflection': '0.074259', 'axis_ratio': '0.628274', 'p2p_azimuth_unwrapped': '-62.701387', 'wind_speed_3': '6.266666666666667', 'wind_dir_3_corr': '128.15', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617593', 'max_deflection': '0.074259', 'axis_ratio': '0.628274', 'p2p_azimuth_unwrapped': '-62.701387', 'wind_speed_3': '6.533333333333334', 'wind_dir_3_corr': '123.16', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617596', 'max_deflection': '0.081239', 'axis_ratio': '0.756065', 'p2p_azimuth_unwrapped': '-28.109222', 'wind_speed_3': '7.333333333333333', 'wind_dir_3_corr': '122.89333333333332', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617599', 'max_deflection': '0.079346', 'axis_ratio': '0.603799', 'p2p_azimuth_unwrapped': '11.647489', 'wind_speed_3': '6.533333333333334', 'wind_dir_3_corr': '125.22333333333334',
'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617602', 'max_deflection': '0.079346', 'axis_ratio': '0.603799', 'p2p_azimuth_unwrapped': '11.647489', 'wind_speed_3': '5.7', 'wind_dir_3_corr': '122.10666666666668', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617605', 'max_deflection': '0.070314', 'axis_ratio': '0.624271', 'p2p_azimuth_unwrapped': '13.35717', 'wind_speed_3': '6.0', 'wind_dir_3_corr': '124.18333333333334', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617608', 'max_deflection': '0.062602', 'axis_ratio': '0.630267', 'p2p_azimuth_unwrapped': '15.184767', 'wind_speed_3': '6.333333333333333', 'wind_dir_3_corr': '129.25666666666666', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617611', 'max_deflection': '0.062602', 'axis_ratio': '0.630267', 'p2p_azimuth_unwrapped': '15.184767', 'wind_speed_3': '6.2', 'wind_dir_3_corr': '133.10333333333332', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617614', 'max_deflection': '0.054864', 'axis_ratio': '0.31044', 'p2p_azimuth_unwrapped': '2.562245', 'wind_speed_3': '5.933333333333334', 'wind_dir_3_corr': '133.73333333333335', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617617',
'max_deflection': '0.046949', 'axis_ratio': '0.139896', 'p2p_azimuth_unwrapped': '17.046552', 'wind_speed_3': '6.4', 'wind_dir_3_corr': '137.81666666666666', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617620', 'max_deflection': '0.046949', 'axis_ratio': '0.139896', 'p2p_azimuth_unwrapped': '17.046552', 'wind_speed_3': '6.566666666666666', 'wind_dir_3_corr': '136.11666666666665', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}, {'epoch': '1574617623', 'max_deflection': '0.052908', 'axis_ratio': '0.27527', 'p2p_azimuth_unwrapped': '26.039389', 'wind_speed_3': '5.966666666666666', 'wind_dir_3_corr': '132.33666666666667', 'Dirp': '0.0437777777777777', 'TSea': '0.0059722222222222', 'Hmax': '0.00095', 'Tmax': '0.0030166666666666', 'Hav': '0.0300111111111111', 'Tav': '0.0023666666666666'}]


def predict_MLP(data):
    reconstructed_model = keras.models.load_model("MLPmodel.h5")
    data = pd.DataFrame.from_dict(data)
    data = data.iloc[:, 3:11]
    results = data.iloc[:, 0:3]
    data = data.to_numpy()
    train = results.to_numpy()
    data = data.astype('float64')
    data = data.astype('int32')
    results = reconstructed_model.predict(data)
    np.savetxt('predicteddata.csv', results, delimiter=',')
predict_MLP(data)

import numpy as np


########################################################################
#                         Download information                         #
########################################################################

FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSefhHMMvN0Uwjnj_vWQgYSvtFOtaoGFWsTIcRuBTnP09NHR7A/viewform?fbzx=5530674395784263977'

# DALES in LAS format
#LAS_TAR_NAME = 'dales_semantic_segmentation_las.tar.gz'
#LAS_UNTAR_NAME = "dales_las"

# DALES in PLY format
PLY_TAR_NAME = 'dales_semantic_segmentation_ply.tar.gz'
PLY_UNTAR_NAME = "parislille"

# DALES in PLY, only version with intensity and instance labels
OBJECTS_TAR_NAME = 'DALESObjects.tar.gz'
OBJECTS_UNTAR_NAME = "parislille"


########################################################################
#                              Data splits                             #
########################################################################

# The validation set was arbitrarily chosen as the x last train tiles:
"""
TILES = {
    'train': [
        'Lille1_1',
        'Lille1_2',
        'Lille2',
        'Paris'],

    'val': [
        'Paris'],

    'test': [
        'ajaccio_2',
        'ajaccio_57',
        'dijon_9']}
"""
TILES = {
    'train': [
        'Paris','Lille1_1_Rotated'],

    'val': [
        'Lille2_Rotated'],

    'test': [
        'Lille1_2_RotatedAscii']}

########################################################################
#                                Labels                                #
########################################################################

PARISLILLE_NUM_CLASSES = 9

ID2TRAINID = np.asarray([0,1,2,3,4,5,6,7,8,9])

CLASS_NAMES = [
    'Unclassified',
    'Ground',
    'Building',
    'Poal Road Sign Traffic Light',
    'Bollard Small Pole',
    'Trash Can',
    'Barrier',
    'Pedestrian',
    'Car',
    'Natural Vegetation']

CLASS_COLORS = np.asarray([
    [243, 214, 171],  # sunset
    [ 70, 115,  66],  # fern green
    [233,  50, 239],
    [243, 238,   0],
    [190, 153, 153],
    [  0, 233,  11],
    [239, 114,   0],
    [214,   66,  54],  # vermillon
    [  0,   8, 116],
    [  20,   20, 20]])

# For instance segmentation
#MIN_OBJECT_SIZE = 100
#THING_CLASSES = [2, 3, 4, 5, 6, 7]
#STUFF_CLASSES = [i for i in range(DALES_NUM_CLASSES) if not i in THING_CLASSES]

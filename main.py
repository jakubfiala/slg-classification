from __future__ import print_function
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
import numpy as np
import mock_data2

# initial distance is infinity so that it's larger than anything
dist = float("inf")
closest_gesture = None

for gesture in mock_data2.gestures:
    # calculate the DTW distance between the new gesture and each of the saved gestures
    cur_dist, path = fastdtw(mock_data2.gesture_new, gesture, dist=euclidean)
    # if smaller than the smallest distance to date, save
    if cur_dist < dist:
        dist = cur_dist
        closest_gesture = gesture

print(closest_gesture)
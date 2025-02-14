import numpy as np
import random

class Encoder:
    def __init__(self, activities):
        self.activities = activities
        self.activity_to_vector = {activity: idx for idx, activity in enumerate(activities)}
        self.vector_to_activity = {idx: activity for idx, activity in enumerate(activities)}
        self.num_activities = len(activities)

    def encode(self, trace):

        return [self.activity_to_vector[activity] for activity in trace]

    def decode(self, encoded_trace):

        return [self.vector_to_activity[idx] for idx in encoded_trace]


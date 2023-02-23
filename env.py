"""
Environment for rrt_2D
@author: huiming zhou
"""
import numpy as np

class Env:
    def __init__(self):
        self.x_range = (0, 50)
        self.y_range = (0, 50)
        self.obs_boundary = self.obs_boundary()
        self.obs_circle = self.obs_circle()
        self.obs_rectangle = self.obs_rectangle()

    @staticmethod
    def obs_boundary():
        obs_boundary = [
            [0, 0, 1, 50],
            [0, 50, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 50],
            
        ]
        return obs_boundary

    @staticmethod
    def obs_rectangle():
        #t1 = np.random.randint(10,20)
        #k1 = np.random.randint(10,20)
        #t2 = np.random.randint(30,50)
        #k2 = np.random.randint(30,50)
        #t3 = np.random.randint(40,45)
        #k3 = np.random.randint(40,45)
        t1=15
        k1=18
        t2 =33
        k2=40
        t3=41
        k3=42

        obs_rectangle = [
            [12, 12, 8, 4],
            [11, 8, 4, 5],
            [30, 32, 8, 11],
            [10, 30, 10, 12],
            [10,15,6,5],
            [23,40,6,8],
            #[int(t3),int(k3),3,3],
            [43,18,4,4],
            [15,28,5,6],
            [25,35,6,3],
            [38,15,8,5],
            [15,4,6,8]
        ]
        return obs_rectangle

    @staticmethod
    def obs_circle():
        obs_cir = [
            #[7, 12, 3],
            #[46, 20, 2],
            #[15, 5, 2],
            #[37, 7, 3],
            #[37, 23, 3]
        ]

        return obs_cir

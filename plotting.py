
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import sys
from scipy.interpolate import make_interp_spline
from scipy.interpolate import BPoly
sys.path.append(os.path.dirname(os.path.abspath(__file__)) +
                "/../../Sampling_based_Planning/")

#from Sampling_based_Planning.rrt_2D import env
import env

class Plotting:
    def __init__(self, x_start, x_goal):
        self.xI, self.xG = x_start, x_goal
        self.env = env.Env()
        self.obs_bound = self.env.obs_boundary
        self.obs_circle = self.env.obs_circle
        self.obs_rectangle = self.env.obs_rectangle

    def animation(self, nodelist, path,path1, name, animation=False):
        self.plot_grid(name)
        self.plot_visited(nodelist, animation)
        self.plot_path(path)
        self.plot_path1(path1)
        plt.show()
    def animation1(self,nodelist,path,path2, name,animation=False):
        self.plot_grid(name)
        self.plot_visited(nodelist, animation)
        self.plot_path(path)
        #self.plot_path1(path1)
        self.plot_path2(path2)
        plt.show()
        

    def animation_connect(self, V1, V2, path, name):
        self.plot_grid(name)
        self.plot_visited_connect(V1, V2)
        self.plot_path(path)

    def plot_grid(self, name):
        fig, ax = plt.subplots()

        for (ox, oy, w, h) in self.obs_bound:
            ax.add_patch(
                patches.Rectangle(
                    (ox, oy), w, h,
                    edgecolor='black',
                    facecolor='black',
                    fill=True
                )
            )

        for (ox, oy, w, h) in self.obs_rectangle:
            ax.add_patch(
                patches.Rectangle(
                    (ox, oy), w, h,
                    #edgecolor='black',
                    facecolor='gray',
                    fill=True
                )
            )

        for (ox, oy, r) in self.obs_circle:
            ax.add_patch(
                patches.Circle(
                    (ox, oy), r,
                    edgecolor='black',
                    facecolor='gray',
                    fill=True
                )
            )

        plt.plot(self.xI[0], self.xI[1], "bs", linewidth=3)
        plt.plot(self.xG[0], self.xG[1], "gs", linewidth=3)
        #plt.show()

        plt.title(name)
        plt.axis("equal")

    @staticmethod
    def plot_visited(nodelist, animation):
        if animation:
            count = 0
            for node in nodelist:
                count += 1
                if node.parent:
                    plt.plot([node.parent.x, node.x], [node.parent.y, node.y], "-g",linewidth=0.5)
                    plt.gcf().canvas.mpl_connect('key_release_event',
                                                 lambda event:
                                                 [exit(0) if event.key == 'escape' else None])
                    if count % 10 == 0:
                        plt.pause(0.001)
                    
        else:
            for node in nodelist:
                if node.parent:
                    plt.plot([node.parent.x, node.x], [node.parent.y, node.y], "-g",linewidth=0.5)

    @staticmethod
    def plot_visited_connect(V1, V2):
        len1, len2 = len(V1), len(V2)

        for k in range(max(len1, len2)):
            if k < len1:
                if V1[k].parent:
                    plt.plot([V1[k].x, V1[k].parent.x], [V1[k].y, V1[k].parent.y], "-g")
            if k < len2:
                if V2[k].parent:
                    plt.plot([V2[k].x, V2[k].parent.x], [V2[k].y, V2[k].parent.y], "-g")

            plt.gcf().canvas.mpl_connect('key_release_event',
                                         lambda event: [exit(0) if event.key == 'escape' else None])

            if k % 2 == 0:
                plt.pause(0.001)

        plt.pause(0.01)

    @staticmethod
    def plot_path(path):
        if len(path) != 0:
            plt.plot([x[0] for x in path], [x[1] for x in path], '-k', linewidth=1)
            plt.pause(0.01)
        plt.pause(2)
        #plt.show()
    def plot_path1(self,path):
        if len(path) != 0:
            plt.plot([x[0] for x in path], [x[1] for x in path], '-b', linewidth=2)
            plt.pause(2)
    def plot_path2(self,path):
        aa=[]
        bb=[]
        if len(path) != 0:
            
            
            for i in range(len(path)):
                aa.append(path[i][0])
                bb.append(path[i][1])
            print(aa)
            print(bb)
            ss = np.array(aa)
            

            qq =np.array(bb)
            X_Y_Spline = make_interp_spline(ss, qq)
            #curve = BPoly(aa,bb)
            X_ = np.linspace(ss.min(),ss.max(), 500)
            #Y_ = curve(X_)
            Y_ = X_Y_Spline(X_)
            plt.plot(X_,Y_, '-r', linewidth=2)
            plt.pause(1)
        #plt.show()
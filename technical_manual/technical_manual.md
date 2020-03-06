![](https://lh3.googleusercontent.com/8TlSVNKd3qhepP0v-Uk2fSnpO7MIU16-h-8feKt-doAqfXKWOORL0A-MVBzpOCZmToXVi-99qGk8Qh_BXWuW8Xgb6-TlOrqbIC-JLkEu-Mj2qK8URRVU6zN4VZ7vCehjXxuN8B4h)

SennAI - User Manual

CA326 Project by Connell Kelly & Patrick Gildea

**Table of Contents**

    Title:                                                      Page:
    1\. Introduction

    - 1.1. Overview                                             2

    - 1.2. Glossary                                             3

    2\. 2. System Architecture                                  4

    3\. High-Level Design                                       5
    
    4\. Problems and Resolution                                 8
    
    5\. Installation Guide                                      9

1\. Introduction
================

1.1. Overview:
==============

Welcome to the SennAI technical manual. The goal of this document is to explain the initial design and the current design of CA326 project, 'SennAI'. It will run through several of the major changes that the project went through (which is also described in more detail in our series of blogs). We were intent on delivering a product based on our functional specifications last semester and we believe that we have fulfilled the vast bulk of our promises.

The goal of this overall project however is to demonstrate the potential of incorporating reinforcement learning into a serious gaming environment and how this can be further implemented into other formats. To demonstrate this in a way users can understand and involve themselves in, the project will be presented as a top-down, 2D racing game with bright contrasting colours and simple designs. It is easy to understand the competitive element of a race and improving lap times, which is the perfect template to demonstrate an AI agent learning to navigate a racetrack through trial and error.

Reinforcement learning is an area of machine learning and for this project we will be making heavy incorporation of the model-free Q-Learning algorithm to instruct the AI agent on how to improve. All of this will be supported by the reinforcement learning toolkit, OpenAI Gym and many functions provided by Pygame. We will go into further detail as we proceed in this document. We've described much information already in regards to the design of various parts of the program in our blogs over the course of five weeks which you can find here: <https://sennaidev.blogspot.com/>

1.2. Glossary:
==============

Menu: Window in program where the user can select what mode that they would like to operate in.

Checkpoint: Visible/Invisible points of reference for the program to record the progress of the user or AI agent's car.

Lidar: A detection system which works on the principle of radar, but uses light from a laser. Detects specific colours in this program.

Reinforcement Learning: An area of machine learning about taking suitable action to maximize reward in a particular situation. It is employed by various software and machines to find the best possible behavior or path it should take in a specific situation.

Q-Learning: A model-free, value-based, reinforcement learning algorithm which is used to find the optimal action-selection policy using a Q function.

OpenAI Gym: An open-source toolkit for developing and comparing reinforcement learning algorithms.

PyGame: A cross-platform set of Python modules designed for writing video games.

Numpy (.npy): A general-purpose array-processing package.

Cloudpickle: Extended pickling support for Python objects.

2\. System Architecture
=======================

![](https://lh3.googleusercontent.com/SCP3iPW-JXgQj8oTkVO9CoF8JgvHlOseKd1B0PJrygZx9RKafYsf-0wYMJsceXOwor0RD1oTVpmyVnrEdVbF6ecznGuDd5mdp-wh8mI0QaO7t60JdW3QEIe3OUO4SS6Zsdv2Ia8f)

SennAI Static Component Diagram (2nd TrainMgr should be LeaderboardMgr)

Above is a static component diagram that conceptualizes the architectural components involved in SennAI's operation. There are several main processors that handle data in the program which considers what mode the user has initiated, what Q-Learning data needs to be recorded or loaded and what information must be saved to the leader after each generation. The components that manage more specific tasks are listed below and incorporate each mode, the Q-Table .npy data and timestep information to be used in the leaderboards. Each of these components have many more moving parts involved, but this is a diagrammatic overview of all components at once.

3\. High-Level Design
=====================

 ![](https://lh5.googleusercontent.com/9BjWAv4kZ7iPZqlUDrtTq8LCuuyVIa6rKT07f3jwytjmpxTAfpt7LOBqRL7qZByNVNlgnA-5m_Ose0fz58In4KUEKVu_oAkhF35U7GbQg4oiDfQNjzvnrAr_K1sNAzAEhQzCUUPc)

High-level Design Diagram of SennAI

Along with the high-level design diagram above, the high-level design of the project revolves around 4 particular parties, being the user, the race window, the Q-Learning process and the leaderboard. Each part is connected to another to create a web of interconnected functions and classes throughout the various .py and .npy files used in the project. The process in described in order below:

1.  Open SennAI

1.  Presented with menu offering four choices

3.  Select 'Play'

1.  Chose easy difficulty (loads 5,000 .npy Q-Table generations)

2.  Chose normal difficulty (loads 10,000 .npy Q-Table generations)

3.  Select start, wait through loading screen and use controls described in the user manual to control the car.

4.  SennAI agent pulls it's exploits track navigation with Q-Table data

5.  Winner is announced and race restarts until user quits

5.  Select 'Train'

1.  Choose a generation level from 0 to 20,000 in steps of 10,000.

2.  SennAI agents attempts to complete racetrack in real-time and Q-Learning data is loaded and recorded.

3.  Unless the window is closed, SennAI will keep generating new generation episodes until it reaches ten million, though the size of the numpy Q-Table would become unmanageable.

7.  Select 'Leaderboard'

1.  Leaderboard is updated with recent generation episode results for the user the view

2.  Return to the menu by selecting back

![](https://lh5.googleusercontent.com/foZ-Qm58RZSRVQv0BUn2o4--zkpvNoIJH61Nw_AuoSjdlqNOQlVYshJVrUr9LbcwxT4mYqTokL8UNvSvYrA2PR7uCraNm4sGplwSSPFt99LtMYG1p1-YbXi2PJIKqMVhiZCLoQNv)

Data Flow Diagram for SennAI

This DFD fulfills the task of delving more deeply into each mode, how they are used and what data is exchanged between them. There are three modes that the user can choose from and each one creates and pulls data in different ways. What happens in one mode however has no bearing on what happens in another, barring leaderboard which records the recent generation episodes from the Play mode.￼ These diagrams are updated and overhauled versions of diagrams used in the functional spec. This was necessary to stay in line with our original specifications while also accommodating new requirements and any that were abandoned during developing.

4\. Problems and Resolution
===========================

We encountered a number of problems while developing our project and have compiled several of the most prominent ones here alongside their potential solutions:

Exit While Loading
------------------

We noticed towards the end of development that when loading a race from 'Play' mode you cannot exit the program by tapping the x in the corner of the pygame window, reason for this being that we cannot check for input from the user while the program is inside of the load_and_simulate() function.  Incorporating multithreading into our program could lead to us being able to check for user input while the q-table is loading.

Lengthy load in Play Mode
-------------------------

Loading the Q-tables for the premade difficulties in Play Mode takes around 30 seconds, this isn't much of a surprise as it can be taxing to load a massive .npy Q-Table file for the program, but we'd like to alleviate this if possible, maybe through caching these files. 

Lidar & Checkpoint Visualisation
--------------------------------

While we successfully developed a way to visually represent the AI agents lidar systems and appropriate race checkpoints, we didn't have enough time to set up a way where the user can toggle them on and off in the 'Train' menu. With more time, some checks could be set up in the program's code that coincide with the option to enable them in the 'Train' menu.

Default Generation Issue
------------------------

After training a generation, if the user leaves the window and returns to the 'Train' mode section, they'll observe that the default generation value is the one that they left on. A check can be put in place to make sure that the value always defaults to 0 when the use enters 'Train' mode.

Smoother Car Controls
---------------------

Currently the car operates on what are known as 'tank controls'. This is where the car has the ability to rotate on the spot and cannot turn without rotating entirely, similarly to a tank with threads instead of wheels. A more detailed controls implementation could help alleviate this.

5\. Installation Guide
======================

Before installation of the main zip folder you need to install the pygame, gym and pygamemenu modules, which can be done via pip installation on the command line.

1.  Install the zip file from.

2.  Unzip the folder

3.  Download q-tables 5000_aft.npy and 10000_aft.npy by following the link given to our google drive folder and place them in the unzipped folder at that same level as menu.py (top-level)

You are now ready to run the program through the terminal
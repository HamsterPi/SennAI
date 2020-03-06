![](https://lh3.googleusercontent.com/b-8myRM7AQSh3NZegexL1AuMLFJv1lHDaXWFNpi6vwZoxC18lGBm0FFEEqA8d3fCRcjre_d2aBRIeyL1etZc6aW1CGzDYqNdM2EKRd-3IQPPwPmHS9PRjsAH45LJSOK5LM4YXFyT)
* * * * *
  
* * * * *

**SennAI - User Manual**

CA326 Project by Connell Kelly and Patrick Gildea

* * * * *
  
* * * * *

**Table of Contents**

    Title:                                                      Page:
    1\. Introduction

    - 1.1. Overview                                             2

    - 1.2. Concepts                                             2

    - 1.3 Controls                                              3

    2\. Program Execution

    - 2.1. Start-up                                             3

    - 2.2. Mode Selection                                       4

    - 2.3 Program Operation                                     4

    3\. External Interface Requirements                         5


1\. Introduction
================

1.1 Overview
------------

Welcome to the SennAI user manual! This document will provide every piece of necessary guidance you will need to effectively operate and understand our program. In short, you will be both watching and competing with an AI agent that learns to navigate a 2D racetrack as fast as possible using reinforcement learning. This could be considered an example of serious gaming where the user has concepts of reinforcement learning demonstrated to them in a gamified context.

1.2 Concepts
------------

There are several concepts expressed in the project that a new user may be unfamiliar with, especially if unaccustomed to machine learning. Here's a short glossary of relevant terms:

**Menu:** Window in program where the user can select what mode that they would like to operate in.

**Checkpoint:** Visible/Invisible points of reference for the program to record the progress of the user or AI agent's car.

**Lidar:** A detection system which works on the principle of radar, but uses light from a laser. Detects specific colours in this program.

**Reinforcement Learning:** An area of machine learning about taking suitable action to maximize reward in a particular situation. It is employed by various software and machines to find the best possible behavior or path it should take in a specific situation.

**Q-Learning:** A model-free, value-based, reinforcement learning algorithm which is used to find the optimal action-selection policy using a Q function.

**OpenAI Gym:** An open-source toolkit for developing and comparing reinforcement learning algorithms.

**PyGame:** A cross-platform set of Python modules designed for writing video games.

**Numpy (.npy):** A general-purpose array-processing package.

1.3 Controls
------------

Listed below will be a collection of all relevant inputs for the project and their effects:

Menu:

-   Arrow keys/mouse - Navigate available choices

-   Enter/Mouse 1 - Confirm selected choice

Play Mode:

-   Arrow up - Accelerate user car

-   Arrow left - Turn user car left

-   Arrow right - Turn user car right

2\. Program Execution
=====================

2.1 Start-up
------------

Once all instructions have been followed in the instructions manual provided in the repository and all necessary external modules and extensions have been installed, you can now start up the program. To do so, complete the following (for Linux operating systems):

1.  Open terminal

2.  Access terminal where SennAI was extracted to

3.  Enter 'python3 SennAI_QL.py'

2.2 Mode Selection
------------------

![](https://lh4.googleusercontent.com/OBIzsHdB6Bgdnfxwx26CO0Up0ztISCW98TVjOUx7mFj2vSYe9Q-astI0MtdA5SVXH_mWFCMaZexIWRr8CrA59t4syP3JtwGGBdXHaj9dWqd6VxDAHwI30NoehlFOeU_TPoJFBEto)

Once the program begins, the user will be presented with the menu where they can select one of four options:

-   Play - Select the difficulty of AI agent and compete with them on a 2D race track to complete a lap the fastest without driving of course.

-   Train - Select the generation level for the AI agent to develop from and watch them improve on the racetrack in real-time. Their lidar system can also be visualised.

-   Leaderboard - Observe recent user and AI agent attempts on the racetrack.

-   Quit - The program is closed.

All selected modes (except 'Quit') can be exited from back to the menu by selecting the back button in the upper right corner of the window.

2.3 Program Operation
---------------------

### 2.3.1 'Play' Mode

![](https://lh6.googleusercontent.com/MW8bnYpH4qhH_-D2XgTGnILk3d1csK8q_zVa-N_0GCBp7RrSzCjbAX5uIKoDMpSIOgF41pxK-5i5nB0o9yo0UYAHRDp2HuU9Lczc7XaDUq5FYLfGHThB_RkiiYS-BLKT2sVBdaHq)

1.  Select 'Play' in the main menu, allowing you to choose from two  difficulties of an AI opponent.

2.  Initiate race and wait approximately 33 seconds to load the data required for the AI agent and the window will open.

3.  The race begins and the user will be expected to complete a lap of the racetrack as fast as possible without driving into the grass.

4.  When a condition is met, the window will close and the user will be notified of the outcome and returned to the menu.

**Win Condition: Complete a lap of the racetrack before the SennAI agent does or SennAI collides with the grass.**

**Lose Condition: The SennAI agent completes a lap before the user does or the user collides with the grass.**

### 2.3.2 'Train' Mode

￼![](https://lh4.googleusercontent.com/K9vizoKcXWItDPDRjLwZqJMHRLFjt68mJ7XKHFSCIShm_kXnFyeW2xtxVLdzBQ6Nr_6dpuvRxWiBB-dICj0k34kHUqytZoweoWeNFnj0BiPE8QP8gdZL1tKwAk_5y8mSnfr3xuLv)

1.  Select 'Train' in the main menu, allowing you to choose from various generation levels of an AI opponent between 0 and 10,000.

2.  Depending on the generation level selected, you may have to wait a period of time before the desired generation has been simulated and loaded, but you can observe any dynamic progress made in timesteps and points printed in terminal.

3.  When the desired generation level is loaded, you can then observe the project demonstrate it's knowledge at completing the track in real-time, while watching them actively improve with new generations.

4.  This process will proceed until the user exits the window and returns to the window.

**There are no win or lose cases here as trial and error is necessary for Q-Learning.**

### 2.3.3 'Leaderboard' Mode

1.  Select 'Leaderboard' in the main menu, allowing you to observe recently completed lap times in the program.

2.  Whenever you're done observing completed lap times, select the back button to return to the menu.

**There are no win or lose cases here.**

3\. Conclusion
==============

Thank you for using our program. We hope it has fulfilled its purpose in demonstrating the potential of reinforcement learning in a gamified context and how it can be applied to many more. If you have time to spare, we would appreciate it if you could fill out a short survey below on how you found our program.

<https://docs.google.com/forms/d/e/1FAIpQLSfqj4lI0bebZEJmZn_Fe5vjI1r3wqhbri9xtxi2nFtc_UnGgQ/viewform?usp=sf_link>
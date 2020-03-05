* * * * *
  
* * * * *

CA326

**Software Requirements Specifications**

For SennAI by Connell Kelly & Patrick Gildea (01/03/2020)

* * * * *

* * * * *

**Table of Contents**

    Title:                                                          Page:
    1\. Introduction

    - 1.1. Purpose                                                      2

    - 1.2. Intended Audience & Reading Suggestions                      2

    - 1.3. Product Scope                                                2
    
    - 1.4. References                                                   3

    2\. Overall Perspective

    - 2.1. Product Perspective                                          3

    - 2.2. Prodcut Functions                                            4

    - 2.3. User Classes and Characteristics                             4

    - 2.4. Operating Environment                                        4
    
    - 2.5. Design and Implementation Constraints                        5
    
    - 2.6. User Documentation                                           5
    
    - 2.7. Assumptions and Dependencies                                 5

    3\. External Interface Requirements

    - 3.1. User Interfaces                                              6

    - 3.2. Hardware Interfaces                                          6

    - 3.3. Software Interfaces                                          6

    - 3.4. Communications Interfaces                                    6

    4\. System Architecture                                             

    - 4.1. Play Mode                                                    7

    - 4.2. Train Mode                                                   7

    - 4.3. Leaderboard Mode                                             8

    5\. Other Nonfunctional Requirements

    - 5.1. Performance Requirements                                     8

    - 5.2. Safety Requirements                                          9
    
    - 5.3. Security Requirements                                        9
    
    - 5.4. Software Quality Attributes                                  9
    
    - 5.5. Business Rules                                               10

    7\. Appendices                                                      10

* * * * *


1\. Introduction
================

1.1 Purpose
-----------

This SRS will aiding in the description of relevant requirements for our CA326 project, SennAI. This will be a top-down, 2D, racing game that's focus is on demonstrating reinforcement learning through the gamification of Q-Learning environment with the AI agent, 'SennAI'. It will be covering several core aspects of the project and how we developed it in accordance with previously outlined requirements to the best of our abilities. In particular we will be paying attention to how we were required to design an effective Q-Learning system and how we circumvented any storage or memory issues we came across. Overall, this document will assist in bridging the gap between the developers and the users.

1.2 Intended Audience & Reading Suggestions 
--------------------------------------------

This document and associated project is intended for a wide variety of potential users and observers. This will help developers understand the preparation and resources required to successfully implement this project. Users have an opportunity to better understand the complexities behind the project by reading about the requirements that were needed for it's development. It is directly intended for our project supervisor and assessor, considering that we intend for it to be part of our overall design of the project and for it to assist in them understanding our development process. One should read this document from start to finish to understand things in an order that builds upon each point of interest.

1.3 Product Scope 
------------------

The goal of this project is to thoroughly demonstrate the potential and flexibility of reinforcement learning and how it can be used in many kinds of contexts. In particular, we will be describing how we can use a Q-Learning algorithm in conjunction with an OpenAI Gym environment to instruct the SennAI agent how to navigate a racetrack as fast as possible and then be used as a competitor for the user who will have the opportunity to race a car on the same racetrack. A user will be able to learn and understand how reinforcement learning works in a simple environment that doesn't lack any of the complexity that makes up machine learning.

1.4 References
--------------

Site that proved very useful in better understanding Q-Learning:

<https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/>

Site for learning how Q-Learning works to create effective reinforcement learning

<https://blog.floydhub.com/an-introduction-to-q-learning-reinforcement-learning/>

Useful for brushing up on unit and integration testing

<https://realpython.com/python-testing/>

2\. Overall Perspective
=======================

![](https://lh6.googleusercontent.com/koX6pfE2Arbu_a0fr_BsaDDzKhoQ2oBJ80wBubkMZ1l-g3wqU06FJvB6lauYcoFcKhm7wtMiPifDY3R_UcJYgubKpI7RCJyZxM0sgk9NegPSGkFhsYCLXqWtudVRrdwXdlUR37ch)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

High-level Design Diagram of SennAI
-----------------------------------

2.1 Product Perspective
-----------------------

SennAI is a new, self-contained product dedicated to effectively demonstrating the gamification of a reinforcement learning environment. It will provide the user with the opportunity to race again a desired difficulty of AI agent, train the AI agent at various levels or observe the leaderboard for the best times accomplished.

![](https://lh6.googleusercontent.com/1-gZ6zi5KpG5B7c9Z4nMto5ri_yrP_s379sS5nHjTKR2pjdzDYHbN8v-XDpHET0k51IVr7-INNJEHb2KdhLytJ2CS0SWauD75P0ASRMVpT250R5PqNYaV0I3W-pNxaj0_wSmzbyr)

SennAI Static Component Diagram

2.2 Product Functions
-----------------------

Major functions of SennAI include:

-   Allow an AI agent to slowly improve its ability to navigate a set racetrack using reinforcement learning.

-   Allow the user to compete with the AI agent of a specific difficulty on the racetrack for the best lap time.

-   Allow the user to observe recent lap completions times on a leaderboard.

![](https://lh4.googleusercontent.com/tIlvA-Ej2mvMPPKyUwIwbSrEn92VvxA2mUznc67YYEAZrd9Go1IG3zCR5bM-2G1U2pUBZDdlRfG2g1_OX9WiuwI9cS-bnEKzS9M2Znbn9wwDzTtoaF_Mdw7Rn57K9LzOt2Ib9K2T)

Data Flow Diagram for SennAI

2.3 User Classes and Characteristics
------------------------------------

Not all classes are ready yet, but here are several class examples and their purposes:

-   Car() found in SennAI_Base.py provides a model with all relevant variables for the agent and user cars found in the program.

-   SennAI2D() evaluates data regarding Car() and also presents parts of the program such as the lidar visualisation.

-   Save_memory() saves a numpy table with a chosen name to the current directory.

-   Simulate() simulates the reinforcement learning process under specific parameters.

2.4 Operating Environment
-------------------------

For this project we intend to operate on Linux operating systems, specifically between OpenSuse and Ubuntu. It will be written in the Python 3.6.5 language on Sublime text editor. SennAI will incorporate several external sets of modules such as OpenAI Gym and Pygame. It will be opened through terminal, which will lead to the menu where the program can be operated independently on. Any generated Q-Tables will be saved and loaded on numpy files.

2.5 Design and Implementation Constraints
-----------------------------------------

There are several limitations and constraints that we ran into over the course of developing this project. One of the most prominent issues we encountered was that of disk space and how the lab computers we used were limited by a 500 megabyte disc space quota. We managed to get it increased to 2 gigabytes, but this still wasn't enough to store the massive Q-Table npy files we needed to generate, so this limited our project's amount of difficulties and potential tracks. By the time we had a solution in the form of flash drives, it was too late in the project's development so we scrapped the ideas and moved on. Evidently, time restrictions were another constraint that limited the scope of our project. Given the time we needed to dedicate to a busy module for the first three weeks, another week would've very likely allowed us to fulfil the project's greater ambitions.

2.6 User Documentation
----------------------

Documents (presented in markdown) to be included in the project:

-   Project Proposal

-   Functional Specifications

-   Technical Specifications

-   User Manual

-   Installation Guide

-   Software Requirements Specifications

2.7 Assumptions and Dependencies
--------------------------------

We assumed that a tile based system to assist in AI agent navigation would be our focus for the project, but we instead deemed that a lidar-based system would be far more successful. The project is currently dependent on several of the modules that OpenAI Gym provides, but we've learned enough that we would be perfectly able to attempt to develop a similar system without it or limited external support. A lot of the project's inner workings are also supported by modules and functions provided by PyGame.

3.External Interface Requirements
=================================

3.1 User Interfaces
-------------------

We had hoped to implement a fully featured menu for our project. With it the user can use the arrow keys and enter or the mouse and left click to select what mode they would like to commit to. These options will be contained within a small window and the race windows themselves will open as full screen. Play mode allows the user to select their desired difficulty and train allows them to select their desired generation level. Each of those modes can be exited via selection the exit choice. Both the menu and race window can be exited by clicking on the close window button. The user has control in the play mode where they use the arrow keys to control a user version of SennAI's car, highlighted in blue.

3.2 Hardware Interfaces
-----------------------

Our program will be supported on Ubuntu, OpenSuse and Windows 10 operating systems. A keyboard will be required to allow for control of the user. Due to the limitations of the lab machines, a large flash drive is recommended for storing npy tables which are required for offering the user various difficulties to play against.

3.3 Software Interfaces
-----------------------

There aren't a lot of data items coming into the project other than basic user input, Q-Tables and modules whose installations are detailed in the installation guide. The project does require components from OpenAI Gym (e.g. spaces), PyGame (e.g. get_at) and Cloudpickle. OpenAI Gym is a toolkit we use for effectively developing our Q-Learning algorithm. PyGame is a collection of modules that allow for the evaluation and presentation of many facets of the project. Cloudpickle extends pickling support for Python objects. While we developed this on OpenSuse, we also tested it on Ubuntu and it should also be viable on Windows 10 with the right modules installed. Q-Tables are the most prominent data item that is used in the project. After generating a number of Q-Tables during the development of the project, we have a number of .npy Q-Table files to pull AI agent navigation knowledge from. To implement a cleaner object-oriented approach, every variable and function will be placed in the appropriate classes without any global variables.

3.4 Communications Interfaces
-----------------------------

There are no communication requirements for this project.

4.System Features
=================

All Features are based on the cases seen in the above data flow diagram.

4.1 Play Mode
-------------

### 4.1.1 Description and Priority

This is the mode available to the user where they can select from two predefined difficulties of AI agent opponent, Easy and Normal and compete with them in a race. This is a high priority feature (9) as it's core to the project as it demonstrates 

### 4.1.2 Stimulus/Response Sequences

When the mode is chosen and a difficulty is selected using keyboard inputs, the play mode is initiated. The appropriate Q-Table of racing data is then loaded and simulated. The user is also given their own car to control and whoever finishes the first lap wins, followed by the window closing and returning to the menu. The users car is controlled using the arrow keys and the race will end if they collide with the edge of the track.

### 4.1.3 Functional Requirements

1.  To begin, there must be a working menu which this mode can be selected from using the keyboard keys or mouse. Of the keyboard keys, only the arrow keys and enter are accepted as inputs, while other inputs will be ignored. Clicking on non-selectable areas of the window will yield no results.

2.  From the 'Play' section, the user can again use the arrow keys and mouse to select their desired level of AI agent difficulty based on levels of generations. The appropriate .npy Q-Tables will need to be present in the directory to allow for them to be loaded and simulated.

3.  The race will take approximately 33 seconds to load and then the race will begin. The AI agent will proceed to operate independently based on the Q-Table data they are provided and the user will be tasked with completing a lap of the track faster than the agent. They can use the up arrow button to accelerate, left to steer left and right to steer right. The cars cannot reverse and there is a certain degree of momentum present in how they travel. When a car completes the track or crashes, the winner is announced and the window closes and the user is shown the menu again. The user can close the race window via the close window button and exit the menu via the exit choice.

4.2 Train Mode
--------------

### 4.2.1 Description and Priority

This is the mode available to the user where they can select from various levels of episode generation for the AI agent and watch the progress they make while reaching this level and what do after. This is the highest priority feature (9) as it carefully illustrates our most important feature, reinforcement learning in action and data to support its success.

### 4.2.2 Stimulus/Response Sequences

When the mode is chosen and a generation episode is selected using keyboard inputs, train mode is initiated. Depending on whether 0 generation or more have been selected, the user will be able to view SennAI immediately learning the track alone or generating to specific level where the user can watch it continue to learn from there. It will continue generating and learning indefinitely until the user 

### 4.2.3 Functional Requirements

To begin, there must be a working menu which this mode can be selected from using the keyboard keys or mouse. Of the keyboard keys, only the arrow keys and enter are accepted as inputs, while other inputs will be ignored. Clicking on non-selectable areas of the window will yield no results.

From the 'Train' section, the user can again use the arrow keys and mouse to select their desired generation level of AI agent from 0 to 20000 in 1000 level increments. [TBD] Option to visualise the lidar system and save the desired level as a npy Q-Table file for later use.

The desired generation level will be loaded while the window is empty and then simulate the track and show the progress being made visually. SennAI will continue to generate new episodes in real-time indefinitely. The user can close the race window via the close window button and exit the menu via the exit choice.

4.3 Leaderboard Mode
--------------------

### 4.3.1 Description and Priority

This is the mode available to the user where they can select the leaderboard option in the menu and view recent generations, their timesteps and points gained.

### 4.3.2 Stimulus/Response Sequences

This mode is chosen by selecting it with either keyboard or mouse input. From there the user can view recently accomplished times by SennAI and the user which are recorded here and printed in more readable format. The user can exit back to the menu by clicking back.

### 4.3.3 Functional Requirements

To begin, there must be a working menu which this mode can be selected from using the keyboard keys or mouse. All recent lap completion/failure times must be recorded and then formatted to be presented to the user. The user will then be provided the option to exit back to the main menu when they're done.

5.Other Nonfunctional Requirements
==================================

5.1 Performance Requirements
----------------------------

There are no major performance requirements needed for this project. We've tested variations of the programs on powerful computers and a weak laptop, all of which provided an adequate system for it. No particular functions have become apparent for any performance issues. However, running more than four races at the same time can cause slow down performance speed in all program windows.

5.2 Safety Requirements
-----------------------

Our project poses no threat to the developers or users. We're not creating Skynet or anything.

5.3 Security Requirements
-------------------------

There are no security requirements needed for this project.

5.4 Software Quality Attributes
-------------------------------

An extremely important non-functional requirement for this project is adequate disc space. Throughout the projects development, we ran into numerous issues generating .npy Q-Tables. Their file sizes increase exponentially as more generations are recorded and this can quickly become a problem e.g. ten thousand generations results in a .npy file of usually over 400 megabytes.

5.5 Business Rules
------------------

These rules are not applicable to our project.

Appendix A: Glossary
--------------------

Reinforcement Learning: An area of machine learning about taking suitable action to maximize reward in a particular situation. It is employed by various software and machines to find the best possible behavior or path it should take in a specific situation.

Q-Learning: A model-free, value-based, reinforcement learning algorithm which is used to find the optimal action-selection policy using a Q function.

OpenAI Gym: An open-source toolkit for developing and comparing reinforcement learning algorithms.

PyGame: A cross-platform set of Python modules designed for writing video games.

Cloudpickle: Extended pickling support for Python objects.

Numpy (.npy): A general-purpose array-processing package.

Appendix B: Analysis Models
---------------------------

![](https://lh6.googleusercontent.com/koX6pfE2Arbu_a0fr_BsaDDzKhoQ2oBJ80wBubkMZ1l-g3wqU06FJvB6lauYcoFcKhm7wtMiPifDY3R_UcJYgubKpI7RCJyZxM0sgk9NegPSGkFhsYCLXqWtudVRrdwXdlUR37ch)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

High-level Design Diagram of SennAI (From 2)

![](https://lh6.googleusercontent.com/1-gZ6zi5KpG5B7c9Z4nMto5ri_yrP_s379sS5nHjTKR2pjdzDYHbN8v-XDpHET0k51IVr7-INNJEHb2KdhLytJ2CS0SWauD75P0ASRMVpT250R5PqNYaV0I3W-pNxaj0_wSmzbyr)

SennAI Static Component Diagram (From 2.1)

![](https://lh4.googleusercontent.com/tIlvA-Ej2mvMPPKyUwIwbSrEn92VvxA2mUznc67YYEAZrd9Go1IG3zCR5bM-2G1U2pUBZDdlRfG2g1_OX9WiuwI9cS-bnEKzS9M2Znbn9wwDzTtoaF_Mdw7Rn57K9LzOt2Ib9K2T)

Data Flow Diagram for SennAI (From 2.2)

Appendix C: To Be Determined List
---------------------------------

-   [TBD] Option to visualise the lidar system

-   [TBD] Save the desired level as a npy Q-Table file for later use.
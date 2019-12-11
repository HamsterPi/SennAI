CA
**RLAI Racing (2020)**
Functional Specification Document
By Connell Kelly & Patrick Gildea


## Table of Contents

   - 1.1. Overview...........................................................Page 1. Introduction
   - 1.2. Project Scope.....................................................Page
   - 1.3. Glossary............................................................Page
   - 2.1. Product/System Functions....................................Page 2. General Description
   - 2.2. User Characteristics and Objectives.......................Page
   - 2.3. Operational Scenarios..........................................Page
   - 2.4. Constraints.........................................................Page
   - 3.1. Software Agent & R.L..........................................Page 3. Functional Requirements
   - 3.2. Game Field..................................................... ..Page
   - 3.3. Race Ruleset.....................................................Page
   - 3.4. Interface Requirements.......................................Page
   - 3.5. User Control.....................................................Page
   - 3.6. Leaderboard.....................................................Page
- 4. System Architecture ​.......................................Page
   - 5.1. Context Diagram ................................................Page 5. High-Level Design
   - 5.2. Data Flow Diagram Diagram ...............................Page
- 6. Preliminary Schedule ​........................................Page
- 6. Appendices ​.........................................................Page


**1. Introduction**
    _A Race in RLAI Racing_

**1.1. Overview**

RLAI Racing (Reinforcement Learning and Artificial Intelligence Racing)
is an application designed to demonstrate reinforcement learning in an
interactive format. It will feature a 2D, real-time, racing game
environment that allows for a machine learning algorithm to develop
varying difficulties of an AI opponent. Reinforcement learning will be the
dataset that is enforced. There is a distinct lack of interactive
reinforcement learning demonstrations online and this project would lend
itself to alleviating that.

**1.2. Project Scope**

The goal of this project is to create an environment that incorporates
machine learning in the form of reinforcement learning. A software agent
known as ​ **_‘SennAI’_** ​will be represented as a simple car and use this
paradigm to learn how to appropriately play a top-down racing game.


The user will be given the opportunity to compete with SennAI on a
simple racetrack from a birds-eye view. The user will use various
keyboard inputs to control their car. SennAI and the user will be
represented by red and blue rectangles respectively and expected to
compete with each other for the best lap. Both cars will be able to pass
through each other without collision. Once the race has ended, the
winner will be presented in a small window. The user will then be
brought to a leaderboard compiling the best time achieved by
themselves and SennAI.
The end goal is to create a thorough demonstration of reinforcement
learning within an interactive environment. RLAI Racing aims to be an
example of the versatility and flexibility found in reinforcement learning
and how it can be effectively applied to all manner of projects, from
simple games to practical problem solvers.

**1.3. Glossary**

**1. Python:** High-level programming language used for primarily
    imperative-style programming, but can also be used for functional
    and object-oriented programming.
    
**2. OpenAI Gym:** Open-source toolkit for developing and comparing
    reinforcement learning algorithms. Created by the AI research
    company, OpenAI.
    
**3. Pygame:** Cross-platform collection of Python modules designed
    for writing and structuring video games.
    
**4. Artificial Intelligence:** Computer systems capable of performing
    tasks that would normally require human intelligence and
    perception.
    
**5. Machine Learning:** Algorithmic and statistical models
    incorporated by computer systems to fulfil through patterns and
    inference.
    
**6. Reinforcement Learning:** Subset of machine learning that trains
    algorithms using a system of reward and punishment.
    
**7. Dataset:** Collection of related and discrete items of related data
    that can be accessed individually or in combination.

**8. Environment:** Set of processes and tools used to create the
    programs and scripts.
    
**9. Real-time:** Data being processed as fast as possible so feedback
    can be available immediately.
    
**10. Time to Finish (TTF):** The total amount of time it takes to
    complete three laps in RLAI Racing.
    
**11. Algorithm:** Sequence of instructions given to instruct a
    computer on how to complete a specific task.
    
**12. Softlock:** An event where triggers are reached in the wrong
    order or not at all and cause the programs script to break or halt
    completely.

**2. General Description**

2.1. Product/System Functions

**2.1.1. User Access**

To run the program, the user will need to have an up-to-date version of
python installed. The user will then be required to download a zip file
containing the program in a .py file along with a README document to
provide any more explanations. Once extracted, the user will be able to
run the program through the .py file.

**2.1.2. Program Initialisation**

The program will begin by loading and showing the user the main menu.
The user can use keyboard inputs here to select between ‘Start Race’,
‘Train SennAI’, ‘View Leaderboard’ or ‘Exit Program’. By selecting ‘Start
Race’, the user will be presented with a tile-based, rectangular racetrack
where they can compete with SennAI after a short countdown. Selecting
‘Train SennAI’ will present the user with the same racetrack, but the only
car present will be SennAI’s. This mode is exclusively for teaching the
agent to complete laps faster for as many generations as the user wants.
SennAI will retain everything it has learned for normal races. If the user
selects ‘View Leaderboard’, they will be presented with the leaderboard
containing developer TTF’s. As the user participates in more races with
SennAI, each lap above a certain threshold will be added to the
leaderboard to be viewed later.

**2.1.3. Racing with SennAI**

The race will begin with a three second countdown after which the cars
can start moving. SennAI will be represented as a red rectangle and the
user as a blue rectangle whose forward directions are to their rightmost
sides and both can move at the same speeds. The user will be able to
move forward with the up arrow button, turn left with the left arrow, turn
right with the right button and brake and reverse with the down button.
The user will be expected to navigate a rectangular racetrack as quickly
as possible, speeding up on the straights and slowing down to handle
the turns. Driving off the racetrack will slow down the user’s car and
hamper their overall TTF. When the user passes the checkered finish
line three times, their car will vanish and their laps will be recorded.
Unless SennAI managed to complete it’s laps beforehand, the racetrack
will remain until SennAI finishes it’s laps. Once finished, both TTF’s are
recorded.

The view of the racetrack will be fixed and overlooking every tile of
visible area, referred to as the game field. The game field will be
designed using a unique module provided by OpenAI called Box2D.
Box2D will be imported to allow for the creation of 2D shapes to
represent the racetrack and cars. Various utilities from Gym itself will
also be incorporated. Any other important modules such as sys and
math will be imported and used whenever necessary for various
algorithms.

The user and SennAI will not have collision, instead passing through one
another if they come to close. There will be an interpreter in place,
analysing each and every frame of SennAI’s movement and how it will
be rewarded. It will not be rewarded any points for visiting tiles outside of
the racetrack or tiles behind it. Parameters will be in place to remove
SennAI if it leaves the track for too long. SennAI will be removed and the
race will end when all tiles have been visited and the user has finished.
Train SennAI’ will also be available to improve SennAI’s proficiency on
the track with the same parameters and rules in place.

**2.1.4. Checkered Flag**

Once the race has ended after the user and SennAI have finished, the
user will be returned to the leaderboard where their TTF’s are recorded.
Afterwards the user will be returned to the main menu. Since the
racetrack will be represented using tiles, they will be used to interpret
how many points SennAI should be awarded. Every frame will be
counted and calculated (1000/tiles - 0.1 * frames) with every tile that
SennAI visits and it will be cumulatively rewarded appropriately for it’s
performance. This also applies to any races had in ‘Train SennAI’.

2.2. User Characteristics and Objectives

Users are expected to know how to use their operating system of choice,
how to extract a zip file and how to run a python program in terminal.
User’s will also be expected to be tactile enough to adequately compete
in the race itself.

From the user’s point of view, the program will present them with the
opportunity to compete in a race with a constantly improving AI opponent
named SennAI. The user will be able to choose whether they want to
start a race where SennAI hasn’t learned the track, or give SennAI a
chance to improve and learn the racetrack in ‘Train SennAI’. They’ll have
the choice of resetting SennAI’s progress whenever they want through
the ‘Options’ button on the taskbar. While training TTF’s won’t be
counted on the leaderboard, normal race TTF’s will be and the user and
SennAI’s times will be compiled there.

The UI will be clear for the user to understand with whatever option
that’s currently selected will be highlighted to prevent any confusion or
accidental exits. This is important given that a user could lose all their
progress with SennAI if the menu isn’t clear enough.
Our goal is to demonstrate reinforcement learning to the user and teach
them about it’s functionality and versatility. Ideally it will be an intuitive
user experience if we can fulfil all our goals.

**Wishlist:**

● An informative main menu that highlights each option selected and
provides a description of it’s function.

● Implementing a speedup feature for ‘Train SennAI’ to bring SennAI
to a legitimate level of proficiency sooner.

● Adding a way of watching multiple previous generations of SennAI
race at once in ‘Train SennAI’.
2.3 Operational Scenarios

1. A user is presented with the RLAI Racing’s main menu. From here
    they choose to ‘Start Race’, ‘Train SennAI’ ‘View Leaderboard’,
    ‘Exit Program or access the taskbar for ‘Options’ or ‘Help’. If the


```
select ‘Start Race’, they will be placed in control of a blue car on a
rectangular racetrack where they will compete with SennAI (red
car), but without any training it’s no competition. After a three
second countdown the race will start and a 90 second timer will
begin. Three laps must be completed by the user and SennAI
within this time or the game will end. Once the race has finished,
the user will be presented with it’s statistics and taken to the
leaderboard where they can check if any TTF’s from the race have
made it on. From here they can exit back to the main menu and
then exit the game.
```

2. A user is presented with the main menu and chooses the
    leaderboard, here they see the developer TTFs along with any
    TFF’s by themselves or SennAI if they have raced already. They
    can exit back to the main menu and then exit the game.

3. A user is presented with the main menu and they choose ‘Train
    SennAI’. From here they see a new generation of SennAI begin
    attempt to complete a lap on the track. They are presented with
    information on the screen about the generation they are viewing.
    Each lap creates a new generation of SennAI and the user can let
    it generate as much as they want. After training SennAI for a while
    the user can return to the menu and choose to ‘Start Race’. Here
    they can race against an improved generation of SennAI. If SennAI
    wins after 3 laps SennAI, the game will wait until the user crosses
    the finish line, unless the timer runs out and their TTF will be
    classified as DNF (Did Not Finish). They will be brought to the
    leaderboard where they can see SennAI’s TTF and alongside their
    own. If the user wishes to reset SennAI’s progress at any point,
    they can do so by accessing ‘Options’ in the taskbar. They can exit
    back to the main menu and then exit the program.


2.4 Constraints

**2.4.1 Experience**

Despite fascination and interest in the topic, but our lack of experience in
the field of machine learning will make development more challenging as
we get to grips with reinforcement learning’s concepts. It will be a
learning process as we get to know a toolkit that we’re unfamiliar with
like OpenAI Gym and understand modules we’re minimally familiar with
from Pygame. Working closely with other projects that are related to ours
should prove helpful.

**2.4.2 Time Shortage**

This project has a short window of time to be developed. This may end
up limiting the amount of features and polish that could be implemented
with more time.

**2.4.3 Memory Issues**

Reinforcement learning can be a very taxing process due to the
numerous calculations that are undertaken. An adequate GPU may need
to be sought out to help handle the issue.

**2.4.3 Visual Problems**

Unfamiliarity with professional game design may make designing the
racetrack and driving properties difficult. We must take care in making
sure RLAI Racing is easy to understand, but also visually detailed show
off the programs full functionality.


**3. Functional Requirements**

3.1. Software Agent & R.L.

**Description**

SennAI is the core of the project and its effective functionality is
paramount to its overall goal of demonstrating reinforcement learning.
It’s goal is to be rewarded with an appropriate
amount of points for visiting as many new tiles
as it can in the lowest amount of time. This
means leaving the starting line and completing
a lap as fast as possible. SennAI will be
represented with a small red rectangle. It’s
ability to improve it’s TTFs will be fulfilled by
incorporating an effective reinforcement
learning algorithm. This will analyse SennAI’s
movement in conjunction with the amount of
frames it takes for it to complete a lap.

**Criticality (HIGH)**

The crux of this project relies on SennAI’s potential
of becoming a legitimate opponent on the programs racetrack. It’s
functionality is core to its ability to improve in ‘Train SennAI’, it’s
competitiveness in normal races and its ability to record laps to the
leaderboard. Vital parameters must be in place to prevent any bugs such
as SennAI being unable to finish a race. Otherwise this could result in
the program being softlocked.

**Technical Problems**

There are several possible issues that can arrive with SennAI’s
development. Being relatively new to machine learning development will
lead trial and error where some bugs may appear. Effective machine
learning algorithms can also be very taxing in terms of computability and
complexibility and managing this could become an issue.

**Dependence On Other Requirements**


While SennAI is the core of the project, it’s development and execution
relies on platforms provided by other requirements. It will require a
legitimate game field to identify tiles. These tiles will be an important
variable in reinforcement learning algorithms determining a reward or
lack there-of for SennAI after a successful lap.
3.2. Game Field

**Description**

To allow for the game to execute correctly, the game field needs to be
adequately tuned to provide a fair and optimal design and ruleset for the
user and SennAI to compete in. This requirement will allow for the
design of the racetrack, the grass field surrounding the track and the
correct triggers in place to notify SennAI when it’s on and off the track.

**Criticality (HIGH)**

This requirement is the visual foundation of the program and its effective
implementation is not only important for the SennAI to function in, but for
the user to comprehend what’s occurring. The game field will be made
up tiles and these tiles are vital to giving SennAI the ability to gauge how
well it is doing and how it will be rewarded for its performance.

**Technical Problems**
Designing a track that takes full advantage of each agent’s capabilities
will be difficult, but simplicity would be key in observing SennAI’s
development the clearest. There’s a possibility that implementing
effective triggers on the racetrack’s corners could allow for a small bug
where SennAI could drive onto the grass, but not be notified that it has
left the track.
**Dependence On Other Requirements**
This requirement relies heavily on a well-made race ruleset to allow for
the game field’s proper usage, otherwise agents won't have a countdown
to allow for fair starts or a way of being removed once both agents have
finished or crossed removal parameters like leaving the track for too
long. Without an intuitive interface, the game field wouldn’t even be
accessible from the main menu.


3.3. Race Ruleset
**Description**
To allow for a race/practice to be handled right, an appropriate rule set
must be in place. Starting countdowns must be in place, along with
parameters that look out for the user or SennAI leaving the track for long
enough to be removed from the race. Either agent can also be removed
if they leave the game field altogether or fail to finish the race before the
overall timer runs out.
**Criticality (HIGH)**
A ruleset is important for both the user and SennAI, as it provides a
blueprint for how to complete a race and how to do so as fast as
possible. It is also focused on preventing either agent breaking the
program by leaving the game field or cheating by crossing the centre
field of grass.
**Technical Problems**
It may prove difficult to differentiate between accidentally driving onto the
grass and cheating by crossing over the centre part of the game field.
Correctly implementing a ruleset with the various triggers found on the
game field could lead to small bugs if not combined perfectly.
**Dependence On Other Requirements**
The race ruleset relies heavily on the game field to implement it
correctly. Without ruleset the game field can’t be raced on without major
bugs appearing, but without the game field, the ruleset cannot be applied
to an environment that can be enforced upon the user and SennAI.
3.4. Interface Requirements
**Description**


Interface/GUI functionality is a requirement that is vital to the correct
presentation of the project, while also facilitating the user’s access to the
program. User’s will also be provided a familiar style of selection with the
arrow keys to select an option and the enter key to confirm selection.
Taskbars will also be incorporated to allow the user to change
parameters, reset SennAI or access helpful information. It will designed
using modules provided by Pygame.
**Criticality (MODERATE)**
Without this requirement, the user will not be afforded the option to
choose what they would like to see. The window the program is present
it won’t be properly optimised and the user won’t be able to select a
mode, instead being stuck with whatever the program has been set up to
start with. This would greatly hamper the user interaction side of ourdataset
project.
**Technical Problems**
It could prove awkward to present the program in a simple interface
format that is easy to understand without losing the complex information
it is trying to share. The project’s needs will be facilitated first, but this
risks making the program more difficult to understand for unfamiliar
users.
**Dependence On Other Requirements**
The interface plays into almost every other requirement, allowing the
user access different modes in the menu and reset SennAI’s progression
from the toolbar. It’s dependent on every other requirement, because
without their functionality, the interface can operate, but without any
result.


3.5. User Control
**Description**
This requirement describes the user’s control of their car in normal race
against SennAI. The control scheme will rely on the directional keys. The
user will be able to control the speed of the car and brake/reverse with
the down directional key. The user's car will represented in blue and be
identical in its capabilities to SennAI’s car. Just like the user, SennAI will
use the same degree of control to learn the racetrack and improve its
performance.
**Criticality (MODERATE)**
User input is an important part of this project’s overall goal and
well-implemented user control is core to that. The user may still be able
to train SennAI and see it become more competent at completing the
track, but will lack the ability to take part in racing against it.
**Technical Problems**
There are a lot of potential bugs that can arise in regards to the user's
car coming into contact with SennAI’s car. To alleviate this, there will be
no collision between them and they will simply pass through one another
if they come into contact.
**Dependence On Other Requirements**
This requirements works in tandem with the game field, given that it’s the
platform that the user will be racing on and it’s triggers encourage the
user to perform better. The race ruleset is required to prevent the user
from cheating or breaking the game, all the while recording the time it
takes for them to complete a lap.


3.6. Leaderboard
**Description**
The leaderboard will display the TTF for SennAI and the user. Upon first
viewing the leaderboard developer times will be visible e.g. “ _Connell’s_ ​
_TTF_ ​” to give the user a goal time for it to beat either directly or via
training of SennAI. The user’s TTF will include the date and time at
which the lap was achieved and the SennAI times will include the
generation at which the time was achieved.
**Criticality (LOW)**
This requirement is of least importance as the other requirements can
function fine without it. Its purpose it to help users get a glimpse of the
learning curve of the between them and SennAI as they both improve on
the racetrack.
**Technical Problems**
As more times are added scrolling will need to be implemented for the
user to be able to view all the times. A cap on the amount of TTF’s that
can be recorded may have to be implemented in case too many are
listed at once.
**Dependence On Other Requirements**
The Leaderboard being a list of times to finish of the AI and User laps
will of course be dependent entirely on the AI functioning and the user's
car functioning


**4. System Architecture**
The system behind the program will be composed of a Python 3.6.
script with modules from OpenAI Gym and Pygame. Above is every
possible user input and their appropriate results.
Modes are accessed individually, but some like ‘Start Race’ and ‘Train
SennAI’ fulfil a similar function of creating a new generation for SennAI
and having it improve its understanding of the track using reinforcement
learning.


**5. High-Level Design**
5.1. Context Diagram


5.2. Data Flow Diagram


**6. Preliminary Schedule**
6.1. Reinforcement Learning Research & Development
    ● Development Window:
       ○ 04/12/2019 - 06/03/
    ● Tasks:
       ○ Fulfilling the goal of creating a legitimate dynamic
          reinforcement learning model.
    ● Software Needed:
       ○ Python 3.6.
       ○ OpenAI Gym
6.2. Interface, Visual Design and User Input
    ● Development Window:
       ○ 06/12/2019 - 06/03/
    ● Tasks:
       ○ Design a working user interface/GUI.


○ Add each user-accessible mode.
○ Create a 2D racetrack complete with relevant triggers.
○ Implement a 2D car that can be controlled by the user.
● Software Needed:
○ Python 3.6.5
○ OpenAI Gym
○ Pygame
6.3. User Manual Creation and Submission
● Development Window:
○ 30/01/2020 - 06/03/2020
● Tasks:
○ Write a detailed, but easy-to-understand manual for RLAI
Racing.
● Software Needed:
○ Microsoft Word (2019)
6.4. Technical Specifications Creation and Submission
● Development Window:
○ 06/02/2020 - 06/03/2020
● Tasks:
○ Explain the technical details of the project in a written
document.
● Software Needed:
○ Google Docs
6.5. Video Walkthrough
● Development Window:
○ 07/02/2020 - 06/03/2020
● Tasks:
○ Demonstrate every detail about RLAI Racing’s functionality
in a video format.
● Software Needed:
○ VEGAS Pro 14.0 Edit
○ Open Broadcaster Software
○ Audacity


6.6. Blogs
● Development Window:
○ 27/01/2020 - 06/03/2020dataset
● Tasks:
○ Provide a log of the project’s development.
● Software Needed:
○ Google Docs
6.7. Presentation
● Development Window:
○ 06/03/2020 - 20/03/2020
● Tasks:
○ Present our project, it’s development and demonstrate it’s
functionality.
● Software Needed:
○ Google Slides


**7. Appendices**
7.1. OpenAI Gym Website:
https://gym.openai.com/
7.2. Pygame Website:
https://www.pygame.org/news
7.1. Wiki for Reinforcement Learning:
https://pathmind.com/wiki/deep-reinforcement-learning
SennAI - Test Log

CA326 Project by Connell Kelly and Patrick Gildea

Welcome to the SennAI Test Log where we have recorded all relevant test notes in relation to this project's development. We have done a number of different tests throughout development and we will go over some examples here.

Survey:
=======

![](https://lh5.googleusercontent.com/gfGTODLaVA7ldqLRn1LQ5gYZqsdO2gUnkN0r-NyXoFsus04OO1PqKticGnj1MBkqf4kRXJScNsmtxSTEliWwiCYAiNOO6dyszknhuwWDEChjMUO8t2oiYThYXLwdI6znL4QiOGRD)

Here we can see the results of having committed to some user testing for our project. In the final week of our project's development, we hosted five different participants in trying our program out. This was all valid as our supervisor had prepared us a GPDR/Ethics form. As seen above, Most users were not very well versed in reinforcement learning, but our program was very beneficial in helping them understand it's fundamentals.

![](https://lh6.googleusercontent.com/3Kjr4Nz1XW1C4XmMGKX5gPd9vThKW_ZWPAHu97fklPituydxA0tCSkWeCWgoXE4UszHibWd35_EYDi_PH3RZbVWimJAVIrj_vOExOR-Ox4AwqEOo10oEuvKnqMBCAaENA-3_ryJl)

Here we can see more dynamic responses to our project. You may need to zoom in to make them out in detail.￼ Many found our presentation to be well handled and that watching the improvements in real-time was worthwhile.

In terms of issues, we had a varied response. Several were concepts we worked on and didn't have time to incorporate like button prompts and a colourblind mode, but some were new and could give us new avenues to improve our program such a more active tutorial.

Unit Testing:
=============

import unittest

Import SennAI_Base

class TestSum(unittest.TestCase):

    def test_get_distance(self):

        self.assertEqual(get_distance(self, 3, 6), 3, "Supposed to be 3")

    def test_rotate_center(self):

        self.assertEqual(rotate_center(car_red.png, 50), 50, "Supposed to be 50")

    def test_detect_radar(self):

        self.assertEqual(detect_radar(self, 90) 90, "Supposed to be 90")

if __name__ == '__main__':

    unittest.main()

Above are examples of unit testing that we implemented for our SennAI_Base file. We found it difficult to perform many unit tests with this project as many functions were void and took no input, while others had inputs far too complex for us to incorporate into our unit testing in only a short period of time. Here we can see expermination with some of our more straightforward functions like get_distance.

Integration Testing:
====================

Integration testing was constantly worked on throughout the project where we were exclusively working on the reinforcement learning system. Here we had only the track, the car and the AI. This would only be one piece of the project, however, as we developed the menu we realised we would have to test them together. After a lot of integration testing between various classes such as Car() and SennAI2D to determine the car systems. With so many moving parts, effective integration testing was an important facet in effectively developing our project.
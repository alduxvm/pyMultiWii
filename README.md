# pyMultiWii


Handles the MultiWii Serial Protocol to send/receive data from boards, also reads UDP data coming from a motion capture system.

This is a text based / console, no GUI, it works for saving data from the multicopter and/or sending commands from a computer via s serial modem.

## Why?

I'm doing systems identification of multicopters being flown by me via a multiwii board. Why do I want to do this? I want to do very precise navigation algorithms using a motion capture system. 

Systems identification is a statistical method to build mathematical models of the multicopters, to have excellent control we require a perfect mathematical model. In order to do a good sysid we require data, lots of data, data coming from the board as well as the pilot and the position in the space (motion capture), so, I require raw imu (accelerometers and gyroscopes), pilot commands (rc channels) and position (x,y,z).

So far, I have a position controller working with the multiwii board being flow by simulink using data from the motion capture system and just sending rc channels via a 3DR robotics radio (roll, pitch, yaw, throttle), you can see a video about that here [TEGO indoor position control](https://vimeo.com/105761692)

I works nice... but I want it to work even nicer and better!!! so, we need all the mathematical models and parameters to be as precise as possible, ergo, systems identification required.

I knew that the 3DR radio was not good enough to send data in a fast way to the ground station... So, I put onboard a Raspberry Pie, this computer ask data to the multwii and also to the motion capture system, and saves it... thats it for now.

![MultWii and Raspberry Pie on a quadcopter](http://www.multiwii.com/forum/download/file.php?id=3360&mode=view "MultWii and Raspberry Pie on a quadcopter")

## Example:

This code has no sleeps or similar stuff, so, its very fast, for example, when asking for Attitude data, the whole process takes 0.016 seconds, thats about 62.5hz, which is pretty fast. The output looks like this:

```
{'angx': -5.1, 'angy': 10.4, 'heading': 170.0}
0.016 
{'angx': -5.3, 'angy': 13.0, 'heading': 170.0}
0.016 
{'angx': -5.6, 'angy': 15.8, 'heading': 171.0}
0.016 
{'angx': -6.0, 'angy': 19.6, 'heading': 172.0}
0.017 
{'angx': -6.2, 'angy': 22.8, 'heading': 173.0}
0.015 
{'angx': -6.5, 'angy': 25.4, 'heading': 173.0}
0.016 
{'angx': -6.6, 'angy': 27.4, 'heading': 173.0}
0.016 
{'angx': -6.6, 'angy': 27.7, 'heading': 173.0}
0.016 
{'angx': -6.3, 'angy': 26.5, 'heading': 173.0}
0.016 
{'angx': -5.9, 'angy': 25.2, 'heading': 173.0}
0.016 
{'angx': -5.6, 'angy': 22.8, 'heading': 172.0}
0.016 
{'angx': -5.2, 'angy': 19.2, 'heading': 172.0}
0.016 
{'angx': -4.7, 'angy': 14.7, 'heading': 171.0}
0.016 
{'angx': -4.3, 'angy': 11.1, 'heading': 170.0}
```

## Caution

This code is still under heavy development, everyday I add and remove stuff. Use caution.
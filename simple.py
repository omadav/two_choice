#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple iohub eye tracker device demo. Shows how monitoring for central
fixation monitoring could be done.
No iohub config .yaml files are needed for this demo.
Demo config is setup for an EyeLink(C) 1000 Desktop System. 
To to use a different eye tracker implementation, change the 
iohub_tracker_class_path and eyetracker_config dict script variables.
"""
from __future__ import absolute_import, division, print_function

from psychopy import core, visual
from psychopy.iohub.client import launchHubServer

# Number if 'trials' to run in demo
TRIAL_COUNT = 2
# Maximum trial time / time timeout
T_MAX = 10.0

iohub_tracker_class_path = 'eyetracker.hw.sr_research.eyelink.EyeTracker'
eyetracker_config = dict()
eyetracker_config['name'] = 'tracker'
eyetracker_config['model_name'] = 'EYELINK 1000 DESKTOP'
eyetracker_config['simulation_mode'] = False
eyetracker_config['runtime_settings'] = dict(sampling_rate=1000,
                                             track_eyes='RIGHT')

# Since no experiment or session code is given, no iohub hdf5 file
# will be saved, but device events are still available at runtime.
io = launchHubServer(**{iohub_tracker_class_path: eyetracker_config})

# Get some iohub devices for future access.
keyboard = io.devices.keyboard
display = io.devices.display
tracker = io.devices.tracker

# run eyetracker calibration
r = tracker.runSetupProcedure()
win = visual.Window(display.getPixelResolution(),
                    units='pix',
                    fullscr=True,
                    allowGUI=False
                    )

#gaze_ok_region = visual.Circle(win, radius=200, units='pix', pos=(-0.5,0))

gaze_ok_region = visual.Rect(
    win=win, name='gaze_ok_region',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=90, pos=(0, 0),
    lineWidth=2, lineColor='red', lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

gaze_dot = visual.GratingStim(win, tex=None, mask='gauss', pos=(0, 0),
                              size=(66, 66), color='red', units='pix')

text_stim_str = 'Eye Position: %.2f, %.2f. In Region: %s\n'
text_stim_str += 'Press space key to start next trial.'
missing_gpos_str = 'Eye Position: MISSING. In Region: No\n'
missing_gpos_str += 'Press space key to start next trial.'

side_str = 'Side: %s' # this is to show which side the participant is looking at

text_stim = visual.TextStim(win, text=text_stim_str,
                            pos=[0, int((-win.size[1]/2)*0.8)], height=24,
                                 color='black',
                                 alignHoriz='center',
                                 alignVert='center', 
                                 wrapWidth=win.size[0] * .9)

text_stim2 = visual.TextStim(win, text=side_str,
                            pos=[0.8, int((-win.size[1]/2)*0.8)], height=24,
                                 color='red',
                                 alignHoriz='center',
                                 alignVert='center', 
                                 wrapWidth=win.size[0] * .9)
                                 
text_stim3 = visual.TextStim(win, text="REWARD!",
                            pos=[0.1, int((-win.size[1]/2)*0.1)], height=24,
                                 color='green',
                                 alignHoriz='center',
                                 alignVert='center', 
                                 wrapWidth=win.size[0] * .9)

# Run Trials.....
t = 0
window = 20 # number of frames to check fixation 
gazeOK = [] # list to save all x positions in the last n frames (n=window)

while t < TRIAL_COUNT:
    io.clearEvents()
    tracker.setRecordingState(True)
    run_trial = True
    tstart_time = core.getTime()
    while run_trial is True:
        # Get the latest gaze position in dispolay coord space..
        gpos = tracker.getLastGazePosition()
        
        # Update stim based on gaze position
        valid_gaze_pos = isinstance(gpos, (tuple, list))
        gaze_in_region = valid_gaze_pos and gaze_ok_region.contains(gpos)

        if valid_gaze_pos:
            # If we have a gaze position from the tracker, update gc stim
            # and text stim.
            if gaze_in_region:
                gaze_in_region = 'Yes'
                gazeOK.append(True)
            else:
                gaze_in_region = 'No'
                gazeOK.append(False)
            
            if len(gazeOK) == window:
                gazeOK.pop(0) # delete first element from list
            
            if all(gazeOK):
                print("REWARD!")
                text_stim3.draw()
                core.wait(.1)
                #win.flip()
                
            text_stim.text = text_stim_str % (gpos[0], gpos[1], gaze_in_region)

            gaze_dot.setPos(gpos) # set current fram position for gaze dot

            if gpos[0] > -100:
               #print("right")
               side = "right"
               text_stim2.text = side_str % side
            elif gpos[0] > -300 and gpos[0] < -100:
               #print("left")
               side = "left"
               text_stim2.text = side_str % side
            #print(gpos[0])

        else:
            # Otherwise just update text stim
            text_stim.text = missing_gpos_str

        # Redraw stim
        gaze_ok_region.draw()
        text_stim.draw()
        text_stim2.draw()
        
        if valid_gaze_pos:
            gaze_dot.draw()

        # Display updated stim on screen.
        flip_time = win.flip()

        # Check any new keyboard char events for a space key.
        # If one is found, set the trial end variable.
        #
        if ' ' in keyboard.getPresses() or core.getTime()-tstart_time > T_MAX:
            run_trial = False

    # Current Trial is Done
    # Stop eye data recording
    tracker.setRecordingState(False)
    t += 1

# All Trials are done
# End experiment
win.close()
tracker.setConnectionState(False)
io.quit()
core.quit()



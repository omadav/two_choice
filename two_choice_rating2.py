#!/usr/bin/env python2
# -*- coding: utf-8 -*-
### TWO CHOICE MULTI-SESSION EXPERIMENT ###
# Author: Omar D. Perez (odperez@caltech.edu)
# Date: January, 2019

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np, csv, random, pumps, time, serial # pumps is Wolfgang's script to control pumps
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
#from numpy.random import random, randint, normal, shuffle
import os  
import sys  
from psychopy.iohub.client import launchHubServer # to make the eye tracker work with iohub

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'two_choice'  # from the Builder filename that created this script
expInfo = {u'participant': u'01', u'session': u'1', u'use_pumps': u'n',
 u'use_scanner': u'y', u'use_eye_tracker': u'y', u'reward': u'money', u'run': '1'}#, u'window':75}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/S%s_session%s_%s' %(expInfo['participant'], expInfo['session'], expInfo['date'])

# Create a csv file to save response times etc. Previous one is the native Psychopy file.
file_name = 'data/Subject%s_session%s_%s_%s' %(expInfo['participant'],
 expInfo['session'], expInfo['reward'], expInfo['date'])
csv_file = open(file_name+'.csv', 'wb')
writer_object = csv.writer(csv_file, delimiter=",") # create object to write in

writer_object.writerow(['event', 't', 'participant', 'trial', 'trial_thisRun', 'session', 'run', 'reward',
 'prob1', 'prob2', 'mag1', 'mag2','resp', 'wasRnf', 'resp_type', 'trial_ID'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Initialize components for Routine "calibrate"
calibrateClock = core.Clock()

iohub_tracker_class_path = 'eyetracker.hw.sr_research.eyelink.EyeTracker'
eyetracker_config = dict()
eyetracker_config['name'] = 'tracker'
eyetracker_config['model_name'] = 'EYELINK 1000 DESKTOP'
eyetracker_config['simulation_mode'] = False
eyetracker_config['runtime_settings'] = dict(sampling_rate=1000, track_eyes='LEFT')

io = launchHubServer(**{iohub_tracker_class_path: eyetracker_config})

# Get some iohub devices for future access.
keyboard = io.devices.keyboard
display = io.devices.display
tracker = io.devices.tracker

# run eyetracker calibration
r = tracker.runSetupProcedure()

# Create the window 
fullScreen = True # whether we want to use the whole screen; set to False to debug

if fullScreen:
    win = visual.Window(size=display.getPixelResolution(), fullscr=True, screen=0,
        allowGUI=False, allowStencil=False,
        monitor='testMonitor', color='black', colorSpace='rgb',
        blendMode='avg', useFBO=False) # FBO must be False for many screens for this to work 
else:
    win = visual.Window(size=[1280, 1024], fullscr=False, screen=0,
        allowGUI=False, allowStencil=False,
        monitor='testMonitor', color='black', colorSpace='rgb',
        blendMode='avg', useFBO=False) # FBO must be False for many screens for this to work 

gaze_dot = visual.GratingStim(win, tex=None, mask='gauss', pos=(0, 0),
                              size=(66, 66), color='red', units='pix')

# Calculate the frame rate 
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate']) # frame duration in secs
else:
    frameDur = 1.0 / 60.0  

# Initialize components for Routine "wait_scanner"
wait_scannerClock = core.Clock() # this initialises clock from wait_scanner() function; starts with '5'

# Initialize components for Routine "stim_table"
stim_tableClock = core.Clock()
p1m1_img = visual.Polygon(
    win=win, name='p1m1_img',
    edges=90, size=(0.3, 0.3),
    ori=0, pos=(-.5, 0.5),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
p1m2_img = visual.Polygon(
    win=win, name='p1m2_img',
    edges=90, size=(0.3, 0.3),
    ori=0, pos=(0, 0.5),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
p1m3_img = visual.Polygon(
    win=win, name='p1m3_img',
    edges=90, size=(0.3, 0.3),
    ori=0, pos=(0.5, 0.5),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
p2m1_img = visual.Polygon(
    win=win, name='p2m1_img',
    edges=90, size=(0.3, 0.3),
    ori=0, pos=(-0.5, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
p2m2_img = visual.Polygon(
    win=win, name='p2m2_img',
    edges=90, size=(0.3, 0.3),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
p2m3_img = visual.Polygon(
    win=win, name='p2m3_img',
    edges=90, size=(0.3, 0.3),
    ori=0, pos=(0.5, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
p3m1_img = visual.Polygon(
    win=win, name='p3m1_img',
    edges=90, size=(0.3, 0.3),
    ori=0, pos=(-0.5, -0.5),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
p3m2_img = visual.Polygon(
    win=win, name='p3m2_img',
    edges=90, size=(0.3, 0.3),
    ori=0, pos=(0, -0.5),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
p3m3_img = visual.Polygon(
    win=win, name='p3m3_img',
    edges=90, size=(0.3, 0.3),
    ori=0, pos=(0.5, -0.5),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
magnitude_title_txt = visual.TextStim(win=win, name='magnitude_title_txt',
    text='Amount\n\n',
    font='Arial',
    pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=-9.0);
mag_low_txt = visual.TextStim(win=win, name='mag_low_txt',
    text='Low',
    font='Arial',
    pos=(-0.5, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
mag_med_txt = visual.TextStim(win=win, name='mag_med_txt',
    text='Medium',
    font='Arial',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-11.0);
mag_high_txt = visual.TextStim(win=win, name='mag_high_txt',
    text='High',
    font='Arial',
    pos=(0.5, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-12.0);
prob_txt1 = visual.TextStim(win=win, name='prob_txt1',
    text='Probability',
    font='Arial',
    pos=(-0.75, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=-13.0);
prob_low_txt = visual.TextStim(win=win, name='prob_low_txt',
    text='Low',
    font='Arial',
    pos=(-0.8, 0.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-14.0);
prob_med_txt = visual.TextStim(win=win, name='prob_med_txt',
    text='Medium',
    font='Arial',
    pos=(-0.8, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-15.0);
prob_high_txt = visual.TextStim(win=win, name='prob_high_txt',
    text='High',
    font='Arial',
    pos=(-0.8, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-16.0);

# Initialize components for Routine "show_rating_scale"

# Create rating object
thirst_rating = visual.RatingScale(win=win, name='thirst_rating', low=0,
high=4, markerStart=2, leftKeys="4", rightKeys="9", acceptKeys="8")

rating_txt = visual.TextStim(win=win, name='rating_txt',
    text='Please rate how thirsty are you right now',
    font='Comic Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "ISI0"
# This is the blank screen shown once
ISI0Clock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "cue1"
cue1Clock = core.Clock()
first_cue = visual.Polygon(
    win=win, name='first_cue',
    edges=90, size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "ISI1"
ISI1Clock = core.Clock()
isi1 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='isi1')

# Initialize components for Routine "cue2"
cue2Clock = core.Clock()
second_cue = visual.Polygon(
    win=win, name='second_cue',
    edges=90, size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "ISI2"
ISI2Clock = core.Clock()
isi2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='isi2')

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
iti = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='iti')

# Initialize components for Routine "trial"
trialClock = core.Clock()
resp_image = visual.ImageStim(
    win=win, name='resp_image',
    image='sin', mask=None,
    ori=0, pos=[0.0, 0.5], size=.4,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
left_frac = visual.Polygon(
    win=win, name='left_frac',
    edges=90, size=(0.5, 0.5),
    ori=0, pos=(-.5, 0),
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
right_frac = visual.Polygon(
    win=win, name='right_frac',
    edges=90, size=(0.5, 0.5),
    ori=0, pos=(0.5, 0),
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# this is to draw a rectangle when participant fixating on either side
gaze_ok_region_left = visual.Rect(
    win=win, name='gaze_ok_region_left',
    width=(0.7, 0.7)[0], height=(0.7, 0.7)[1],
    ori=90, pos=(-0.5, 0),
    lineWidth=2, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
gaze_ok_region_right = visual.Rect(
    win=win, name='gaze_ok_region_right',
    width=(0.7, 0.7)[0], height=(0.7, 0.7)[1],
    ori=90, pos=(0.5, 0),
    lineWidth=2, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "chosen"
chosenClock = core.Clock()
left_chosen = visual.Polygon(
    win=win, name='right_chosen',
    edges=90, size=(0.5, 0.5),
    ori=0, pos=(-.5, 0),
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
right_chosen = visual.Polygon(
    win=win, name='right_chosen',
    edges=90, size=(0.5, 0.5),
    ori=0, pos=(0.5, 0),
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
selection_arrow = visual.ImageStim(
    win=win, name='selection_arrow',
    image='stim/arrow.png', mask=None,
    ori=0, pos=[0,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ISI3"
ISI3Clock = core.Clock()
isi3 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='isi3')

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
left_feedback = visual.ImageStim(
    win=win, name='left_feedback',
    image='stim/no_reward1.png', mask=None,
    ori=0, pos=[-0.55, 0], size=.8,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
right_feedback = visual.ImageStim(
    win=win, name='right_feedback',
    image='stim/rewarded.png', mask=None,
    ori=0, pos=[0.55, 0], size=.8,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
missed_trial_feedback = visual.ImageStim(
    win=win, name='missed_trial_feedback',
    image='stim/missed_trial_feedback.png', mask=None,
    ori=0, pos=[0, 0], size=1.5,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "ISI4"
ISI4Clock = core.Clock()
isi4 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='isi4')

# Initialize components for Routine "rnf_delivery"
rnf_deliveryClock = core.Clock()
rnf_delivery_img = visual.ImageStim(
    win=win, name='rnf_delivery_img',
    image='none', mask=None,
    ori=0, pos=(0, 0), size=.7,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

#### START BEGIN EXPERIMENT SNIPPET ####
t, globalTime = 0, 0 # initialize so that the TextBoxes below don't complain 

# Fixation cross as a text stim with text equal to +
fix_cross = visual.TextStim(win=win, ori=0, name='fixation',
                            text='+', font='Arial', pos=[0, 0], 
                            height=0.3, wrapWidth=None, color='white', 
                            colorSpace='rgb', opacity=1, depth=0.0)

# the following are TEXTBOX objects for debugging purposes. 
# Otherwise there are memory leaks if you update textstim
# objects on every frame due to some problem with pyglet

globalClock_txt = visual.TextStim(win=win, ori=0, 
                        text='globalTime: ' + str(round(0.00, 2)), font='Arial',
                        pos=[-0.8, -0.4], height=0.05, wrapWidth=None, color='blue', 
                        colorSpace='rgb', opacity=1, depth=0.0)
                        # visual.TextBox(window=win, text="", font_size=20,
                        #  font_color=[-1, -1, 1], size=(1.9, .3), pos=(-0.8, -0.4), 
                        #  grid_horz_justification='center', units='norm')

t_txt = visual.TextBox(window=win, text='t: ' + str(round(t, 2)), font_size=20,
                         font_color=[-1, -1, 1], size=(1.9, .3), pos=(-0.8, .6), 
                         grid_horz_justification='center', units='norm')

run_txt = visual.TextBox(window=win, text='run name: ' + expInfo['run'], font_size=20,
                         font_color=[-1, -1, 1], size=(1.9, .3), pos=(-0.8, 0.5), 
                         grid_horz_justification='center', units='norm')

rnf_delivery_img_txt = visual.TextBox(window=win, text='text', font_size=20,
                         font_color=[-1, -1, 1], size=(1.9, .3), pos=(-0.6, 0.4), 
                         grid_horz_justification='center', units='norm')

time_fixating_txt = visual.TextStim(win=win, ori=0, name='fixation', 
                        text='time_fixating: ' + str(round(0.00, 2)), font='Arial',
                        pos=[0.0, -0.2], height=0.3, wrapWidth=None, color='white', 
                        colorSpace='rgb', opacity=1, depth=0.0)

mag_txt =  visual.TextBox(window=win, text='text', font_size=20,
                         font_color=[-1, -1, 1], size=(1.9, .3), pos=(-0.8, 0.7), 
                         grid_horz_justification='center', units='norm')

reward_txt =  visual.TextBox(window=win, text='text', font_size=20,
                         font_color=[-1, -1, 1], size=(1.9, .3), pos=(-0.8, 0.3), 
                         grid_horz_justification='center', units='norm')

isReinforced_txt =  visual.TextBox(window=win, text='text', font_size=20,
                         font_color=[-1, -1, 1], size=(1.9, .3), pos=(-0.8, 0.2), 
                         grid_horz_justification='center', units='norm')

response_txt =  visual.TextBox(window=win, text='text', font_size=20,
                         font_color=[-1, -1, 1], size=(1.9, .3), pos=(-0.8, 0.1), 
                         grid_horz_justification='center', units='norm')

prob_txt =  visual.TextBox(window=win, text='text', font_size=20,
                         font_color=[-1, -1, 1], size=(1.9, .3), pos=(-0.8, -0.3), 
                         grid_horz_justification='center', units='norm')

trial_txt = visual.TextBox(window=win, text='text', font_size=20,
                         font_color=[-1, -1, 1], size=(1.9, .3), pos=(0, 0.8), 
                         grid_horz_justification='center', units='norm')


# Initialise some variables to be used in the routines

debug = False # are we showing the debugging stuff on the screen?
autopilot = False # if True, responds automatically in each trial (for debugging purposes, default is False)
nMissed = 0 # to track how many missed trials and show them on screen
gaze_pos = None
isReinforced, run, trial_thisRun = 0, 0, 0 # flag for whether the trial was reinforced; current run; trial number in this run

# Handy functions, including Wolfgang's pumps script

def show_rating_scale():    

    rating_trialClock = core.Clock() # create clock for the rating (not really needed)
    # Create some handy timers
    # globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    # ------Prepare to start Routine "rating_trial"-------
    t = 0
    rating_trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    thirst_rating.reset()
    # keep track of which components have finished
    rating_trialComponents = [thirst_rating, rating_txt]
    for thisComponent in rating_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "rating_trial"-------
    while continueRoutine:
        # get current time
        t = rating_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *thirst_rating* updates
        if t >= 0.0 and thirst_rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            thirst_rating.tStart = t
            thirst_rating.frameNStart = frameN  # exact frame index
            thirst_rating.setAutoDraw(True)
        continueRoutine &= thirst_rating.noResponse  # a response ends the trial
        
        # *rating_txt* updates
        if t >= 0.0 and rating_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_txt.tStart = t
            rating_txt.frameNStart = frameN  # exact frame index
            rating_txt.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rating_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

        if not thirst_rating.noResponse:
            continueRoutine = False

    # -------Ending Routine "rating_trial"-------
    for thisComponent in rating_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('thirst_rating.response', thirst_rating.getRating())
    thisExp.nextEntry()
    # the Routine "rating_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

def msg_to_screen(text_stim, autodraw=False):
    ''' this functions draw text onto the screen 
    (not using it because causes memory leakage) '''
    #text_object=visual.TextStim(win, text=msg, pos=(x,y), color=u'white')
    text_stim.setAutoDraw(autodraw) # autodraw is false so that the txt doesn't appear constantly
    text_stim.draw()

def show_debugging_stuff():
    ''' set text for stims to show every frame
    These are all textBox objects so it does work well without any memory problems '''
    #globalClock_txt.setText("globalClock: %s" %str(round(globalTime, 2)))
    t_txt.setText('t:  %s' %str(round(t, 2)))               
    run_txt.setText('run: %d' %run)
    rnf_delivery_img_txt.setText('rnf_delivery_img:  %s' %str(rnf_delivery_img.image))
    mag_txt.setText('mag1:%d mag2:%d' %(mag1, mag2))
    reward_txt.setText('reward: %s' %str(reward))
    isReinforced_txt.setText('isReinforced: %s' %str(isReinforced))
    prob_txt.setText('prob1: %.2f prob2: %.2f' %(prob1, prob2))
    trial_txt.setText('trial: %d' %trial_thisRun)
    #cond_file_txt.setText('conditions_'+expInfo['reward']+'_'+expInfo['resp_type']+'_'+expInfo['run']+'.xlsx')

    # show text stims on every frame
    t_txt.draw()
    run_txt.draw()
    rnf_delivery_img_txt.draw()
    mag_txt.draw()
    reward_txt.draw()
    isReinforced_txt.draw()
    prob_txt.draw()
    trial_txt.draw()
    #globalClock_txt.draw()
    #cond_file_txt.draw()

def wait_for_scanner():
    ''' wait for number 5 and creates global clock (down in the script) '''
    n_discard = 1 # this in Python means zero discarded triggers
    #wait_txt.setAutoDraw(True)
    #print 'inside wait_for_scanner'
    if expInfo['reward'] == "juice": # when in a juice session, show the thirst scale
        show_rating_scale()

    show_stim_table() # if not the last run, show the screen

    for k in xrange(n_discard):
        keys = event.waitKeys(keyList='5') # waits for trigger 
        if k == 0:
            clock = core.Clock() # set clock 0 to time of first scan
        #wait_txt.setText(str(n_discard - k - 1))
        win.flip()
    wait_txt.autoDraw = False
    win.flip()
    return clock

def configure_pumps(volume=.45, diameter=26.77, rate=60, direction='INF', address=0):
    ''' configure pumps for the experiment 
    Create serial connection (in Windows PC is usually COM3)
    This ser.port variable needs to be changed according to which computer
    is running the task '''

    ser = serial.Serial() # Create serial connection
    ser.baudrate = 1200 # this is the default rate (1200)
    ser.port = 'COM5' # change according to name Device Manager shows. Use the previous to last usb on the stim pc in the scanner at caltech.
    p = pumps.scan()

    if len(p):
        if len(p) > 1:
            print "Found more than one pump!...that's weird"
        else:
            print "Found only one pump... that's good enough"

        dev_address = p[0][1]
        p = pumps.Pump(ser.name)

        for address in xrange(3):
            s = p.volume(volume, address=address)  # how much to dispense
            s = p.diameter(diameter, address=address) # diameter of syringe
            s = p.rate(rate, address=address) # how fast
            s = p.direction(direction, address=address) # pump (not suck) liquid
    return p 

def deliver_juice(mag):
    for squirt in xrange(mag):
        p.run(address)
        core.wait(.4)
        #time.sleep(.5) # try to see whether core.wait() would work better

def show_stim_table():
	global wait_txt

	endExpNow = False  # flag for 'escape' or other condition => quit the exp
	trials_2 = data.TrialHandler(nReps=1, method='sequential', extraInfo=expInfo, originPath=-1, 
		trialList=data.importConditions('conditions_probe_'+expInfo['reward']+'.xlsx'), seed=None, name='trials_2')

	thisExp.addLoop(trials_2)  # add the loop to the experiment
	thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    
	if thisTrial_2 != None:
	    for paramName in thisTrial_2.keys():
	        exec(paramName + '= thisTrial_2.' + paramName)

	for thisTrial_2 in trials_2:
	    currentLoop = trials_2
	    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
	    if thisTrial_2 != None:
	        for paramName in thisTrial_2.keys():
	            exec(paramName + '= thisTrial_2.' + paramName)
	    # ------Prepare to start Routine "stim_table"-------
	    t = 0
	    stim_tableClock.reset()  # clock
	    frameN = -1
	    continueRoutine = True
	    # update component parameters for each repeat
	    p1m1_img.setFillColor(p1)
	    p1m2_img.setFillColor(p1)
	    p1m3_img.setFillColor(p1)
	    p2m1_img.setFillColor(p2)
	    p2m2_img.setFillColor(p2)
	    p2m3_img.setFillColor(p2)
	    p3m1_img.setFillColor(p3)
	    p3m2_img.setFillColor(p3)
	    p3m3_img.setFillColor(p3)
	    key_resp_2 = event.BuilderKeyResponse()
	    p1m1_img.edges = m1
	    p1m2_img.edges = m2
	    p1m3_img.edges = m3
	    p2m1_img.edges = m1
	    p2m2_img.edges = m2
	    p2m3_img.edges = m3
	    p3m1_img.edges = m1
	    p3m2_img.edges = m2
	    p3m3_img.edges = m3
	    
	    # keep track of which components have finished
	    stim_tableComponents = [p1m1_img, p1m2_img, p1m3_img, p2m1_img, p2m2_img, p2m3_img,
	     p3m1_img, p3m2_img, p3m3_img, magnitude_title_txt, mag_low_txt, mag_med_txt, mag_high_txt,
	      prob_txt1, prob_low_txt, prob_med_txt, prob_high_txt, key_resp_2]
	    
	    for thisComponent in stim_tableComponents:
	        if hasattr(thisComponent, 'status'):
	            thisComponent.status = NOT_STARTED

	    # -------Start Routine "stim_table"-------
	    while continueRoutine:
	        # get current time
	        t = stim_tableClock.getTime()
	        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
	        # update/draw components on each frame
	        
	        # *p1m1_img* updates
	        if t >= 0.0 and p1m1_img.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            p1m1_img.tStart = t
	            p1m1_img.frameNStart = frameN  # exact frame index
	            p1m1_img.setAutoDraw(True)
	        
	        # *p1m2_img* updates
	        if t >= 0.0 and p1m2_img.status == NOT_STARTED:
	            # keep track of start time/frame for later5
	            p1m2_img.tStart = t
	            p1m2_img.frameNStart = frameN  # exact frame index
	            p1m2_img.setAutoDraw(True)
	        
	        # *p1m3_img* updates
	        if t >= 0.0 and p1m3_img.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            p1m3_img.tStart = t
	            p1m3_img.frameNStart = frameN  # exact frame index
	            p1m3_img.setAutoDraw(True)
	        
	        # *p2m1_img* updates
	        if t >= 0.0 and p2m1_img.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            p2m1_img.tStart = t
	            p2m1_img.frameNStart = frameN  # exact frame index
	            p2m1_img.setAutoDraw(True)
	        
	        # *p2m2_img* updates
	        if t >= 0.0 and p2m2_img.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            p2m2_img.tStart = t
	            p2m2_img.frameNStart = frameN  # exact frame index
	            p2m2_img.setAutoDraw(True)
	        
	        # *p2m3_img* updates
	        if t >= 0.0 and p2m3_img.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            p2m3_img.tStart = t
	            p2m3_img.frameNStart = frameN  # exact frame index
	            p2m3_img.setAutoDraw(True)
	        
	        # *p3m1_img* updates
	        if t >= 0.0 and p3m1_img.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            p3m1_img.tStart = t
	            p3m1_img.frameNStart = frameN  # exact frame index
	            p3m1_img.setAutoDraw(True)
	        
	        # *p3m2_img* updates
	        if t >= 0.0 and p3m2_img.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            p3m2_img.tStart = t
	            p3m2_img.frameNStart = frameN  # exact frame index
	            p3m2_img.setAutoDraw(True)
	        
	        # *p3m3_img* updates
	        if t >= 0.0 and p3m3_img.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            p3m3_img.tStart = t
	            p3m3_img.frameNStart = frameN  # exact frame index
	            p3m3_img.setAutoDraw(True)
	        
	        # *magnitude_title_txt* updates
	        if t >= 0.0 and magnitude_title_txt.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            magnitude_title_txt.tStart = t
	            magnitude_title_txt.frameNStart = frameN  # exact frame index
	            magnitude_title_txt.setAutoDraw(True)
	        
	        # *mag_low_txt* updates
	        if t >= 0.0 and mag_low_txt.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            mag_low_txt.tStart = t
	            mag_low_txt.frameNStart = frameN  # exact frame index
	            mag_low_txt.setAutoDraw(True)
	        
	        # *mag_med_txt* updates
	        if t >= 0.0 and mag_med_txt.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            mag_med_txt.tStart = t
	            mag_med_txt.frameNStart = frameN  # exact frame index
	            mag_med_txt.setAutoDraw(True)
	        
	        # *mag_high_txt* updates
	        if t >= 0.0 and mag_high_txt.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            mag_high_txt.tStart = t
	            mag_high_txt.frameNStart = frameN  # exact frame index
	            mag_high_txt.setAutoDraw(True)
	        
	        # *prob_txt1* updates
	        if t >= 0.0 and prob_txt1.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            prob_txt1.tStart = t
	            prob_txt1.frameNStart = frameN  # exact frame index
	            prob_txt1.setAutoDraw(True)
	        
	        # *prob_low_txt* updates
	        if t >= 0.0 and prob_low_txt.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            prob_low_txt.tStart = t
	            prob_low_txt.frameNStart = frameN  # exact frame index
	            prob_low_txt.setAutoDraw(True)
	        
	        # *prob_med_txt* updates
	        if t >= 0.0 and prob_med_txt.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            prob_med_txt.tStart = t
	            prob_med_txt.frameNStart = frameN  # exact frame index
	            prob_med_txt.setAutoDraw(True)
	        
	        # *prob_high_txt* updates
	        if t >= 0.0 and prob_high_txt.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            prob_high_txt.tStart = t
	            prob_high_txt.frameNStart = frameN  # exact frame index
	            prob_high_txt.setAutoDraw(True)
	        
	        # *key_resp_2* updates
	        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
	            # keep track of start time/frame for later
	            key_resp_2.tStart = t
	            key_resp_2.frameNStart = frameN  # exact frame index
	            key_resp_2.status = STARTED
	            # keyboard checking is just starting
	            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
	            event.clearEvents(eventType='keyboard')
	        if key_resp_2.status == STARTED:
	            theseKeys = event.getKeys(keyList=['space', 'j'])
	            
	            # check for quit:
	            if "escape" in theseKeys:
	                endExpNow = True
	            if len(theseKeys) > 0:  # at least one key was pressed
	                key_resp_2.keys = theseKeys[-1]  # just the last key pressed

                    if key_resp_2.keys == 'space':
                        #print('space pressed')
                        wait_txt = visual.TextStim(win, 'Waiting for scanner ... ', pos=(0, -.85))
                        wait_txt.draw()
                        win.flip()
                        key_resp_2.rt = key_resp_2.clock.getTime()
                        continueRoutine = False # the 'space' key ends the routine and goes to the next run
                    elif key_resp_2.keys == 'j': #if key_resp_2.keys != 'space':
                        deliver_juice(1)
	        
	        # check if all components have finished
	        if not continueRoutine:  # a component has requested a forced-end of Routine
	            break
	        continueRoutine = False  # will revert 5to True if at least one component still running
	        for thisComponent in stim_tableComponents:
	            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
	                continueRoutine = True
	                break  # at least one component has not yet finished
	        
	        # check for quit (the Esc key)
	        if endExpNow or event.getKeys(keyList=["escape"]):
	            tracker.setConnectionState(False) # stop recording from eye-tracker so that a et_data file is created
	            io.quit()
	            core.quit()
	        
	        # refresh the screen
	        if continueRoutine:  # don't flip if this routine555 is over or we'll get a blank screen
	            win.flip()

	    # -------Ending Routine "stim_table"-------
	    for thisComponent in stim_tableComponents:
	        if hasattr(thisComponent, "setAutoDraw"):
	            thisComponent.setAutoDraw(False)
	    # check responses
	    if key_resp_2.keys in ['', [], None]:  # No response was made
	        key_resp_2.keys=None
	    trials_2.addData('key_resp_2.keys',key_resp_2.keys)
	    if key_resp_2.keys != None:  # we had a response
	        trials_2.addData('key_resp_2.rt', key_resp_2.rt)


##########################
# EXPERIMENT STARTS HERE #
##########################

# Configure pumps
if expInfo['use_pumps'] == 'y':  
    p = configure_pumps()
    address = 0 # use first pump

#if trial_thisRun == 0:
#	show_stim_table()


if expInfo['use_scanner'] == 'y': # test
    globalClock = wait_for_scanner() # wait_for_scanner returns the clock that starts when scanner starts
    #core.Clock()  # to track the time5 since experiment started
else:
    globalClock = core.Clock() # create global clock in case scanner is not used5

routineTimer = core.CountdownTimer()  # timer for each routine; resets every time a routine starts

# Draw text on every frame when debugging
fix_cross.setAutoDraw(True) # draw fixation cross on every frame

# these are the numbers for each run (these should be the "selection" numbers below, taken from the xls conditions file)
# run1: 0-36  run2: 36-72   run3: 72-108  run4: 108-144
print('run: %s')%expInfo['run']

# Now we use the run number from the menu to select the rows that correspond to that run and to the end.
if expInfo['run'] == '1':
    rows_xls = u'0:144'
elif expInfo['run'] == '2':
    rows_xls = u'36:144'
elif expInfo['run'] == '3':
    rows_xls = u'72:144'
elif expInfo['run'] == '4':
    rows_xls = u'108:144'

# This creates the trials object that will be used to take the conditions for each trial
# It is sequential because the randomisation is done in excel
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_'+expInfo['reward']+'.xlsx', selection=rows_xls), seed=None, name='trials')# , selection=u'108:144' this selection goe449988889848s after xlsx, separated by comma, inside the parenthesis

thisExp.addLoop(trials)  # add the loop to the experiment6

thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values

nTrials = 36 # taken from selection inside trials object above; change to 36 if running the whole task

# Create ITIs
ITI_intervals = [5]
ITI_temp = [4.0000,4.0571,4.1143,4.1714,4.2286,4.2857,4.3429,4.4000,4.4571,4.5143,4.5714,4.6286,4.6857,4.7429,4.8000,4.8571,4.9143,4.9714,5.0286,5.0857,5.1429,5.2000,5.2571,5.3143,5.3714,5.4286,5.4857,5.5429,5.6000,5.6571,5.7143,5.7714,5.8286,5.8857,5.9429,6.0000]

np.random.shuffle(ITI_temp)

for idx in range(nTrials):
    ITI_intervals.append(ITI_temp[idx])

# Create ISIs; use one vector and shuffle it for each of the ISI1,...ISI4

ISI1_intervals = [2,2.0286,	2.0571,	2.0857,	2.1143,	2.1429,	2.1714,	2.2,2.2286,	2.2571,	2.2857,	2.3143,	2.3429,	2.3714,	2.4,2.4286,	2.4571,	2.4857,	2.5143,	2.5429,	2.5714,	2.6,2.6286,	2.6571,	2.6857,	2.7143,	2.7429,	2.7714,	2.8, 2.8286,2.8571,	2.8857,	2.9143,	2.9429,	2.9714,	3]
print("ISI1_interval" + str(ISI1_intervals))
ISI2_intervals = [2,2.0286,	2.0571,	2.0857,	2.1143,	2.1429,	2.1714,	2.2,2.2286,	2.2571,	2.2857,	2.3143,	2.3429,	2.3714,	2.4,2.4286,	2.4571,	2.4857,	2.5143,	2.5429,	2.5714,	2.6,2.6286,	2.6571,	2.6857,	2.7143,	2.7429,	2.7714,	2.8, 2.8286,2.8571,	2.8857,	2.9143,	2.9429,	2.9714,	3]        

ISI3_intervals = [2,2.0286,	2.0571,	2.0857,	2.1143,	2.1429,	2.1714,	2.2,2.2286,	2.2571,	2.2857,	2.3143,	2.3429,	2.3714,	2.4,2.4286,	2.4571,	2.4857,	2.5143,	2.5429,	2.5714,	2.6,2.6286,	2.6571,	2.6857,	2.7143,	2.7429,	2.7714,	2.8, 2.8286,2.8571,	2.8857,	2.9143,	2.9429,	2.9714,	3]        

ISI4_intervals = [2,2.0286,	2.0571,	2.0857,	2.1143,	2.1429,	2.1714,	2.2,2.2286,	2.2571,	2.2857,	2.3143,	2.3429,	2.3714,	2.4,2.4286,	2.4571,	2.4857,	2.5143,	2.5429,	2.5714,	2.6,2.6286,	2.6571,	2.6857,	2.7143,	2.7429,	2.7714,	2.8, 2.8286,2.8571,	2.8857,	2.9143,	2.9429,	2.9714,	3]        

np.random.shuffle(ISI1_intervals) # create 36 intervals for ISI1
print("ISI1_intervals: " + str(ISI1_intervals))
np.random.shuffle(ISI2_intervals) # same for the rest
print("ISI2_intervals: " + str(ISI2_intervals))
np.random.shuffle(ISI3_intervals)
print("ISI3_intervals: " + str(ISI3_intervals))
np.random.shuffle(ISI4_intervals)
print("ISI4_intervals: " + str(ISI4_intervals))

# -------Start looping trials-------

trialsClock = core.Clock() # this is the clock to try to time everything to it

if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    
    currentLoop = trials
    
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys(): 
            exec(paramName + '= thisTrial.' + paramName)
    
    if trial_thisRun == 0 and run > 0: # create intervals to be used as ISIs and ITIs after each run
        
        # Create ITIs
        ITI_intervals = [5]
        ITI_temp = [4.0000,4.0571,4.1143,4.1714,4.2286,4.2857,4.3429,4.4000,4.4571,4.5143,4.5714,4.6286,4.6857,4.7429,4.8000,4.8571,4.9143,4.9714,5.0286,5.0857,5.1429,5.2000,5.2571,5.3143,5.3714,5.4286,5.4857,5.5429,5.6000,5.6571,5.7143,5.7714,5.8286,5.8857,5.9429,6.0000]

        np.random.shuffle(ITI_temp)

        for idx in range(nTrials):
            ITI_intervals.append(ITI_temp[idx])

        # Create ISIs; use one vector and shuffle it for each of the ISI1,...ISI4

        ISI1_intervals = [2,2.0286,	2.0571,	2.0857,	2.1143,	2.1429,	2.1714,	2.2,2.2286,	2.2571,	2.2857,	2.3143,	2.3429,	2.3714,	2.4,2.4286,	2.4571,	2.4857,	2.5143,	2.5429,	2.5714,	2.6,2.6286,	2.6571,	2.6857,	2.7143,	2.7429,	2.7714,	2.8, 2.8286,2.8571,	2.8857,	2.9143,	2.9429,	2.9714,	3]
        print("ISI1_interval" + str(ISI1_intervals))
        ISI2_intervals = [2,2.0286,	2.0571,	2.0857,	2.1143,	2.1429,	2.1714,	2.2,2.2286,	2.2571,	2.2857,	2.3143,	2.3429,	2.3714,	2.4,2.4286,	2.4571,	2.4857,	2.5143,	2.5429,	2.5714,	2.6,2.6286,	2.6571,	2.6857,	2.7143,	2.7429,	2.7714,	2.8, 2.8286,2.8571,	2.8857,	2.9143,	2.9429,	2.9714,	3]        

        ISI3_intervals = [2,2.0286,	2.0571,	2.0857,	2.1143,	2.1429,	2.1714,	2.2,2.2286,	2.2571,	2.2857,	2.3143,	2.3429,	2.3714,	2.4,2.4286,	2.4571,	2.4857,	2.5143,	2.5429,	2.5714,	2.6,2.6286,	2.6571,	2.6857,	2.7143,	2.7429,	2.7714,	2.8, 2.8286,2.8571,	2.8857,	2.9143,	2.9429,	2.9714,	3]        

        ISI4_intervals = [2,2.0286,	2.0571,	2.0857,	2.1143,	2.1429,	2.1714,	2.2,2.2286,	2.2571,	2.2857,	2.3143,	2.3429,	2.3714,	2.4,2.4286,	2.4571,	2.4857,	2.5143,	2.5429,	2.5714,	2.6,2.6286,	2.6571,	2.6857,	2.7143,	2.7429,	2.7714,	2.8, 2.8286,2.8571,	2.8857,	2.9143,	2.9429,	2.9714,	3]        

        np.random.shuffle(ISI1_intervals) # create 36 intervals for ISI1
        print("ISI1_intervals: " + str(ISI1_intervals))
        np.random.shuffle(ISI2_intervals) # same for the rest
        print("ISI2_intervals: " + str(ISI2_intervals))
        np.random.shuffle(ISI3_intervals)
        print("ISI3_intervals: " + str(ISI3_intervals))
        np.random.shuffle(ISI4_intervals)
        print("ISI4_intervals: " + str(ISI4_intervals))

        print("new ITI_intervals: " + str(ITI_intervals))
        #print run
        globalClock = wait_for_scanner() # wait_for_scanner returns the clock that starts when scanner starts

    trialsClock.reset() # reset the trial clock time everything w/r to it

    t0_trial = trialsClock.getTime() # tick start of trial

    print("trial: %d" %trials.thisN)

    first_cue_presented = np.random.randint(1, 3) # sample 1 or 2 (3 excluded in Python)

    # ------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ITI_duration = ITI_intervals.pop(0) #ISI_intervals.pop(0) #np.random.uniform(3)
    # keep track of which components have finished
    ITIComponents = [iti]
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # save in csv
    trials.addData("ITI_On", str(globalClock.getTime()))        
    # thisExp.nextEntry()

    writer_object.writerow(["ITI_on", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), trial_thisRun, expInfo['session'], run, reward, str(prob1),
      str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    # -------Start Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        globalTime = globalClock.getTime()

        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iti* period
        if t >= 0.0 and iti.status == NOT_STARTED:
            # keep track of start time/frame for later
            iti.tStart = t
            iti.frameNStart = frameN  # exact frame index
            iti.start(ITI_duration)
        elif iti.status == STARTED:  # one frame should pass before updating params and completing
            iti.complete()  # finish the static period
        
        # check if current lenght of trial greater than intended platonically
        if trialsClock.getTime() - t0_trial > ITI_duration:
            continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        if t < ITI_duration and continueRoutine == False: # if less than intended, continue routine
            continueRoutine = True
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        if debug:
            show_debugging_stuff()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    print("trial %d" %trials.thisN + "\n" +  "ITI_duration: " + str(ITI_duration))
    print("prob1: %.2f"+", prob2: %.2f"+", mag1: %i" + ", mag2: %i")%(prob1, prob2, mag1, mag2)

    # save in csv

    trials.addData("ITI_Off", str(globalClock.getTime()))

    writer_object.writerow(["ITI_off", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), trial_thisRun, expInfo['session'], run, reward, str(prob1),
      str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # present cues

    if first_cue_presented == 1:
        #def present_cue1(isi_duration=0):
        # ------Prepare to start Routine "cue1"-------
        t = 0
        cue1Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1)
        # update component parameters for each repeat
        first_cue.setFillColor(color_left)
        first_cue.edges = n_edges_left

        ##### START BEGIN ROUTINE SNIPPET #####

        trials.addData("cue1_On", str(globalClock.getTime()))
        #thisExp.nextEntry()

        writer_object.writerow(["cue1_On", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), trial_thisRun, expInfo['session'], run, reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])

        ##### END BEGIN ROUTINE SNIPPET #####

        # keep track of which components have finished
        cue1Components = [first_cue]
        for thisComponent in cue1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # END BEGIN ROUTINE CUE1 SNIPPET

        # -------Start Routine "cue1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cue1Clock.getTime()     
            globalTime = globalClock.getTime()      

            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *first_cue* updates
            if t >= 0 and first_cue.status == NOT_STARTED:
                # keep track of start time/frame for later
                first_cue.tStart = t
                first_cue.frameNStart = frameN  # exact frame index
                first_cue.setAutoDraw(True)
            frameRemains = 0 + 1 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if first_cue.status == STARTED and t >= frameRemains:
                first_cue.setAutoDraw(False)

            if trialsClock.getTime() - t0_trial > ITI_duration + 1: # if current length, greater than intended, stop routine
                continueRoutine = False

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cue1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            if continueRoutine == False and t < 1:
                continueRoutine = not continueRoutine # if less than intended duration, continue the routine

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            if debug:
                show_debugging_stuff()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen            
                win.flip()

        # -------Ending Routine "cue1"-------
        for thisComponent in cue1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        ###### START END ROUTINE CUE1 SNIPPET #####

        trials.addData("cue1_Off", str(globalClock.getTime()))
        # thisExp.nextEntry()

        writer_object.writerow(["cue1_Off", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), trial_thisRun, expInfo['session'], run, reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])

        ##### FINISH END ROUTINE CUE1 SNIPPET #####

        #def present_ISI1():    
        # ------Prepare to start Routine "ISI1"-------
        # ISI 1
        t = 0
        ISI1Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        ISI1_duration = ISI1_intervals.pop(0) # pop(0) assigns ISI_intervals[0] and drops it from list
        print(ISI1_duration)
        # keep track of which components have finished
        ISI1Components = [isi1]
        for thisComponent in ISI1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        trials.addData("ISI1_On", str(globalClock.getTime()))
        # thisExp.nextEntry()

        # -------Start Routine "ISI1"-------
        while continueRoutine:
            # get current time
            t = ISI1Clock.getTime()
            globalTime = globalClock.getTime()

            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *isi1* period
            if t >= 0.0 and isi1.status == NOT_STARTED:
                # keep track of start time/frame for later
                isi1.tStart = t
                isi1.frameNStart = frameN  # exact frame index
                isi1.start(ISI1_duration) # take duration from ISI_intervals list
            elif isi1.status == STARTED:  # one frame should pass before updating params and completing
                isi1.complete()  # finish the static period

            if trialsClock.getTime() - t0_trial > ITI_duration + 1 + ISI1_duration: # if current length, greater than intended, stop routine
                continueRoutine = False 
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            if continueRoutine == False and t < ISI1_duration:
                continueRoutine = True # if less than intended duration, continue the routine

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            if debug:
                show_debugging_stuff()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "ISI1"-------
        for thisComponent in ISI1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        # the Routine "ISI1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

        trials.addData("ISI1_Off", str(globalClock.getTime()))
        # thisExp.nextEntry()

        # return(ISI1_duration)

        # def present_cue2(isi_duration=0):
        # ------Prepare to start Routine "cue2"-------
        t = 0
        cue2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1)

        ##### START BEGIN ROUTINE SNIPPET #####

        # update component parameters for each repeat
        second_cue.setFillColor(color_right)
        second_cue.edges = n_edges_right

        trials.addData("cue2_On", str(globalClock.getTime()))
        # thisExp.nextEntry()

        writer_object.writerow(["cue2_On", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), trial_thisRun, expInfo['session'], run, reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])

        ##### END BEGIN ROUTINE SNIPPET #####

        # keep track of which components have finished
        cue2Components = [second_cue]
        for thisComponent in cue2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "cue2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cue2Clock.getTime()
            globalTime = globalClock.getTime()

            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *second_cue* updates
            if t >= 0 and second_cue.status == NOT_STARTED:
                # keep track of start time/frame for later
                second_cue.tStart = t
                second_cue.frameNStart = frameN  # exact frame index
                second_cue.setAutoDraw(True)                
            frameRemains = 0 + 1 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if second_cue.status == STARTED and t >= frameRemains:
                second_cue.setAutoDraw(False)

            if trialsClock.getTime() - t0_trial > ITI_duration + 1 + ISI1_duration + 1: # if current length, greater than intended, stop routine
                continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cue2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            if continueRoutine == False and t < 1:
                continueRoutine = True # if less than intended duration, continue the routine

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            if debug:
                show_debugging_stuff()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "cue2"-------
        for thisComponent in cue2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        #### START END ROUTINE CUE2 SNIPPET ####

        trials.addData("cue2_Off", str(globalClock.getTime()))
        # thisExp.nextEntry()

        writer_object.writerow(["cue2_Off", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), trial_thisRun, expInfo['session'], run, reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])

        #### FINISH END ROUTINE CUE2 SNIPPET ####
    else:
        # def present_cue2(isi_duration=0):
        # ------Prepare to start Routine "cue2"-------
        t = 0
        cue2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1)

        ##### START BEGIN ROUTINE SNIPPET #####

        # update component parameters for each repeat
        second_cue.setFillColor(color_right)
        second_cue.edges = n_edges_right

        trials.addData("cue2_On", str(globalClock.getTime()))
        # thisExp.nextEntry()

        writer_object.writerow(["cue2_On", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), trial_thisRun, expInfo['session'], run, reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])

        ##### END BEGIN ROUTINE SNIPPET #####

        # keep track of which components have finished
        cue2Components = [second_cue]
        for thisComponent in cue2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "cue2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cue2Clock.getTime()
            globalTime = globalClock.getTime()

            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *second_cue* updates
            if t >= 0 and second_cue.status == NOT_STARTED:
                # keep track of start time/frame for later
                second_cue.tStart = t
                second_cue.frameNStart = frameN  # exact frame index
                second_cue.setAutoDraw(True)                
            frameRemains = 0 + 1 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if second_cue.status == STARTED and t >= frameRemains:
                second_cue.setAutoDraw(False)

            if trialsClock.getTime() - t0_trial > ITI_duration + 1: #+ ISI1_duration + 1: # if current length, greater than intended, stop routine
                continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cue2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            if continueRoutine == False and t < 1:
                continueRoutine = True # if less than intended duration, continue the routine

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            if debug:
                show_debugging_stuff()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "cue2"-------
        for thisComponent in cue2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        #### START END ROUTINE CUE2 SNIPPET ####

        trials.addData("cue2_Off", str(globalClock.getTime()))
        # thisExp.nextEntry()

        writer_object.writerow(["cue2_Off", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), trial_thisRun, expInfo['session'], run, reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])

        #### FINISH END ROUTINE CUE2 SNIPPET ####

                #def present_ISI1():    
        # ------Prepare to start Routine "ISI1"-------
        # ISI 1
        t = 0
        ISI1Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        ISI1_duration = ISI1_intervals.pop(0) # pop(0) assigns ISI_intervals[0] and drops it from list
        # keep track of which components have finished
        ISI1Components = [isi1]
        for thisComponent in ISI1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        trials.addData("ISI1_On", str(globalClock.getTime()))
        # thisExp.nextEntry()

        # -------Start Routine "ISI1"-------
        while continueRoutine:
            # get current time
            t = ISI1Clock.getTime()
            globalTime = globalClock.getTime()

            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *isi1* period
            if t >= 0.0 and isi1.status == NOT_STARTED:
                # keep track of start time/frame for later
                isi1.tStart = t
                isi1.frameNStart = frameN  # exact frame index
                isi1.start(ISI1_duration) # take duration from ISI_intervals list
            elif isi1.status == STARTED:  # one frame should pass before updating params and completing
                isi1.complete()  # finish the static period

            if trialsClock.getTime() - t0_trial > ITI_duration + 1 + ISI1_duration: # if current length, greater than intended, stop routine
                continueRoutine = False 
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            if continueRoutine == False and t < ISI1_duration:
                continueRoutine = True # if less than intended duration, continue the routine

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            if debug:
                show_debugging_stuff()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "ISI1"-------
        for thisComponent in ISI1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        # the Routine "ISI1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

        trials.addData("ISI1_Off", str(globalClock.getTime()))
        # thisExp.nextEntry()

        # return(ISI1_duration)
    #def present_cue1(isi_duration=0):
        # ------Prepare to start Routine "cue1"-------
        t = 0
        cue1Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1)
        # update component parameters for each repeat
        first_cue.setFillColor(color_left)
        first_cue.edges = n_edges_left

        ##### START BEGIN ROUTINE SNIPPET #####

        trials.addData("cue1_On", str(globalClock.getTime()))
        #thisExp.nextEntry()

        writer_object.writerow(["cue1_On", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), trial_thisRun, expInfo['session'], run, reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])

        ##### END BEGIN ROUTINE SNIPPET #####

        # keep track of which components have finished
        cue1Components = [first_cue]
        for thisComponent in cue1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # END BEGIN ROUTINE CUE1 SNIPPET

        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cue1Clock.getTime()     
            globalTime = globalClock.getTime()      

            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *first_cue* updates
            if t >= 0 and first_cue.status == NOT_STARTED:
                # keep track of start time/frame for later
                first_cue.tStart = t
                first_cue.frameNStart = frameN  # exact frame index
                first_cue.setAutoDraw(True)
            frameRemains = 0 + 1 - win.monitorFramePeriod * 0.75  # most of one frame p94499eriod left
            if first_cue.status == STARTED and t >= frameRemains:
                first_cue.setAutoDraw(False)

            if trialsClock.getTime() - t0_trial > ITI_duration + 1 + ISI1_duration + 1: # if current length, greater than intended, stop routine
                continueRoutine = False

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cue1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            if continueRoutine == False and t < 1:
                continueRoutine = not continueRoutine # if less than intended duration, continue the routine

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            if debug:
                show_debugging_stuff()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen            
                win.flip()

        # -------Ending Routine "cue1"-------
        for thisComponent in cue1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        ###### START END ROUTINE CUE1 SNIPPET #####

        trials.addData("cue1_Off", str(globalClock.getTime()))
        # thisExp.nextEntry()

        writer_object.writerow(["cue1_Off", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), trial_thisRun, expInfo['session'], run, reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])

        ##### FINISH END ROUTINE CUE1 SNIPPET #####

    # Presentation of single cues finished; go to choice trial

    # ------Prepare to start Routine "ISI2"-------
    # ISI 2
    t = 0
    ISI2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ISI2_duration = ISI2_intervals.pop(0) #np.random.uniform(3)
    # keep track of which components have finished
    ISI2Components = [isi2]
    for thisComponent in ISI2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    trials.addData("ISI2_On", str(globalClock.getTime()))

    # -------Start Routine "ISI2"-------
    while continueRoutine:
        # get current time
        t = ISI2Clock.getTime()
        globalTime = globalClock.getTime()

        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi2* period
        if t >= 0.0 and isi2.status == NOT_STARTED:
            # keep track of start time/frame for later
            isi2.tStart = t
            isi2.frameNStart = frameN  # exact frame index
            isi2.start(ISI2_duration)
        elif isi2.status == STARTED:  # one frame should pass before updating params and completing
            isi2.complete()  # finish the static period
        
        if trialsClock.getTime() - t0_trial > ITI_duration + 1 + ISI1_duration + 1 + ISI2_duration: # if current length, greater than intended, stop routine
            continueRoutine = False  
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        if t < ISI2_duration and continueRoutine == False:
            continueRoutine = True

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        if debug:
            show_debugging_stuff()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI2"-------
    for thisComponent in ISI2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ISI2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    trials.addData("ISI2_Off", str(globalClock.getTime()))

    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3)

    # update component parameters for each repeat
    resp_image.setImage(resp_img)
    left_frac.setFillColor(color_left)
    right_frac.setFillColor(color_right)
    left_frac.edges = n_edges_left
    right_frac.edges = n_edges_right

    # left_frac.setImage(stim1)
    # right_frac.setImage(stim2)

    key_resp_2 = event.BuilderKeyResponse()
    mouse = event.Mouse(win=win, visible=False)

    #### START BEGIN ROUTINE SNIPPET ####

    tick_trial = globalClock.getTime() # tick to calculate

    arrow_x_pos = None
    #ISI_duration = np.random.uniform(2)    

    # window = expInfo['window'] # number of frames to check fixation; monitor runs at 75 HZ

    side = None

    fix_cross.setAutoDraw(False)

    trials.addData("trial_On", str(globalClock.getTime()))

    writer_object.writerow(["trial_On", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), trial_thisRun, expInfo['session'], run, reward,
      str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    #### FINISH BEGIN ROUTINE SNIPPET ####
    
    # keep track of which components have finished
    trialComponents = [resp_image, left_frac, right_frac, key_resp_2, mouse]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED  

    # clear ET events and start recording again for this trial
    # if resp_type == "gaze":
    #     io.clearEvents()
    #     tracker.setRecordingState(True)
    
    # we will start and stop tracking the eye for both button presses and saccades
    # if it doesn't work, just uncomment the three lines above and erase the two below
    io.clearEvents()
    tracker.setRecordingState(True)
    
    # create lists to save booleans for side participant's looking
    # this, apparently, needs to be between io.ClearEvents() and setRecordingState
    gazeOK_left_list = [] # list to save all x positions in the last n frames (n=window)
    gazeOK_right_list = [] # same for right side
    gazeOK_center_list = [] # same for centre

    fixatingClock = core.Clock()
    time_fixating = 0
    isFixating = False
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        globalTime = globalClock.getTime()

        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

        # *resp_image* updates
        if t >= 0.0 and resp_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp_image.tStart = t
            resp_image.frameNStart = frameN  # exact frame index
            resp_image.setAutoDraw(True)
        frameRemains = 0.0 + 3 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if resp_image.status == STARTED and t >= frameRemains:
            resp_image.setAutoDraw(False)

        # *left_frac* updates
        if t >= 0 and left_frac.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_frac.tStart = t
            left_frac.frameNStart = frameN  # exact frame index
            left_frac.setAutoDraw(True)
        frameRemains = 0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if left_frac.status == STARTED and t >= frameRemains:
            left_frac.setAutoDraw(False)
        
        # *right_frac* updates
        if t >= 0 and right_frac.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_frac.tStart = t
            right_frac.frameNStart = frameN  # exact frame index
            right_frac.setAutoDraw(True)
        frameRemains = 0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if right_frac.status == STARTED and t >= frameRemains:
            right_frac.setAutoDraw(False)

        if trialsClock.getTime() - t0_trial > ITI_duration + 1 + ISI1_duration + 1 + ISI2_duration + 3: # if current length, greater than intended, stop routine
            continueRoutine = False  
        
        if resp_type == "gaze":
            #isfixating = False

            # *mouse* updates, only to trick psychopy 
            if t >= 0.0 and mouse.status == NOT_STARTED:
                # keep track of start time/frame for later
                mouse.tStart = t
                mouse.frameNStart = frameN  # exact frame index
                mouse.status = STARTED
                event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
            
            eyeinfo = tracker.getLastSample() # # dictionary with all info about gaze (12th and 13th position are x and y pos)

            eyeinfo1 = tracker.getLastGazePosition() 
            valid_gaze_pos = isinstance(eyeinfo1, list) 

            gaze_pos = tracker.getPosition()

            if type(gaze_pos) in [list, tuple]: 
            #if frameN > 1 and valid_gaze_pos: #and eyeinfo[22] != 0: # eyeinfo[22] is pupil size

                x_pos, y_pos = gaze_pos
                #x_pos, y_pos = eyeinfo[12], eyeinfo[13]
                #gaze_pos = [x_pos, y_pos] # xpos from the dictionary, the x coordinate
               
                gaze_dot.setPos(gaze_pos)#[x_pos, y_pos]) # set position for gaze dot
                gaze_dot.draw()
                time_fixating = 0

                # Check fixation
                if x_pos <= -100:# and y_pos < 100 and y_pos > -100:left_frac.contains([x_pos, y_pos]):
                    gaze_ok_region_left.draw() 
                    #side = "left"
                    isFixating = True                    
                    time_fixating = fixatingClock.getTime()
                    if time_fixating >= 1.5:
                        key_resp_2.keys = "4"
                        continueRoutine = False    
                        key_resp_2.rt = key_resp_2.clock.getTime()                                   
                elif x_pos >= 100:# and y_pos < 100 and y_pos > -100:right_frac.contains([x_pos, y_pos]):# 
                    gaze_ok_region_right.draw() 
                    #side = "right"
                    isFixating = True                    
                    time_fixating = fixatingClock.getTime()
                    if time_fixating >= 1.5:
                        key_resp_2.keys = "9"
                        key_resp_2.rt = key_resp_2.clock.getTime()
                        continueRoutine = False
                else: #changed from else to elif #if x_pos >= -100 and x_pos <= 100:                    
                    #side = "center"
                    isFixating = False
                    time_fixating = 0
                    fixatingClock.reset()
               
        elif resp_type == "button":
            # *key_resp_2* updates
            if t >= 0.0 and key_resp_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_2.tStart = t
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if key_resp_2.status == STARTED and t >= frameRemains:
                key_resp_2.status = STOPPED
            if key_resp_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['4', '9'])
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True                
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        #### START EACH FRAME SNIPPET ####

        if debug:
            show_debugging_stuff()

        #### FINISH EACH FRAME SNIPPET FOR "TRIAL" ROUTINE ####

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        if t < 3 and continueRoutine == False:
            continueRoutine = True

        if endExpNow or event.getKeys(keyList=["escape"]):
            tracker.setConnectionState(False) # stop recording from eye-tracker
            io.quit()
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    if autopilot:
        if trial_thisRun in range(0, 35, 2): # to make the computer respond automatically in some trials
            key_resp_2.keys = '9'
        else: 
            key_resp_2.keys = '4'

    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
    trials.addData('key_resp_2.keys', key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)

    #### START END ROUTINE SNIPPET ####

    if key_resp_2.keys == '4':
        arrow_x_pos = -0.5    
        isReinforced = np.random.binomial(1, prob1)
    
    elif key_resp_2.keys == '9':
        arrow_x_pos = 0.5
        isReinforced = np.random.binomial(1, prob2)
    
    elif key_resp_2.keys == None: # replace None from Python with 'none' string
        nMissed += 1
        isReinforced = 0 
        key_resp_2.keys = 'none'
    
    if key_resp_2.keys != 'none':  # we had a response
        trials.addData("wasRewarded", isReinforced)
    else: # we did not have a response
        trials.addData("wasRewarded", 0) # never rewarded if did not respond
    
    trials.addData("globalTime", globalTime)
    
    # save in csv
    trials.addData("trial_Off", str(globalClock.getTime()))

    writer_object.writerow(["trial_Off", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), trial_thisRun, expInfo['session'], run, reward, str(prob1),
      str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    # if resp_type == "gaze":
    #     io.clearEvents()
    #     tracker.setRecordingState(False) # stop recording for this trial    
    
    # we will start and stop tracking the eye for both button presses and saccades
    # if it doesn't work, just uncomment the three lines above
    io.clearEvents()
    tracker.setRecordingState(False) # stop recording for this trial   

    # tic again when trial routine ends
    toc_trial = globalClock.getTime()

    # this is the total length of the trial; could be less than the one set above because a choice finishes the routine
    trial_length = toc_trial - tick_trial 

    ##### FINISH END ROUTINE SNIPPET #####
   
    # ------Prepare to start Routine "chosen"-------
    t = 0
    chosenClock.reset()  # clock
    frameN = -1
    continueRoutine = True

    # show arrow so that trial + choice routines are always the same length
    routineTimer.add(1) 

    # update component parameters for each repeat
    left_chosen.setFillColor(color_left)
    right_chosen.setFillColor(color_right)
    left_chosen.edges = n_edges_left
    right_chosen.edges = n_edges_right
    
    selection_arrow.setPos([-7,-1])
    
    # Start Begin Routine snippet ("chosen" routine)
    if key_resp_2.keys == 'none':
        selection_arrow.setOpacity(0)
        fix_cross.setColor("grey")
    
    selection_arrow.setPos([arrow_x_pos, -0.4])

    trials.addData("chosen_on", str(globalClock.getTime()))

    writer_object.writerow(["chosen_On", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), trial_thisRun, expInfo['session'], run, reward, str(prob1),
      str(prob2), str(mag1), str(mag2), key_resp_2.keys, isReinforced, resp_type, trial_ID])
    
    # Finish Begin Routine snippet
    # keep track of which components have finished
    chosenComponents = [left_chosen, right_chosen, selection_arrow]
    for thisComponent in chosenComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "chosen"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = chosenClock.getTime()
        globalTime = globalClock.getTime()

        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *left_chosen* updates
        if t >= 0 and left_chosen.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_chosen.tStart = t
            left_chosen.frameNStart = frameN  # exact frame index
            left_chosen.setAutoDraw(True)
        frameRemains = 0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if left_chosen.status == STARTED and t >= frameRemains:
            left_chosen.setAutoDraw(False)
        
        # *right_chosen* updates
        if t >= 0 and right_chosen.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_chosen.tStart = t
            right_chosen.frameNStart = frameN  # exact frame index
            right_chosen.setAutoDraw(True)
        frameRemains = 0 + 1 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if right_chosen.status == STARTED and t >= frameRemains:
            right_chosen.setAutoDraw(False)
        
        # *selection_arrow* updates
        if t >= 0.0 and selection_arrow.status == NOT_STARTED:
            # keep track of start time/frame for later
            selection_arrow.tStart = t
            selection_arrow.frameNStart = frameN  # exact frame index
            selection_arrow.setAutoDraw(True)
        frameRemains = 0.0 + 1 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if selection_arrow.status == STARTED and t >= frameRemains:
            selection_arrow.setAutoDraw(False)

        # Start Each Frame snippet

        if trialsClock.getTime() - t0_trial > ITI_duration + 1 + ISI1_duration + 1 + ISI2_duration + 3 + 1: # if current length, greater than intended, stop routine
            continueRoutine = False  

        if t < 1 and continueRoutine == False:
            continueRoutine = True
             
        if debug:
            show_debugging_stuff()

        # Finish Each Frame snippet
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in chosenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]): 
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "chosen"-------
    for thisComponent in chosenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    trials.addData("chosen_off", str(globalClock.getTime()))

    #### START END ROUTINE SNIPPET ####
    writer_object.writerow(["chosen_Off", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), trial_thisRun, expInfo['session'], run, reward, str(prob1),
      str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    selection_arrow.setOpacity(1)
    fix_cross.setAutoDraw(True) # redraw fixation cross on the screen after choice 
    
    #### FINISH END ROUTINE SNIPPET ####

    # ------Prepare to start Routine "ISI3"-------
    t = 0
    ISI3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    tick_ISI3 = ISI3Clock.getTime()

    # modify duration so as to counteract the fact that the trial 
    # routine ends sooner when a reponse has been made.
    ISI3_duration = ISI3_intervals.pop(0) + 3 - trial_length #np.random.uniform(3) 
    # keep track of which components have finished
    ISI3Components = [isi3]
    for thisComponent in ISI3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    trials.addData("ISI3_On", str(globalClock.getTime()))
    
    # -------Start Routine "ISI3"-------
    while continueRoutine:
        # get current time
        t = ISI3Clock.getTime()
        globalTime = globalClock.getTime()

        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi3* period
        if t >= 0.0 and isi3.status == NOT_STARTED:
            # keep track of start time/frame for later
            isi3.tStart = t
            isi3.frameNStart = frameN  # exact frame index
            isi3.start(ISI3_duration)
        elif isi3.status == STARTED:  # one frame should pass before updating params and completing
            isi3.complete()  # finish the static period

        #### START EACH FRAME SNIPPET ####
        if trialsClock.getTime() - t0_trial > ITI_duration + 1 + ISI1_duration + 1 + ISI2_duration + 3 + 1 + ISI3_duration: # if current length, greater than intended, stop routine
            continueRoutine = False  

        if debug:
            show_debugging_stuff()

        #### FINISH EACH FRAME SNIPPET ####
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI3"-------
    for thisComponent in ISI3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #toc_ISI3 = ISI3Clock.getTime()

    #ISI3_duration = toc_ISI3 - tick_ISI3 # total duration of ISI3 to modify following ISI duration

    trials.addData("ISI3_Off", str(globalClock.getTime()))

    # the Routine "ISI3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1)
    # update component parameters for each repeat
    
    #### START BEGIN ROUTINE ("FEEDBACK" ROUTINE) SNIPPET ####

    trials.addData("feedback_On", str(globalClock.getTime()))

    writer_object.writerow(["feedback_On", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), trial_thisRun, expInfo['session'], run, reward, 
     str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    if key_resp_2.keys == '4': # response left
        right_feedback.setOpacity(0) # make dissapear the right feed img
        missed_trial_feedback.setOpacity(0)
        
        if isReinforced:      
            #outcome_text.setText('')           
            left_feedback.setImage('stim/rewarded.png')
        elif not isReinforced:
            #outcome_text.setText('')            
            left_feedback.setImage('stim/no_reward1.png') 
            #left_feedback.setSize(1.3)
    
    elif key_resp_2.keys == '9': # response right
        left_feedback.setOpacity(0) # make dissapear the left feed img
        missed_trial_feedback.setOpacity(0)

        if isReinforced:    
            #outcome_text.setText('')        
            right_feedback.setImage('stim/rewarded.png')
        elif not isReinforced:
            #outcome_text.setText('')            
            right_feedback.setImage('stim/no_reward1.png')
            #right_feedback.setSize(1.3)
    
    elif key_resp_2.keys == 'none':
        #outcome_text.setText('')
        left_feedback.setOpacity(0)
        right_feedback.setOpacity(0)
        missed_trial_feedback.setOpacity(1)
        missed_trial_feedback.size = 1.5
    
    #### FINISH BEGIN ROUTINE SNIPPET ("FEEDBACK" ROUTINE) ####

    # keep track of which components have finished
    feedbackComponents = [left_feedback, right_feedback, missed_trial_feedback]#, outcome_text]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        globalTime = globalClock.getTime()

        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *left_feedback* updates
        if t >= 0.0 and left_feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_feedback.tStart = t
            left_feedback.frameNStart = frameN  # exact frame index
            left_feedback.setAutoDraw(True)
        frameRemains = 0.0 + 1 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if left_feedback.status == STARTED and t >= frameRemains:
            left_feedback.setAutoDraw(False)
        
        # *right_feedback* updates
        if t >= 0.0 and right_feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_feedback.tStart = t
            right_feedback.frameNStart = frameN  # exact frame index
            right_feedback.setAutoDraw(True)
        frameRemains = 0.0 + 1 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if right_feedback.status == STARTED and t >= frameRemains:
            right_feedback.setAutoDraw(False)
        
        # *missed_trial_feedback* updates
        if t >= 0.0 and missed_trial_feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            missed_trial_feedback.tStart = t
            missed_trial_feedback.frameNStart = frameN  # exact frame index
            missed_trial_feedback.setAutoDraw(True)
        frameRemains = 0.0 + 1 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if missed_trial_feedback.status == STARTED and t >= frameRemains:
            missed_trial_feedback.setAutoDraw(False)

        # # *outcome_text* updates
        # if t >= 0.0 and outcome_text.status == NOT_STARTED:
        #     # keep track of start time/frame for later
        #     outcome_text.tStart = t
        #     outcome_text.frameNStart = frameN  # exact frame index
        #     outcome_text.setAutoDraw(True)
        # frameRemains = 0.0 + 1 - win.monitorFramePeriod * 0.75  # most of one frame period left
        # if outcome_text.status == STARTED and t >= frameRemains:
        #     outcome_text.setAutoDraw(False)

        ##### START EACH FRAME SNIPPET #####

        if trialsClock.getTime() - t0_trial > ITI_duration + 1 + ISI1_duration + 1 + ISI2_duration + 3 + 1 + ISI3_duration + 1: # if current length, greater than intended, stop routine
            continueRoutine = False  

        if t < 1 and continueRoutine == False:
            continueRoutine = True
             
        if debug:
            show_debugging_stuff()

        ##### FINISH EACH FRAME SNIPPET #####
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    ##### START END ROUTINE SNIPPET FOR FEEDBACK ROUTINE ####

    trials.addData("feedback_Off", str(globalClock.getTime()))
    
    writer_object.writerow(["feedback_Off", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), trial_thisRun, expInfo['session'], run, reward,
      str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    # take colour back to stimuli for next trial
    right_feedback.setOpacity(1) 
    left_feedback.setOpacity(1)
    missed_trial_feedback.setOpacity(1)
    
    #### FINISH END ROUTINE SNIPPET FOR FEEDBACK ROUTINE ####    
    
    # ------Prepare to start Routine "ISI4"-------
    t = 0
    ISI4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ISI4_duration = ISI4_intervals.pop(0) # np.random.uniform(3)
    # keep track of which components have finished
    ISI4Components = [isi4]
    for thisComponent in ISI4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    trials.addData("ISI4_On", str(globalClock.getTime()))
    
    # -------Start Routine "ISI4"-------
    while continueRoutine:
        # get current time
        t = ISI4Clock.getTime()
        globalTime = globalClock.getTime()

        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi4* period
        if t >= 0.0 and isi4.status == NOT_STARTED:
            # keep track of start time/frame for later
            isi4.tStart = t
            isi4.frameNStart = frameN  # exact frame index
            isi4.start(ISI4_duration)
        elif isi4.status == STARTED:  # one frame should pass before updating params and completing
            isi4.complete()  # finish the static period
        
        ##### START EACH FRAME SNIPPET #####

        if trialsClock.getTime() - t0_trial > ITI_duration + 1 + ISI1_duration + 1 + ISI2_duration + 3 + 1 + ISI3_duration + 1 + ISI4_duration: # if current length, greater than intended, stop routine
            continueRoutine = False  

        if t < ISI4_duration and continueRoutine == False:
            continueRoutine = True
             
        if debug:
            show_debugging_stuff()

        ##### FINISH EACH FRAME SNIPPET #####

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI4"-------
    for thisComponent in ISI4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ISI4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    trials.addData("ISI4_Off", str(globalClock.getTime()))
    
    # ------Prepare to start Routine "rnf_delivery"-------
    t = 0
    rnf_deliveryClock.reset() # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.5)

    # update component parameters for each repeat

    trials.addData("rnf_delivery_On", str(globalClock.getTime()))

    writer_object.writerow(["rnf_delivery_On", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), trial_thisRun, expInfo['session'], run, reward,
      str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])

    # keep track of which components have finished
    rnf_deliveryComponents = [rnf_delivery_img]
    for thisComponent in rnf_deliveryComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    rnf_delivery_img.setOpacity(1) # show stimuli again
    fix_cross.setAutoDraw(False) # draw fixation cross on every frame

    if isReinforced:
        #rnf_delivery_img.setOpacity(1)
        if expInfo['reward'] == "money":
            rnf_delivery_img.size = 1.3 
            rnf_delivery_img.setPos([0, 0])
            if key_resp_2.keys == "4":
                if mag1 == 1:
                    rnf_delivery_img.setImage('stim/reward_money1.png')
                    #rnf_delivery_img.setPos([0.0, 0.0])                      
                elif mag1 == 2:
                    rnf_delivery_img.setImage('stim/reward_money2.png')
                    #rnf_delivery_img.setPos([0.0, 0.0])
                elif mag1 == 3: 
                    rnf_delivery_img.setImage('stim/reward_money3.png')
                    #rnf_delivery_img.setPos([0.0, 0.0])
            elif key_resp_2.keys == "9":
                if mag2 == 1:
                    rnf_delivery_img.setImage('stim/reward_money1.png')
                    #rnf_delivery_img.setPos([0.0, 0.0])
                elif mag2 == 2:
                    rnf_delivery_img.setImage('stim/reward_money2.png')
                    #rnf_delivery_img.setPos([0.0, 0.0])
                elif mag2 == 3: 
                    rnf_delivery_img.setImage('stim/reward_money3.png') 
                    #rnf_delivery_img.setPos([0.0, 0.0])

        elif expInfo['reward'] == "juice":             

            if key_resp_2.keys == "4":
                if mag1 == 1:
                    rnf_delivery_img.setImage('stim/reward_juice1.png')
                    rnf_delivery_img.setAutoDraw(True)
                    win.flip()
                    deliver_juice(1)                     
                elif mag1 == 2:
                    rnf_delivery_img.setImage('stim/reward_juice2.png')
                    rnf_delivery_img.setAutoDraw(True)
                    win.flip()
                    deliver_juice(2)                    
                elif mag1 == 3:
                    rnf_delivery_img.setImage('stim/reward_juice3.png')
                    rnf_delivery_img.setAutoDraw(True)
                    win.flip()
                    deliver_juice(3)
            elif key_resp_2.keys == "9":
                if mag2 == 1:
                    rnf_delivery_img.setImage('stim/reward_juice1.png')
                    rnf_delivery_img.setAutoDraw(True)
                    win.flip()
                    deliver_juice(1)
                    #rnf_delivery_img.setSize(0.0)
                elif mag2 == 2:
                    rnf_delivery_img.setImage('stim/reward_juice2.png')
                    rnf_delivery_img.setAutoDraw(True)                    
                    win.flip()
                    deliver_juice(2)
                    #rnf_delivery_img.setSize(0.0)
                elif mag2 == 3:
                    rnf_delivery_img.setImage('stim/reward_juice3.png')
                    rnf_delivery_img.setAutoDraw(True)
                    win.flip()
                    deliver_juice(3)
                    #rnf_delivery_img.setSize(0.0)
    else:
        #rnf_delivery_img.setOpacity(0)  
        rnf_delivery_img.size = .8
        rnf_delivery_img.setImage('stim/not_reinforced.png')
    
    # -------Start Routine "rnf_delivery"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rnf_deliveryClock.getTime()
        globalTime = globalClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rnf_delivery_img* updates
        if t >= 0.0 and rnf_delivery_img.status == NOT_STARTED:
            # keep track of start time/frame for later
            rnf_delivery_img.tStart = t
            rnf_delivery_img.frameNStart = frameN  # exact frame index
            rnf_delivery_img.setAutoDraw(True)
        frameRemains = 0.0 + 3.5 - win.monitorFramePeriod * 0.75  # most of one frame period 4
        if rnf_delivery_img.status == STARTED and t >= frameRemains:
            rnf_delivery_img.setAutoDraw(False)

        ##### START EACH FRAME SNIPPET #####
        if trialsClock.getTime() - t0_trial > ITI_duration + 1 + ISI1_duration + 1 + ISI2_duration + 3 + 1 + ISI3_duration + 1 + ISI4_duration + 3.5: # if current length, greater than intended, stop routine
            continueRoutine = False  

        if t < 3.5 and continueRoutine == False:
            continueRoutine = True
             
        if debug:
            show_debugging_stuff()

        ##### FINISH EACH FRAME SNIPPET #####       
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rnf_deliveryComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    for thisComponent in rnf_deliveryComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #### BEGIN END ROUTINE SNIPPET ####

    trials.addData("rnf_delivery_Off", str(globalClock.getTime()))

    writer_object.writerow(["rnf_delivery_Off", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), trial_thisRun, expInfo['session'], run, reward,
      str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])

    fix_cross.setAutoDraw(True) # draw fixation cross on every frame
    fix_cross.setColor("white")

    #### FINISH END ROUTINE SNIPPET ####
    
    # Show screen to wait for next run
    # trials.thisN is the actual trial
    # it does not depend on the run
    # it just counts from 0 to 143 (total n of trials)
    if trial_thisRun in [35]: # actual trial is trial_thisRun + 1
        # update variables

        # trial_thisRun = 0 # this is the trial within the run; reset AFTER final ITI
        
        # ------Prepare to start Routine "ITI"-------
        # ISI 2
        t = 0
        ITIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        ITI_duration = ITI_intervals.pop(0) #ISI_intervals.pop(0) #np.random.uniform(3)
        # keep track of which components have finished
        ITIComponents = [iti]
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # save in csv
        trials.addData("final_ITI_On", str(globalClock.getTime()))

        writer_object.writerow(["final_ITI_on", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), trial_thisRun, expInfo['session'], run, reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
        
        # -------Start Routine "final ITI"-------
        while continueRoutine:
            # get current time
            t = ITIClock.getTime()
            globalTime = globalClock.getTime()

            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *iti* period
            if t >= 0.0 and iti.status == NOT_STARTED:
                # keep track of start time/frame for later
                iti.tStart = t
                iti.frameNStart = frameN  # exact frame index
                iti.start(ITI_duration)
            elif iti.status == STARTED:  # one frame should pass before updating params and completing
                iti.complete()  # finish the static period
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            if debug:
                show_debugging_stuff()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "ITI"-------
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        ##### START END ROUTINE SNIPPET FOR FINAL ITI ROUTINE ####
    
        # save in csv
        trials.addData("final_ITI_off", str(globalClock.getTime()))

        # if run == 3:
        # 	show_rating_scale()
        
        writer_object.writerow(["final_ITI_off", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), trial_thisRun, expInfo['session'], run, reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])       

        # update values for run and trial (goes to 0 again)
        run += 1
        trial_thisRun = 0 # this is the trial within the run; reset AFTER final ITI

        #### FINISH END ROUTINE SNIPPET FOR FINAL ITI ROUTINE ####    
    else:
        # finished trial
        trial_thisRun += 1 # this is the trial within the run
        
    thisExp.nextEntry()
# completed 1 repeats of 'trials'(only one repeat in this cond file for this exp)

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# Finish and close everything
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
thisExp.abort()  # or data files will save again on exit
win.close()
tracker.setConnectionState(False)
io.quit()
core.quit()
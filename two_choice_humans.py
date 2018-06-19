#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np, csv, random, pumps, time, serial # pumps is Wolfgang's code to control pumps
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  
import sys  
from psychopy.iohub.client import launchHubServer # to make eye tracker work


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'two_choice'  # from the Builder filename that created this script
expInfo = {u'participant': u'01', u'session': u'1', u'run': u'1', u'use_pumps': u'n',
 u'use_scanner': u'y', u'use_eye_tracker': u'n', u'reward': u'money', u'resp_type': u'button', u'window':75}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_session%s_run%s' %(expInfo['participant'], expName,
 expInfo['date'], expInfo['session'], expInfo['run'])

# Create a csv file to save response times etc. Previous one is the native Psychopy file.
file_name = 'data/S%s_run%s_session%s_%s' %(expInfo['participant'], expInfo['run'],
 expInfo['session'], expInfo['reward'])
csv_file = open(file_name+'.csv', 'wb')
writer_object = csv.writer(csv_file, delimiter=",") # create object to write in

writer_object.writerow(['event', 't', 'participant', 'trial', 'session', 'run', 'reward',
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
eyetracker_config['simulation_mode'] = True
eyetracker_config['runtime_settings'] = dict(sampling_rate=1000, track_eyes='RIGHT')

io = launchHubServer(**{iohub_tracker_class_path: eyetracker_config})

# Get some iohub devices for future access.
keyboard = io.devices.keyboard
display = io.devices.display
tracker = io.devices.tracker

# run eyetracker calibration
r = tracker.runSetupProcedure()

# Create the window
win = visual.Window(
    display.getPixelResolution(), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0.506,0.506,0.506], colorSpace='rgb',
    blendMode='avg', useFBO=False) # FBO must be False for many screens for it to work

gaze_dot = visual.GratingStim(win, tex=None, mask='gauss', pos=(0, 0),
                              size=(66, 66), color='red', units='pix')

# Calculate the frame rate 
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate']) # frame duration in secs
else:
    frameDur = 1.0 / 60.0  

# Initialize components for Routine "wait_scanner"
wait_scannerClock = core.Clock()

# Initialize components for Routine "blank_screen1"
blank_screen1Clock = core.Clock()
ISI0 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI0')

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

# Initialize components for Routine "ISI3"
ISI3Clock = core.Clock()

isi3 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='isi3')

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

# Initialize components for Routine "ISI4"
ISI4Clock = core.Clock()
isi4 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='isi4')

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
left_feedback = visual.ImageStim(
    win=win, name='left_feedback',
    image='stim/noReward.png', mask=None,
    ori=0, pos=[-0.5, 0], size=.4,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
right_feedback = visual.ImageStim(
    win=win, name='right_feedback',
    image='stim/reward.png', mask=None,
    ori=0, pos=[0.5, 0], size=.4,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
outcome_text = visual.TextStim(win=win, name='outcome_text',
    text='Trial missed!',
    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "ISI5"
ISI5Clock = core.Clock()
isi5 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='isi5')

# Initialize components for Routine "rnf_delivery"
rnf_deliveryClock = core.Clock()
rnf_delivery_txt = visual.TextStim(win=win, name='rnf_delivery_txt',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='Red', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ISI6"
ISI6Clock = core.Clock()
isi6 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='isi6')

# Initialize components for Routine "blank_screen2"
blank_screen2Clock = core.Clock()
ISI_endExp = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_endExp')

#### START BEGIN EXPERIMENT SNIPPET ####
colors = []
t = 0.00
currentRun = 1

# Fixation cross as a text stim with text equal to +
fix_cross = visual.TextStim(win=win, ori=0,	name='fixation',
						  	text='+', font='Arial',	pos=[0, 0], 
						  	height=0.3, wrapWidth=None, color='white', 
						  	colorSpace='rgb', opacity=1, depth=0.0)

# the following are TEXTBOX objects for debugging purposes. 
# Otherwise there are memory leaks if you update textstim
# objects on every frame due to some problem with pyglet

t_txt = visual.TextBox(window=win, text='t: ' + str(round(t, 2)), font_size=20,
                         font_color=[-1, -1, 1], size=(1.9, .3), pos=(-0.8, .6), 
                         grid_horz_justification='center', units='norm')

run_txt = visual.TextBox(window=win, text='run name: ' + expInfo['run'], font_size=20,
                         font_color=[-1, -1, 1], size=(1.9, .3), pos=(-0.8, 0.5), 
                         grid_horz_justification='center', units='norm')

currentRun_txt = visual.TextBox(window=win, text='text', font_size=20,
                         font_color=[-1, -1, 1], size=(1.9, .3), pos=(-0.8, 0.4), 
                         grid_horz_justification='center', units='norm')

time_fixating_txt = visual.TextStim(win=win, ori=0, name='fixation', 
						text='time_fixating: ' + str(round(0.00, 2)), font='Arial',
						pos=[0.0, -0.2], height=0.3, wrapWidth=None, color='white', 
						colorSpace='rgb', opacity=1, depth=0.0)

debug = True # are we showing the debugging stuff on the screen?
nMissed = 0 # to track how many missed trials and show them on screen
#gazeOK_center_list , gazeOK_right_list, gazeOK_left_list =  [], [], [] # to debug, comment if not debugging
#isFixatingLeft = False
gaze_pos = None

# Handy functions, including Wolfgang's pumps 
def msg_to_screen(text_stim, autodraw=False):
	#text_object=visual.TextStim(win, text=msg, pos=(x,y), color=u'white')
    text_stim.setAutoDraw(autodraw) # autodraw is false so that the txt doesn't appear constantly
    text_stim.draw()

def show_debugging_stuff():
	''' set text for stims to show every frame '''
	t_txt.setText('t:  %s' %str(round(t, 2)))	            
	run_txt.setText('run_name:  ' + expInfo['run'])
	currentRun_txt.setText('current run:  %s' %str(currentRun))
	#cond_file_txt.setText('conditions_'+expInfo['reward']+'_'+expInfo['resp_type']+'_'+expInfo['run']+'.xlsx')

    # show text stims on every frame
	t_txt.draw()
	run_txt.draw()
	currentRun_txt.draw()
	#cond_file_txt.draw()

def wait_for_scanner():
    ''' discard the first scans '''
    n_discard = 3
    wait_txt = visual.TextStim(win, 'Waiting for Scanner ...', color="black")
    wait_txt.setAutoDraw(True)
    win.flip()
    for k in xrange(n_discard):
    	keys = event.waitKeys(keyList='5')
    	if k == 0:
    		clock = core.Clock() # set clock 0 to time of first scan
    	wait_txt.setText(str(n_discard - k - 1))
    	win.flip()
    wait_txt.setAutoDraw(False)
    win.flip()
    return clock

def wait_for_next_run():
    continueRoutine = True
    wait_txt = visual.TextStim(win, 'Waiting for next run ...', color="black")
    wait_txt.setAutoDraw(True)

    while continueRoutine:
        win.flip()
        for i in range(2):
            keys = event.waitKeys(keyList='c')
            wait_txt.setText('Ready?')
            win.flip()
        wait_txt.setAutoDraw(False)
        continueRoutine = False

def configure_pumps(volume=.75, diameter=26.77, rate=60, direction='INF', address=0):
    ''' configure pumps for the experiment 
    Create serial connection (in Rangel's PC is COM3)
    This needs to be changed according to which computer
    is running the task '''

    ser = serial.Serial() # Create serial connection
    ser.baudrate = 1200 # this is the default rate (1200)
    ser.port = 'COM3' # change according to name Device Manager shows

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
    for squirt in range(mag):
        p.run(address)
        time.sleep(.5) # try to see whether core.wait() would work better

# configure pumps
if expInfo['use_pumps'] == 'y':  
    p = configure_pumps()
    address = 0 # use first pump

if expInfo['use_scanner'] == 'y':
    globalClock = wait_for_scanner() # wait_for_scanner returns the clock that starts when scanner starts
    #core.Clock()  # to track the time since experiment started
else:
    globalClock = core.Clock() # create global clock in case scanner is not used

routineTimer = core.CountdownTimer()  # timer for each routine; resets every time they start

#### FINISH BEGIN EXPERIMENT SNIPPET ####

##########################
# EXPERIMENT STARTS HERE #
##########################

# To randomise each run (or run), we shuffle the two runs (or runs) and response types
# Since we have 4 conditions files, this should make it nice and neat
# Within each cond file though, everything is randomised 

run_list = np.random.permutation([1, 2]).tolist()
response_type_list = np.random.permutation([u'button', u'gaze']).tolist()

# expInfo['run'] = str(run_number) # assign the 
# expInfo['resp_type'] = response_type

# set up handler to look after randomisation of conditions etc

trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_v2.xlsx', selection=u'0:5'), 
    seed=None, name='trials')		

thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values

# Draw text on every frame when debugging
fix_cross.setAutoDraw(True)

# ------Prepare to start Routine "blank_screen1"-------
t = 0
blank_screen1Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
blank_screen1Components = [ISI0]
for thisComponent in blank_screen1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "blank_screen1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blank_screen1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *ISI0* period
    if t >= 0.0 and ISI0.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI0.tStart = t
        ISI0.frameNStart = frameN  # exact frame index
        ISI0.start(5)
    elif ISI0.status == STARTED:  # one frame should pass before updating params and completing
        ISI0.complete()  # finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank_screen1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank_screen1"-------
for thisComponent in blank_screen1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# -------Start looping trials-------

if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys(): 
            exec(paramName + '= thisTrial.' + paramName)

    first_cue_presented = np.random.randint(1, 3) # sample 1 or 2 (3 excluded in Python)

    # Randomise which cue is presented first in the sequential stage
    if first_cue_presented == 1:

        # ------Prepare to start Routine "cue1"-------
        t = 0
        cue1Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        first_cue.setFillColor(color_left)
        first_cue.edges = n_edges_left

        ##### START BEGIN ROUTINE SNIPPET #####
        
        writer_object.writerow(["cue1_On", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), expInfo['session'], expInfo['run'], reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])

        ##### END BEGIN ROUTINE SNIPPET #####

        # keep track of which components have finished
        cue1Components = [first_cue]
        for thisComponent in cue1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # io.clearEvents()
        # tracker.setRecordingState(True)

        # END BEGIN ROUTINE CUE1 SNIPPET

        # -------Start Routine "cue1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cue1Clock.getTime()           

            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *first_cue* updates
            if t >= 0 and first_cue.status == NOT_STARTED:
                # keep track of start time/frame for later
                first_cue.tStart = t
                first_cue.frameNStart = frameN  # exact frame index
                first_cue.setAutoDraw(True)
            frameRemains = 0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if first_cue.status == STARTED and t >= frameRemains:
                first_cue.setAutoDraw(False)

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cue1Components:
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
        
        # -------Ending Routine "cue1"-------
        for thisComponent in cue1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        ###### START END ROUTINE CUE1 SNIPPET #####
        
        writer_object.writerow(["cue1_Off", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), expInfo['session'], expInfo['run'], reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])

        # io.clearEvents()
        # tracker.setRecordingState(False)
        
        ##### FINISH END ROUTINE CUE1 SNIPPET #####
        
        # ------Prepare to start Routine "ISI1"-------
        t = 0
        ISI1Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        ISI_duration = np.random.uniform(3)
        # keep track of which components have finished
        ISI1Components = [isi1]
        for thisComponent in ISI1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ISI1"-------
        while continueRoutine:
            # get current time
            t = ISI1Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *isi1* period
            if t >= 0.0 and isi1.status == NOT_STARTED:
                # keep track of start time/frame for later
                isi1.tStart = t
                isi1.frameNStart = frameN  # exact frame index
                isi1.start(ISI_duration)                
            elif isi1.status == STARTED:  # one frame should pass before updating params and completing
                isi1.complete()  # finish the static period
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI1Components:
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
        
        # -------Ending Routine "ISI1"-------
        for thisComponent in ISI1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "ISI1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "cue2"-------
        t = 0
        cue2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1)
        # update component parameters for each repeat
        second_cue.setFillColor(color_right)
        second_cue.edges = n_edges_right

        ##### START BEGIN ROUTINE SNIPPET #####
        
        writer_object.writerow(["cue2_On", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), expInfo['session'], expInfo['run'], reward, str(prob1),
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
            t_txt.draw()
            run_txt.draw()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *second_cue* updates
            if t >= 0 and second_cue.status == NOT_STARTED:
                # keep track of start time/frame for later
                second_cue.tStart = t
                second_cue.frameNStart = frameN  # exact frame index
                second_cue.setAutoDraw(True)                
            frameRemains = 0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if second_cue.status == STARTED and t >= frameRemains:
                second_cue.setAutoDraw(False)      
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cue2Components:
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
        
        # -------Ending Routine "cue2"-------
        for thisComponent in cue2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # START END ROUTINE CUE2 SNIPPET
        
        writer_object.writerow(["cue2_Off", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), expInfo['session'], expInfo['run'], reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
        
        # FINISH END ROUTINE CUE2 SNIPPET

    elif first_cue_presented == 2:
                # ------Prepare to start Routine "cue2"-------
        t = 0
        cue2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1)
        # update component parameters for each repeat
        second_cue.setFillColor(color_right)
        second_cue.edges = n_edges_right

        # START BEGIN ROUTINE CUE2 SNIPPET
        
        writer_object.writerow(["cue2_On", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), expInfo['session'], expInfo['run'], reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
        
        # END BEGIN ROUTINE CUE2 SNIPPET

        # keep track of which components have finished
        cue2Components = [second_cue]
        for thisComponent in cue2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "cue2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cue2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *second_cue* updates
            if t >= 0 and second_cue.status == NOT_STARTED:
                # keep track of start time/frame for later
                second_cue.tStart = t
                second_cue.frameNStart = frameN  # exact frame index
                second_cue.setAutoDraw(True)
            frameRemains = 0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if second_cue.status == STARTED and t >= frameRemains:
                second_cue.setAutoDraw(False) 
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cue2Components:
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
        
        # -------Ending Routine "cue2"-------
        for thisComponent in cue2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # START END ROUTINE CUE2 SNIPPET
        
        writer_object.writerow(["cue2_Off", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), expInfo['session'], expInfo['run'], reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
        
        # ------Prepare to start Routine "ISI1"-------
        t = 0
        ISI1Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        ISI_duration = np.random.uniform(3)
        # keep track of which components have finished
        ISI1Components = [isi1]
        for thisComponent in ISI1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ISI1"-------
        while continueRoutine:
            # get current time
            t = ISI1Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *isi1* period
            if t >= 0.0 and isi1.status == NOT_STARTED:
                # keep track of start time/frame for later
                isi1.tStart = t
                isi1.frameNStart = frameN  # exact frame index
                isi1.start(ISI_duration)
            elif isi1.status == STARTED:  # one frame should pass before updating params and completing
                isi1.complete()  # finish the static period

            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI1Components:
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
        
        # -------Ending Routine "ISI1"-------
        for thisComponent in ISI1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "ISI1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # ------Prepare to start Routine "cue1"-------
        t = 0
        cue1Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        first_cue.setFillColor(color_left)
        first_cue.edges = n_edges_left
        # START BEGIN ROUTINE CUE1 SNIPPET
        
        writer_object.writerow(["cue1_On", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), expInfo['session'], expInfo['run'], reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])

        # END BEGIN ROUTINE CUE1 SNIPPET

        # keep track of which components have finished
        cue1Components = [first_cue]
        for thisComponent in cue1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "cue1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cue1Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *first_cue* updates
            if t >= 0 and first_cue.status == NOT_STARTED:
                # keep track of start time/frame for later
                first_cue.tStart = t
                first_cue.frameNStart = frameN  # exact frame index
                first_cue.setAutoDraw(True)
            frameRemains = 0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if first_cue.status == STARTED and t >= frameRemains:
                first_cue.setAutoDraw(False)    
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cue1Components:
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
        
        # -------Ending Routine "cue1"-------
        for thisComponent in cue1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        # START END ROUTINE CUE1 SNIPPET
        
        writer_object.writerow(["cue1_Off", str(globalClock.getTime()), expInfo['participant'],
         str(trials.thisN), expInfo['session'], expInfo['run'], reward, str(prob1),
          str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
        
        # FINISH END ROUTINE CUE1 SNIPPET

    # CONTINUE AFTER COUNTERBALANCING PRESENTATION OF CUE1 AND CUE2 

    # ------Prepare to start Routine "ISI2"-------
    t = 0
    ISI2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ISI_duration = np.random.uniform(3)
    # keep track of which components have finished
    ISI2Components = [isi2]
    for thisComponent in ISI2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI2"-------
    while continueRoutine:
        # get current time
        t = ISI2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi2* period
        if t >= 0.0 and isi2.status == NOT_STARTED:
            # keep track of start time/frame for later
            isi2.tStart = t
            isi2.frameNStart = frameN  # exact frame index
            isi2.start(ISI_duration)
        elif isi2.status == STARTED:  # one frame should pass before updating params and completing
            isi2.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI2Components:
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
    
    # -------Ending Routine "ISI2"-------
    for thisComponent in ISI2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ISI2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.00)

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

    # Start Begin Routine snippet
    
    arrow_x_pos = -0.5    
    #ISI_duration = np.random.uniform(2)    

    window = expInfo['window'] # number of frames to check fixation; monitor runs at 75 HZ

    side = None

    fix_cross.setAutoDraw(False)

    writer_object.writerow(["trial_On", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), expInfo['session'], expInfo['run'], reward,
      str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    # Finish Begin Routine snippet    
    
    # keep track of which components have finished
    trialComponents = [resp_image, left_frac, right_frac, key_resp_2, mouse]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED  

    # clear ET events and start recording again for this trial
    if resp_type == "gaze":
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
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

        # *resp_image* updates
        if t >= 0.0 and resp_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp_image.tStart = t
            resp_image.frameNStart = frameN  # exact frame index
            resp_image.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
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
                elif x_pos >= 100:# and y_pos < 100 and y_pos > -100:right_frac.contains([x_pos, y_pos]):# 
                    gaze_ok_region_right.draw() 
                    #side = "right"
                    isFixating = True                    
                    time_fixating = fixatingClock.getTime()
                    if time_fixating >= 1.5:
                        key_resp_2.keys = "9"
                        continueRoutine = False                   
                else: #if x_pos >= -100 and x_pos <= 100:                    
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
        
        # Start Each Frame snippet

        if debug:
            show_debugging_stuff()

        # Finish Each Frame snippet for "Trial" Routine #

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

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
    
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
    trials.addData('key_resp_2.keys',key_resp_2.keys)
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
        trials.addData("wasRewarded", 0) #never rewarded if did not respond
    
    trials.addData("globalTime", globalClock.getTime())
    
    # save in csv
    writer_object.writerow(["trial_Off", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), expInfo['session'], expInfo['run'], reward, str(prob1),
      str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    if resp_type == "gaze":
        io.clearEvents()
        tracker.setRecordingState(False) # stop recording for this trial    

    ##### FINISH END ROUTINE SNIPPET #####
   
    # ------Prepare to start Routine "chosen"-------
    t = 0
    chosenClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    left_chosen.setFillColor(color_left)
    right_chosen.setFillColor(color_right)
    left_chosen.edges = n_edges_left
    right_chosen.edges = n_edges_right
    
    selection_arrow.setPos([-7,-1])
    
    # Start Begin Routine snippet ("chosen" routine)
    if key_resp_2.keys == 'none':
        selection_arrow.setOpacity(0)
    
    selection_arrow.setPos([arrow_x_pos,-0.4])
    writer_object.writerow(["chosen_On", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), expInfo['session'], expInfo['run'], reward, str(prob1),
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
        frameRemains = 0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if right_chosen.status == STARTED and t >= frameRemains:
            right_chosen.setAutoDraw(False)
        
        # *selection_arrow* updates
        if t >= 0.0 and selection_arrow.status == NOT_STARTED:
            # keep track of start time/frame for later
            selection_arrow.tStart = t
            selection_arrow.frameNStart = frameN  # exact frame index
            selection_arrow.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if selection_arrow.status == STARTED and t >= frameRemains:
            selection_arrow.setAutoDraw(False)

        # Start Each Frame snippet
             
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
    writer_object.writerow(["chosen_Off", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), expInfo['session'], expInfo['run'], reward, str(prob1),
      str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    selection_arrow.setOpacity(1)
    fix_cross.setAutoDraw(True) # redraw fixation cross on the screen after choice 
    
    # ------Prepare to start Routine "ISI4"-------
    t = 0
    ISI4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ISI_duration = np.random.uniform(3)
    # keep track of which components have finished
    ISI4Components = [isi4]
    for thisComponent in ISI4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI4"-------
    while continueRoutine:
        # get current time
        t = ISI4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi4* period
        if t >= 0.0 and isi4.status == NOT_STARTED:
            # keep track of start time/frame for later
            isi4.tStart = t
            isi4.frameNStart = frameN  # exact frame index
            isi4.start(ISI_duration)
        elif isi4.status == STARTED:  # one frame should pass before updating params and completing
            isi4.complete()  # finish the static period

        # Start Each Frame snippet
             
        if debug:
            show_debugging_stuff()

        # Finish Each Frame snippet
        
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
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    
    # Start Begin Routine ("feedback" routine) snippet
    
    if key_resp_2.keys == '4':
        right_feedback.setOpacity(0)
        
        if isReinforced:      
            outcome_text.setText('')           
            left_feedback.setImage('stim/reward.png')
        elif not isReinforced:
            outcome_text.setText('')
            left_feedback.setImage('stim/noReward.png') 
    
    elif key_resp_2.keys == '9':
        left_feedback.setOpacity(0) 
        
        if isReinforced:    
            outcome_text.setText('')        
            right_feedback.setImage('stim/reward.png')
        elif not isReinforced:
            outcome_text.setText('')
            right_feedback.setImage('stim/noReward.png')
    
    elif key_resp_2.keys == 'none':
        outcome_text.setText('Trial missed!')
        left_feedback.setOpacity(0)
        right_feedback.setOpacity(0)
    
    writer_object.writerow(["feedback_On", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), expInfo['session'], expInfo['run'], reward,
      str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    
    # Finish Begin Routine snippet ("feedback" routine)
    # keep track of which components have finished
    feedbackComponents = [left_feedback, right_feedback, outcome_text]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *left_feedback* updates
        if t >= 0.0 and left_feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_feedback.tStart = t
            left_feedback.frameNStart = frameN  # exact frame index
            left_feedback.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if left_feedback.status == STARTED and t >= frameRemains:
            left_feedback.setAutoDraw(False)
        
        # *right_feedback* updates
        if t >= 0.0 and right_feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_feedback.tStart = t
            right_feedback.frameNStart = frameN  # exact frame index
            right_feedback.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if right_feedback.status == STARTED and t >= frameRemains:
            right_feedback.setAutoDraw(False)
        
        # *outcome_text* updates
        if t >= 0.0 and outcome_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            outcome_text.tStart = t
            outcome_text.frameNStart = frameN  # exact frame index
            outcome_text.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if outcome_text.status == STARTED and t >= frameRemains:
            outcome_text.setAutoDraw(False)

        ##### Start Each Frame snippet #####
             
        if debug:
            show_debugging_stuff()

        ##### Finish Each Frame snippet #####
        
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
    ##### START END ROUTINE FOR FEEDBACK ROUTINE ####
    
    writer_object.writerow(["feedback_Off", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), expInfo['session'], expInfo['run'], reward,
      str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    # take colour back to stimuli for next trial
    right_feedback.setOpacity(1) 
    left_feedback.setOpacity(1)
    
    #### FINISH END ROUTINE SNIPPET FOR FEEDBACK ROUTINE ####    
    
    # ------Prepare to start Routine "ISI5"-------
    t = 0
    ISI5Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ISI_duration = np.random.uniform(3)
    # keep track of which components have finished
    ISI5Components = [isi5]
    for thisComponent in ISI5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI5"-------
    while continueRoutine:
        # get current time
        t = ISI5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi5* period
        if t >= 0.0 and isi5.status == NOT_STARTED:
            # keep track of start time/frame for later
            isi5.tStart = t
            isi5.frameNStart = frameN  # exact frame index
            isi5.start(ISI_duration)
        elif isi5.status == STARTED:  # one frame should pass before updating params and completing
            isi5.complete()  # finish the static period
        
        ##### Start Each Frame snippet #####
             
        if debug:
            show_debugging_stuff()

        ##### Finish Each Frame snippet #####

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI5"-------
    for thisComponent in ISI5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ISI5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rnf_delivery"-------
    t = 0
    rnf_deliveryClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    writer_object.writerow(["rnf_delivery_On", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), expInfo['session'], expInfo['run'], reward,
      str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    if isReinforced:
        if reward=="money":
            if key_resp_2.keys == "left":
                rnf_delivery_txt.setText("You have won \n" + "%d token(s)!" %mag1)
                rnf_delivery_txt.setColor("Black", colorSpace="rgb")
            elif key_resp_2.keys == "right":
                rnf_delivery_txt.setText("You have won \n" + "%d token(s)!" %mag2)
                rnf_delivery_txt.setColor("Black", colorSpace="rgb")
        elif reward=="juice":
            if key_resp_2.keys == "left":
                rnf_delivery_txt.setText("You have won \n" + "%d squirt(s) of juice!" %mag1)
                rnf_delivery_txt.setColor("Black", colorSpace="rgb")
                
            elif key_resp_2.keys == "right":
                rnf_delivery_txt.setText("You have won \n" + "%d squirt(s) of juice!" %mag2)
                rnf_delivery_txt.setColor("Black", colorSpace="rgb")
                
    elif not isReinforced:
        rnf_delivery_txt.setText("Nothing won")
        rnf_delivery_txt.setColor("Black", colorSpace="rgb")
    
    # keep track of which components have finished
    rnf_deliveryComponents = [rnf_delivery_txt]
    for thisComponent in rnf_deliveryComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "rnf_delivery"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rnf_deliveryClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rnf_delivery_txt* updates
        if t >= 0.0 and rnf_delivery_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            rnf_delivery_txt.tStart = t
            rnf_delivery_txt.frameNStart = frameN  # exact frame index
            rnf_delivery_txt.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if rnf_delivery_txt.status == STARTED and t >= frameRemains:
            rnf_delivery_txt.setAutoDraw(False)

        ##### Start Each Frame snippet #####
             
        if debug:
            show_debugging_stuff()

        ##### Finish Each Frame snippet #####       
        
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

    if isReinforced and reward=="juice": # use pumps after reinforcement
        if key_resp_2.keys == "right":
            deliver_juice(mag2) # mag2 is magnitude right in conditions file
        else: 
            deliver_juice(mag1) # mag1 is magnitued left
    
    # -------Ending Routine "rnf_delivery"-------
    for thisComponent in rnf_deliveryComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    writer_object.writerow(["rnf_delivery_Off", str(globalClock.getTime()), expInfo['participant'],
     str(trials.thisN), expInfo['session'], expInfo['run'], reward,
      str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    
    # ------Prepare to start Routine "ISI6"-------
    t = 0
    ISI6Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ISI_duration = np.random.uniform(3)
    # keep track of which components have finished
    ISI6Components = [isi6]
    for thisComponent in ISI6Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI6"-------
    while continueRoutine:
        # get current time
        t = ISI6Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi6* period
        if t >= 0.0 and isi6.status == NOT_STARTED:
            # keep track of start time/frame for later
            isi6.tStart = t
            isi6.frameNStart = frameN  # exact frame index
            isi6.start(ISI_duration)
        elif isi6.status == STARTED:  # one frame should pass before updating params and completing
            isi6.complete()  # finish the static period

        ##### Start Each Frame snippet #####
             
        if debug:
            show_debugging_stuff()

        ##### Finish Each Frame snippet #####            
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI6"-------
    for thisComponent in ISI6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ISI6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
   
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

currentRun += 1

# show screen to wait for next run
if currentRun in [1,2,3]: # if not the last run, show the screen
	wait_for_next_run()

# Experiment finished, now show last blank screen

# ------Prepare to start Routine "blank_screen2"-------
t = 0
blank_screen2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)

blank_screen2Components = [ISI_endExp]
for thisComponent in blank_screen2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "blank_screen2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blank_screen2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

    if t >= 0.0 and ISI_endExp.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_endExp.tStart = t
        ISI_endExp.frameNStart = frameN  # exact frame index
        ISI_endExp.start(10)
    elif ISI_endExp.status == STARTED:  # one frame should pass before updating params and completing
        ISI_endExp.complete()  # finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank_screen2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank_screen2"-------
for thisComponent in blank_screen2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Finish and close all connections
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
thisExp.abort()  # or data files will save again on exit
win.close()
tracker.setConnectionState(False)
io.quit()
core.quit()
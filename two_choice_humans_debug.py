#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.6),
    on Thu 17 May 2018 12:57:29 PM PDT
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'two_choice_juice_money'  # from the Builder filename that created this script
expInfo = {u'eye_tracker': u'NO', u'session': u'001', u'participant': u'001', u'pumps': u'NO', u'reward': u'juice'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0.506,0.506,0.506], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "cue1"
cue1Clock = core.Clock()
first_cue = visual.ImageStim(
    win=win, name='first_cue',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=400,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "ISI1"
ISI1Clock = core.Clock()

isi1 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='isi1')

# Initialize components for Routine "cue2"
cue2Clock = core.Clock()
second_cue = visual.ImageStim(
    win=win, name='second_cue',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=400,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "ISI2"
ISI2Clock = core.Clock()
isi2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='isi2')


# Initialize components for Routine "trial"
trialClock = core.Clock()
resp_image = visual.ImageStim(
    win=win, name='resp_image',
    image='sin', mask=None,
    ori=0, pos=[0.0, 0.5], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
left_frac = visual.ImageStim(
    win=win, name='left_frac',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[-400, 0], size=400,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
right_frac = visual.ImageStim(
    win=win, name='right_frac',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[400, 0], size=400,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Start Begin Experiment snippet 

# Import libraries
import numpy as np, csv, random
import pumps

# libraries for eye tracking
from pylink import *
import time
import gc
import sys
import os

RIGHT_EYE = 1
LEFT_EYE = 0
BINOCULAR = 2
SCREENWIDTH = 1024
SCREENHEIGHT = 768

debug = True # are we showing the debugging stuff on the screen?
nMissed = 0

def msg_to_screen(msg,x,y, autodraw=False):
    ''' Shows message on the screen '''
    text_object=visual.TextStim(win, text=msg, pos=(x,y), color=u'red')
    text_object.setAutoDraw(autodraw) # autodraw is false so that the txt doesn't appear constantly
    text_object.draw()

def show_debugging_stuff():
    ''' When debug is True, we show this during the 'trial' routine'''
    t_txt=visual.TextStim(win, text='t: ' + str(round(t,2)), pos=(-0.5, 0.6), color=u'black')
    t_txt.draw()

    globalTimer_txt=visual.TextStim(win, text='timer: ' + str(round(globalClock.getTime(),2)), pos=(0.5, -0.6), color=u'black')
    globalTimer_txt.draw()

    #msg_to_screen('block: ' + str(block), -0.7, -0.9)
    msg_to_screen('prob1: ' + str(prob1), -0.6, -0.7)
    msg_to_screen('prob2: '+ str(prob2), -0.6, -0.8)
    msg_to_screen('stim1: ' + str(stim1), -0.6, -0.5)
    msg_to_screen('stim2: '+str(stim2), -0.6, -0.6)
    msg_to_screen('mag1: '+str(mag1), -0.6, 0.7)
    msg_to_screen('mag2: '+str(mag2), -0.6, 0.6)
    msg_to_screen('reward: '+str(reward), 0.5, -0.7)
    msg_to_screen('nMissed: '+str(nMissed), 0.5, -0.8)
    msg_to_screen('eye tracker?: '+expInfo['eye_tracker'], 0.5, -0.9)

if expInfo["eye_tracker"] == "YES":
    # eye tracking functions
    def end_trial():
        '''Ends recording: adds 100 msec of data to catch final events'''
        endRealTimeMode()  
        pumpDelay(100)    
        getEYELINK().stopRecording()
        while getEYELINK().getkey() : 
            pass

    def tracker_log_pre_event(trial, stimulus_name='no_name'):
        #Always send a TRIALID message before starting to record.
        #EyeLink Data Viewer defines the start of a trial by the TRIALID message.  
        #This message is different than the start of recording message START that is logged when the trial recording begins. 
        #The Data viewer will not parse any messages, events, or samples, that exist in the data file prior to this message.
        msg = "TRIALID %d" % trial
        getEYELINK().sendMessage(msg)
        msg = "!V TRIAL_VAR_DATA %d" % trial
        getEYELINK().sendMessage(msg)
        
        #The following loop does drift correction at the start of each trial
        while True:
            # Checks whether we are still connected to the tracker
            if not getEYELINK().isConnected():
                return ABORT_EXPT   
            # Does drift correction and handles the re-do camera setup situations
            try:
                error = getEYELINK().doDriftCorrect(SCREENWIDTH // 2, SCREENHEIGHT // 2, 1, 1)
                if error != 27: 
                    break
                else:
                    getEYELINK().doTrackerSetup()
            except:
                getEYELINK().doTrackerSetup()

        #switch tracker to idle and give it time to complete mode switch
        getEYELINK().setOfflineMode()
        msecDelay(50) 

        #start recording samples and events to edf file and over the link. 
        error = getEYELINK().startRecording(1, 1, 1, 1)
        if error:
            return error

        #disable python garbage collection to avoid delays
        gc.disable()

        #begin the realtime mode
        beginRealTimeMode(100)

        #determine trial start time
        startTime = currentTime()

        # This supplies the title of the current trial at the bottom of the eyetracker display
        message = "record_status_message 'Stimulus: %s, Trial %d/%d '" % (stimulus_name, trial, NTRIALS)
        getEYELINK().sendCommand(message)

        return startTime


    def tracker_log_post_event(startTime, button):
        # determine trial time at which initial display came on
        drawTime = (currentTime() - startTime)
        getEYELINK().sendMessage("%d DISPLAY ON" % drawTime)
        getEYELINK().sendMessage("SYNCTIME %d" % drawTime)
        try: 
            getEYELINK().waitForBlockStart(100,1,0) 
        except RuntimeError: 
            if getLastError()[0] == 0: # wait time expired without link data 
                end_trial()
                print ("ERROR: No link samples received!") 
                return TRIAL_ERROR 
            else: # for any other status simply re-raise the exception 
                raise
                    
        #determine which eye is-are available
        eye_used = getEYELINK().eyeAvailable() #determine which eye(s) are available 
        if eye_used == RIGHT_EYE:
            getEYELINK().sendMessage("EYE_USED 1 RIGHT")
        elif eye_used == LEFT_EYE or eye_used == BINOCULAR:
            getEYELINK().sendMessage("EYE_USED 0 LEFT")
            eye_used = LEFT_EYE
        else:
            print ("Error in getting the eye information!")
            return TRIAL_ERROR

        # reset keys and buttons on tracker
        getEYELINK().flushKeybuttons(0)

        getEYELINK().sendMessage("TRIAL_RESULT %d" % button)
        #return exit record status
        ret_value = getEYELINK().getRecordingStatus()
        #end realtime mode
        endRealTimeMode()
        #re-enable python garbage collection to do memory cleanup at the end of trial
        gc.enable()

        return ret_value


    def eval_gaze(x, x_list, window=20, margin=100):
        ''' calculate average gaze over the last "window" measurements.
        Returns left/right choice, depending on whether this average
        was smaller/larger than screenwidth/2 +/- "margin" '''
        button = -1 # this means participant not looking at either side

        x_list.insert(0, x) 

        if len(x_list) > window:
            _ = x_list.pop()

        if len(x_list) == window:
            m = np.mean(x_list) # takes the average of x positions in the last window
            if m > SCREENWIDTH / 2 + margin: # if looking right
                button = 1
            elif m < SCREENWIDTH / 2 - margin: # if looking left
                button = 0

        return button

    # MORE EYE TRACKING STUFF #

    # change current directory to the one where this code is located 
    # this way resource stimuli like images and sounds can be located using relative paths
    spath = os.path.dirname(sys.argv[0])
    if len(spath) !=0: os.chdir(spath)

    #initialize tracker object with default IP address.
    #created objected can now be accessed through getEYELINK()
    eyelinktracker = EyeLink()
    #Here is the starting point of the experiment
    #Initializes the graphics
    #INSERT THIRD PARTY GRAPHICS INITIALIZATION HERE IF APPLICABLE 
    # openGraphics((SCREENWIDTH, SCREENHEIGHT),32)
    print 1

    #Opens the EDF file.
    edfFileName = "TEST.EDF"
    getEYELINK().openDataFile(edfFileName)  

    #flush all key presses and set tracker mode to offline.
    flushGetkeyQueue() 
    getEYELINK().setOfflineMode()        
    print 2
    #Sets the display coordinate system and sends mesage to that effect to EDF file;
    getEYELINK().sendCommand("screen_pixel_coords =  0 0 %d %d" %(SCREENWIDTH - 1, SCREENHEIGHT - 1))
    getEYELINK().sendMessage("DISPLAY_COORDS  0 0 %d %d" %(SCREENWIDTH - 1, SCREENHEIGHT - 1))

    tracker_software_ver = 0
    eyelink_ver = getEYELINK().getTrackerVersion()
    if eyelink_ver == 3:
        tvstr = getEYELINK().getTrackerVersionString()
        vindex = tvstr.find("EYELINK CL")
        tracker_software_ver = int(float(tvstr[(vindex + len("EYELINK CL")):].strip()))

    if eyelink_ver>=2:
        getEYELINK().sendCommand("select_parser_configuration 0")
        if eyelink_ver == 2: #turn off scenelink camera stuff
            getEYELINK().sendCommand("scene_camera_gazemap = NO")
    else:
        getEYELINK().sendCommand("saccade_velocity_threshold = 35")
        getEYELINK().sendCommand("saccade_acceleration_threshold = 9500")
    print 3

    # set EDF file contents 
    getEYELINK().sendCommand("file_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT")
    if tracker_software_ver>=4:
        getEYELINK().sendCommand("file_sample_data  = LEFT,RIGHT,GAZE,AREA,GAZERES,STATUS,HTARGET,INPUT")
    else:
        getEYELINK().sendCommand("file_sample_data  = LEFT,RIGHT,GAZE,AREA,GAZERES,STATUS,INPUT")

    # set link data (used for gaze cursor) 
    getEYELINK().sendCommand("link_event_filter = LEFT,RIGHT,FIXATION,FIXUPDATE,SACCADE,BLINK,BUTTON,INPUT")
    if tracker_software_ver>=4:
        getEYELINK().sendCommand("link_sample_data  = LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,HTARGET,INPUT")
    else:
        getEYELINK().sendCommand("link_sample_data  = LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,INPUT")
    print 4
    setCalibrationColors( (0, 0, 0),(255, 255, 255))   #Sets the calibration target and background color
    print 5
    myHeight = 20 #SCREENWIDTH//70
    myWidth = 20 #SCREENWIDTH//300
    print 6
    setTargetSize(myHeight, myWidth)     #select best size for calibration target
    print 7
    setCalibrationSounds("", "", "")
    print 8
    setDriftCorrectSounds("", "off", "off")

    #Do the tracker setup at the beginning of the experiment.
    getEYELINK().doTrackerSetup()
    print 9

if expInfo["pumps"] == "YES":
    def configure_pumps(volume=.75, diameter=26.77, rate=60, direction='INF', address=0):
        ''' configure pumps for the experiment '''
        
        p = pumps.Pump('/dev/ttyUSB0')

        s = p.volume(volume, address=address)  # how much to dispense
        s = p.diameter(diameter, address=address) # diameter of syringe
        s = p.rate(rate, address=address) # how fast
        s = p.direction(direction, address=address) # pump (not suck) liquid

        return p 
         
    p = configure_pumps()
    address = 0 # use first pump

# create a csv file to save response times etc
file_name = 'data/S%s_%s_%s_%s' %(expInfo['participant'], expInfo['date'], expInfo['session'], expInfo['reward'])
csv_file = open(file_name+'.csv', 'wb')
writer_object = csv.writer(csv_file, delimiter=",") 

writer_object.writerow(['event', 't', 'participant', 'trial', 'session', 'reward', 'prob1', 'prob2', 'mag1', 'mag2','resp', 'wasRnf', 'resp_type'])#'response.keys', 'response.rt', 'wasRnf', 'trials.thisN', 'trial']) # this is the first row with headers for columns



# Initialize components for Routine "ISI3"
ISI3Clock = core.Clock()

isi3 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='isi3')

# Initialize components for Routine "chosen"
chosenClock = core.Clock()
left_chosen = visual.ImageStim(
    win=win, name='left_chosen',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[-400, 0], size=400,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
right_chosen = visual.ImageStim(
    win=win, name='right_chosen',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[400, 0], size=400,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
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
    ori=0, pos=[-0.5, 0], size=.5,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
right_feedback = visual.ImageStim(
    win=win, name='right_feedback',
    image='stim/reward.png', mask=None,
    ori=0, pos=[0.5, 0], size=.5,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
outcome_text = visual.TextStim(win=win, name='outcome_text',
    text='Trial missed!',
    font='Arial',
    pos=[0, 0], height=0.6, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=-2.0);
outcome_image = visual.ImageStim(
    win=win, name='outcome_image',
    image='stim/pound_coin_royal_mint.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)


# Initialize components for Routine "ISI5"
ISI5Clock = core.Clock()
isi5 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='isi5')


# Initialize components for Routine "rnf_delivery"
rnf_deliveryClock = core.Clock()
rnf_delivery_txt = visual.TextStim(win=win, name='rnf_delivery_txt',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='Red', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "ISI6"
ISI6Clock = core.Clock()
isi6 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='isi6')


# Initialize components for Routine "goodbye"
goodbyeClock = core.Clock()
goodbye_txt = visual.TextStim(win=win, name='goodbye_txt',
    text='Session finished! \n\nTrials missed: ',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1,
    depth=0.0);
nMissed_txt = visual.TextStim(win=win, name='nMissed_txt',
    text='default text',
    font='Arial',
    pos=(0.4, -0.65), height=0.3, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=-1.0);


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_'+expInfo['reward']+'.xlsx', selection='20:23'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "cue1"-------
    t = 0
    cue1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    first_cue.setImage(stim1)
    # START BEGIN ROUTINE CUE1 SNIPPET
    
    writer_object.writerow(["cue1_On", str(globalClock.getTime()), expInfo['participant'], str(trials.thisN), expInfo['session'], reward, str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
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
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cue1"-------
    for thisComponent in cue1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # START END ROUTINE CUE1 SNIPPET
    
    writer_object.writerow(["cue1_Off", str(globalClock.getTime()), expInfo['participant'], str(trials.thisN), expInfo['session'], reward, str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    # FINISH END ROUTINE CUE1 SNIPPET
    
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
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    second_cue.setImage(stim2)
    # START BEGIN ROUTINE CUE2 SNIPPET
    
    writer_object.writerow(["cue2_On", str(globalClock.getTime()), expInfo['participant'], str(trials.thisN), expInfo['session'], reward, str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
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
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cue2"-------
    for thisComponent in cue2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # START END ROUTINE CUE2 SNIPPET
    
    writer_object.writerow(["cue2_Off", str(globalClock.getTime()), expInfo['participant'], str(trials.thisN), expInfo['session'], reward, str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    # FINISH END ROUTINE CUE2 SNIPPET
    
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
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    resp_image.setImage(resp_img)
    left_frac.setImage(stim1)
    right_frac.setImage(stim2)
    key_resp_2 = event.BuilderKeyResponse()
    
    # Start Begin Routine trial snippet
    
    arrow_x_pos = -0.5
    ISI_duration = np.random.uniform(3)
    
    writer_object.writerow(["trial_On", str(globalClock.getTime()), expInfo['participant'], str(trials.thisN), expInfo['session'], reward, str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    #frac1, frac2 = stimNames[np.random.randint(1,10)], stimNames[np.random.randint(1,10)]
    
    if expInfo['eye_tracker'] == "YES":
        startTime = tracker_log_pre_event(trials.thisN, stimulus_name=trial_ID)
    
    nSData = None
    sData = None
    button = -1 # 0 = left, 1 = right
    x_list = []
    
    # Finish begin routine trial snippet
    
    # keep track of which components have finished
    trialComponents = [resp_image, left_frac, right_frac, key_resp_2]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # Start Each Frame snippet
        
        #tGlobal = globalClock.getTime()
        
        if debug:
            show_debugging_stuff()
        
        if expInfo['eye_tracker'] == "YES":
            error = getEYELINK().isRecording()  # First check if recording is aborted 
        
            if error != 0:
                end_trial()
            else:
                # see if there are any new samples
                nSData = getEYELINK().getNewestSample() # check for new sample update
        
                # Do we have a sample in the sample buffer? 
                # and does it differ from the one we've seen before?
                if(nSData != None and (sData == None or nSData.getTime() != sData.getTime())):
                    # it is a new sample, let's mark it for future comparisons.
                    sData = nSData 
                    # Detect if the new sample has data for the eye currently being tracked, 
                    if eye_used == RIGHT_EYE and sData.isRightSample():
                        x, y = sData.getRightEye().getGaze()
                        button = eval_gaze(x, x_list)
                    elif eye_used != RIGHT_EYE and sData.isLeftSample():
                        x, y = sData.getLeftEye().getGaze()
                        button = eval_gaze(x, x_list)
        
            # Finish Each Frame snippet
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    # Start End Routine snippet
    if key_resp_2.keys == 'left':# or button == 0:
        arrow_x_pos = -0.6    
        isReinforced = np.random.binomial(1, prob1)
    
    elif key_resp_2.keys == 'right': # or button == 1:
        arrow_x_pos = 0.6
        isReinforced = np.random.binomial(1, prob2)
    
    elif key_resp_2.keys == None:# or button == -1: # replace None from Python with 'none' string
        nMissed += 1
        isReinforced = 0 
        key_resp_2.keys = 'none'
    
    if key_resp_2.keys != 'none':# or button != -1:  # we had a response
        trials.addData("wasRewarded", isReinforced)
    else: # we did not have a response
        trials.addData("wasRewarded", 0) #never rewarded if did not respond
    trials.addData("globalTime", globalClock.getTime())
    
    # save in csv
    writer_object.writerow(["trial_Off", str(globalClock.getTime()), expInfo['participant'], str(trials.thisN), expInfo['session'], reward, str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    if expInfo['eye_tracker'] == "YES":
        ret_value = tracker_log_post_event(startTime, button)
    
    
    # Finish End Routine snippet
    
    
    # ------Prepare to start Routine "ISI3"-------
    t = 0
    ISI3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ISI_duration = 0
    # keep track of which components have finished
    ISI3Components = [isi3]
    for thisComponent in ISI3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI3"-------
    while continueRoutine:
        # get current time
        t = ISI3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi3* period
        if t >= 0.0 and isi3.status == NOT_STARTED:
            # keep track of start time/frame for later
            isi3.tStart = t
            isi3.frameNStart = frameN  # exact frame index
            isi3.start(ISI_duration)
        elif isi3.status == STARTED:  # one frame should pass before updating params and completing
            isi3.complete()  # finish the static period
        
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
    
    # the Routine "ISI3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "chosen"-------
    t = 0
    chosenClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    left_chosen.setImage(stim1)
    right_chosen.setImage(stim2)
    selection_arrow.setPos([-7,-1])
    
    # Start Begin Routine snippet ("chosen" routine)
    
    if key_resp_2.keys == 'none':
        selection_arrow.setOpacity(0)
    
    selection_arrow.setPos([arrow_x_pos,-0.5])
    writer_object.writerow(["chosen_On", str(globalClock.getTime()), expInfo['participant'], str(trials.thisN), expInfo['session'], reward, str(prob1), str(prob2), str(mag1), str(mag2), key_resp_2.keys, isReinforced, resp_type, trial_ID])
    
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
    
    # START END ROUTINE FEEDBACK SNIPPET #
    
    writer_object.writerow(["chosen_Off", str(globalClock.getTime()), expInfo['participant'], str(trials.thisN), expInfo['session'], reward, str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    selection_arrow.setOpacity(1)
    
    # FINISH END ROUTINE FEEDBACK SNIPPET #
    
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
    
    if key_resp_2.keys == 'left':
        right_feedback.setOpacity(0)
        
        if isReinforced:      
            outcome_text.setText('')           
            left_feedback.setImage('stim/reward.png')
        elif not isReinforced:
            outcome_text.setText('')
            left_feedback.setImage('stim/noReward.png') 
    
    elif key_resp_2.keys == 'right':
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
    
    writer_object.writerow(["feedback_On", str(globalClock.getTime()), expInfo['participant'], str(trials.thisN), expInfo['session'], reward, str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    
    # Finish Begin Routine snippet ("feedback" routine)
    # keep track of which components have finished
    feedbackComponents = [left_feedback, right_feedback, outcome_text, outcome_image]
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
        
        # *outcome_image* updates
        if t >= 0.0 and outcome_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            outcome_image.tStart = t
            outcome_image.frameNStart = frameN  # exact frame index
            outcome_image.setAutoDraw(True)
        frameRemains = 0.0 + 0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if outcome_image.status == STARTED and t >= frameRemains:
            outcome_image.setAutoDraw(False)
        
        
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
    ##### START END ROUTINE SNIPPET FOR FEEDBACK ####
    
    writer_object.writerow(["feedback_Off", str(globalClock.getTime()), expInfo['participant'], str(trials.thisN), expInfo['session'], reward, str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    # take colour back to stimuli for next trial
    right_feedback.setOpacity(1) 
    left_feedback.setOpacity(1)
    
    #### FINISH END ROUTINE SNIPPET FOR FEEDBACK ####
    
    
    
    
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
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    writer_object.writerow(["rnf_delivery_On", str(globalClock.getTime()), expInfo['participant'], str(trials.thisN), expInfo['session'], reward, str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    if isReinforced:
        if reward=="money":
            if key_resp_2.keys == "left":
                rnf_delivery_txt.setText("You have won %d tokens!" %mag1)
                rnf_delivery_txt.setColor([1,1,1], colorSpace="rgb")
            elif key_resp_2.keys == "right":
                rnf_delivery_txt.setText("You have won %d tokens!" %mag2)
                rnf_delivery_txt.setColor([1,1,1], colorSpace="rgb")
        elif reward=="juice":
            if key_resp_2.keys == "left":
                rnf_delivery_txt.setText("You have won %d squirts of juice!" %mag1)
                rnf_delivery_txt.setColor([1,1,1], colorSpace="rgb")
                #for squirt in range(mag1):
                #    p.run(address)
                #    time.sleep(.5)
            elif key_resp_2.keys == "right":
                rnf_delivery_txt.setText("You have won %d squirts of juice!" %mag2)
                rnf_delivery_txt.setColor([1,1,1], colorSpace="rgb")
                #for squirt in range(mag2):
                #    p.run(address)
                #    time.sleep(.5)
    elif not isReinforced:
        rnf_delivery_txt.setText("Nothing won")
        rnf_delivery_txt.setColor([1,-1,-1], colorSpace="rgb")
    
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
    
    # -------Ending Routine "rnf_delivery"-------
    for thisComponent in rnf_deliveryComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    writer_object.writerow(["rnf_delivery_Off", str(globalClock.getTime()), expInfo['participant'], str(trials.thisN), expInfo['session'], reward, str(prob1), str(prob2), str(mag1), str(mag2), '', '', '', trial_ID])
    
    
    # ------Prepare to start Routine "ISI6"-------
    t = 0
    ISI6Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ISI_duration = np.random.uniform(2.5)
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

# ------Prepare to start Routine "goodbye"-------
t = 0
goodbyeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
nMissed_txt.setText(nMissed)

key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
goodbyeComponents = [goodbye_txt, nMissed_txt, key_resp_3]
for thisComponent in goodbyeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "goodbye"-------
while continueRoutine:
    # get current time
    t = goodbyeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *goodbye_txt* updates
    if t >= 0.0 and goodbye_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        goodbye_txt.tStart = t
        goodbye_txt.frameNStart = frameN  # exact frame index
        goodbye_txt.setAutoDraw(True)
    frameRemains = 0.0 + 60- win.monitorFramePeriod * 0.75  # most of one frame period left
    if goodbye_txt.status == STARTED and t >= frameRemains:
        goodbye_txt.setAutoDraw(False)
    
    # *nMissed_txt* updates
    if t >= 0.0 and nMissed_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        nMissed_txt.tStart = t
        nMissed_txt.frameNStart = frameN  # exact frame index
        nMissed_txt.setAutoDraw(True)
    frameRemains = 0.0 + 60- win.monitorFramePeriod * 0.75  # most of one frame period left
    if nMissed_txt.status == STARTED and t >= frameRemains:
        nMissed_txt.setAutoDraw(False)
    
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['f'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "goodbye"-------
for thisComponent in goodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "goodbye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()




if getEYELINK() != None:
    # File transfer and cleanup!
    getEYELINK().setOfflineMode()        
    msecDelay(500) 

    #Close the file and transfer it to Display PC
    getEYELINK().closeDataFile()
    getEYELINK().receiveDataFile(edfFileName, edfFileName)
    getEYELINK().close()








# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

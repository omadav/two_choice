# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 21:33:01 2015

@author: erik  marsja se
Full script for the tutorial on http://www.marsja.se/trialhandler-a-psychopy-tutorial/
"""

from psychopy import data, visual, core, event

visual_targets = [digit for digit in xrange(1,9)]

targets_responses = []
for target in visual_targets:
   
   if target %2 == 0:
        correct_response = 'x'

   else:
        correct_response = 'z'
   
   targets_responses.append({'Target':target, 'CorrectResponse':correct_response})
    

trials = data.TrialHandler(targets_responses,20, method='random')


trials.data.addDataType('Response')
trials.data.addDataType('Accuracy')
print(trials)

# experiment_window = visual.Window(size=(800,600),winType='pyglet',fullscr=False,
#                         screen=0, monitor='testMonitor', 
#                         color="black", colorSpace='rgb')


# screen_text = visual.TextStim(experiment_window,text=None,
#                               alignHoriz="center", color = 'white')
                              
# trial_timer = core.Clock()
# accuracy = 0

# for trial in trials:
#     current_time = 0
#     trial_still_running = True
#     trial_timer.reset()
#     while trial_still_running:
#         current_time = trial_timer.getTime()
        
#         if current_time <=.4:
#             screen_text.setText('+')
#             screen_text.draw()
            
#         if current_time >= .4 and current_time <=.8:
#             screen_text.setText(trial['Target'])
#             screen_text.draw()
            
#         if current_time >= .8 and current_time <=1.8:
#             screen_text.setText('+')
#             screen_text.draw()
            
#             responded = event.getKeys()
#             if responded:
#                 print responded

#                 if trial['CorrectResponse'] == responded[0]:
#                     accuracy = 1
#                 else: accuracy = 0

#         if current_time >= 1.8:
#             if not responded:
#                 accuracy = 0
                
#             trial_still_running = False
#         experiment_window.flip()

# 	trials.data.add('Accuracy', accuracy)
#     trials.data.add('Response', responded[0])

# trials.saveAsExcel(fileName='data.csv',
#                   sheetName = 'rawData',
#                   stimOut=[], 
#                   dataOut=['all_raw'])

# experiment_window.close()
# core.quit()
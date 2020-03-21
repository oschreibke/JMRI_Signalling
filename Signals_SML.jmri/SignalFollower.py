import jmri
import java
import java.beans

# reflect the aspects shown on basic signal masts onto SBB type L masts

# based on a script by Bob Jacobsen, copyright 2016
# reworked and extended Otto Schreibke 2020
# License: GPL

# map the basic aspects to the SBB aspects
myDict = {
    "Stop": "Halt",
    "Approach": "FB2",
    "Clear": "FB1"
}


# Define the listeners. 
class SignalFollowerListener(java.beans.PropertyChangeListener):

  def set(self, oSource, oTarget) :
    self.oSource = oSource  
    self.oTarget = oTarget
    self.oSource.addPropertyChangeListener(self)
    return
    
  def propertyChange(self, event):
    # map the source aspect to the target and set accordingly
    self.oTarget.setAspect(myDict.get(self.oSource.getAspect()))
    return

# Iterate ovet the masts collection
#   - set the initial state (Halt) of the non-virtual masts
#     for whatever good reason, simply setting the aspect to be followed doesn't work
#   - set the event listerers on the source masts
#   - set the initial follower state

for m in masts.getNamedBeanSet():
    if m.userName[0] != "v":     # not a virtual mast
        m.setAspect("Halt")      # initialise all followers to "Halt"
        
        # set the event handlers and set the initial following
        source = masts.getSignalMast("v" + m.userName)
        if source:
            SignalFollowerListener().set(source, m)
            m.setAspect(myDict.get(source.getAspect()))
        else:
            print "Couldn't find corresponding source mast for " + m.userName        

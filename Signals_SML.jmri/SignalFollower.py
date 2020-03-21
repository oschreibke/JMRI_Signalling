import jmri
import java
import java.beans

#for sn in masts.getNamedBeanSet():
#   if sn.userName[0] == "v":
#        print sn.userName + " " + sn.getAspect() # + " " + sn.getAspectName()

#for m in masts.getNamedBeanSet():
#    print m.userName + " " + m.getMastType() + " " + m.getSignalSystem() 

#for m in masts.getNamedBeanSet():
#    if m.userName[0] != "v":
#        m.setAspect("Halt")

myDict = {
"Stop": "Halt",
"Approach": "FB2",
"Clear": "FB1"
}

for m in masts.getNamedBeanSet():
    if m.userName[0] != "v":
        a = m.getAspect()
        if not a:
            a = "Unknown"
        print m.userName + " " + a 
        source = masts.getSignalMast("v" + m.userName)
        if source:
            print "Source: " + source.userName + " is showing " + source.getAspect() 
            print "Setting aspect on " + m.userName + " from " + a + " to " + myDict.get(source.getAspect())
            m.setAspect(myDict.get(source.getAspect()))
            print m.userName + " " + m.getAspect() 
        else:
            print "Couldn't find source for " + m.userName
        

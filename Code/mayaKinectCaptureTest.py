# script created by pymel.tools.mel2py from mel file:
# c:\python_cvpr\workspace\mayapython2\src\testpymel\mayakinectcapturetest.mel

import pymel.core as pm
from Cython.Shadow import NULL
	

KinectSkelNames = [	"SKEL_HEAD", 
					"SKEL_NECK",
					"SKEL_TORSO",
					"SKEL_WAIST",
					"SKEL_LEFT_COLLAR",
					"SKEL_LEFT_SHOULDER",
					"SKEL_LEFT_ELBOW",
					"SKEL_LEFT_WRIST",
					"SKEL_LEFT_HAND",
					"SKEL_LEFT_FINGERTIP",
					"SKEL_RIGHT_COLLAR",
					"SKEL_RIGHT_SHOULDER",
					"SKEL_RIGHT_ELBOW",
					"SKEL_RIGHT_WRIST",
					"SKEL_RIGHT_HAND",
					"SKEL_RIGHT_FINGERTIP",
					"SKEL_LEFT_HIP",
					"SKEL_LEFT_KNEE",
					"SKEL_LEFT_ANKLE",
					"SKEL_LEFT_FOOT",
					"SKEL_RIGHT_HIP",
					"SKEL_RIGHT_KNEE",
					"SKEL_RIGHT_ANKLE",
					"SKEL_RIGHT_FOOT"]

KinectSkelJoints = [ "SKEL_HEAD", 
                    "SKEL_NECK",
                    "SKEL_WAIST",
                    
                    "SKEL_LEFT_SHOULDER",
                    "SKEL_LEFT_ELBOW",
                    "SKEL_LEFT_HAND",
                    
                    "SKEL_RIGHT_SHOULDER",
                    "SKEL_RIGHT_ELBOW",
                    "SKEL_RIGHT_HAND",
                    
                    "SKEL_LEFT_HIP",
                    "SKEL_LEFT_KNEE",
                    "SKEL_LEFT_FOOT",
                    
                    "SKEL_RIGHT_HIP",
                    "SKEL_RIGHT_KNEE",
                    "SKEL_RIGHT_FOOT"]

point = [[0.0,0.0,0.0],
		[0.0,0.0,0.0],
		[0.0,0.0,0.0],
		[0.0,0.0,0.0],
		[0.0,0.0,0.0],
		[0.0,0.0,0.0],
		[0.0,0.0,0.0],
		[0.0,0.0,0.0],
		[0.0,0.0,0.0],
		[0.0,0.0,0.0],
		[0.0,0.0,0.0],
		[0.0,0.0,0.0],
		[0.0,0.0,0.0],
		[0.0,0.0,0.0],
		[0.0,0.0,0.0]]

def connectDevice():
	serverAddress = KinectTest_TextFieldGrp_ServerAddress.getText()
	serverAddress = serverAddress + ":" + str(KinectTest_IntFieldGrp_Port.getValue1())
	pm.defineDataServer(s=serverAddress,d='KinectCapture')
	#melGlobals.initVar( 'string[]', 'KinectSkelNames' )
	i=0
	for i in range(0,24):
		pm.attachDeviceAttr((KinectSkelNames[i] + ".translateX"),ax=(KinectSkelNames[i] + "_POS:X"),d="KinectCapture")
		pm.setAttrMapping(ax=(KinectSkelNames[i] + "_POS:X"),scale=-0.01,d="KinectCapture",at=(KinectSkelNames[i] + ".translateX"))
		pm.attachDeviceAttr((KinectSkelNames[i] + ".translateY"),ax=(KinectSkelNames[i] + "_POS:Y"),d="KinectCapture")
		pm.setAttrMapping(ax=(KinectSkelNames[i] + "_POS:Y"),scale=+0.01,d="KinectCapture",at=(KinectSkelNames[i] + ".translateY"))
		pm.attachDeviceAttr((KinectSkelNames[i] + ".translateZ"),ax=(KinectSkelNames[i] + "_POS:Z"),d="KinectCapture")
		pm.setAttrMapping(ax=(KinectSkelNames[i] + "_POS:Z"),scale=-0.01,d="KinectCapture",at=(KinectSkelNames[i] + ".translateZ"))

		pm.attachDeviceAttr((KinectSkelNames[i] + ".rotateX"),ax=(KinectSkelNames[i] + "_ORI:X"),d="KinectCapture")
		pm.setAttrMapping(ax=(KinectSkelNames[i] + "_ORI:X"),scale=-1.0,d="KinectCapture",at=(KinectSkelNames[i] + ".rotateX"))
		pm.attachDeviceAttr((KinectSkelNames[i] + ".rotateY"),ax=(KinectSkelNames[i] + "_ORI:Y"),d="KinectCapture")
		pm.setAttrMapping(ax=(KinectSkelNames[i] + "_ORI:Y"),scale=-1.0,d="KinectCapture",at=(KinectSkelNames[i] + ".rotateY"))
		pm.attachDeviceAttr((KinectSkelNames[i] + ".rotateZ"),ax=(KinectSkelNames[i] + "_ORI:Z"),d="KinectCapture")
		pm.setAttrMapping(ax=(KinectSkelNames[i] + "_ORI:Z"),scale=-1.0,d="KinectCapture",at=(KinectSkelNames[i] + ".rotateZ"))
		
	pm.attachDeviceAttr("KINECT_HAND.translateX",ax="HAND_POS:X",d="KinectCapture")
	pm.setAttrMapping(ax="HAND_POS:X",scale=1.3,d="KinectCapture",at="KINECT_HAND.translateX")
	pm.attachDeviceAttr("KINECT_HAND.translateY",ax="HAND_POS:Y",d="KinectCapture")
	pm.setAttrMapping(ax="HAND_POS:Y",scale=1.3,d="KinectCapture",at="KINECT_HAND.translateY")
	pm.attachDeviceAttr("KINECT_HAND.translateZ",ax="HAND_POS:Z",d="KinectCapture")
	pm.setAttrMapping(ax="HAND_POS:Z",scale=1.3,d="KinectCapture",at="KINECT_HAND.translateZ")
	
	Recording = True
	print Recording

def discDevice():
	pm.defineDataServer(undefine=True,d='KinectCapture')

def OpenCommandPort():
	#srcType='mel'
	pm.commandPort(n=(":"+str(KinectTest_IntFieldGrp_CmdPort.getValue1())))
	#pm.commandPort(n=(":"+str(KinectTest_IntFieldGrp_CmdPort.getValue1())), stp=srcType) 
	#pm.commandPort(n=':9998')

def makeSkel():
	pm.select( d=True )
	pm.joint(p=point[0])
	pm.joint('joint1',p=point[1])
	pm.joint('joint2',p=point[2])
	
	pm.joint('joint2',p=point[3])
	pm.joint('joint4',p=point[4])
	pm.joint('joint5',p=point[5])
	
	pm.joint('joint2',p=point[6])
	pm.joint('joint7',p=point[7])
	pm.joint('joint8',p=point[8])
	
	pm.joint('joint3',p=point[9])
	pm.joint('joint10',p=point[10])
	pm.joint('joint11',p=point[11])
	
	pm.joint('joint3',p=point[12])
	pm.joint('joint13',p=point[13])
	pm.joint('joint14',p=point[14])

#Create Locator to catch the raw data from OpenNI server
#Create Kinect Skeleton with 15 joints
#Link Locator with joints by setting pointConstraint 
def makeNull():
	#pm.melGlobals.initVar( 'string[]', 'KinectSkelNames' )
	i=0
	for i in range(0,24):
		pm.spaceLocator(p=(0, 0, 0),n=KinectSkelNames[i])
		
	pm.spaceLocator(p=(0, 0, 0),n="KINECT_HAND")
	

	for i in range(0,15):
		point[i] = [0.0,0.0,0.0]

	makeSkel()
	
	for i in range(0,15):
	    pm.rename('joint'+str(i+1), KinectSkelJoints[i]+'_jt')

		
	for i in range(0,15):
	    pm.pointConstraint( KinectSkelJoints[i], KinectSkelJoints[i]+'_jt' )
	    pm.orientConstraint( KinectSkelJoints[i], KinectSkelJoints[i]+'_jt' )

    #Create Camera
	cam = pm.camera()[1]
	#print pm.camera(cam, query=True, aspectRatio=True)
	cam.setAspectRatio(3)
	print cam.getAspectRatio()


def makeIK():
	print "Create IK"
	
	#disconnect first, and then reconnect after IK creation
	discDevice()
	
	#record joint location
	for i in range(0,15):
		point[i] = pm.joint(KinectSkelJoints[i]+'_jt', p=True, q=1)
		
	#delete old joints#
	pm.delete( 'SKEL_HEAD_jt' )
	
	makeSkel()
	
	for i in range(0,15):
		pm.rename('joint'+str(i+1), KinectSkelJoints[i]+'_jt')

	pm.ikHandle(n='L_arm', sj=KinectSkelJoints[3]+'_jt', ee=KinectSkelJoints[5]+'_jt',dh=False, eh=True)
	pm.ikHandle(n='R_arm', sj=KinectSkelJoints[6]+'_jt', ee=KinectSkelJoints[8]+'_jt',dh=False, eh=True)
	pm.ikHandle(n='L_leg', sj=KinectSkelJoints[9]+'_jt', ee=KinectSkelJoints[11]+'_jt',dh=False, eh=True)
	pm.ikHandle(n='R_leg', sj=KinectSkelJoints[12]+'_jt', ee=KinectSkelJoints[14]+'_jt',dh=False, eh=True)
	
	#Create IK End effector controls using point constraint
	pm.pointConstraint( KinectSkelJoints[5], 'L_arm' )
	pm.pointConstraint( KinectSkelJoints[8], 'R_arm' )
	pm.pointConstraint( KinectSkelJoints[11], 'L_leg' )
	pm.pointConstraint( KinectSkelJoints[14], 'R_leg' )
	
	'''
	#Create IK End effector controls using aim constraint
	pm.aimConstraint( KinectSkelJoints[5], 'L_arm' )
	pm.aimConstraint( KinectSkelJoints[8], 'R_arm' )
	pm.aimConstraint( KinectSkelJoints[11], 'L_leg' )
	pm.aimConstraint( KinectSkelJoints[14], 'R_leg' )
	'''
	
	#Add back the original pointConstraint ()
	pm.pointConstraint( KinectSkelJoints[0], KinectSkelJoints[0]+'_jt')
	pm.pointConstraint( KinectSkelJoints[1], KinectSkelJoints[1]+'_jt')
	pm.pointConstraint( KinectSkelJoints[2], KinectSkelJoints[2]+'_jt')
	pm.pointConstraint( KinectSkelJoints[3], KinectSkelJoints[3]+'_jt')
	pm.pointConstraint( KinectSkelJoints[6], KinectSkelJoints[6]+'_jt')
	pm.pointConstraint( KinectSkelJoints[9], KinectSkelJoints[9]+'_jt')
	pm.pointConstraint( KinectSkelJoints[12], KinectSkelJoints[12]+'_jt')

	print "reconnect!!!"	
	connectDevice()
	print "connect again!?"
	SwitchPerspective()
	

def remakeSkel():
	#disconnect first, and then reconnect after IK creation
	discDevice()

	#delete old joints#
	pm.delete( 'SKEL_HEAD_jt' )

	for i in range(0,15):
		point[i] = [0.0,0.0,0.0]

	makeSkel()
	
	for i in range(0,15):
	    pm.rename('joint'+str(i+1), KinectSkelJoints[i]+'_jt')

	for i in range(0,15):
	    pm.pointConstraint( KinectSkelJoints[i], KinectSkelJoints[i]+'_jt' )

	print "reconnect!!!"	
	connectDevice()
	print "connect again!?"
	SwitchPerspective()

	
def SwitchPerspective():
	print "SwitchPerpective"
	

	#Attach attribute and set mapping of camera's position("SKEL_HEAD") and orientation("SKEL_NECK")
	pm.attachDeviceAttr(("camera1" + ".translateX"),ax=("SKEL_HEAD" + "_POS:X"),d="KinectCapture")
	pm.setAttrMapping(ax=("SKEL_HEAD" + "_POS:X"),scale=-0.01,d="KinectCapture",at=("camera1" + ".translateX"))
	pm.attachDeviceAttr(("camera1" + ".translateY"),ax=("SKEL_HEAD" + "_POS:Y"),d="KinectCapture")
	pm.setAttrMapping(ax=("SKEL_HEAD" + "_POS:Y"),scale=+0.01,d="KinectCapture",at=("camera1" + ".translateY"))
	pm.attachDeviceAttr(("camera1" + ".translateZ"),ax=("SKEL_HEAD" + "_POS:Z"),d="KinectCapture")
	pm.setAttrMapping(ax=("SKEL_HEAD" + "_POS:Z"),scale=-0.01,d="KinectCapture",at=("camera1" + ".translateZ"))
	
	pm.attachDeviceAttr(("camera1"+".rotateX"),ax=("SKEL_HEAD" + "_ORI:X"),d="KinectCapture")
	pm.setAttrMapping(ax=("SKEL_HEAD" + "_ORI:X"),scale=-1.0,d="KinectCapture",at=("camera1"+".rotateX"))
	pm.attachDeviceAttr(("camera1"+".rotateY"),ax=("SKEL_HEAD" + "_ORI:Y"),d="KinectCapture")
	pm.setAttrMapping(ax=("SKEL_HEAD" + "_ORI:Y"),scale=1.0,d="KinectCapture",at=("camera1"+".rotateY"))
	pm.attachDeviceAttr(("camera1"+".rotateZ"),ax=("SKEL_HEAD" + "_ORI:Z"),d="KinectCapture")
	pm.setAttrMapping(ax=("SKEL_HEAD" + "_ORI:Z"),scale=-1.0,d="KinectCapture",at=("camera1"+".rotateZ"))
	'''
	pm.attachDeviceAttr(("camera1"+".rotateX"),ax=("SKEL_LEFT_ELBOW" + "_ORI:X"),d="KinectCapture")
	pm.setAttrMapping(ax=("SKEL_LEFT_ELBOW" + "_ORI:X"),scale=-1.0,d="KinectCapture",at=("camera1"+".rotateX"))
	pm.attachDeviceAttr(("camera1"+".rotateY"),ax=("SKEL_LEFT_ELBOW" + "_ORI:Y"),d="KinectCapture")
	pm.setAttrMapping(ax=("SKEL_LEFT_ELBOW" + "_ORI:Y"),scale=1.0,d="KinectCapture",at=("camera1"+".rotateY"))
	pm.attachDeviceAttr(("camera1"+".rotateZ"),ax=("SKEL_LEFT_ELBOW" + "_ORI:Z"),d="KinectCapture")
	pm.setAttrMapping(ax=("SKEL_LEFT_ELBOW" + "_ORI:Z"),scale=-1.0,d="KinectCapture",at=("camera1"+".rotateZ"))
	'''
	#Switch Perspective view from persp to camera1
	
		

###############################
#Integration of gesture part
###############################
def ActiveRecord(recordId):
	if recordId == "Start":
		print "Go into live record" 
		pm.enableDevice(device="KinectCapture",enable=True,monitor=1)
		pm.recordDevice(playback=True,dr=1000,d="KinectCapture")
		
	elif recordId == "Stop":
		print "Stop recording"
		pm.recordDevice(st=False,d="KinectCapture")
		pm.applyTake( device="KinectCapture" )
		

def mayaKinectGesture(gestureId):
	if gestureId == "Wave":
		print "Wave Gesture\n"
		#print "go into live record" 
		#ActiveRecord("Start")
		print "make IK for skeleton" 
		makeIK()
	
	elif gestureId == "Click":
		print "Click Gesture\n"
		#print "Stop recording"
		#ActiveRecord("Stop")
		print "recreate normal skeleton"
		remakeSkel()
		
###############################
	
def mayaKinectCaptureTest():
	global KinectTest_TextFieldGrp_ServerAddress
	global KinectTest_IntFieldGrp_Port
	global KinectTest_IntFieldGrp_CmdPort
	global Recording
	
	hwnd = pm.window('mayaKinectCaptureTestUI_MainWindow',sizeable=True,menuBar=True,title="Kinect capture test")
	masterLayout = pm.columnLayout()
	pm.setParent('..')
	
	#Buttons
	pm.setParent(masterLayout)
	
	pm.columnLayout(adjustableColumn=1)
	
	KinectTest_TextFieldGrp_ServerAddress = pm.textFieldGrp(cw2=(100, 100),tx="localhost",l="Server Address",w=200)
	
	KinectTest_IntFieldGrp_Port = pm.intFieldGrp(v1=9999,cw2=(100, 100),l="port",w=200,nf=1)
	
	pm.separator(w=200)
	
	pm.button(c=lambda *args: makeNull(),al="center",w=200,l="Create Skeleton")
	
	pm.separator(w=200)
	
	pm.rowLayout(nc=2,cw2=(100, 100))
	
	pm.button(c=lambda *args: connectDevice(),al="center",w=100,l="Connect")
	
	pm.button(c=lambda *args: discDevice(),al="center",w=100,l="Disconnect")
	
	pm.setParent('..')
	
	pm.separator(w=200)
	
	#pm.intFieldGrp('KinectTest_IntFieldGrp_CmdPort',v1=9998,cw2=(100, 100),l="Command Port",w=200,nf=1)
	
	KinectTest_IntFieldGrp_CmdPort = pm.intFieldGrp(v1=9998,cw2=(100, 100),l="Command Port",w=200,nf=1)
	#KinectTest_IntFieldGrp_CmdPort = pm.intFieldGrp(v1=9998,cw2=(100, 100),l="Command Port",w=200,nf=1)
	
	pm.button(c=lambda *args: OpenCommandPort(),al="center",w=200,l="Open CommandPort")
	
	pm.separator(w=200)

	pm.button(c=lambda *args: makeIK(),al="center",w=200,l="Create IK")
	pm.button(c=lambda *args: remakeSkel(),al="center",w=200,l="Recreate Skeleton")
	
	pm.separator(w=200)

	pm.button(c=lambda *args: SwitchPerspective(),al="center",w=200,l="Change Perspective")
	
	pm.separator(w=200)

	
	pm.rowLayout(nc=2,cw2=(100, 100))
	
	pm.button(c=lambda *args: ActiveRecord("Start"),al="center",w=100,l="Start Record")
	
	pm.button(c=lambda *args: ActiveRecord("Stop"),al="center",w=100,l="Stop Record")
	#pm.button(c=lambda *args: LiveRecord(),al="center",w=200,l="Record / Stop Record")

	pm.setParent('..')
	
	pm.window(hwnd,h=300,e=1,w=210)
	
	pm.showWindow(hwnd)
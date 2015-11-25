####IMPORTS
import time, sys, signal, atexit
import pyupm_uln200xa as upmULN200XA

# Instantiate a Stepper motor on a ULN200XA Darlington Motor Driver
# This was tested with the Grove Geared Step Motor with Driver
# Código retirado do site https://software.intel.com/en-us/iot/hardware/sensors/uln200xa-stepper-driver
# Código modificado do original

	 

	# Inicializando um ULN2003XA stepper objeto
	# ULN200XA(stepsPerRevolution, i1, i2, i3, i4)
	# i1 a i4 são os pinos ligados à placa (8 a 11)
	myUln200xa = upmULN200XA.ULN200XA(4096, 8, 9, 10, 11)	 

	#########################################################

	## Exit handlers ##
	# This stops python from printing a stacktrace
	# when you hit control-C
	def SIGINTHandler(signum, frame):
	raise SystemExit	

	# This lets you run code on exit,
	# including functions from myUln200xa
	def exitHandler():
	    print "Exiting"
	    sys.exit(0)
	 

	# Register exit handlers

	atexit.register(exitHandler)
	signal.signal(signal.SIGINT, SIGINTHandler)	 

	#######################################################	

	##Controle da velocidade do motor
	myUln200xa.setSpeed(5) # 5 RPMs

	##DIR_CW = sentido antihorário
	myUln200xa.setDirection(upmULN200XA.ULN200XA.DIR_CW)	 

	print "Rotating 1 revolution clockwise."

	##Setando os passos do motor
	myUln200xa.stepperSteps(4096)	 

	print "Sleeping for 2 seconds..."
	time.sleep(2)

	 

	print "Rotating 1/2 revolution counter clockwise."

	##DIR_CCW = Sentido horário
	myUln200xa.setDirection(upmULN200XA.ULN200XA.DIR_CCW)
	##Passos
	myUln200xa.stepperSteps(2048)	 

	# release
	myUln200xa.release()	 

	# exitHandler is called automatically

import csv

#read in the template for the GeD definition
f_geo = open("COSISMEX.Ge.DetectorBuild.geo.template","r")
ged_geo_template = f_geo.read()
f_geo.close()

f_det_anl = open("COSISMEX.Ge.DetectorBuild.det.template","r")
ged_det_anl_template = f_det_anl.read()
f_det_anl.close()

CrystalDiameter_A = []
HandleSpan_B = []
DetectorWidthX_C = []
DetectorWidthY_D = []
DetectorHeight_E = []
HandleThickness_F = []
HandleBridgeThickness_G = []

with open("FlightDetectorMapping.csv", "r") as Dimensionsstream:
	lines = Dimensionsstream.readlines()

for i,line in enumerate(lines[2:]): #skip header
	currentline = line.split(",")
	CrystalDiameter_A.append(currentline[3])
	HandleSpan_B.append(currentline[4])
	DetectorWidthX_C.append(currentline[5])
	DetectorWidthY_D.append(currentline[6])
	DetectorHeight_E.append(currentline[7])
	HandleThickness_F.append(currentline[8])
	HandleBridgeThickness_G.append(currentline[9])
	
GuardRingSize = 0.3

fnames = []

detlines = ['']
triggerlines = [ '' ]

#TODO generalize to 16 detectors to get Q#L# with modulo of 4
for i,detheight in enumerate(DetectorHeight_E):
	
	Q = int(i/4)
	L = i % 4

	lines = ['Constant CrystalDiameter_Q' + str(Q) + '_L' + str(L) + ' ' + str(CrystalDiameter_A[i]),\
			'Constant HandleSpan_Q' + str(Q) + '_L' + str(L) + ' ' + str(HandleSpan_B[i]),\
			'Constant DetectorWidthX_Q' + str(Q) + '_L' + str(L) + ' ' + str(DetectorWidthX_C[i]),\
			'Constant DetectorWidthY_Q' + str(Q) + '_L' + str(L) + ' ' + str(DetectorWidthY_D[i]),\
			'Constant DetectorHeight_Q' + str(Q) + '_L' + str(L) + ' ' + str(DetectorHeight_E[i]),\
			'Constant HandleThickness_Q' + str(Q) + '_L' + str(L) + ' ' + str(HandleThickness_F[i]),\
			'Constant HandleBridgeThickness_Q' + str(Q) + '_L' + str(L) + ' ' + str(HandleBridgeThickness_G[i]),\
			'Constant GuardRingSize_Q' + str(Q) + '_L' + str(L) + ' ' + str(GuardRingSize),\
			'']

	fname = 'COSISMEX.Ge.Q'+str(Q)+'L'+str(L)+'.geo'; fnames.append(fname)
	fout = open(fname,'w')
	fout.writelines(map(lambda x:x + '\n',lines))
	fout.write( ged_geo_template.replace('QQ_QQ', 'Q' + str(Q) + '_L' + str(L)) )
	fout.close()

	fname = 'COSISMEX.Ge.Q'+str(Q)+'L'+str(L)+'.det'; fnames.append(fname)
	fout = open(fname,'w')
	fout.write( ged_det_anl_template.replace('QQ_QQ', 'Q'+str(Q)+'_L'+ str(L)).replace('QQQQ', 'Q'+str(Q)+'L'+str(L)).replace('GeD_X', 'GeD_'+str(i)) )
	fout.close()


print(fnames)



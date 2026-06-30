# massmodel-cosi-payload
Mass model of COSI Flight Model used in Payload Calibrations

Each of the 16 GeDs has a unique .geo and .det file to describe the passive material and detector attributes. These are generated automatically through the GeD_Python_BuildScript.py script, which populates the templates (COSISMEX.Ge.DetectorBuild.geo.template, COSISMEX.Ge.DetectorBuild.det.template) with the detector dimensions given in the FlightDetectorMapping.csv file. 

The Flight Module detector dimensions are taken from the COSI FM Detector Tech Info Tracking spreadsheet (6/26), which defines the A-F measured parameters for each detector. 


<img width="418" height="483" alt="Screenshot 2026-06-29 at 9 56 37 PM" src="https://github.com/user-attachments/assets/20ad28f1-a296-4afd-87ba-c11075bcff39" />

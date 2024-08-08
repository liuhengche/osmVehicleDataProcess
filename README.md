~~# osmWebWizard data process~~
~~Codes that process .xml and .csv with osm.sumocfg that generated from [osmWebWiard](https://sumo.dlr.de/docs/Tutorials/OSMWebWizard.html)~~

~~## Explanation~~
~~- AutoFCD.py processes Floating Car Data, which contains location and speed along with other information for every vehicle in the network at every time step. The output behaves somewhat like a super-accurate high-frequency GPS device for each vehicle.~~
~~- AutoVehiPosi.py processes raw dump data, which contains detailed information for each edge, each vehicle and each simulation step.~~

~~## Usage~~
~~- `--sumoPath` is the path to osm.sumocfg obtained from osmWebWizard, `--savePath` is the desired save path~~
~~- run  `python /path/to/.py/ --sumoPath --savePath`~~
<br><br><br> Just add `<fcd-output value="FCD.xml"/>` in the `output` section of `osm.sumocfg`. I am too rubbish TwT

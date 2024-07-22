import subprocess
import os
import argparse

curDir = os.getcwd()

def genSavePath(sumoPath,savePath):
    folderName = os.path.basename(sumoPath)
    # os.chdir(savePath)
    # os.mkdir(folderName)
    savePath = os.path.join(savePath,folderName)
    if not os.path.exists(savePath):
        os.makedirs(savePath)
    return savePath

def sumocfg2xml(sumoPath,savePath):
    os.chdir(sumoPath)
    xmlDir = os.path.join(savePath, "FCD.xml")
    print("the xmlDir is " + xmlDir)
    FCDcommand = "sumo -c osm.sumocfg --fcd-output " + xmlDir
    subprocess.call(FCDcommand, shell=True)
    return xmlDir

def xml2csv(xmlDir):
    os.chdir(curDir)
    xml2csvCommand = "python xml2csv.py " + xmlDir
    subprocess.call(xml2csvCommand, shell=True)

def main(args):
    sumoPath = args.sumoPath
    savePath = args.savePath
    savePath = genSavePath(sumoPath, savePath)
    xmlDir = sumocfg2xml(sumoPath, savePath)
    xml2csv(xmlDir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--sumoPath', type=str, help="path to .sumocfg")
    parser.add_argument('--savePath', type=str, help="path to save .xml & .csv")
    args = parser.parse_args()
    main(args)
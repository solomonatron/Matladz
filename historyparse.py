# Script to retrieve the last command used on Matlab, based off the History.xml file.
# Requires the location of the History.xml file on your system - see python historyparse.py -h
#
# To find folder location of History.xml on your system use 'prefdir' command in Matlab.

import xml.etree.ElementTree
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser(prog='historyparse')
	parser.add_argument('filename',metavar='filename',help='Location of Matlab Command History XML File')
	args = parser.parse_args()

	history_file = args.filename

	e = xml.etree.ElementTree.parse(history_file).getroot()

	sessions = e.findall("./session");
	last_session = sessions[-1];

	commands = last_session.findall("./command");
	last_command = commands[-1];

	command_text = last_command.text;

	print ">> " + command_text


from district import District

from block import Block, OverSwitch, Route
from turnout import Turnout, SlipSwitch
from signal import Signal
from button import Button

from constants import HyYdPt, RESTRICTING, MAIN, DIVERGING, SLOW, NORMAL, REVERSE, EMPTY, SLIPSWITCH

CJBlocks = ["OSYCJE", "OSYCJW"]
EEBlocks = ["OSYEEE", "OSYEEW"]
KLBlocks = ["OSYKLE", "OSYKLW"]

class Yard (District):
	def __init__(self, name, frame, screen):
		District.__init__(self, name, frame, screen)
		self.sw17 = None
		self.sw21 = None

	def Draw(self):
		District.Draw(self)
		self.drawCrossing()

	def DrawRoute(self, block):
		if block.GetName() in KLBlocks:
			self.drawCrossing()

	def drawCrossing(self):
		s17 = NORMAL if self.sw17.IsNormal() else REVERSE
		s21 = NORMAL if self.sw21.IsNormal() else REVERSE

		if s17 == REVERSE:
			blkstat = self.sw17.GetBlockStatus()
		elif s21 == REVERSE:
			blkstat = self.sw21.GetBlockStatus()
		else:
			blkstat = EMPTY

		bmp = "diagright" if s17 == REVERSE else "diagleft" if s21 == REVERSE else "cross"
		bmp = self.generictiles["crossing"].getBmp(blkstat, bmp)
		self.frame.DrawTile(self.screen, (104, 12), bmp)

	def DoTurnoutAction(self, turnout, state):
		tn = turnout.GetName()
		if turnout.GetType() == SLIPSWITCH:
			if tn == "YSw19":
				bstat = NORMAL if self.turnouts["YSw17"].IsNormal() else REVERSE
				turnout.SetStatus([state, bstat])
				turnout.Draw()

		else:
			District.DoTurnoutAction(self, turnout, state)

		if tn in [ "YSw17", "YSw19", "YSw21" ]:
			self.drawCrossing()
			if tn == "YSw17":
				trnout = self.turnouts["YSw19"]
				trnout.UpdateStatus()
				trnout.Draw()

	def DetermineRoute(self, blocks):
		for bname in blocks:
			block = self.frame.GetBlockByName(bname)
			if bname == "OSYCJW":
				s1 = 'N' if self.turnouts["YSw1"].IsNormal() else 'R'
				s3 = 'N' if self.turnouts["YSw3"].IsNormal() else 'R'

				if s3 == "N":
					block.SetRoute(self.routes["YRtY11L10"])
				else:
					if s1 == 'N':
						block.SetRoute(self.routes["YRtY11L20"])
					else:
						block.SetRoute(self.routes["YRtY11P50"])

			elif bname == "OSYCJE":
				s1 = 'N' if self.turnouts["YSw1"].IsNormal() else 'R'
				s3 = 'N' if self.turnouts["YSw3"].IsNormal() else 'R'
				if s3 == "R":
					block.SetRoute(None)
				elif s1 == "N":
					block.SetRoute(self.routes["YRtY21L20"])
				else:
					block.SetRoute(self.routes["YRtY21P50"])

			elif bname == "OSYEEW":
				s7 = 'N' if self.turnouts["YSw7"].IsNormal() else 'R'
				s9 = 'N' if self.turnouts["YSw9"].IsNormal() else 'R'
				s11 = 'N' if self.turnouts["YSw11"].IsNormal() else 'R'
				if s7 == "N" and s9 == "N":
					block.SetRoute(self.routes["YRtY10Y11"])
				elif s7 == 'N' and s9 == 'R' and s11 == 'R':
					block.SetRoute(self.routes["YRtY30Y11"])
				elif s7 == 'N' and s9 == 'R' and s11 == 'N':
					block.SetRoute(self.routes["YRtY87Y11"])
				else:
					block.SetRoute(None)

			elif bname == "OSYEEE":
				s7 = 'N' if self.turnouts["YSw7"].IsNormal() else 'R'
				s9 = 'N' if self.turnouts["YSw9"].IsNormal() else 'R'
				s11 = 'N' if self.turnouts["YSw11"].IsNormal() else 'R'
				if s7 == 'N':
					block.SetRoute(self.routes["YRtY20Y21"])
				elif s7 == 'R' and s9 == 'R' and s11 == 'R':
					block.SetRoute(self.routes["YRtY30Y21"])
				elif s7 == 'R' and s9 == 'R' and s11 == 'N':
					block.SetRoute(self.routes["YRtY87Y21"])
				elif s7 == 'R' and s9 == 'N':
					block.SetRoute(self.routes["YRtY10Y21"])
				else:
					block.SetRoute(None)

			elif bname == "OSYKLE":
				s17 = 'N' if self.turnouts["YSw17"].IsNormal() else 'R'
				s19 = 'N' if self.turnouts["YSw19"].IsNormal() else 'R'
				s21 = 'N' if self.turnouts["YSw21"].IsNormal() else 'R'
				s23 = 'N' if self.turnouts["YSw23"].IsNormal() else 'R'
				s25 = 'N' if self.turnouts["YSw25"].IsNormal() else 'R'
				s27 = 'N' if self.turnouts["YSw27"].IsNormal() else 'R'
				s29 = 'N' if self.turnouts["YSw29"].IsNormal() else 'R'
				if s17+s21+s23+s25+s27 == "NNNNN":
					block.SetRoute(self.routes["YRtY20Y51"])
				elif s17+s21+s23+s25 == "NNNR":
					block.SetRoute(self.routes["YRtY20Y50"]) 
				elif s17+s21+s23+s25+s27 == "NNNNR":
					block.SetRoute(self.routes["YRtY20Y70"])
				elif s17+s19+s21+s23+s29 == "NRNRN":
					block.SetRoute(self.routes["YRtY20Y52"])
				elif s17+s19+s21+s23+s29 == "NRNRR":
					block.SetRoute(self.routes["YRtY20Y53"])
				elif s17+s19+s21 == "RRN":
					block.SetRoute(self.routes["YRtY20Y60"])
				else:
					block.SetRoute(None)

			elif bname == "OSYKLW":
				s17 = 'N' if self.turnouts["YSw17"].IsNormal() else 'R'
				s19 = 'N' if self.turnouts["YSw19"].IsNormal() else 'R'
				s21 = 'N' if self.turnouts["YSw21"].IsNormal() else 'R'
				s23 = 'N' if self.turnouts["YSw23"].IsNormal() else 'R'
				s25 = 'N' if self.turnouts["YSw25"].IsNormal() else 'R'
				s27 = 'N' if self.turnouts["YSw27"].IsNormal() else 'R'
				s29 = 'N' if self.turnouts["YSw29"].IsNormal() else 'R'
				if s17+s19+s21+s29 == "NNNN":
					block.SetRoute(self.routes["YRtY10Y52"])
				elif s17+s21+s23+s25 == "NRNR":
					block.SetRoute(self.routes["YRtY10Y50"])
				elif s17+s21+s23+s25+s27 == "NRNNN":
					block.SetRoute(self.routes["YRtY10Y51"])
				elif s17+s21+s23+s25+s27 == "NRNNR":
					block.SetRoute(self.routes["YRtY10Y70"])
				elif s17+s19+s21+s29 == "NNNR":
					block.SetRoute(self.routes["YRtY10Y53"])
				elif s17+s19+s21 == "NRN":
					block.SetRoute(self.routes["YRtY10Y60"])
				else:
					block.SetRoute(None)

			elif bname == "OSYWKL":
				s33 = 'N' if self.turnouts["YSw33"].IsNormal() else 'R'
				if s33 == "N":
					block.SetRoute(self.routes["YRtY30Y51"])
				else:
					block.SetRoute(self.routes["YRtY30Y50"])

	def CrossingEastWestBoundary(self, blk1, blk2):
		if blk1.GetName() == "OSYWKL" and blk2.GetName() == "Y30":
			return True
		if blk1.GetName() == "OSYKLE" and blk2.GetName() == "Y70":
			return True
		if blk1.GetName() == "OSYKLW" and blk2.GetName() == "Y70":
			return True

		return False

	def PerformButtonAction(self, btn):
		bname = btn.GetName()

	def DefineBlocks(self, tiles):
		self.blocks = {}
		self.osBlocks = {}

		self.blocks["Y10"] = Block(self, self.frame, "Y10",
			[
				(tiles["eobleft"],  self.screen, (107, 11), False),
				(tiles["horiznc"],  self.screen, (108, 11), False),
				(tiles["horiz"],    self.screen, (109, 11), False),
				(tiles["horiznc"],  self.screen, (110, 11), False),
				(tiles["horiz"],    self.screen, (111, 11), False),
				(tiles["horiznc"],  self.screen, (112, 11), False),
				(tiles["eobright"], self.screen, (113, 11), False),
			], False)

		self.blocks["Y11"] = Block(self, self.frame, "Y11",
			[
				(tiles["eobleft"],  self.screen, (122, 11), False),
				(tiles["horiznc"],  self.screen, (123, 11), False),
				(tiles["horiz"],    self.screen, (124, 11), False),
				(tiles["horiznc"],  self.screen, (125, 11), False),
				(tiles["horiz"],    self.screen, (126, 11), False),
				(tiles["horiznc"],  self.screen, (127, 11), False),
				(tiles["eobright"], self.screen, (128, 11), False),
			], False)

		self.blocks["Y20"] = Block(self, self.frame, "Y10",
			[
				(tiles["eobleft"],  self.screen, (107, 13), False),
				(tiles["horiznc"],  self.screen, (108, 13), False),
				(tiles["horiz"],    self.screen, (109, 13), False),
				(tiles["horiznc"],  self.screen, (110, 13), False),
				(tiles["horiz"],    self.screen, (111, 13), False),
				(tiles["horiznc"],  self.screen, (112, 13), False),
				(tiles["eobright"], self.screen, (113, 13), False),
			], True)

		self.blocks["Y21"] = Block(self, self.frame, "Y21",
			[
				(tiles["eobleft"],  self.screen, (122, 13), False),
				(tiles["horiznc"],  self.screen, (123, 13), False),
				(tiles["horiz"],    self.screen, (124, 13), False),
				(tiles["horiznc"],  self.screen, (125, 13), False),
				(tiles["horiz"],    self.screen, (126, 13), False),
				(tiles["horiznc"],  self.screen, (127, 13), False),
				(tiles["eobright"], self.screen, (128, 13), False),
			], True)

		self.blocks["Y30"] = Block(self, self.frame, "Y30",
			[
				(tiles["eobright"],       self.screen, (111, 7), False),
				(tiles["turnrightleft"],  self.screen, (110, 7), False),
				(tiles["diagright"],      self.screen, (109, 6), False),
				(tiles["diagright"],      self.screen, (108, 5), False),
				(tiles["diagright"],      self.screen, (107, 4), False),
				(tiles["turnrightright"], self.screen, (106, 3), False),
				(tiles["horiz"],          self.screen, (83, 3), False),
				(tiles["horiznc"],        self.screen, (84, 3), False),
				(tiles["horiz"],          self.screen, (85, 3), False),
				(tiles["horiznc"],        self.screen, (86, 3), False),
				(tiles["horiz"],          self.screen, (87, 3), False),
				(tiles["horiznc"],        self.screen, (88, 3), False),
				(tiles["horiz"],          self.screen, (89, 3), False),
				(tiles["horiznc"],        self.screen, (90, 3), False),
				(tiles["horiz"],          self.screen, (91, 3), False),
				(tiles["horiznc"],        self.screen, (92, 3), False),
				(tiles["horiz"],          self.screen, (93, 3), False),
				(tiles["horiznc"],        self.screen, (94, 3), False),
				(tiles["horiz"],          self.screen, (95, 3), False),
				(tiles["horiznc"],        self.screen, (96, 3), False),
				(tiles["horiz"],          self.screen, (97, 3), False),
				(tiles["horiznc"],        self.screen, (98, 3), False),
				(tiles["horiz"],          self.screen, (99, 3), False),
				(tiles["horiznc"],        self.screen, (100, 3), False),
				(tiles["horiz"],          self.screen, (101, 3), False),
				(tiles["horiznc"],        self.screen, (102, 3), False),
				(tiles["horiz"],          self.screen, (103, 3), False),
				(tiles["horiznc"],        self.screen, (104, 3), False),
				(tiles["horiz"],          self.screen, (105, 3), False),
				(tiles["turnleftleft"],   self.screen, (82, 3), False),
				(tiles["turnrightup"],    self.screen, (81, 4), False),
				(tiles["vertical"],       self.screen, (81, 5), False),
				(tiles["verticalnc"],     self.screen, (81, 6), False),
				(tiles["vertical"],       self.screen, (81, 7), False),
				(tiles["verticalnc"],     self.screen, (81, 8), False),
				(tiles["vertical"],       self.screen, (81, 9), False),
				(tiles["verticalnc"],     self.screen, (81, 10), False),
				(tiles["vertical"],       self.screen, (81, 11), False),
				(tiles["turnleftdown"],   self.screen, (81, 12), False),
				(tiles["turnrightleft"],  self.screen, (82, 13), False),
				(tiles["eobright"],       self.screen, (83, 13), False),
			], False)

		self.blocks["Y50"] = Block(self, self.frame, "Y50",
			[
				(tiles["eobleft"],        self.screen, (89, 15), False),
				(tiles["horiz"],          self.screen, (90, 15), False),
				(tiles["horiznc"],        self.screen, (91, 15), False),
				(tiles["horiz"],          self.screen, (92, 15), False),
				(tiles["horiznc"],        self.screen, (93, 15), False),
				(tiles["horiz"],          self.screen, (94, 15), False),
				(tiles["eobright"],       self.screen, (95, 15), False),
			], True)

		self.blocks["Y51"] = Block(self, self.frame, "Y51",
			[
				(tiles["eobleft"],        self.screen, (89, 13), False),
				(tiles["horiz"],          self.screen, (90, 13), False),
				(tiles["horiznc"],        self.screen, (91, 13), False),
				(tiles["horiz"],          self.screen, (92, 13), False),
				(tiles["horiznc"],        self.screen, (93, 13), False),
				(tiles["horiz"],          self.screen, (94, 13), False),
				(tiles["eobright"],       self.screen, (95, 13), False),
			], True)

		self.blocks["Y52"] = Block(self, self.frame, "Y52",
			[
				(tiles["eobleft"],        self.screen, (85, 9), False),
				(tiles["horiz"],          self.screen, (86, 9), False),
				(tiles["horiznc"],        self.screen, (87, 9), False),
				(tiles["horiz"],          self.screen, (88, 9), False),
				(tiles["horiznc"],        self.screen, (89, 9), False),
				(tiles["horiz"],          self.screen, (90, 9), False),
				(tiles["horiznc"],        self.screen, (91, 9), False),
				(tiles["horiz"],          self.screen, (92, 9), False),
				(tiles["horiznc"],        self.screen, (93, 9), False),
				(tiles["eobright"],       self.screen, (94, 9), False),
			], True)

		self.blocks["Y53"] = Block(self, self.frame, "Y53",
			[
				(tiles["eobleft"],        self.screen, (85, 7), False),
				(tiles["horiz"],          self.screen, (86, 7), False),
				(tiles["horiznc"],        self.screen, (87, 7), False),
				(tiles["horiz"],          self.screen, (88, 7), False),
				(tiles["horiznc"],        self.screen, (89, 7), False),
				(tiles["horiz"],          self.screen, (90, 7), False),
				(tiles["horiznc"],        self.screen, (91, 7), False),
				(tiles["horiz"],          self.screen, (92, 7), False),
				(tiles["horiznc"],        self.screen, (93, 7), False),
				(tiles["eobright"],       self.screen, (94, 7), False),
			], True)

		self.blocks["Y60"] = Block(self, self.frame, "Y70",
			[
				(tiles["houtline"],       self.screen, (93, 5), False),
				(tiles["houtline"],       self.screen, (94, 5), False),
			], True)

		self.blocks["Y70"] = Block(self, self.frame, "Y70",
			[
				(tiles["houtline"],       self.screen, (93, 11), False),
				(tiles["houtline"],       self.screen, (94, 11), False),
				(tiles["houtline"],       self.screen, (95, 11), False),
				(tiles["horiznc"],        self.screen, (13, 30), False),
				(tiles["horiz"],          self.screen, (14, 30), False),
				(tiles["horiznc"],        self.screen, (15, 30), False),
				(tiles["horiz"],          self.screen, (16, 30), False),
				(tiles["horiznc"],        self.screen, (17, 30), False),
				(tiles["horiz"],          self.screen, (18, 30), False),
				(tiles["horiznc"],        self.screen, (19, 30), False),
				(tiles["eobright"],       self.screen, (20, 30), False),
			], False)

		self.blocks["Y87"] = Block(self, self.frame, "Y87",
			[
				(tiles["eobleft"],        self.screen, (56, 30), False),
				(tiles["horiz"],          self.screen, (57, 30), False),
				(tiles["horiznc"],        self.screen, (58, 30), False),
				(tiles["horiz"],          self.screen, (59, 30), False),
				(tiles["horiznc"],        self.screen, (60, 30), False),
				(tiles["horiz"],          self.screen, (61, 30), False),
				(tiles["horiznc"],        self.screen, (62, 30), False),
				(tiles["horiz"],          self.screen, (63, 30), False),
				(tiles["horiznc"],        self.screen, (64, 30), False),
				(tiles["houtline"],       self.screen, (110, 9), False),
				(tiles["houtline"],       self.screen, (111, 9), False),
				(tiles["houtline"],       self.screen, (112, 9), False),
			], False)

		self.blocks["OSYEEW"] = OverSwitch(self, self.frame, "OSYEEW", 
			[
				(tiles["eobleft"],        self.screen, (112, 7), False),
				(tiles["turnrightright"], self.screen, (113, 7), False),
				(tiles["diagright"],      self.screen, (114, 8), False),
				(tiles["diagright"],      self.screen, (116, 10), False),
				(tiles["eobleft"],        self.screen, (113, 9), False),
				(tiles["horiz"],          self.screen, (114, 9), False),
				(tiles["eobleft"],        self.screen, (114, 11), False),
				(tiles["horiz"],          self.screen, (115, 11), False),
				(tiles["horiznc"],        self.screen, (116, 11), False),
				(tiles["horiz"],          self.screen, (119, 11), False),
				(tiles["horiznc"],        self.screen, (120, 11), False),
				(tiles["eobright"],       self.screen, (121, 11), False),
			],
			False)

		self.blocks["OSYEEE"] = OverSwitch(self, self.frame, "OSYEEE", 
			[
				(tiles["eobleft"],        self.screen, (112, 7), False),
				(tiles["turnrightright"], self.screen, (113, 7), False),
				(tiles["diagright"],      self.screen, (114, 8), False),
				(tiles["diagright"],      self.screen, (116, 10), False),
				(tiles["eobleft"],        self.screen, (113, 9), False),
				(tiles["horiz"],          self.screen, (114, 9), False),
				(tiles["eobleft"],        self.screen, (114, 11), False),
				(tiles["horiz"],          self.screen, (115, 11), False),
				(tiles["horiznc"],        self.screen, (116, 11), False),
				(tiles["diagright"],      self.screen, (119, 12), False),
				(tiles["eobleft"],        self.screen, (114, 13), False),
				(tiles["horiz"],          self.screen, (115, 13), False),
				(tiles["horiznc"],        self.screen, (116, 13), False),
				(tiles["horiz"],          self.screen, (117, 13), False),
				(tiles["horiznc"],        self.screen, (118, 13), False),
				(tiles["horiz"],          self.screen, (119, 13), False),
				(tiles["eobright"],       self.screen, (121, 13), False),				
			],
			True)

		self.blocks["OSYCJE"] = OverSwitch(self, self.frame, "OSYCJE", 
			[
				(tiles["eobleft"],  self.screen, (129, 13), False),
				(tiles["horiznc"],  self.screen, (130, 13), False),
				(tiles["horiznc"],  self.screen, (131, 13), False),
				(tiles["horiz"],    self.screen, (134, 13), False),
				(tiles["horiznc"],  self.screen, (135, 13), False),
				(tiles["eobright"], self.screen, (136, 13), False),
				(tiles["diagright"], self.screen, (134, 14), False),
				(tiles["turnrightleft"], self.screen, (135, 15), True),
				(tiles["eobright"], self.screen, (136, 15), False),
			], 
			True)

		self.blocks["OSYCJW"] = OverSwitch(self, self.frame, "OSYCJW", 
			[
				(tiles["eobleft"],  self.screen, (129, 11), False),
				(tiles["horiznc"],  self.screen, (131, 11), False),
				(tiles["horiz"],    self.screen, (132, 11), False),
				(tiles["horiznc"],  self.screen, (133, 11), False),
				(tiles["horiz"],    self.screen, (134, 11), False),
				(tiles["horiznc"],  self.screen, (135, 11), False),
				(tiles["eobright"], self.screen, (136, 11), False),
				(tiles["diagright"],self.screen, (131, 12), False),
				(tiles["horiz"],    self.screen, (134, 13), False),
				(tiles["horiznc"],  self.screen, (135, 13), False),
				(tiles["eobright"], self.screen, (136, 13), False),
				(tiles["diagright"], self.screen, (134, 14), False),
				(tiles["turnrightleft"], self.screen, (135, 15), True),
				(tiles["eobright"], self.screen, (136, 15), False),
			], 
			False)

		self.blocks["OSYKLW"] = OverSwitch(self, self.frame, "OSYKLW", 
			[
				(tiles["eobleft"],       self.screen, (95, 5), False),
				(tiles["horiz"],         self.screen, (96, 5), False),
				(tiles["turnrightright"],self.screen, (97, 5), False),
				(tiles["diagright"],     self.screen, (98, 6), False),
				(tiles["diagright"],     self.screen, (99, 7), False),
				(tiles["diagright"],     self.screen, (100, 8), False),
				(tiles["diagright"],     self.screen, (101, 9), False),
				(tiles["diagright"],     self.screen, (102, 10), False),
				(tiles["horiznc"],       self.screen, (104, 11), False),
				(tiles["eobright"],      self.screen, (106, 11), False),
				(tiles["eobleft"],       self.screen, (95, 7), False),
				(tiles["turnrightright"],self.screen, (96, 7), False),
				(tiles["diagright"],     self.screen, (97, 8), False),
				(tiles["diagright"],     self.screen, (99, 10), False),
				(tiles["horiz"],         self.screen, (101, 11), False),
				(tiles["horiznc"],       self.screen, (102, 11), False),
				(tiles["eobleft"],       self.screen, (95, 9), False),
				(tiles["horiz"],         self.screen, (96, 9), False),
				(tiles["horiznc"],       self.screen, (97, 9), False),
				(tiles["eobleft"],       self.screen, (96, 11), False),
				(tiles["turnrightright"],self.screen, (97, 11), False),
				(tiles["diagright"],     self.screen, (98, 12), False),
				(tiles["horiznc"],       self.screen, (101, 13), False),
				(tiles["eobleft"],       self.screen, (96, 13), False),
				(tiles["horiz"],         self.screen, (97, 13), False),
				(tiles["horiznc"],       self.screen, (98, 13), False),
				(tiles["eobleft"],       self.screen, (96, 15), False),
				(tiles["horiz"],         self.screen, (97, 15), False),
				(tiles["turnleftright"], self.screen, (98, 15), False),
				(tiles["diagleft"],      self.screen, (99, 14), False),
			],
			False)

		self.blocks["OSYKLE"] = OverSwitch(self, self.frame, "OSYKLE", 
			[
				(tiles["eobleft"],       self.screen, (95, 5), False),
				(tiles["horiz"],         self.screen, (96, 5), False),
				(tiles["turnrightright"],self.screen, (97, 5), False),
				(tiles["diagright"],     self.screen, (98, 6), False),
				(tiles["diagright"],     self.screen, (99, 7), False),
				(tiles["diagright"],     self.screen, (100, 8), False),
				(tiles["diagright"],     self.screen, (101, 9), False),
				(tiles["diagright"],     self.screen, (102, 10), False),
				(tiles["horiznc"],       self.screen, (104, 13), False),
				(tiles["eobright"],      self.screen, (106, 13), False),
				(tiles["eobleft"],       self.screen, (95, 7), False),
				(tiles["turnrightright"],self.screen, (96, 7), False),
				(tiles["diagright"],     self.screen, (97, 8), False),
				(tiles["diagright"],     self.screen, (99, 10), False),
				(tiles["diagright"],     self.screen, (101, 12), False),
				(tiles["horiznc"],       self.screen, (102, 11), False),
				(tiles["eobleft"],       self.screen, (95, 9), False),
				(tiles["horiz"],         self.screen, (96, 9), False),
				(tiles["horiznc"],       self.screen, (97, 9), False),
				(tiles["eobleft"],       self.screen, (96, 11), False),
				(tiles["turnrightright"],self.screen, (97, 11), False),
				(tiles["diagright"],     self.screen, (98, 12), False),
				(tiles["horiznc"],       self.screen, (101, 13), False),
				(tiles["eobleft"],       self.screen, (96, 13), False),
				(tiles["horiz"],         self.screen, (97, 13), False),
				(tiles["horiznc"],       self.screen, (98, 13), False),
				(tiles["eobleft"],       self.screen, (96, 15), False),
				(tiles["horiz"],         self.screen, (97, 15), False),
				(tiles["turnleftright"], self.screen, (98, 15), False),
				(tiles["diagleft"],      self.screen, (99, 14), False),
			],
			True)

		self.blocks["OSYWKL"] = OverSwitch(self, self.frame, "OSYWKL", 
			[
				(tiles["eobleft"],       self.screen, (84, 13), False),
				(tiles["horiznc"],       self.screen, (86, 13), False),
				(tiles["horiz"],         self.screen, (87, 13), False),
				(tiles["eobright"],      self.screen, (88, 13), False),
				(tiles["diagright"],      self.screen, (86, 14), False),
				(tiles["turnrightleft"], self.screen, (87, 15), False),
				(tiles["eobright"],      self.screen, (88, 15), False),
			],
			True)

		self.osBlocks["OSYCJW"] = [ "Y11", "L10", "L20", "P50" ]
		self.osBlocks["OSYCJE"] = [ "Y21", "L20", "P50" ]
		self.osBlocks["OSYEEW"] = [ "Y11", "Y10", "Y87", "Y30" ]
		self.osBlocks["OSYEEE"] = [ "Y21", "Y20", "Y10", "Y87", "Y30" ]
		self.osBlocks["OSYKLW"] = [ "Y10", "Y70", "Y60", "Y53", "Y52", "Y51", "Y50" ]
		self.osBlocks["OSYKLE"] = [ "Y20", "Y70", "Y60", "Y53", "Y52", "Y51", "Y50" ]
		self.osBlocks["OSYWKL"] = [ "Y30", "Y50", "Y51" ]

		return self.blocks

	def DefineTurnouts(self, tiles, blocks):
		self.turnouts = {}

		toList = [
			[ "YSw1",  "torightright",   CJBlocks, (133, 13) ],
			[ "YSw3",  "torightright",   CJBlocks, (130, 11) ],
			[ "YSw3b",  "torightleft",   CJBlocks, (132, 13) ],

			[ "YSw7",  "torightleft",    EEBlocks, (120, 13) ],
			[ "YSw7b", "torightright",   EEBlocks, (118, 11) ],
			[ "YSw9",  "torightleft",    EEBlocks, (117, 11) ],
			[ "YSw11", "toleftupinv",    EEBlocks, (115, 9) ],

			[ "YSw17", "torightleft",    KLBlocks, (105, 13) ],
			[ "YSw21", "toleftleft",     KLBlocks, (105, 11) ],
			[ "YSw21b","toleftright",    KLBlocks, (103, 13) ],
			[ "YSw23", "torightleft",    KLBlocks, (102, 13) ],
			[ "YSw23b","toleftdowninv",  KLBlocks, (100, 11) ],
			[ "YSw25", "toleftleft",     KLBlocks, (100, 13) ],
			[ "YSw27", "torightleft",    KLBlocks, (99, 13) ],
			[ "YSw29", "toleftupinv",    KLBlocks, (98, 9) ],

			[ "YSw33", "torightright",   ["OSYWKL"], (85, 13) ]
		]

		for tonm, tileSet, blks, pos in toList:
			trnout = Turnout(self, self.frame, tonm, self.screen, tiles[tileSet], pos)
			for blknm in blks:
				blocks[blknm].AddTurnout(trnout)
			self.turnouts[tonm] = trnout

		trnout = SlipSwitch(self, self.frame, "YSw19", self.screen, tiles["ssleft"], (103, 11))
		blocks["OSYKLW"].AddTurnout(trnout)
		blocks["OSYKLE"].AddTurnout(trnout)
		trnout.SetControllers(None, self.turnouts["YSw17"])
		self.turnouts["YSw19"] = trnout
		
		self.turnouts["YSw3"].SetPairedTurnout(self.turnouts["YSw3b"])
		self.turnouts["YSw7"].SetPairedTurnout(self.turnouts["YSw7b"])
		self.turnouts["YSw21"].SetPairedTurnout(self.turnouts["YSw21b"])
		self.turnouts["YSw23"].SetPairedTurnout(self.turnouts["YSw23b"])

		# preserve these values so we can efficiently draw the slip switch and crossover when necessary
		self.sw17 = self.turnouts["YSw17"]
		self.sw21 = self.turnouts["YSw21"]

		self.osTurnouts = {}
		self.osTurnouts["OSYCJW"] = [ "YSw1", "YSw3", "YSw3b" ]
		self.osTurnouts["OSYCJE"] = [ "YSw1", "YSw3", "YSw3b" ]
		self.osTurnouts["OSYEEW"] = [ "YSw7", "YSw7b", "YSw9", "YSw11" ]
		self.osTurnouts["OSYEEE"] = [ "YSw7", "YSw7b", "YSw9", "YSw11" ]
		self.osTurnouts["OSYKLW"] = [ "YSw17", "YSw19", "YSw21", "YSw21b", "YSw23", "YSw23b", "YSw25", "YSw27", "YSw29" ]
		self.osTurnouts["OSYKLE"] = [ "YSw17", "YSw19", "YSw21", "YSw21b", "YSw23", "YSw23b", "YSw25", "YSw27", "YSw29" ]
		self.osTurnouts["OSYWKL"] = [ "YSw33" ]
		
		return self.turnouts

	def DefineSignals(self, tiles):
		self.signals = {}

		sigList = [
			[ "Y2L",  True,    "right", (129, 12) ],
			[ "Y2R",  False,   "left",  (136, 10) ],
			[ "Y4L",  True,    "right", (129, 14) ],
			[ "Y4RA", False,   "left",  (136, 14) ],
			[ "Y4RB", False,   "left",  (136, 12) ],

			[ "Y8LA", True,    "right", (114, 12) ],
			[ "Y8LB", True,    "right", (113, 10) ],
			[ "Y8LC", True,    "right", (112, 8)  ],
			[ "Y8R",  False,   "left",  (121, 10) ],
			[ "Y10L", True,    "right", (114, 14) ],
			[ "Y10R", False,   "left",  (121, 12) ],

			[ "Y22L",  True,   "right", (95, 6) ],
			[ "Y22R",  False,  "left",  (106, 10) ],
			[ "Y24LA", True,   "right", (95, 10) ],
			[ "Y24LB", True,   "right", (95, 8) ],
			[ "Y26LA", True,   "right", (96, 16) ],
			[ "Y26LB", True,   "right", (96, 14) ],
			[ "Y26LC", True,   "right", (96, 12) ],
			[ "Y26R",  False,  "left",  (106, 12)],

			[ "Y34L",  True,   "right", (84, 14) ],
			[ "Y34RA", False,  "left",  (88, 14) ],
			[ "Y34RB", False,  "left",  (88, 12) ],
		]
		for signm, east, tileSet, pos in sigList:
			self.signals[signm]  = Signal(self, self.screen, self.frame, signm, east, pos, tiles[tileSet])  

		self.routes = {}
		self.osSignals = {}

		# cornell junction
		block = self.blocks["OSYCJW"]
		self.routes["YRtY11L10"] = Route(self.screen, block, "YRtY11L10", "L10", [ (129, 11), (130, 11), (131, 11), (132, 11), (133, 11), (134, 11), (135, 11), (136, 11) ], "Y11", [RESTRICTING, MAIN])
		self.routes["YRtY11L20"] = Route(self.screen, block, "YRtY11L20", "L20", [ (129, 11), (130, 11), (131, 12), (132, 13), (133, 13), (134, 13), (135, 13), (136, 13) ], "Y11", [RESTRICTING, RESTRICTING])
		self.routes["YRtY11P50"] = Route(self.screen, block, "YRtY11P50", "P50", [ (129, 11), (130, 11), (131, 12), (132, 13), (133, 13), (134, 14), (135, 15), (136, 15) ], "Y11", [RESTRICTING, DIVERGING])

		block = self.blocks["OSYCJE"]
		self.routes["YRtY21L20"] = Route(self.screen, block, "YRtY21L20", "Y21", [ (129, 13), (130, 13), (131, 13), (132, 13), (133, 13), (134, 13), (135, 13), (136, 13) ], "L20", [MAIN, RESTRICTING])
		self.routes["YRtY21P50"] = Route(self.screen, block, "YRtY21P50", "Y21", [ (129, 13), (130, 13), (131, 13), (132, 13), (133, 13), (134, 14), (135, 15), (136, 15) ], "P50", [DIVERGING, RESTRICTING])

		self.signals["Y2L"].AddPossibleRoutes("OSYCJW", [ "YRtY11L10", "YRtY11L20", "YRtY11P50" ])
		self.signals["Y2R"].AddPossibleRoutes("OSYCJW", [ "YRtY11L10" ])

		self.signals["Y4L"].AddPossibleRoutes("OSYCJE", [ "YRtY21L20", "YRtY21P50" ])
		self.signals["Y4RB"].AddPossibleRoutes("OSYCJE", [ "YRtY21L20" ])
		self.signals["Y4RB"].AddPossibleRoutes("OSYCJW", [ "YRtY11L20" ])
		self.signals["Y4RA"].AddPossibleRoutes("OSYCJE", [ "YRtY21P50" ])
		self.signals["Y4RA"].AddPossibleRoutes("OSYCJW", [ "YRtY11P50" ])

		self.osSignals["OSYCJW"] = [ "Y2L", "Y2R", "Y4RA", "Y4RB" ]
		self.osSignals["OSYCJE"] = [ "Y2L", "Y4L", "Y4RA", "Y4RB" ]

		# east end junction
		block = self.blocks["OSYEEW"] 
		self.routes["YRtY10Y11"] = Route(self.screen, block, "YRtY10Y11", "Y11", [ (114, 11), (115, 11), (116, 11), (117, 11), (118, 11), (119, 11), (120, 11), (121, 11) ], "Y10", [RESTRICTING, MAIN])
		self.routes["YRtY30Y11"] = Route(self.screen, block, "YRtY30Y11", "Y11", [ (112, 7), (113, 7), (114, 8), (115, 9), (116, 10), (117, 11), (118, 11), (119, 11), (120, 11), (121, 11) ], "Y30", [RESTRICTING, DIVERGING])
		self.routes["YRtY87Y11"] = Route(self.screen, block, "YRtY87Y11", "Y11", [ (113, 9), (114, 9), (115, 9), (116, 10), (117, 11), (118, 11), (119, 11), (120, 11), (121, 11) ], "Y87", [RESTRICTING, RESTRICTING])

		block = self.blocks["OSYEEE"]
		self.routes["YRtY20Y21"] = Route(self.screen, block, "YRtY20Y21", "Y20", [ (114, 13), (115, 13), (116, 13), (117, 13), (118, 13), (119, 13), (120, 13), (121, 13) ], "Y21", [MAIN, RESTRICTING])
		self.routes["YRtY30Y21"] = Route(self.screen, block, "YRtY30Y21", "Y30", [ (112, 7), (113, 7), (114, 8), (115, 9), (116, 10), (117, 11), (118, 11), (119, 12), (120, 13), (121, 13) ], "Y21", [RESTRICTING, RESTRICTING])
		self.routes["YRtY87Y21"] = Route(self.screen, block, "YRtY87Y21", "Y87", [ (113, 9), (114, 9), (115, 9), (116, 10), (117, 11), (118, 11), (119, 12), (120, 13), (121, 13) ], "Y21", [RESTRICTING, RESTRICTING])
		self.routes["YRtY10Y21"] = Route(self.screen, block, "YRtY10Y21", "Y10", [ (114, 11), (115, 11), (116, 11), (117, 11), (118, 11), (119, 12), (120, 13), (121, 13) ], "Y21", [RESTRICTING, RESTRICTING])

		self.signals["Y8LA"].AddPossibleRoutes("OSYEEW", ["YRtY10Y11"])
		self.signals["Y8LA"].AddPossibleRoutes("OSYEEE", ["YRtY10Y21"])
		self.signals["Y8LB"].AddPossibleRoutes("OSYEEW", ["YRtY87Y11"])
		self.signals["Y8LB"].AddPossibleRoutes("OSYEEE", ["YRtY87Y21"])
		self.signals["Y8LC"].AddPossibleRoutes("OSYEEW", ["YRtY30Y11"])
		self.signals["Y8LC"].AddPossibleRoutes("OSYEEE", ["YRtY30Y21"])
		self.signals["Y8R"].AddPossibleRoutes("OSYEEW", ["YRtY10Y11", "YRtY87Y11", "YRtY30Y11"])
		self.signals["Y10L"].AddPossibleRoutes("OSYEEE", ["YRtY20Y21"])
		self.signals["Y10R"].AddPossibleRoutes("OSYEEE", ["YRtY20Y21", "YRtY10Y21", "YRtY87Y21", "YRtY30Y21"])

		self.osSignals["OSYEEW"] = [ "Y8LA", "Y8LB", "Y8LC", "Y8R" ]
		self.osSignals["OSYEEE"] = [ "Y8LA", "Y8LB", "Y8LC", "Y10L", "Y10R" ]

		# Kale interlocking
		block = self.blocks["OSYKLE"]
		self.routes["YRtY20Y51"] = Route(self.screen, block, "YRtY20Y51", "Y51", [ (96, 13), (97, 13), (98, 13), (99, 13), (100, 13), (101, 13), (102, 13), (103, 13), (104, 13), (105, 13), (106, 13) ], "Y20", [RESTRICTING, RESTRICTING])
		self.routes["YRtY20Y50"] = Route(self.screen, block, "YRtY20Y50", "Y50", [ (96, 15), (97, 15), (98, 15), (99, 14), (100, 13), (101, 13), (102, 13), (103, 13), (104, 13), (105, 13), (106, 13) ], "Y20", [RESTRICTING, RESTRICTING])
		self.routes["YRtY20Y70"] = Route(self.screen, block, "YRtY20Y70", "Y70", [ (96, 11), (97, 11), (98, 12), (99, 13), (100, 13), (101, 13), (102, 13), (103, 13), (104, 13), (105, 13), (106, 13) ], "Y20", [RESTRICTING, DIVERGING])
		self.routes["YRtY20Y52"] = Route(self.screen, block, "YRtY20Y52", "Y52", [ (95, 9), (96, 9), (97, 9), (98, 9), (99, 10), (100, 11), (101, 12), (102, 13), (103, 13), (104, 13), (105, 13), (106, 13) ], "Y20", [RESTRICTING, RESTRICTING])
		self.routes["YRtY20Y53"] = Route(self.screen, block, "YRtY20Y53", "Y53", [ (95, 7), (96, 7), (97, 8), (98, 9), (99, 10), (100, 11), (101, 12), (102, 13), (103, 13), (104, 13), (105, 13), (106, 13) ], "Y20", [RESTRICTING, RESTRICTING])
		self.routes["YRtY20Y60"] = Route(self.screen, block, "YRtY20Y60", "Y60", [ (95, 5), (96, 5), (97, 5), (98, 6), (99, 7), (100, 8), (101, 9), (102, 10), (103, 11), (104, 12), (105, 13), (106, 13) ], "Y20", [RESTRICTING, RESTRICTING])

		block = self.blocks["OSYKLW"]
		self.routes["YRtY10Y52"] = Route(self.screen, block, "YRtY10Y52", "Y10", [ (95, 9), (96, 9), (97, 9), (98, 9), (99, 10), (100, 11), (101, 11), (102, 11), (103, 11), (104, 11), (105, 11), (106, 11) ], "Y52", [RESTRICTING, SLOW])
		self.routes["YRtY10Y50"] = Route(self.screen, block, "YRtY10Y50", "Y10", [ (96, 15), (97, 15), (98, 15), (99, 14), (100, 13), (101, 13), (102, 13), (103, 13), (104, 12), (105, 11), (106, 11) ], "Y50", [RESTRICTING, SLOW])
		self.routes["YRtY10Y51"] = Route(self.screen, block, "YRtY10Y51", "Y10", [ (96, 13), (97, 13), (98, 13), (99, 13), (100, 13), (101, 13), (102, 13), (103, 13), (104, 12), (105, 11), (106, 11) ], "Y51", [RESTRICTING, RESTRICTING])
		self.routes["YRtY10Y70"] = Route(self.screen, block, "YRtY10Y70", "Y10", [ (96, 11), (97, 11), (98, 12), (99, 13), (100, 13), (101, 13), (102, 13), (103, 13), (104, 12), (105, 11), (106, 11) ], "Y70", [RESTRICTING, RESTRICTING])
		self.routes["YRtY10Y53"] = Route(self.screen, block, "YRtY10Y53", "Y10", [ (95, 7), (96, 7), (97, 8), (98, 9), (99, 10), (100, 11), (101, 11), (102, 11), (103, 11), (104, 11), (105, 11), (106, 11) ], "Y53", [RESTRICTING, SLOW])
		self.routes["YRtY10Y60"] = Route(self.screen, block, "YRtY10Y60", "Y10", [ (95, 5), (96, 5), (97, 5), (98, 6), (99, 7), (100, 8), (101, 9), (102, 10), (103, 11), (104, 11), (105, 11), (106, 11) ], "Y60", [RESTRICTING, RESTRICTING])

		self.signals["Y22R"].AddPossibleRoutes("OSYKLW", [ "YRtY10Y50", "YRtY10Y51", "YRtY10Y52", "YRtY10Y53", "YRtY10Y60", "YRtY10Y70" ])
		self.signals["Y26R"].AddPossibleRoutes("OSYKLE", [ "YRtY20Y50", "YRtY20Y51", "YRtY20Y52", "YRtY20Y53", "YRtY20Y60", "YRtY20Y70" ])
		self.signals["Y22L"].AddPossibleRoutes("OSYKLW", [ "YRtY10Y60" ])
		self.signals["Y22L"].AddPossibleRoutes("OSYKLE", [ "YRtY20Y60" ])
		self.signals["Y24LA"].AddPossibleRoutes("OSYKLW", [ "YRtY10Y52" ])
		self.signals["Y24LA"].AddPossibleRoutes("OSYKLE", [ "YRtY20Y52" ])
		self.signals["Y24LB"].AddPossibleRoutes("OSYKLW", [ "YRtY10Y53" ])
		self.signals["Y24LB"].AddPossibleRoutes("OSYKLE", [ "YRtY20Y53" ])
		self.signals["Y26LA"].AddPossibleRoutes("OSYKLW", [ "YRtY10Y50" ])
		self.signals["Y26LA"].AddPossibleRoutes("OSYKLE", [ "YRtY20Y50" ])
		self.signals["Y26LB"].AddPossibleRoutes("OSYKLW", [ "YRtY10Y51" ])
		self.signals["Y26LB"].AddPossibleRoutes("OSYKLE", [ "YRtY20Y51" ])
		self.signals["Y26LC"].AddPossibleRoutes("OSYKLW", [ "YRtY10Y70" ])
		self.signals["Y26LC"].AddPossibleRoutes("OSYKLE", [ "YRtY20Y70" ])

		self.osSignals["OSYKLW"] = [ "Y22R", "Y22L", "Y24LA", "Y24LB", "Y26LA", "Y26LB", "Y26LC" ]
		self.osSignals["OSYKLE"] = [ "Y26R", "Y22L", "Y24LA", "Y24LB", "Y26LA", "Y26LB", "Y26LC" ]

		# Kale west end
		block = self.blocks["OSYWKL"]
		self.routes["YRtY30Y51"] = Route(self.screen, block, "YRtY30Y51", "Y30", [ (84, 13), (85, 13), (86, 13), (87, 13), (88, 13) ], "Y51", [SLOW, RESTRICTING])
		self.routes["YRtY30Y50"] = Route(self.screen, block, "YRtY30Y50", "Y30", [ (84, 13), (85, 13), (86, 14), (87, 15), (88, 15) ], "Y50", [SLOW, RESTRICTING])

		self.signals["Y34L"].AddPossibleRoutes("OSYWKL", [ "YRtY30Y51", "YRtY30Y50" ])
		self.signals["Y34RA"].AddPossibleRoutes("OSYWKL", [ "YRtY30Y50" ])
		self.signals["Y34RB"].AddPossibleRoutes("OSYWKL", [ "YRtY30Y51" ])

		self.osSignals["OSYWKL"] = [ "Y34L", "Y34RA", "Y34RB" ]

		return self.signals

	def DefineButtons(self, tiles):
		self.buttons = {}
		self.osButtons = {}


		return self.buttons
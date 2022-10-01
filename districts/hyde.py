from district import District

from block import Block, OverSwitch, Route
from turnout import Turnout
from signal import Signal
from button import Button

from constants import LaKr, RESTRICTING, MAIN, DIVERGING

class Hyde (District):
	def __init__(self, name, frame, screen):
		District.__init__(self, name, frame, screen)

	def DetermineRoute(self, blocks):
		for bname in blocks:
			block = self.frame.GetBlockByName(bname)
			if bname == "OSHWW":
				s1 = 'N' if self.turnouts["HSw1"].IsNormal() else 'R'
				s3 = 'N' if self.turnouts["HSw3"].IsNormal() else 'R'
				s5 = 'N' if self.turnouts["HSw5"].IsNormal() else 'R'
				s7 = 'N' if self.turnouts["HSw7"].IsNormal() else 'R'

				if s1 + s3 == "NN":
					block.SetRoute(self.routes["HRtH11H12"])
				elif s1 + s3 == "NR":
					block.SetRoute(self.routes["HRtH11H34"])
				elif s1 + s5 == "RN":
					block.SetRoute(self.routes["HRtH11H33"])
				elif s1 + s5 + s7 == "RRN":
					block.SetRoute(self.routes["HRtH11H32"])
				elif s1 + s5 + s7 == "RRR":
					block.SetRoute(self.routes["HRtH11H31"])

			elif bname == "OSHWW2":			
				s7 = 'N' if self.turnouts["HSw7"].IsNormal() else 'R'
				if s7 == "N":
					block.SetRoute(self.routes["HRtH30H31"])

			elif bname == "OSHWE":
				s9  = 'N' if self.turnouts["HSw9"].IsNormal() else 'R'
				s11 = 'N' if self.turnouts["HSw11"].IsNormal() else 'R'
				s13 = 'N' if self.turnouts["HSw13"].IsNormal() else 'R'

				if s9 + s11 == "NN":
					block.SetRoute(self.routes["HRtH21H22"])
				elif s9 + s11 == "NR":
					block.SetRoute(self.routes["HRtH21H43"])
				elif s9 + s13 == "RN":
					block.SetRoute(self.routes["HRtH21H42"])
				elif s9 + s13 == "RR":
					block.SetRoute(self.routes["HRtH21H41"])

			elif bname == "OSHEW":
				s15 = 'N' if self.turnouts["HSw15"].IsNormal() else 'R'
				s17 = 'N' if self.turnouts["HSw17"].IsNormal() else 'R'
				s19 = 'N' if self.turnouts["HSw19"].IsNormal() else 'R'
				s21 = 'N' if self.turnouts["HSw21"].IsNormal() else 'R'

				if s21 == "R":
					block.SetRoute(self.routes["HRtH13H31"])
				elif s21 + s19 == "NR":
					block.SetRoute(self.routes["HRtH13H32"])
				elif s21 + s19 + s17 == "NNR":
					block.SetRoute(self.routes["HRtH13H33"])
				elif s21 + s19 + s17 + s15 == "NNNR":
					block.SetRoute(self.routes["HRtH13H34"])
				elif s21 + s19 + s17 + s15 == "NNNN":
					block.SetRoute(self.routes["HRtH12H13"])

			elif bname == "OSHEE":
				s23 = 'N' if self.turnouts["HSw23"].IsNormal() else 'R'
				s25 = 'N' if self.turnouts["HSw25"].IsNormal() else 'R'
				s27 = 'N' if self.turnouts["HSw27"].IsNormal() else 'R'
				s29 = 'N' if self.turnouts["HSw29"].IsNormal() else 'R'
				if s29 == "R":
					block.SetRoute(self.routes["HRtH23H40"])
				elif s29+s27 == "NN":
					block.SetRoute(self.routes["HRtH22H23"])
				elif s29+s27+s25 == "NRR":
					block.SetRoute(self.routes["HRtH23H43"])
				elif s29+s27+s25+s23 == "NRNR":
					block.SetRoute(self.routes["HRtH23H42"])
				elif s29+s27+s25+s23 == "NRNN":
					block.SetRoute(self.routes["HRtH23H41"])

	def PerformButtonAction(self, btn):
		bname = btn.GetName()
		if bname in self.osButtons["OSHWW"]:
			osBlk = self.blocks["OSHWW"]
			if osBlk.IsBusy():
				self.reportBlockBusy("OSHWW")
				return

			btn.Press(refresh=True)
			self.frame.ClearButtonAfter(2, btn)
			if bname == "HWWB2":
				self.frame.Request({"turnout": {"name": "HSw1", "status": "R" }})
				self.frame.Request({"turnout": {"name": "HSw3", "status": "R" }})
				self.frame.Request({"turnout": {"name": "HSw7", "status": "R" }})
			elif bname == "HWWB3":
				self.frame.Request({"turnout": {"name": "HSw1", "status": "R" }})
				self.frame.Request({"turnout": {"name": "HSw3", "status": "R" }})
				self.frame.Request({"turnout": {"name": "HSw7", "status": "N" }})
			elif bname == "HWWB4":
				self.frame.Request({"turnout": {"name": "HSw1", "status": "R" }})
				self.frame.Request({"turnout": {"name": "HSw3", "status": "N" }})
			elif bname == "HWWB5":
				self.frame.Request({"turnout": {"name": "HSw1", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw3", "status": "R" }})
			elif bname == "HWWB6":
				self.frame.Request({"turnout": {"name": "HSw1", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw3", "status": "N" }})

		elif bname in self.osButtons["OSHWW2"]:
			osBlk = self.blocks["OSHWW2"]
			if osBlk.IsBusy():
				self.reportBlockBusy("OSHWW2")
				return

			btn.Press(refresh=True)
			self.frame.ClearButtonAfter(2, btn)
			if bname == "HWWB1":
				self.frame.Request({"turnout": {"name": "HSw7", "status": "N" }})

		elif bname in self.osButtons["OSHWE"]:
			osBlk = self.blocks["OSHWE"]
			if osBlk.IsBusy():
				self.reportBlockBusy("OSHWE")
				return

			btn.Press(refresh=True)
			self.frame.ClearButtonAfter(2, btn)
			if bname == "HWEB1":
				self.frame.Request({"turnout": {"name": "HSw9", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw11", "status": "N" }})
			if bname == "HWEB2":
				self.frame.Request({"turnout": {"name": "HSw9", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw11", "status": "R" }})
			elif bname == "HWEB3":
				self.frame.Request({"turnout": {"name": "HSw9", "status": "R" }})
				self.frame.Request({"turnout": {"name": "HSw11", "status": "N" }})
			elif bname == "HWEB4":
				self.frame.Request({"turnout": {"name": "HSw9", "status": "R" }})
				self.frame.Request({"turnout": {"name": "HSw11", "status": "R" }})

		elif bname in self.osButtons["OSHEW"]:
			osBlk = self.blocks["OSHEW"]
			if osBlk.IsBusy():
				self.reportBlockBusy("OSHEW")
				return

			btn.Press(refresh=True)
			self.frame.ClearButtonAfter(2, btn)
			if bname == "HEWB1":
				self.frame.Request({"turnout": {"name": "HSw21", "status": "R" }})
			if bname == "HEWB2":
				self.frame.Request({"turnout": {"name": "HSw21", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw19", "status": "R" }})
			elif bname == "HEWB3":
				self.frame.Request({"turnout": {"name": "HSw21", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw19", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw17", "status": "R" }})
			elif bname == "HEWB4":
				self.frame.Request({"turnout": {"name": "HSw21", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw19", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw17", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw15", "status": "R" }})
			elif bname == "HEWB5":
				self.frame.Request({"turnout": {"name": "HSw21", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw19", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw17", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw15", "status": "N" }})

		elif bname in self.osButtons["OSHEE"]:
			osBlk = self.blocks["OSHEE"]
			if osBlk.IsBusy():
				self.reportBlockBusy("OSHEE")
				return

			btn.Press(refresh=True)
			self.frame.ClearButtonAfter(2, btn)
			if bname == "HEEB1":
				self.frame.Request({"turnout": {"name": "HSw27", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw29", "status": "N" }})
			if bname == "HEEB2":
				self.frame.Request({"turnout": {"name": "HSw25", "status": "R" }})
				self.frame.Request({"turnout": {"name": "HSw27", "status": "R" }})
				self.frame.Request({"turnout": {"name": "HSw29", "status": "N" }})
			elif bname == "HEEB3":
				self.frame.Request({"turnout": {"name": "HSw23", "status": "R" }})
				self.frame.Request({"turnout": {"name": "HSw25", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw27", "status": "R" }})
				self.frame.Request({"turnout": {"name": "HSw29", "status": "N" }})
			elif bname == "HEEB4":
				self.frame.Request({"turnout": {"name": "HSw23", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw25", "status": "N" }})
				self.frame.Request({"turnout": {"name": "HSw27", "status": "R" }})
				self.frame.Request({"turnout": {"name": "HSw29", "status": "N" }})
			elif bname == "HEEB5":
				self.frame.Request({"turnout": {"name": "HSw29", "status": "R" }})

	def DefineBlocks(self, tiles):
		self.blocks = {}
		self.osBlocks = {}

		self.blocks["H11"] = Block(self, self.frame, "H11",
			[
				(tiles["horiz"], self.screen, (13,13), False),
				(tiles["horiznc"], self.screen, (14,13), False),
				(tiles["horiz"], self.screen, (15,13), False),
				(tiles["horiznc"], self.screen, (16,13), False),
				(tiles["horiz"], self.screen, (17,13), False),
				(tiles["horiznc"], self.screen, (18,13), False),
				(tiles["horiz"], self.screen, (19,13), False),
				(tiles["horiznc"], self.screen, (20,13), False),

				(tiles["eobleft"], LaKr, (123,11), False),
				(tiles["horiz"], LaKr, (124,11), False),
				(tiles["horiznc"], LaKr, (125,11), False),
				(tiles["horiz"], LaKr, (126,11), False),
				(tiles["horiznc"], LaKr, (127,11), False),
			], False)

		self.blocks["H12"] = Block(self, self.frame, "H12",
			[
				(tiles["horiz"], self.screen, (33,13), False),
				(tiles["horiznc"], self.screen, (34,13), False),
				(tiles["horiz"], self.screen, (35,13), False),
				(tiles["horiznc"], self.screen, (36,13), False),
				(tiles["horiz"], self.screen, (37,13), False),
				(tiles["horiznc"], self.screen, (38,13), False),
				(tiles["horiz"], self.screen, (39,13), False),
				(tiles["horiznc"], self.screen, (40,13), False),
			], False)


		self.blocks["H30"] = Block(self, self.frame, "H30",
			[
				(tiles["horiznc"], self.screen, (13, 11), False),
				(tiles["horiz"], self.screen, (14, 11), False),
				(tiles["horiznc"], self.screen, (15, 11), False),
				(tiles["horiz"], self.screen, (16, 11), False),
				(tiles["horiznc"], self.screen, (17, 11), False),
				(tiles["horiz"], self.screen, (18, 11), False),
				(tiles["turnleftright"], self.screen, (19, 11), False),
				(tiles["diagleft"], self.screen, (20, 10), False),
				(tiles["diagleft"], self.screen, (21, 9), False),
				(tiles["diagleft"], self.screen, (22, 8), False),
				(tiles["diagleft"], self.screen, (23, 7), False),
				(tiles["diagleft"], self.screen, (24, 6), False),
				(tiles["turnleftleft"], self.screen, (25, 5), True),
				(tiles["horiz"], self.screen, (26, 5), False),

				(tiles["eobleft"], LaKr, (106, 9), False),
				(tiles["horiznc"], LaKr, (107, 9), False),
				(tiles["horiz"], LaKr, (108, 9), False),
				(tiles["horiznc"], LaKr, (109, 9), False),
				(tiles["horiz"], LaKr, (110, 9), False),
				(tiles["horiznc"], LaKr, (111, 9), False),
				(tiles["horiz"], LaKr, (112, 9), False),
				(tiles["horiznc"], LaKr, (113, 9), False),
				(tiles["horiz"], LaKr, (114, 9), False),
				(tiles["horiznc"], LaKr, (115, 9), False),
				(tiles["horiz"], LaKr, (116, 9), False),
				(tiles["horiznc"], LaKr, (117, 9), False),
				(tiles["horiz"], LaKr, (118, 9), False),
				(tiles["horiznc"], LaKr, (119, 9), False),
				(tiles["horiz"], LaKr, (120, 9), False),
				(tiles["horiznc"], LaKr, (121, 9), False),
				(tiles["horiz"], LaKr, (122, 9), False),
				(tiles["horiznc"], LaKr, (123, 9), False),
				(tiles["horiz"], LaKr, (124, 9), False),
				(tiles["horiznc"], LaKr, (125, 9), False),
				(tiles["horiz"], LaKr, (126, 9), False),
				(tiles["horiznc"], LaKr, (127, 9), False),
			],
			False)

		self.blocks["H31"] = Block(self, self.frame, "H31",
			[
				(tiles["horiz"], self.screen, (33,5), False),
				(tiles["horiznc"], self.screen, (34,5), False),
				(tiles["horiz"], self.screen, (35,5), False),
				(tiles["horiznc"], self.screen, (36,5), False),
				(tiles["horiz"], self.screen, (37,5), False),
				(tiles["horiznc"], self.screen, (38,5), False),
				(tiles["horiz"], self.screen, (39,5), False),
				(tiles["horiznc"], self.screen, (40,5), False),
			], False)

		self.blocks["H32"] = Block(self, self.frame, "H32",
			[
				(tiles["horiz"], self.screen, (33,7), False),
				(tiles["horiznc"], self.screen, (34,7), False),
				(tiles["horiz"], self.screen, (35,7), False),
				(tiles["horiznc"], self.screen, (36,7), False),
				(tiles["horiz"], self.screen, (37,7), False),
				(tiles["horiznc"], self.screen, (38,7), False),
				(tiles["horiz"], self.screen, (39,7), False),
				(tiles["horiznc"], self.screen, (40,7), False),
			], False)

		self.blocks["H33"] = Block(self, self.frame, "H33",
			[
				(tiles["horiz"], self.screen, (33,9), False),
				(tiles["horiznc"], self.screen, (34,9), False),
				(tiles["horiz"], self.screen, (35,9), False),
				(tiles["horiznc"], self.screen, (36,9), False),
				(tiles["horiz"], self.screen, (37,9), False),
				(tiles["horiznc"], self.screen, (38,9), False),
				(tiles["horiz"], self.screen, (39,9), False),
				(tiles["horiznc"], self.screen, (40,9), False),
			], False)

		self.blocks["H34"] = Block(self, self.frame, "H34",
			[
				(tiles["horiz"], self.screen, (33,11), False),
				(tiles["horiznc"], self.screen, (34,11), False),
				(tiles["horiz"], self.screen, (35,11), False),
				(tiles["horiznc"], self.screen, (36,11), False),
				(tiles["horiz"], self.screen, (37,11), False),
				(tiles["horiznc"], self.screen, (38,11), False),
				(tiles["horiz"], self.screen, (39,11), False),
				(tiles["horiznc"], self.screen, (40,11), False),
			], False)

		self.blocks["OSHWW"] = OverSwitch(self, self.frame, "OSHWW", 
			[
				(tiles["horiznc"], self.screen, (31, 5), False),
				(tiles["diagleft"], self.screen, (29, 6), False),
				(tiles["diagleft"], self.screen, (27, 8), False),
				(tiles["diagleft"], self.screen, (25, 10), False),
				(tiles["diagleft"], self.screen, (24, 11), False),
				(tiles["diagleft"], self.screen, (23, 12), False),
				(tiles["eobleft"], self.screen, (21, 13), False),
				(tiles["horiznc"], self.screen, (23, 13), False),
				(tiles["horiz"], self.screen, (24, 13), False),

				(tiles["horiznc"], self.screen, (29, 7), False),
				(tiles["horiz"], self.screen, (30, 7), False),
				(tiles["horiznc"], self.screen, (31, 7), False),

				(tiles["horiznc"], self.screen, (27, 9), False),
				(tiles["horiz"], self.screen, (28, 9), False),
				(tiles["horiznc"], self.screen, (29, 9), False),
				(tiles["horiz"], self.screen, (30, 9), False),
				(tiles["horiznc"], self.screen, (31, 9), False),

				(tiles["diagleft"], self.screen, (26, 12), False),
				(tiles["turnleftleft"], self.screen, (27, 11), True),
				(tiles["horiz"], self.screen, (28, 11), False),
				(tiles["horiznc"], self.screen, (29, 11), False),
				(tiles["horiz"], self.screen, (30, 11), False),
				(tiles["horiznc"], self.screen, (31, 11), False),

				(tiles["horiz"], self.screen, (26, 13), False),
				(tiles["horiznc"], self.screen, (27, 13), False),
				(tiles["horiz"], self.screen, (28, 13), False),
				(tiles["horiznc"], self.screen, (29, 13), False),
				(tiles["horiz"], self.screen, (30, 13), False),
				(tiles["horiznc"], self.screen, (31, 13), False),
			], 
			False)

		self.blocks["OSHWW2"] = OverSwitch(self, self.frame, "OSHWW2", 
			[
				(tiles["horiznc"], self.screen, (31, 5), False),
				(tiles["horiz"], self.screen, (28, 5), False),
				(tiles["horiznc"], self.screen, (29, 5), False),
			], 
			False)

		self.osBlocks["OSHWW"] = [ "H11", "H12", "H31", "H32", "H33", "H34" ]
		self.osBlocks["OSHWW2"] = [ "H30", "H31" ]

		self.blocks["H21"] = Block(self, self.frame, "H21",
			[
				(tiles["horiz"],   self.screen, (13, 15), False),
				(tiles["horiznc"], self.screen, (14, 15), False),
				(tiles["horiz"],   self.screen, (15, 15), False),
				(tiles["horiznc"], self.screen, (16, 15), False),
				(tiles["horiz"],   self.screen, (17, 15), False),
				(tiles["eobleft"], LaKr,        (123,13), False),
				(tiles["horiz"],   LaKr,        (124,13), False),
				(tiles["horiznc"], LaKr,        (125,13), False),
				(tiles["horiz"],   LaKr,        (126,13), False),
				(tiles["horiznc"], LaKr,        (127,13), False),
			], True)
		self.blocks["H21"].AddStoppingBlock([
				(tiles["horiznc"], self.screen, (18, 15), False),
				(tiles["horiz"],   self.screen, (19, 15), False),
				(tiles["eobright"], self.screen, (20, 15), False),
			], True)

		self.blocks["H22"] = Block(self, self.frame, "H22",
			[
				(tiles["horiz"],   self.screen, (33, 15), False),
				(tiles["horiznc"], self.screen, (34, 15), False),
				(tiles["horiz"],   self.screen, (35, 15), False),
				(tiles["horiznc"], self.screen, (36, 15), False),
				(tiles["horiz"],   self.screen, (37, 15), False),
				(tiles["horiznc"], self.screen, (38, 15), False),
				(tiles["horiz"],   self.screen, (39, 15), False),
				(tiles["horiznc"], self.screen, (40, 15), False),
			], True)

		self.blocks["H43"] = Block(self, self.frame, "H43",
			[
				(tiles["horiz"],   self.screen, (33, 17), False),
				(tiles["horiznc"], self.screen, (34, 17), False),
				(tiles["horiz"],   self.screen, (35, 17), False),
				(tiles["horiznc"], self.screen, (36, 17), False),
				(tiles["horiz"],   self.screen, (37, 17), False),
				(tiles["horiznc"], self.screen, (38, 17), False),
				(tiles["horiz"],   self.screen, (39, 17), False),
				(tiles["horiznc"], self.screen, (40, 17), False),
			], True)

		self.blocks["H42"] = Block(self, self.frame, "H42",
			[
				(tiles["horiz"],   self.screen, (33, 19), False),
				(tiles["horiznc"], self.screen, (34, 19), False),
				(tiles["horiz"],   self.screen, (35, 19), False),
				(tiles["horiznc"], self.screen, (36, 19), False),
				(tiles["horiz"],   self.screen, (37, 19), False),
				(tiles["horiznc"], self.screen, (38, 19), False),
				(tiles["horiz"],   self.screen, (39, 19), False),
				(tiles["horiznc"], self.screen, (40, 19), False),
			], True)

		self.blocks["H41"] = Block(self, self.frame, "H41",
			[
				(tiles["horiz"],   self.screen, (33, 21), False),
				(tiles["horiznc"], self.screen, (34, 21), False),
				(tiles["horiz"],   self.screen, (35, 21), False),
				(tiles["horiznc"], self.screen, (36, 21), False),
				(tiles["horiz"],   self.screen, (37, 21), False),
				(tiles["horiznc"], self.screen, (38, 21), False),
				(tiles["horiz"],   self.screen, (39, 21), False),
				(tiles["horiznc"], self.screen, (40, 21), False),
			], True)

		self.blocks["H40"] = Block(self, self.frame, "H40",
			[
				(tiles["horiz"],   self.screen, (13, 17), False),
				(tiles["horiznc"], self.screen, (14, 17), False),
				(tiles["horiz"],   self.screen, (15, 17), False),
				(tiles["horiznc"], self.screen, (16, 17), False),
				(tiles["horiz"],   self.screen, (17, 17), False),
				(tiles["horiznc"], self.screen, (18, 17), False),
				(tiles["horiz"],   self.screen, (19, 17), False),
				(tiles["horiznc"], self.screen, (20, 17), False),
				(tiles["turnrightright"], self.screen, (21, 17), False),
				(tiles["diagright"], self.screen, (22, 18), False),
				(tiles["diagright"], self.screen, (23, 19), False),
				(tiles["diagright"], self.screen, (24, 20), False),
				(tiles["diagright"], self.screen, (25, 21), False),
				(tiles["diagright"], self.screen, (26, 22), False),
				(tiles["turnrightleft"], self.screen, (27, 23), False),
				(tiles["horiz"],   self.screen, (28, 23), False),
				(tiles["horiznc"], self.screen, (29, 23), False),
				(tiles["horiz"],   self.screen, (30, 23), False),
				(tiles["horiznc"], self.screen, (31, 23), False),
				(tiles["horiz"],   self.screen, (32, 23), False),
				(tiles["horiznc"], self.screen, (33, 23), False),
				(tiles["horiz"],   self.screen, (34, 23), False),
				(tiles["horiznc"], self.screen, (35, 23), False),
				(tiles["horiz"],   self.screen, (36, 23), False),
				(tiles["horiznc"], self.screen, (37, 23), False),
				(tiles["horiz"],   self.screen, (38, 23), False),
				(tiles["horiznc"], self.screen, (39, 23), False),
				(tiles["horiznc"], self.screen, (40, 23), False),
				(tiles["eobleft"], LaKr,        (123,15), False),
				(tiles["horiz"],   LaKr,        (124,15), False),
				(tiles["horiznc"], LaKr,        (125,15), False),
				(tiles["horiz"],   LaKr,        (126,15), False),
				(tiles["horiznc"], LaKr,        (127,15), False),
			], True)

		self.blocks["OSHWE"] = OverSwitch(self, self.frame, "OSHWE", 
			[
				(tiles["eobleft"], self.screen, (21, 15), False),
				(tiles["horiznc"], self.screen, (23, 15), False),
				(tiles["horiz"],   self.screen, (24, 15), False),
				(tiles["horiznc"], self.screen, (26, 15), False),
				(tiles["horiz"],   self.screen, (27, 15), False),
				(tiles["horiznc"], self.screen, (28, 15), False),
				(tiles["horiz"],   self.screen, (29, 15), False),
				(tiles["horiznc"], self.screen, (30, 15), False),
				(tiles["horiz"],   self.screen, (31, 15), False),

				(tiles["diagright"], self.screen, (26, 16), False),
				(tiles["turnrightleft"], self.screen, (27, 17), False),
				(tiles["horiznc"], self.screen, (28, 17), False),
				(tiles["horiz"],   self.screen, (29, 17), False),
				(tiles["horiznc"], self.screen, (30, 17), False),
				(tiles["horiz"],   self.screen, (31, 17), False),

				(tiles["diagright"], self.screen, (23, 16), False),
				(tiles["diagright"], self.screen, (24, 17), False),
				(tiles["diagright"], self.screen, (25, 18), False),
				(tiles["horiz"],   self.screen, (27, 19), False),
				(tiles["horiznc"], self.screen, (28, 19), False),
				(tiles["horiz"],   self.screen, (29, 19), False),
				(tiles["horiznc"], self.screen, (30, 19), False),
				(tiles["horiz"],   self.screen, (31, 19), False),

				(tiles["diagright"], self.screen, (27, 20), False),
				(tiles["turnrightleft"], self.screen, (28, 21), False),
				(tiles["horiz"],   self.screen, (29, 21), False),
				(tiles["horiznc"], self.screen, (30, 21), False),
				(tiles["horiz"],   self.screen, (31, 21), False),

			], True)

		self.osBlocks["OSHWE"] = [ "H21", "H22", "H41", "H42", "H43" ]

		self.blocks["H13"] = Block(self, self.frame, "H13",
			[
				(tiles["horiznc"], self.screen, (60, 13), False),
				(tiles["horiz"],   self.screen, (61, 13), False),
				(tiles["horiznc"], self.screen, (62, 13), False),
				(tiles["horiz"],   self.screen, (63, 13), False),
				(tiles["horiznc"], self.screen, (64, 13), False),

				(tiles["horiz"],   LaKr,        (40, 9), False),
				(tiles["horiznc"], LaKr,        (41, 9), False),
				(tiles["horiz"],   LaKr,        (42, 9), False),
				(tiles["horiznc"], LaKr,        (43, 9), False),
				(tiles["horiz"],   LaKr,        (44, 9), False),
				(tiles["eobright"], LaKr,       (45, 9), False),
			], False)
		self.blocks["H13"].AddStoppingBlock([
				(tiles["eobleft"], self.screen, (57, 13), False),
				(tiles["horiznc"], self.screen, (58, 13), False),
				(tiles["horiz"],   self.screen, (59, 13), False),
				], False)

		self.blocks["OSHEW"] = OverSwitch(self, self.frame, "OSHEW", 
			[
				(tiles["horiznc"], self.screen, (42, 5), False),
				(tiles["horiz"],   self.screen, (43, 5), False),
				(tiles["horiznc"], self.screen, (44, 5), False),
				(tiles["horiz"],   self.screen, (45, 5), False),
				(tiles["turnrightright"], self.screen, (46, 5), False),
				(tiles["diagright"],      self.screen, (47, 6), False),
				(tiles["diagright"],      self.screen, (48, 7), False),
				(tiles["diagright"],      self.screen, (49, 8), False),
				(tiles["diagright"],      self.screen, (50, 9), False),
				(tiles["diagright"],      self.screen, (51, 10), False),
				(tiles["diagright"],      self.screen, (52, 11), False),
				(tiles["diagright"],      self.screen, (53, 12), False),
				(tiles["horiznc"],  self.screen, (55, 13), False),
				(tiles["eobright"], self.screen, (56, 13), False),

				(tiles["horiznc"], self.screen, (42, 7), False),
				(tiles["horiz"],   self.screen, (43, 7), False),
				(tiles["horiznc"], self.screen, (44, 7), False),
				(tiles["turnrightright"], self.screen, (45, 7), False),
				(tiles["diagright"],      self.screen, (46, 8), False),
				(tiles["diagright"],      self.screen, (47, 9), False),
				(tiles["diagright"],      self.screen, (48, 10), False),
				(tiles["diagright"],      self.screen, (49, 11), False),
				(tiles["diagright"],      self.screen, (50, 12), False),
				(tiles["horiznc"], self.screen, (52, 13), False),
				(tiles["horiz"],   self.screen, (53, 13), False),

				(tiles["horiznc"], self.screen, (42, 9), False),
				(tiles["horiz"],   self.screen, (43, 9), False),
				(tiles["turnrightright"], self.screen, (44, 9), False),
				(tiles["diagright"],      self.screen, (45, 10), False),
				(tiles["diagright"],      self.screen, (46, 11), False),
				(tiles["diagright"],      self.screen, (47, 12), False),
				(tiles["horiznc"], self.screen, (49, 13), False),
				(tiles["horiz"],   self.screen, (50, 13), False),

				(tiles["horiznc"], self.screen, (42, 11), False),
				(tiles["turnrightright"], self.screen, (43, 11), False),
				(tiles["diagright"],      self.screen, (44, 12), False),
				(tiles["horiznc"], self.screen, (46, 13), False),
				(tiles["horiz"],   self.screen, (47, 13), False),

				(tiles["horiznc"], self.screen, (42, 13), False),
				(tiles["horiz"],   self.screen, (43, 13), False),
				(tiles["horiznc"], self.screen, (44, 13), False),

			], 
			False)

		self.osBlocks["OSHEW"] = [ "H13" ]

		self.blocks["H23"] = Block(self, self.frame, "H23",
			[
				(tiles["eobleft"], self.screen, (57, 15), False),
				(tiles["horiznc"], self.screen, (58, 15), False),
				(tiles["horiz"],   self.screen, (59, 15), False),
				(tiles["horiznc"], self.screen, (60, 15), False),
				(tiles["horiz"],   self.screen, (61, 15), False),
				(tiles["horiznc"], self.screen, (62, 15), False),
				(tiles["horiz"],   self.screen, (63, 15), False),
				(tiles["horiznc"], self.screen, (64, 15), False),

				(tiles["horiz"],   LaKr,        (40, 15), False),
				(tiles["horiznc"], LaKr,        (41, 15), False),
				(tiles["horiz"],   LaKr,        (42, 15), False),
				(tiles["horiznc"], LaKr,        (43, 15), False),
				(tiles["horiz"],   LaKr,        (44, 15), False),
				(tiles["eobright"], LaKr,       (45, 15), False),
			], True)

		self.blocks["OSHEE"] = OverSwitch(self, self.frame, "OSHEE", 
			[
				(tiles["horiznc"], self.screen, (42, 15), False),
				(tiles["horiz"],   self.screen, (43, 15), False),
				(tiles["horiznc"], self.screen, (44, 15), False),
				(tiles["horiz"],   self.screen, (45, 15), False),
				(tiles["horiznc"], self.screen, (46, 15), False),
				(tiles["horiz"],   self.screen, (47, 15), False),
				(tiles["horiznc"], self.screen, (48, 15), False),
				(tiles["horiz"],   self.screen, (49, 15), False),
				(tiles["horiznc"], self.screen, (51, 15), False),
				(tiles["horiz"],   self.screen, (52, 15), False),
				(tiles["horiznc"], self.screen, (54, 15), False),
				(tiles["horiz"],   self.screen, (55, 15), False),
				(tiles["eobright"], self.screen, (56, 15), False),

				(tiles["horiznc"], self.screen, (42, 17), False),
				(tiles["horiz"],   self.screen, (43, 17), False),
				(tiles["horiznc"], self.screen, (44, 17), False),
				(tiles["horiz"],   self.screen, (45, 17), False),
				(tiles["horiznc"], self.screen, (46, 17), False),
				(tiles["horiz"],   self.screen, (47, 17), False),
				(tiles["diagleft"], self.screen, (49, 16), False),

				(tiles["horiznc"], self.screen, (42, 19), False),
				(tiles["horiz"],   self.screen, (43, 19), False),
				(tiles["horiznc"], self.screen, (44, 19), False),
				(tiles["horiz"],   self.screen, (45, 19), False),
				(tiles["diagleft"], self.screen, (47, 18), False),

				(tiles["horiznc"], self.screen, (42, 21), False),
				(tiles["horiz"],   self.screen, (43, 21), False),
				(tiles["turnleftright"], self.screen, (44, 21), False),
				(tiles["diagleft"], self.screen, (45, 20), False),

				(tiles["horiznc"], self.screen, (42, 23), False),
				(tiles["horiz"],   self.screen, (43, 23), False),
				(tiles["horiznc"], self.screen, (44, 23), False),
				(tiles["turnleftright"], self.screen, (45, 23), False),
				(tiles["diagleft"], self.screen, (46, 22), False),
				(tiles["diagleft"], self.screen, (47, 21), False),
				(tiles["diagleft"], self.screen, (48, 20), False),
				(tiles["diagleft"], self.screen, (49, 19), False),
				(tiles["diagleft"], self.screen, (50, 18), False),
				(tiles["diagleft"], self.screen, (51, 17), False),
				(tiles["diagleft"], self.screen, (52, 16), False),
			], True)

		self.osBlocks["OSHEE"] = [ "H23" ]

		return self.blocks

	def DefineTurnouts(self, tiles, blocks):
		self.turnouts = {}

		toList = [
			[ "HSw7b", "toleftleft",    "OSHWW2", (30, 5) ],

			[ "HSw1",  "toleftright",   "OSHWW", (22, 13) ],
			[ "HSw3",  "toleftright",   "OSHWW", (25, 13) ],
			[ "HSw5",  "torightupinv",  "OSHWW", (26, 9) ],
			[ "HSw7",  "torightupinv",  "OSHWW", (28, 7) ],

			[ "HSw9",  "torightright",  "OSHWE", (22, 15) ],
			[ "HSw11", "torightright",  "OSHWE", (25, 15) ],
			[ "HSw13", "toleftdowninv", "OSHWE", (26, 19) ],

			[ "HSw15", "torightleft",   "OSHEW", (45, 13) ],
			[ "HSw17", "torightleft",   "OSHEW", (48, 13) ],
			[ "HSw19", "torightleft",   "OSHEW", (51, 13) ],
			[ "HSw21", "torightleft",   "OSHEW", (54, 13) ],

			[ "HSw23", "torightdown",   "OSHEE", (46, 19) ],
			[ "HSw25", "torightdown",   "OSHEE", (48, 17) ],
			[ "HSw27", "toleftleft",    "OSHEE", (50, 15) ],
			[ "HSw29", "toleftleft",    "OSHEE", (53, 15) ],
		]

		for tonm, tileSet, blknm, pos in toList:
			trnout = Turnout(self, self.frame, tonm, self.screen, tiles[tileSet], pos)
			blocks[blknm].AddTurnout(trnout)
			self.turnouts[tonm] = trnout
		
		for tonm in [ to[0] for to in toList ]:
			self.turnouts[tonm].SetRouteControl(True)

		self.turnouts["HSw7"].SetPairedTurnout(self.turnouts["HSw7b"])
		self.turnouts["HSw3"].SetPairedTurnout(self.turnouts["HSw5"])
		self.turnouts["HSw11"].SetPairedTurnout(self.turnouts["HSw13"])

		self.osTurnouts = {}
		self.osTurnouts["OSHWW"] = ["HSw1", "HSw3", "HSw5", "HSw7" ]
		self.osTurnouts["OSHWW2"] = [ "HSw7b" ]
		self.osTurnouts["OSHWE"] = ["HSw9", "HSw11", "HSw13" ]
		self.osTurnouts["OSHEW"] = ["HSw15", "HSw17", "HSw19", "HSw21" ]
		self.osTurnouts["OSHEE"] = ["HSw23", "HSw25", "HSw27", "HSw29" ]
		
		return self.turnouts

	def DefineSignals(self, tiles):
		self.signals = {}

		sigList = [
			[ "H4LA", False, "left",  (32, 14) ],
			[ "H4LB", False, "left",  (32, 16) ],
			[ "H4LC", False, "left",  (32, 18) ],
			[ "H4LD", False, "left",  (32, 20) ],
			[ "H4R",  True,  "right", (21, 16) ],
			[ "H6LA", False, "left",  (32, 6) ],
			[ "H6LB", False, "left",  (32, 8) ],
			[ "H6LC", False, "left",  (32,10) ],
			[ "H6LD", False, "left",  (32, 12) ],
			[ "H6R",  True,  "right", (21, 14) ],
			[ "H8L",  False, "left",  (32, 4) ],
			[ "H8R",  True,  "right", (27, 6) ],
			[ "H10L", False, "left",  (56, 14) ],
			[ "H10RA", True, "right", (41, 16) ],
			[ "H10RB", True, "right", (41, 18) ],
			[ "H10RC", True, "right", (41, 20) ],
			[ "H10RD", True, "right", (41, 22) ],
			[ "H10RE", True, "right", (41, 24) ],
			[ "H12RA", True, "right", (41, 6) ],
			[ "H12RB", True, "right", (41, 8) ],
			[ "H12RC", True, "right", (41, 10) ],
			[ "H12RD", True, "right", (41, 12) ],
			[ "H12RE", True, "right", (41, 14) ],
			[ "H12L", False, "left", (56, 12) ],
		]
		for signm, east, tileSet, pos in sigList:
			self.signals[signm]  = Signal(self, self.screen, self.frame, signm, east, pos, tiles[tileSet])  

		self.routes = {}
		block = self.blocks["OSHWW"]
		self.routes["HRtH11H12"] = Route(self.screen, block, "HRtH11H12", "H12", [ (21, 13), (22, 13), (23, 13), (24, 13), (25, 13), (26, 13), (27, 13), (28, 13), (29, 13), (30, 13), (31, 13) ], "H11", [RESTRICTING, RESTRICTING])
		self.routes["HRtH11H31"] = Route(self.screen, block, "HRtH11H31", "H31", [ (21, 13), (22, 13), (23, 12), (24, 11), (25, 10), (26, 9), (27, 8), (28, 7), (29, 6), (30, 5), (31, 5) ], "H11", [RESTRICTING, RESTRICTING])
		self.routes["HRtH11H32"] = Route(self.screen, block, "HRtH11H32", "H32", [ (21, 13), (22, 13), (23, 12), (24, 11), (25, 10), (26, 9), (27, 8), (28, 7), (29, 7), (30, 7), (31, 7) ], "H11", [RESTRICTING, RESTRICTING])
		self.routes["HRtH11H33"] = Route(self.screen, block, "HRtH11H33", "H33", [ (21, 13), (22, 13), (23, 12), (24, 11), (25, 10), (26, 9), (27, 9), (28, 9), (29, 9), (30, 9), (31, 9) ], "H11", [RESTRICTING, RESTRICTING])
		self.routes["HRtH11H34"] = Route(self.screen, block, "HRtH11H34", "H34", [ (21, 13), (22, 13), (23, 13), (24, 13), (25, 13), (26, 12), (27, 11), (28, 11), (29, 11), (30, 11), (31, 11)], "H11", [RESTRICTING, RESTRICTING])

		block = self.blocks["OSHWW2"]			
		self.routes["HRtH30H31"] = Route(self.screen, block, "HRtH30H31", "H31", [ (28, 5), (29, 5), (30, 5), (31, 5) ], "H30", [RESTRICTING, MAIN])

		block = self.blocks["OSHWE"]
		self.routes["HRtH21H22"] = Route(self.screen, block, "HRtH21H22", "H21", [ (21, 15), (22, 15), (23, 15), (24, 15), (25, 15), (26, 15), (27, 15), (28, 15), (29, 15), (30, 15), (31, 15) ], "H22", [MAIN, RESTRICTING])
		self.routes["HRtH21H41"] = Route(self.screen, block, "HRtH21H41", "H21", [ (21, 15), (22, 15), (23, 16), (24, 17), (25, 18), (26, 19), (27, 20), (28, 21), (29, 21), (30, 21), (31, 21) ], "H41", [DIVERGING, RESTRICTING])
		self.routes["HRtH21H42"] = Route(self.screen, block, "HRtH21H42", "H21", [ (21, 15), (22, 15), (23, 16), (24, 17), (25, 18), (26, 19), (27, 19), (28, 19), (29, 19), (30, 19), (31, 19) ], "H42", [DIVERGING, RESTRICTING])
		self.routes["HRtH21H43"] = Route(self.screen, block, "HRtH21H43", "H21", [ (21, 15), (22, 15), (23, 15), (24, 15), (25, 15), (26, 16), (27, 17), (28, 17), (29, 17), (30, 17), (31, 17) ], "H43", [DIVERGING, RESTRICTING])

		block = self.blocks["OSHEW"]
		self.routes["HRtH13H31"] = Route(self.screen, block, "HRtH13H31", "H13", [(42, 5), (43, 5), (44, 5), (45, 5), (46, 5), (47, 6), (48, 7), (49, 8), (50, 9), (51, 10), (52, 11), (53, 12), (54, 13), (55, 13), (56, 13)], "H31", [RESTRICTING, DIVERGING])
		self.routes["HRtH13H32"] = Route(self.screen, block, "HRtH13H32", "H13", [(42, 7), (43, 7), (44, 7), (45, 7), (46, 8), (47, 9), (48, 10), (49, 11), (50, 12), (51, 13), (52, 13), (53, 13), (54, 13), (55, 13), (56, 13)], "H32", [RESTRICTING, DIVERGING])
		self.routes["HRtH13H33"] = Route(self.screen, block, "HRtH13H33", "H13", [(42, 9), (43, 9), (44, 9), (45, 10), (46, 11), (47, 12), (48, 13), (49, 13), (50, 13), (51, 13), (52, 13), (53, 13), (54, 13), (55, 13), (56, 13)], "H33", [RESTRICTING, DIVERGING])
		self.routes["HRtH13H34"] = Route(self.screen, block, "HRtH13H34", "H13", [(42, 11), (43, 11), (44, 12), (45, 13), (46, 13), (47, 13), (48, 13), (49, 13), (50, 13), (51, 13), (52, 13), (53, 13), (54, 13), (55, 13), (56, 13)], "H34", [RESTRICTING, DIVERGING])
		self.routes["HRtH12H13"] = Route(self.screen, block, "HRtH12H13", "H13", [(42, 13), (43, 13), (44, 13), (45, 13), (46, 13), (47, 13), (48, 13), (49, 13), (50, 13), (51, 13), (52, 13), (53, 13), (54, 13), (55, 13), (56, 13)], "H12", [RESTRICTING, MAIN])

		block = self.blocks["OSHEE"]
		self.routes["HRtH22H23"] = Route(self.screen, block, "HRtH22H23", "H22", [(42, 15), (43, 15), (44, 15), (45, 15), (46, 15), (47, 15), (48, 15), (49, 15), (50, 15), (51, 15), (52, 15), (53, 15), (54, 15), (55, 15), (56, 15)], "H23", [RESTRICTING, RESTRICTING])
		self.routes["HRtH23H40"] = Route(self.screen, block, "HRtH23H40", "H40", [(42, 23), (43, 23), (44, 23), (45, 23), (46, 22), (47, 21), (48, 20), (49, 19), (50, 18), (51, 17), (52, 16), (53, 15), (54, 15), (55, 15), (56, 15)], "H23", [RESTRICTING, RESTRICTING])
		self.routes["HRtH23H43"] = Route(self.screen, block, "HRtH23H43", "H43", [(42, 17), (43, 17), (44, 17), (45, 17), (46, 17), (47, 17), (48, 17), (49, 16), (50, 15), (51, 15), (52, 15), (53, 15), (54, 15), (55, 15), (56, 15)], "H23", [RESTRICTING, RESTRICTING])
		self.routes["HRtH23H42"] = Route(self.screen, block, "HRtH23H42", "H42", [(42, 19), (43, 19), (44, 19), (45, 19), (46, 19), (47, 18), (48, 17), (49, 16), (50, 15), (51, 15), (52, 15), (53, 15), (54, 15), (55, 15), (56, 15)], "H23", [RESTRICTING, RESTRICTING])
		self.routes["HRtH23H41"] = Route(self.screen, block, "HRtH23H41", "H41", [(42, 21), (43, 21), (44, 21), (45, 20), (46, 19), (47, 18), (48, 17), (49, 16), (50, 15), (51, 15), (52, 15), (53, 15), (54, 15), (55, 15), (56, 15)], "H23", [RESTRICTING, RESTRICTING])

		self.signals["H4LA"].AddPossibleRoutes("OSHWE", [ "HRtH21H22" ])
		self.signals["H4LB"].AddPossibleRoutes("OSHWE", [ "HRtH21H43" ])
		self.signals["H4LC"].AddPossibleRoutes("OSHWE", [ "HRtH21H42" ])
		self.signals["H4LD"].AddPossibleRoutes("OSHWE", [ "HRtH21H41" ])
		self.signals["H4R"].AddPossibleRoutes("OSHWE",  [ "HRtH21H41", "HRtH21H42", "HRtH21H43", "HRtH21H22" ])

		self.signals["H6LA"].AddPossibleRoutes("OSHWW", [ "HRtH11H32" ])
		self.signals["H6LB"].AddPossibleRoutes("OSHWW", [ "HRtH11H33" ])
		self.signals["H6LC"].AddPossibleRoutes("OSHWW", [ "HRtH11H34" ])
		self.signals["H6LD"].AddPossibleRoutes("OSHWW", [ "HRtH11H12" ])
		self.signals["H6R"].AddPossibleRoutes("OSHWW",  [ "HRtH11H31", "HRtH11H32", "HRtH11H33", "HRtH11H34", "HRtH11H12" ])

		self.signals["H8L"].AddPossibleRoutes("OSHWW",  [ "HRtH11H31" ])
		self.signals["H8L"].AddPossibleRoutes("OSHWW2", [ "HRtH30H31" ])
		self.signals["H8R"].AddPossibleRoutes("OSHWW2", [ "HRtH30H31" ])

		self.signals["H10L"].AddPossibleRoutes("OSHEE",  [ "HRtH22H23", "HRtH23H40", "HRtH23H41", "HRtH23H42", "HRtH23H43" ])
		self.signals["H10RA"].AddPossibleRoutes("OSHEE", [ "HRtH22H23" ])
		self.signals["H10RB"].AddPossibleRoutes("OSHEE", [ "HRtH23H43" ])
		self.signals["H10RC"].AddPossibleRoutes("OSHEE", [ "HRtH23H42" ])
		self.signals["H10RD"].AddPossibleRoutes("OSHEE", [ "HRtH23H41" ])
		self.signals["H10RE"].AddPossibleRoutes("OSHEE", [ "HRtH23H40" ])

		self.signals["H12L"].AddPossibleRoutes("OSHEW",  [ "HRtH13H31", "HRtH13H32", "HRtH13H33", "HRtH13H34", "HRtH12H13" ])
		self.signals["H12RA"].AddPossibleRoutes("OSHEW", [ "HRtH13H31" ])
		self.signals["H12RB"].AddPossibleRoutes("OSHEW", [ "HRtH13H32" ])
		self.signals["H12RC"].AddPossibleRoutes("OSHEW", [ "HRtH13H33" ])
		self.signals["H12RD"].AddPossibleRoutes("OSHEW", [ "HRtH13H34" ])
		self.signals["H12RE"].AddPossibleRoutes("OSHEW", [ "HRtH12H13" ])

		self.osSignals = {}
		self.osSignals["OSHWW"] = [ "H8L", "H6LA", "H6LB", "H6LC", "H6LD", "H6R" ]
		self.osSignals["OSHWW2"] = [ "H8L", "H8R" ]
		self.osSignals["OSHWE"] = [ "H4LA", "H4LB", "H4LC", "H4LD", "H4R" ]
		self.osSignals["OSHEW"] = [ "H12L", "H12RA", "H12RB", "H12RC", "H12RD", "H12RE" ]
		self.osSignals["OSHEE"] = [ "H10L", "H10RA", "H10RB", "H10RC", "H10RD", "H10RE" ]
		return self.signals

	def DefineButtons(self, tiles):
		self.buttons = {}
		self.osButtons = {}

		b = Button(self, self.screen, self.frame, "HWWB1", (27, 5), tiles)
		self.buttons["HWWB1"] = b

		b = Button(self, self.screen, self.frame, "HWWB2", (32, 5), tiles)
		self.buttons["HWWB2"] = b

		b = Button(self, self.screen, self.frame, "HWWB3", (32, 7), tiles)
		self.buttons["HWWB3"] = b

		b = Button(self, self.screen, self.frame, "HWWB4", (32, 9), tiles)
		self.buttons["HWWB4"] = b

		b = Button(self, self.screen, self.frame, "HWWB5", (32, 11), tiles)
		self.buttons["HWWB5"] = b

		b = Button(self, self.screen, self.frame, "HWWB6", (32, 13), tiles)
		self.buttons["HWWB6"] = b

		self.osButtons["OSHWW"] = [ "HWWB2", "HWWB3", "HWWB4", "HWWB5", "HWWB6" ]
		self.osButtons["OSHWW2"] = [ "HWWB1" ]

		b = Button(self, self.screen, self.frame, "HWEB1", (32, 15), tiles)
		self.buttons["HWEB1"] = b

		b = Button(self, self.screen, self.frame, "HWEB2", (32, 17), tiles)
		self.buttons["HWEB2"] = b

		b = Button(self, self.screen, self.frame, "HWEB3", (32, 19), tiles)
		self.buttons["HWEB3"] = b

		b = Button(self, self.screen, self.frame, "HWEB4", (32, 21), tiles)
		self.buttons["HWEB4"] = b

		self.osButtons["OSHWE"] = [ "HWEB1", "HWEB2", "HWEB3", "HWEB4" ]

		b = Button(self, self.screen, self.frame, "HEWB1", (41, 5), tiles)
		self.buttons["HEWB1"] = b

		b = Button(self, self.screen, self.frame, "HEWB2", (41, 7), tiles)
		self.buttons["HEWB2"] = b

		b = Button(self, self.screen, self.frame, "HEWB3", (41, 9), tiles)
		self.buttons["HEWB3"] = b

		b = Button(self, self.screen, self.frame, "HEWB4", (41, 11), tiles)
		self.buttons["HEWB4"] = b

		b = Button(self, self.screen, self.frame, "HEWB5", (41, 13), tiles)
		self.buttons["HEWB5"] = b

		self.osButtons["OSHEW"] = [ "HEWB1", "HEWB2", "HEWB3", "HEWB4", "HEWB5" ]

		b = Button(self, self.screen, self.frame, "HEEB1", (41, 15), tiles)
		self.buttons["HEEB1"] = b

		b = Button(self, self.screen, self.frame, "HEEB2", (41, 17), tiles)
		self.buttons["HEEB2"] = b

		b = Button(self, self.screen, self.frame, "HEEB3", (41, 19), tiles)
		self.buttons["HEEB3"] = b

		b = Button(self, self.screen, self.frame, "HEEB4", (41, 21), tiles)
		self.buttons["HEEB4"] = b

		b = Button(self, self.screen, self.frame, "HEEB5", (41, 23), tiles)
		self.buttons["HEEB5"] = b

		self.osButtons["OSHEE"] = [ "HEEB1", "HEEB2", "HEEB3", "HEEB4", "HEEB5" ]

		return self.buttons
import os

from bitmaps import BitMaps
from constants import EMPTY, OCCUPIED, CLEARED, NORMAL, REVERSE, RED, GREEN, STOP

class Tile:
	def __init__(self, name, bmps):
		self.name = name
		self.bmps = bmps

	def getBmp(self, status, east, revflag):
		if status == OCCUPIED:
			if east:
				k = "red-left" if revflag else "red-right"
			else:
				k = "red-right" if revflag else "red-left"
			try:
				bmp = self.bmps[k]
			except KeyError:
				bmp = self.bmps["red"]
			return bmp

		if status == CLEARED:
			if east:
				k = "green-left" if revflag else "green-right"
			else:
				k = "green-right" if revflag else "green-left"
			try:
				bmp = self.bmps[k]
			except KeyError:
				bmp = self.bmps["green"]
			return bmp

		return self.bmps["white"]

class GenericTile:
	def __init__(self, name, bmps):
		self.name = name
		self.bmps = bmps

	def getBmp(self, status, tag):
		prefix = ""
		if status == OCCUPIED:
			prefix = "red-"
		elif status == CLEARED:
			prefix = "green-"
		else:
			prefix = "white-"

		try:
			bmp = self.bmps[prefix+tag]
		except:
			bmp = self.bmps[tag]
		return bmp


class TurnoutTile:
	def __init__(self, name, nbmps, rbmps):
		self.name = name
		self.nbmps = nbmps
		self.rbmps = rbmps

	def getBmp(self, tostat, blkstat, east):
		if tostat == NORMAL:
			bmps = self.nbmps
		else:
			bmps = self.rbmps

		if blkstat == OCCUPIED:
			return bmps["red"]

		if blkstat == CLEARED:
			return bmps["green"]

		return bmps["white"]

class SlipSwitchTile:
	def __init__(self, name, nnbmps, nrbmps, rnbmps, rrbmps):
		self.name = name
		self.nnbmps = nnbmps
		self.nrbmps = nrbmps
		self.rnbmps = rnbmps
		self.rrbmps = rrbmps


	def getBmp(self, tostat, blkstat):
		if tostat == [NORMAL, NORMAL]:
			bmps = self.nnbmps
		elif tostat == [NORMAL, REVERSE]:
			bmps = self.nrbmps
		elif tostat == [REVERSE, NORMAL]:
			bmps = self.rnbmps
		else: # tostat == [REVERSE, REVERSE]
			bmps = self.rrbmps

		if blkstat == OCCUPIED:
			return bmps["red"]

		if blkstat == CLEARED:
			return bmps["green"]

		return bmps["white"]


class SignalTile:
	def __init__(self, name, bmps):
		self.name = name
		self.bmps = bmps

	def getBmp(self, sig):
		if sig.aspect == STOP:
			return self.bmps["red"]
		elif sig.aspect == GREEN:
			return self.bmps["green"]
		else:
			return self.bmps["green"]


def loadTiles(bitmaps):
	b = bitmaps.track

	tiles = {}
	tiles["horiz"] = Tile("horiz", {
		"white": b.straight.normal,
		"green": b.straight.routed,
		"green-right": b.straight.rightrouted,
		"green-left": b.straight.leftrouted,
		"red-right": b.straight.rightoccupied,
		"red-left": b.straight.leftoccupied,
		"red": b.straight.occupied})
	tiles["horiznc"] = Tile("horiz", {
		"white": b.straight.normal,
		"green": b.straight.routed,
		"red": b.straight.occupied})
	tiles["houtline"] = Tile("houtline", {
		"white": b.straightoutline.normal,
		"green": b.straightoutline.routed,
		"red": b.straightoutline.occupied})
	tiles["vertical"] = Tile("vertical", {
		"white": b.vertical.normal,
		"green": b.vertical.routed,
		"green-right": b.vertical.uprouted,
		"green-left": b.vertical.downrouted,
		"red-right": b.vertical.upoccupied,
		"red-left": b.vertical.downoccupied,
		"red": b.vertical.occupied})
	tiles["verticalnc"] = Tile("vertical", {
		"white": b.vertical.normal,
		"green": b.vertical.routed,
		"red": b.vertical.occupied})
	tiles["eobleft"] = Tile("eobleft", {
		"white": b.eobleft.normal,
		"green": b.eobleft.routed,
		"red": b.eobleft.occupied})
	tiles["eobright"] = Tile("eobright", {
		"white": b.eobright.normal,
		"green": b.eobright.routed,
		"red": b.eobright.occupied})
	tiles["diagleft"] = Tile("diagleft", {
		"white": b.diagleft.normal,
		"green": b.diagleft.routed,
		"red": b.diagleft.occupied})
	tiles["diagright"] = Tile("diagright", {
		"white": b.diagright.normal,
		"green": b.diagright.routed,
		"red": b.diagright.occupied})
	tiles["turnleftright"] = Tile("turnleftright", {
		"white": b.turnleftright.normal,
		"green": b.turnleftright.routed,
		"red": b.turnleftright.occupied})
	tiles["turnleftleft"] = Tile("turnleftleft", {
		"white": b.turnleftleft.normal,
		"green": b.turnleftleft.routed,
		"red": b.turnleftleft.occupied})
	tiles["turnrightleft"] = Tile("turnrightleft", {
		"white": b.turnrightleft.normal,
		"green": b.turnrightleft.routed,
		"red": b.turnrightleft.occupied})
	tiles["turnrightright"] = Tile("turnrightright", {
		"white": b.turnrightright.normal,
		"green": b.turnrightright.routed,
		"red": b.turnrightright.occupied})

	tiles["turnrightup"] = Tile("turnrightup", {
		"white": b.turnrightup.normal,
		"green": b.turnrightup.routed,
		"red": b.turnrightright.occupied})

	tiles["turnleftdown"] = Tile("turnleftdown", {
		"white": b.turnleftdown.normal,
		"green": b.turnleftdown.routed,
		"red": b.turnleftdown.occupied})

	turnouts = {}
	turnouts["torightleft"] = TurnoutTile("torightleft", 
		{
			"white": b.torightleft.normal.normal,
			"green": b.torightleft.normal.routed,
			"red": b.torightleft.normal.occupied
		},
		{
			"white": b.torightleft.reversed.normal,
			"green": b.torightleft.reversed.routed,
			"red": b.torightleft.reversed.occupied
		}
	)

	turnouts["torightright"] = TurnoutTile("torightright", 
		{
			"white": b.torightright.normal.normal,
			"green": b.torightright.normal.routed,
			"red": b.torightright.normal.occupied
		},
		{
			"white": b.torightright.reversed.normal,
			"green": b.torightright.reversed.routed,
			"red": b.torightright.reversed.occupied
		}
	)

	turnouts["torightup"] = TurnoutTile("torightup", 
		{
			"white": b.torightup.normal.normal,
			"green": b.torightup.normal.routed,
			"red": b.torightup.normal.occupied
		},
		{
			"white": b.torightup.reversed.normal,
			"green": b.torightup.reversed.routed,
			"red": b.torightup.reversed.occupied
		}
	)

	turnouts["toleftup"] = TurnoutTile("toleftup", 
		{
			"white": b.toleftup.normal.normal,
			"green": b.toleftup.normal.routed,
			"red": b.toleftup.normal.occupied
		},
		{
			"white": b.toleftup.reversed.normal,
			"green": b.toleftup.reversed.routed,
			"red": b.toleftup.reversed.occupied
		}
	)

	turnouts["toleftupinv"] = TurnoutTile("toleftup", 
		{
			"white": b.toleftup.reversed.normal,
			"green": b.toleftup.reversed.routed,
			"red": b.toleftup.reversed.occupied
		},
		{
			"white": b.toleftup.normal.normal,
			"green": b.toleftup.normal.routed,
			"red": b.toleftup.normal.occupied
		}
	)

	turnouts["torightupinv"] = TurnoutTile("torightup", 
		{
			"white": b.torightup.reversed.normal,
			"green": b.torightup.reversed.routed,
			"red": b.torightup.reversed.occupied
		},
		{
			"white": b.torightup.normal.normal,
			"green": b.torightup.normal.routed,
			"red": b.torightup.normal.occupied
		}
	)

	turnouts["torightdown"] = TurnoutTile("torightdown", 
		{
			"white": b.torightdown.normal.normal,
			"green": b.torightdown.normal.routed,
			"red": b.torightdown.normal.occupied
		},
		{
			"white": b.torightdown.reversed.normal,
			"green": b.torightdown.reversed.routed,
			"red": b.torightdown.reversed.occupied
		}
	)

	turnouts["toleftleft"] = TurnoutTile("toleftleft", 
		{
			"white": b.toleftleft.normal.normal,
			"green": b.toleftleft.normal.routed,
			"red": b.toleftleft.normal.occupied
		},
		{
			"white": b.toleftleft.reversed.normal,
			"green": b.toleftleft.reversed.routed,
			"red": b.toleftleft.reversed.occupied
		}
	)

	turnouts["toleftleftinv"] = TurnoutTile("toleftleftinv", 
		{
			"white": b.toleftleft.reversed.normal,
			"green": b.toleftleft.reversed.routed,
			"red": b.toleftleft.reversed.occupied
		},
		{
			"white": b.toleftleft.normal.normal,
			"green": b.toleftleft.normal.routed,
			"red": b.toleftleft.normal.occupied
		}
	)
	
	turnouts["toleftright"] = TurnoutTile("toleftright", 
		{
			"white": b.toleftright.normal.normal,
			"green": b.toleftright.normal.routed,
			"red": b.toleftright.normal.occupied
		},
		{
			"white": b.toleftright.reversed.normal,
			"green": b.toleftright.reversed.routed,
			"red": b.toleftright.reversed.occupied
		}
	)
	
	turnouts["toleftdown"] = TurnoutTile("toleftdown", 
		{
			"white": b.toleftdown.normal.normal,
			"green": b.toleftdown.normal.routed,
			"red": b.toleftdown.normal.occupied
		},
		{
			"white": b.toleftdown.reversed.normal,
			"green": b.toleftdown.reversed.routed,
			"red": b.toleftdown.reversed.occupied
		}
	)
	
	turnouts["toleftdowninv"] = TurnoutTile("toleftdowninv", 
		{
			"white": b.toleftdown.reversed.normal,
			"green": b.toleftdown.reversed.routed,
			"red": b.toleftdown.reversed.occupied
		},
		{
			"white": b.toleftdown.normal.normal,
			"green": b.toleftdown.normal.routed,
			"red": b.toleftdown.normal.occupied
		}
	)

	slipswitches = {}
	turnouts["ssleft"] = SlipSwitchTile("ssleft",
		{ # NN
			"white": b.slipleft.nn.normal,
			"green": b.slipleft.nn.routed,
			"red":   b.slipleft.nn.occupied
		},
		{ # NR
			"white": b.slipleft.nr.normal,
			"green": b.slipleft.nr.routed,
			"red":   b.slipleft.nr.occupied
		},
		{ # RN
			"white": b.slipleft.rn.normal,
			"green": b.slipleft.rn.routed,
			"red":   b.slipleft.rn.occupied
		},
		{ # RR
			"white": b.slipleft.rr.normal,
			"green": b.slipleft.rr.routed,
			"red":   b.slipleft.rr.occupied
		}

	)

	generictiles = {}
	generictiles["crossing"] = GenericTile("crossing",
		{
			"white-diagright": b.diagright.normal,
			"green-diagright": b.diagright.routed,
			"red-diagright": b.diagright.occupied,
			"white-diagleft": b.diagleft.normal,
			"green-diagleft": b.diagleft.routed,
			"red-diagleft": b.diagleft.occupied,
			"cross": b.cross
		})
	b = bitmaps.signals
	signals = {}
	signals["left"] = SignalTile("C11", 
		{
			"green": b.left.green,
			"red": b.left.red
		})
	signals["right"] = SignalTile("C12", 
		{
			"green": b.right.green,
			"red": b.right.red
		})

	return tiles, turnouts, slipswitches, signals, generictiles

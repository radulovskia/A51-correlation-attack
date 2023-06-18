class LFSR:
	
	def __init__(self,i,length,clockingBit,tappedBits): 
		self.i,self.length,self.register,self.clockingBit,self.tappedBits = i,length,[0]*length,clockingBit,tappedBits
	
	def _getID(self):	  					return self.i
	def _getRegister(self): 				return self.register
	def _getBit(self,i):				    return self.register[i]
	def _getLength(self): 					return self.length
	def _getClockingBit(self): 				return self.register[self.clockingBit]
	def _getTappedBits(self):  				return self.tappedBits
	
	def _setID(self,i):	  					self.i = i
	def _setLength(self,length): 			self.length = length
	def _setRegister(self,register):        self.register = register
	def _setClockingBit(self,clockingBit): 	self.clockingBit = clockingBit
	def _setTappedBits(self,tappedBits):  	self.tappedBits = tappedBits

	def __str__(self) -> str:
		return f"Register ID: {self.i}\nRegister: {self.register}\n"

class A51:
	def _get_session_key(self):
		return self.session_key
	
	def _get_keystream(self):
		return self.keystream

	def __init__(self, session_key):
		# largest index (ms tapped bit) first
		x = LFSR(1,19,8,[18,17,16,13])
		y = LFSR(2,22,10,[21,20])
		z = LFSR(3,23,10,[22,21,20,7])
		self.lfsrX, self.lfsrY, self.lfsrZ, self.session_key, self.keystream = x, y, z, session_key, ""

	# def clock_SK(self):
		if len(self.session_key) != 64:
			raise Exception("Session key must have length = 64")
		for bit in list(self.session_key):
			# lfsrX
			nMsb = bit
			for i in range(len(self.lfsrX.tappedBits)):
				nMsb = nMsb ^ self.lfsrX.register[self.lfsrX.tappedBits[i]]
			self.lfsrX._setRegister([nMsb]+self.lfsrX._getRegister()[0:self.lfsrX._getLength()-1])
			# lfsrY
			nMsb = bit
			for i in range(len(self.lfsrY.tappedBits)):
				nMsb = nMsb ^ self.lfsrY.register[self.lfsrY.tappedBits[i]]
			self.lfsrY._setRegister([nMsb]+self.lfsrY._getRegister()[0:self.lfsrY._getLength()-1])
			# lfsrZ
			nMsb = bit
			for i in range(len(self.lfsrZ.tappedBits)):
				nMsb = nMsb ^ self.lfsrZ.register[self.lfsrZ.tappedBits[i]]
			self.lfsrZ._setRegister([nMsb]+self.lfsrZ._getRegister()[0:self.lfsrZ._getLength()-1])

	# initial state is here
	# def clock_100(self):
		for j in range(100):
			clockingBits = [self.lfsrX._getClockingBit(), self.lfsrY._getClockingBit(), self.lfsrZ._getClockingBit()]
			oneCount, zeroCount = clockingBits.count('1'), clockingBits.count(0)
			majorityBit  = 1 if max(oneCount, zeroCount) == oneCount else 0
			# lfsrX #
			if self.lfsrX._getClockingBit() == majorityBit:
				nMsb = self.lfsrX.register[self.lfsrX.tappedBits[0]]
				for i in range(1, len(self.lfsrX.tappedBits)):
					nMsb = nMsb ^ self.lfsrX.register[self.lfsrX.tappedBits[i]]
				self.lfsrX._setRegister([nMsb]+self.lfsrX._getRegister()[0:self.lfsrX._getLength()-1])
			# lfsrY #
			if self.lfsrY._getClockingBit() == majorityBit:
				nMsb = self.lfsrY.register[self.lfsrY.tappedBits[0]]
				for i in range(1, len(self.lfsrY.tappedBits)):
					nMsb = nMsb ^ self.lfsrY.register[self.lfsrY.tappedBits[i]]
				self.lfsrY._setRegister([nMsb]+self.lfsrY._getRegister()[0:self.lfsrY._getLength()-1])
			# lfsrZ #
			if self.lfsrZ._getClockingBit() == majorityBit:
				nMsb = self.lfsrZ.register[self.lfsrZ.tappedBits[0]]
				for i in range(1, len(self.lfsrZ.tappedBits)):
					nMsb = nMsb ^ self.lfsrZ.register[self.lfsrZ.tappedBits[i]]
				self.lfsrZ._setRegister([nMsb]+self.lfsrZ._getRegister()[0:self.lfsrZ._getLength()-1])
	# warm-up phase is here
	# originally 228 bits of keystream are generated
	def generate_keystream(self, x):		
		self.keystream = []
		for j in range(x):
			clockingBits = [self.lfsrX._getClockingBit(), self.lfsrY._getClockingBit(), self.lfsrZ._getClockingBit()]
			oneCount,zeroCount = clockingBits.count('1'),clockingBits.count(0)
			majorityBit  = 1 if max(oneCount,zeroCount)==oneCount else 0
			# lfsrX #
			if self.lfsrX._getClockingBit() == majorityBit:
				nMsb = self.lfsrX.register[self.lfsrX.tappedBits[0]]
				for i in range(1, len(self.lfsrX.tappedBits)):
					nMsb = nMsb ^ self.lfsrX.register[self.lfsrX.tappedBits[i]]
				self.lfsrX._setRegister([nMsb]+self.lfsrX._getRegister()[0:self.lfsrX._getLength()-1])	
			# lfsrY #
			if self.lfsrY._getClockingBit() == majorityBit:
				nMsb = self.lfsrY.register[self.lfsrY.tappedBits[0]]
				for i in range(1, len(self.lfsrY.tappedBits)):
					nMsb = nMsb ^ self.lfsrY.register[self.lfsrY.tappedBits[i]]
				self.lfsrY._setRegister([nMsb]+self.lfsrY._getRegister()[0:self.lfsrY._getLength()-1])
			# lfsrZ #
			if self.lfsrZ._getClockingBit() == majorityBit:
				nMsb = self.lfsrZ.register[self.lfsrZ.tappedBits[0]]
				for i in range(1, len(self.lfsrZ.tappedBits)):
					nMsb = nMsb ^ self.lfsrZ.register[self.lfsrZ.tappedBits[i]]
				self.lfsrZ._setRegister([nMsb]+self.lfsrZ._getRegister()[0:self.lfsrZ._getLength()-1])
			self.keystream.append(self.lfsrX._getBit(self.lfsrX._getLength()-1) ^ self.lfsrY._getBit(self.lfsrY._getLength()-1) ^ self.lfsrZ._getBit(self.lfsrZ._getLength()-1))
		return self.keystream

	def encrypt(self, plainText):
		# self.clock_SK()
		# self.clock_100()
		self.generate_keystream(len(plainText))
		res = []
		for i in range(len(plainText)):
			res.append(self.keystream[i] ^ plainText[i])
		return res
	
	def decrypt(self, cipherText):
		res = []
		for i in range(len(cipherText)):
			res.append(self.keystream[i] ^ cipherText[i])
		return res
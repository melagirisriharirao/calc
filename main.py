import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
import math
import decimal


class calculator(Widget):	
	labtext = ObjectProperty(None) # This is the object that returns the text value of label
	sinlab = ObjectProperty(None)  
	coslab = ObjectProperty(None)
	tanlab = ObjectProperty(None)
	anglelab = ObjectProperty(None)
	dellab = ObjectProperty(None)

	def __init__(self,**kwargs):
		super(calculator,self).__init__(**kwargs)
		Window.bind(on_keyboard=self.Android_back_click)

	def Android_back_click(self,window,key,*largs):
		if key == 27:
			App.get_running_app().stop()
	
	def _doit(self, bp):
		
		if bp == "=":
			self.dellab.text = "CLR"
			val = self.labtext.text
			val = val.split()
			try:
				l = len(val)
				for i in val:
					if i == "pi":
						y = val.index("pi")
						if y != 0:											
							if val[y-1] in ("0","1","2","3","4","5","6","7","8","9"):
								val[y-1] = val[y-1] + "*" + str(math.pi)
								res = eval(val[y-1])
								val[y-1] = str(res)
								del val[y]
							else:
								res = str(math.pi)
								val[y] = res
						else:
							res = str(math.pi)
							val[y] = res
					if i == "!":
						y = val.index("!")
						res = val[y-1]
						res = str(math.factorial(int(res)))
						val[y-1] = res
						del val[y]
					if i == "(":
						y = val.index("(")
						if val[y-1] in ("sin","cos","tan","sqrt"):
							del val[y]
						else:
							val[y] = val[y]
					if i == ")":
						y = val.index(")")
						if val[y-2] in ("sin","cos","tan","sqrt"):
							del val[y]
						else:
							val[y] = val[y]
					print(val)

				for i in val:
					if i == ")":
						y = val.index(")")
						if val[y-2] == "sqrt":
							del val[y]

				for i in val:
					print(val)
					if i == "(":
						y = val.index("(")
						if val[y-1] in ("sin","cos","tan","sqrt"):
							del val[y]
						else:
							val[y] = val[y]
					if i == ")":
						y = val.index(")")
						if val[y-2] in ("sin","cos","tan","sqrt"):
							del val[y]
						else:
							val[y] = val[y]
					if i == "sin":
						y = val.index("sin")
						res = val[y] + val[y+1]
						if val[y-1] not in ("+","-","*","/"):
							val[y-1] = val[y-1] + "*"
						if self.anglelab.text == "RAD":
							res = str(round((math.sin(float(res[3:]))),2))
						else:
							res = str(math.sin(math.radians((float(res[3:])))))
						val[y] = res
						del val[y+1]
					if i == "cos":
						y = val.index("cos")
						res = val[y] + val[y+1]
						if val[y-1] not in ("+","-","*","/"):
							val[y-1] += "*"
						if self.anglelab.text == "RAD":
							res = str(round(math.cos(float(res[3:])),2))
						else:
							res = str(math.cos(math.radians((float(res[3:])))))
						val[y] = res
						del val[y+1]
					if i == "tan":
						y = val.index("tan")
						res = val[y] + val[y+1]
						if val[y-1] not in ("+","-","*","/"):
							val[y-1] = val[y-1] + "*"
						if self.anglelab.text == "RAD":
							res = str(round(math.tan(float(res[3:])),2))
						else:
							res = str(math.tan(math.radians((float(res[3:])))))
						val[y] = res
						del val[y+1]	
					if i == "!":
						y = val.index("!")
						res = val[y-1]
						res = str(math.factorial(int(res)))
						val[y-1] = res
						del val[y]	
					if i == "e^":
						y = val.index("e^")
						res = val[y+1]
						if val[y-1] not in ("+","-","*","/"):
							val[y-1] = val[y-1] + "*"
						res = str(math.pow(math.e, float(res)))
						val[y] = res
						del val[y+1]
					if i == "arcsin":
						y = val.index("arcsin")
						res = val[y] + val[y+1]
						if val[y-1] not in ("+","-","*","/"):
							val[y-1] = val[y-1] + "*"
						if self.anglelab.text == "RAD":
							res = str(math.asin(float(res[6:])))
						else:
							res = str(math.degrees(math.asin((float(res[6:])))))
						val[y] = res
						del val[y+1]
					if i == "arccos":
						y = val.index("arccos")
						res = val[y] + val[y+1]
						if val[y-1] not in ("+","-","*","/"):
							val[y-1] = val[y-1] + "*"
						if self.anglelab.text == "RAD":
							res = str(math.acos(float(res[6:])))
						else:
							res = str(math.degrees(math.acos(float(res[6:]))))
						val[y] = res
						del val[y+1]
					if i == "arctan":
						y = val.index("arctan")
						res = val[y] + val[y+1]
						if val[y-1] not in ("+","-","*","/"):
							val[y-1] = val[y-1] + "*"
						if self.anglelab.text == "RAD":
							res = str(math.atan(float(res[6:])))
						else:
							res = str(math.degrees(math.atan(float(res[6:]))))
						val[y] = res
						del val[y+1]
					if i == "sqrt":
						y = val.index("sqrt")
						res = val[y+1]
						res = str(math.sqrt(float(res)))
						val[y] = res
						del val[y+1]
					if i == "log":
						y = val.index("log")
						res = val[y+1]
						if val[y-1] not in ("+","-","*","/"):
							val[y-1] = val[y-1] + "*"
						res = str(math.log((float(res)), 10))
						val[y] = res
						del val[y+1]
					if i == "ln":
						y = val.index("ln")
						res = val[y+1]
						if val[y-1] not in ("+","-","*","/"):
							val[y-1] = val[y-1] + "*"
						res = str(math.log((float(res)), math.e))
						val[y] = res
						del val[y+1]
					if i == "^":
						y = val.index("^")
						resone = val[y-1]
						restwo = val[y+1]
						res = str(math.pow(float(resone),(float(restwo))))
						val[y] = res
						del val[y-1]
						del val[y]
						
				val = ''.join(val)
				val = str(eval(val))
			
				if len(val)>24:
					val = '%.2E' % decimal.Decimal(val)
					self.labtext.text = val
				else:
					self.labtext.text = val
			except:
				self.labtext.text = "math ERROR"
		else:
			self.labtext.text += bp				

	def _changelab(self, bp):
		if bp == "INV":
			if self.sinlab.text == " sin ":				
				self.sinlab.text = " arcsin "
				self.coslab.text = " arccos "
				self.tanlab.text = " arctan "
			else:
				self.sinlab.text = " sin "
				self.coslab.text = " cos "
				self.tanlab.text = " tan "
		if bp == "RAD":
			self.anglelab.text = "DEG"
			if bp == "DEG":
				self.anglelab.text = "RAD"
		if bp == "DEG":
			self.anglelab.text = "RAD"
			if bp == "RAD":
				self.anglelab.text = "DEG"
		if bp == "DEL":
			if len(self.labtext.text)>=1:					
				val = self.labtext.text
				val = val.split()
				del val[-1]
				val = ' '.join(val)
				self.labtext.text = val + " "
			else:
				self.labtext.text = self.labtext.text
		if bp == "CLR":
			self.labtext.text = ""
			self.dellab.text = "DEL"

class calcApp(App):
	def build(self):
		self.calc = calculator()
		return self.calc
		
	def on_pause(self):
		return True
	def on_resume(self):
		pass
	
if __name__ == "__main__":
	calcApp().run()
	

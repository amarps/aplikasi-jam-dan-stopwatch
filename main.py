from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

from time import strftime

Window.clearcolor = get_color_from_hex('##101216')

class WidgetJam(App):
	sw_started = False
	sw_seconds = 0

	def update(self, nap):
		if self.sw_started:
			self.sw_seconds += nap

		self.root.ids.bagong.text = strftime('[b]%H[/b]:%M:%S')

		m, s = divmod(self.sw_seconds, 60)
		self.root.ids.stopwatch.text = ('%02d:%02d.[size=20]%02d[/size]' % 
										(int (m), int(s), int(s * 100 % 100)))

	def on_start(self):
		Clock.schedule_interval(self.update, 0)

	def start_stop(self):
		self.root.ids.start_stop.text = 'Start' if self.sw_started else 'Stop'
		self.sw_started = not self.sw_started

	def reset(self):
		if self.sw_started:
			self.root.ids.start_stop.text = 'Start'
			self.sw_started = False

		self.sw_seconds = 0

LabelBase.register(name="Eczar",
	fn_regular="Eczar-Regular.ttf",
	fn_bold="Eczar-Bold.ttf",
	fn_italic="Eczar-Medium.ttf",
	fn_bolditalic="Eczar-ExtraBold.ttf")

if __name__ == '__main__':
	WidgetJam().run()
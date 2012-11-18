#! usr/bin/env python

"""
Tracks steep and cheap and launches window on discovering a deal that you are interested in. 
@author: Subhodeep Moitra(smoitra@cs.cmu.edu)
@license : BSD

"""

from Tkinter import Label, Tk
import os,time
import urllib2


# constants
POLL_PERIOD=30 # hit site every 30s
kwdlist = ["alpine","gloves","mountaineering","climbing",\
"sleeping bag","bivy","hardshell","trail running","houdini"];

class MsgWindow() :
	""" Displays information in a dialog window """ 
	def __init__(self,_text) : 
		root = Tk()
		root.title("Steep Hound alert")
		label = Label(root,text=_text)
		label.pack(ipadx=5,ipady=5,padx=5,pady=5)
		root.after(5000,root.destroy)
		root.mainloop()

def find_title(html) :
	""" Finds the title from the page """ 
	search_str1 = '<h2 id="product_title">'
	search_str2 = '</h2>'
	pos1= html.find(search_str1)
	pos2 = html.find(search_str2,pos1)
	return html[pos1+len(search_str1):pos2]


if __name__ == '__main__' : 
	title = title_old = None
	while True : 
		response = urllib2.urlopen('http://steepandcheap.com')
		html = response.read().lower()
		# Check freshness condition
		title = find_title(html)
		print "Title is:", title
		if title != title_old : 
			match = [w for w in kwdlist if w in html]
			if len(match) > 0 : 
				msg = MsgWindow("Found: "+",".join(match)+"\n"+title)			
			title_old = title
		time.sleep(POLL_PERIOD)
	


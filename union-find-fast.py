import argparse
from sys import stdin
import pygame as pg

width,height = 1200,800
screen = pg.display.set_mode((width,height))
clock = pg.time.Clock()



	


class UF:
	def __init__(self,n):
		self.n=n
		self.cost=0
		self.ol_cost = []
		self.ol_tot=[]
		self.it=0
		self.total=0
		self.count = n
		self.id = list(range(n))

	def find(self,p):
		while p != self.id[p]:
			self.cost += 1
			p = self.id[p]
		return p

	def union(self,p,q):
		pRoot= self.find(p)
		qRoot = self.find(q)

		if qRoot != pRoot:
			self.id[pRoot] = qRoot
			self.count-=1

	def is_connected(self,p,q):
		if self.find(p) == self.find(q):
			return True
		return False


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='SMTH')
	parser.add_argument('--verbose','-v',action='count',default=0)
	
	args = parser.parse_args()
	if args.verbose == 1:
		show = True
	else:
		show = False



	n = int(input())
	uf = UF(n)
	a = 0
	def step(uf):
		uf.it +=1
		line = input()
		p,q = map(int,line.split())
		if uf.is_connected(p,q):
			#print(p,q)
			pass
			
		else:
			uf.union(p,q)
		if show:
			print(p,q,uf.id)
		else:
			print(p,q)
		uf.total+=uf.cost
		uf.ol_cost.append(uf.cost)
		uf.ol_tot.append(uf.total/uf.it)
		uf.cost=0
	while True:
		a+=1
		try:
			step(uf)
		except:
			pass
		o = 0
		if max(uf.ol_cost)!=0:
			h = height/max(uf.ol_cost)
		else:
			h=1
		#print(max(uf.ol_cost),height,uf.ol_cost)
		for cost in uf.ol_cost:
			o+=width/uf.n
			pg.draw.polygon(screen,(255,0,0),((o,cost*h),(o,cost*h+2),(o+2,h*cost+2),(o+2,h*cost)))
		o=0
		for tot_cost in uf.ol_tot:
			o+=width/uf.n
			pg.draw.polygon(screen,(0,255,0),((o,height-tot_cost),(o,height-tot_cost+2),(o+2,height-tot_cost+2),(o+2,height-tot_cost)))
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
		
			pg.display.flip()
			screen.fill((0,0,0))

	print(uf.count,uf.cost,uf.total)

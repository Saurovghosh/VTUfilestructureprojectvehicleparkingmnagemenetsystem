def pos(v,t,m):
	if m=="TwoWheeler":
		a=open("twowheel.txt")
		lines = a.readlines()
		a.close()
		p=-1
		r=-1
		q=0
		for i in lines:
			q=q+1
			p=i.find(v)
			r=i.find(t)

			if p!=-1 and r!=-1:
				flag=i
				break
		if p!=-1 and r!=-1:
			del lines[q-1]
			b=open("twowheel.txt","w+")
			for line in lines:
				b.write(line)
			b.close()

	if m=="ThreeWheeler":
		a=open("threewheel.txt")
		lines = a.readlines()
		a.close()
		p=-1
		r=-1
		q=0
		for i in lines:
			q=q+1
			p=i.find(v)
			r=i.find(t)

			if p!=-1 and r!=-1:
				flag=i
				break
		if p!=-1 and r!=-1:
			del lines[q-1]
			b=open("threewheel.txt","w+")
			for line in lines:
				b.write(line)
			b.close()
			
	if m=="FourWheeler":
		a=open("fourwheel.txt")
		lines = a.readlines()
		a.close()
		p=-1
		r=-1
		q=0
		for i in lines:
			q=q+1
			p=i.find(v)
			r=i.find(t)

			if p!=-1 and r!=-1:
				flag=i
				break
		if p!=-1 and r!=-1:
			del lines[q-1]
			b=open("fourwheel.txt","w+")
			for line in lines:
				b.write(line)
			b.close()
	if m=="Others":
		a=open("other.txt")
		lines = a.readlines()
		a.close()
		p=-1
		r=-1
		q=0
		for i in lines:
			q=q+1
			p=i.find(v)
			r=i.find(t)

			if p!=-1 and r!=-1:
				flag=i
				break
		if p!=-1 and r!=-1:
			del lines[q-1]
			b=open("other.txt","w+")
			for line in lines:
				b.write(line)
			b.close()

	


		
from sys import stdin,argv;p=0;i={">":"p+=1;","<":"p-=1","+":"d[p]+=1","-":"d[p]-=1",".":"print chr(d[p]),",",":"d[p]=ord(stdin.read(1))","[":"while d[p]:","]":""};d=[0]*30000;n="";z=0;
for t in open(argv[1]).read():
	if t in i:n+=" "*z;n+=i[t]+"\n"
	if t=="[":z+=1
	elif t=="]":z-=1
exec n

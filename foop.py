
#iniconfig
import sys

class foop:
  def __init__(self):
    self.pts={}
    self.var={"foo":"foo"}
    self.ps=[]#print stack
  class Foop_Error(Exception):
    #print("oof")
    pass
  def psflush(self):
    for i in self.ps:
      print(i)
    self.ps=[]
  def varput(self,var,val):
    self.var[var]=val
  def varpul(self):
    return self.var
  def fooperror(cline,linestring):
    print("|FOOP ERROR")
    print("|at line {0}".format(cline))
    print("|{0}".format(linestring))
  def phase(self,text):
    if type(text)==list:pass
    if type(text)==str:text=text.split("\n")
    a=0
    c=[]
    for x in text:
      #if x.startswith("C#"):
      if x==';' or x==';\n':
        print(x)
        text.pop(a)
        a-=1
      elif x.startswith("//"):
        text.remove(x)
      elif x == '':
        text.remove('')
      else:
        c.append(x)
      a+=1
    return c
  def interpreter(self,lines : list):
    print(lines)
    mode=[]
    cl=0;#curent line
    linesn=len(lines)
    self.var['lines']=linesn
    self.var['foo']='foo'
    while linesn != cl:
      ## pre line var
      pasic_line=False#test if the line can be runed
      ## line prep
      while pasic_line == False:
        line=lines[cl]
        line=line.replace("\n","")
        if line.startswith(";"):
          if "dent" in mode:
            line=line[1:]
            pasic_line=True
          else:
            cl+=1
            if "dent" in mode:mode.remove("dent")
        else:
          pasic_line=True
      ogl=line
      ## varables
      self.var["cl"]=cl
      ## user defined varables
      if line.find("$")!=-1:
        a=-1
        while a != 0:
          a=line.find("$")+1
          b=line.find("$",a)
          c=line[a:b]
          #print(a,b,c)
          if a == 0 and b == -1:
            continue
          elif a != b and c in self.var:
            line=line.replace("${0}$".format(str(c))
            ,str(self.var[c]))
          elif b == -1:
            fooperror(cl,ogl)
            print("|malformed varable statement")
            break
          else:
            fooperror(cl,ogl)
            print("|{0} is not a varable".format(c))
            break
          
            
      if line.find("(")!=-1:
        a=-1;b=-1
        while a != 0:
          a=line.find("(")+1
          b=line.find(")")
          c=line[a:b]
          if a!=0and b!=-1:
            if c.find("+")!=-1:
              d=c.split("+")
              e=int(d[0])+int(d[1])
              line=line.replace("({})".format(c),str(e))
            elif c.find("-")!=-1:
              d=c.split("-")
              e=int(d[0])-int(d[1])
              line=line.replace("({})".format(c),str(e))
            elif c.find("*")!=-1:
              d=c.split("*")
              e=int(d[0])*int(d[1])
              line=line.replace("({})".format(c),str(e))
            elif c.find("/")!=-1:
              d=c.split("/")
              e=int(d[0])/int(d[1])
              line=line.replace("({})".format(c),str(e))
            elif c.find("==")!=-1:
              d=c.split("==")
              if d[0]==d[1]:e="true"
              else:e="false"
              line=line.replace("({})".format(c),str(e))
      if line.startswith("#"):
        var=line[1:].split("=")
        self.var[var[0]]=var[1]
      if line.startswith("C#"):
        var=line[2:].split("=")
        self.var[var[0]]=var[1]
      if line.find(":"):
        imb=line[:line.find(":")]
        if imb=="jump":
          cl=int(line.split(":")[1])
          if linesn-1 < cl or -1 >= cl:raise self.Foop_Error("Can't jump out of index")
        if imb=="print":
          self.ps.append(line.split(":")[1])
        if imb=="end":
          cl=linesn-1;self.ps.append("|end")
        if imb=="if":
          f=line.split(":")[1]
          if f == "true":
            mode.append("dent")
        
      cl+=1
    self.psflush()
foopint=foop()
foopint.varput("foo","foo")
if len(sys.argv)>1:
  #
  #x=""
  #for i in foo.phase(open("foop","r").read()):
  #  x=x+i+"\n"
  #open("foop.p","w").write(x)
  #run=sys.argv[1]
  foo.interpreter(open(run,"r").readlines())
else:
  f=""
  print('S|foop.py cml')
  print("S|type 'quit:' to exit ")
  while f!="quit:":
    f=input("foop>")
    foopint.interpreter([f])
  #foop.foop().interpreter("import /[aba,foop]/")
  #foop.foop().interpreter("var foo = p")


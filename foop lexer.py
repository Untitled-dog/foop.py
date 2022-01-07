import sys
def fooperror(cline,linestring):
  print("|FOOP ERROR")
  print("|at line {0}".format(cline))
  print("|{0}".format(linestring))
tokens={}
"WHITESPACE"
"LINE_BREAK"
"NEWLINE"
"LETTER"
"DIGIT"
"OPERATOR"
"STRING_QUOTE"
"SINGLE_LINE_COMMENT"
"MULTI_LINE_COMMENT_START"
"MULTI_LINE_COMMENT_END"
"UNKNOWN"
class foop:
  def __init__(self):
    self.pts={}
    self.var={"foo":"foo"}
    self.ps=[]#print stack
  class Foop_Error(Exception):
    #print("oof")
    pass
  def varput(self,var,val):
    self.var[var]=val
  def varpul(self):
    return self.var
  def lexer(self):
    pass
  def interpreter(self,lines : list):
    mode=["dent"]
    v='';
    cl=0;#curent line
    linesn=len(lines)
    for x in lines:
      if x.startswith("C#"):
        var=x.replace("C#","")
        var=var.split("=")
        self.var[var[0]]=var[1]
      else:
        break
    while linesn != cl:
      ## line prep
      line=lines[cl]
      ogl=line
      line=line.replace("\n","")
      self.var["cl"]=cl
      if line.startswith(";"):
        if "dent" in mode:line=line[1:]
        else:line=""
      else:
        if "dent" in mode:mode.remove("dent")
      ## var
      if line.find("$")!=-1:
        a=0
        while a != -1:
          a=line.find("$")
          if a != -1:
            varp=line.find("$",a+1)
            c=line[a+1:varp]
            if varp == -1:
              fooperror(cl,ogl)
              print("|malformed varable statement")
              break
            if c in self.var:
              line=line.replace("${0}$".format(str(c)),str(self.var[c]))
            else:
              fooperror(cl,ogl)
              print("|{0} is not a varable".format(c));break
      if line.find("(")!=-1:
        a=0;b=-1
        while a != -1:
          a=line.find("(")
          b=line.find(")")
          if a != -1 and b != -1:
            c=line[a+1:b]
            if c.find("+")!=-1:
              d=c.split("+")
              e=int(d[0])+int(d[1])
              line=line.replace("({})".format(c),str(e))
      if line.startswith("#"):
        var=line.replace("#","")
        var=var.split("=")
        self.var[var[0]]=var[1]
      if line.find(":"):
        imb=line[:line.find(":")]
        if imb=="jump":
          cl=int(line.split(":")[1])
          if linesn-1 < cl or -1 >= cl:raise self.Foop_Error("Can't jump out of index")
        if imb=="print":self.ps.append(line.split(":")[1])
        if imb=="end":cl=linesn-1;self.ps.append("|end")
        if imb=="if":
          f=line.split(":")[1]
          if f == "true":
            mode.append("dent")
      cl+=1
    self.psflush()

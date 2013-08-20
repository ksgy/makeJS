import sys
from xml.dom import minidom

class makeJS():
    
    # TODO handle exceptions (malformed html/xml, etc)
    # TODO use createDocumentFragment

    elemcounter = {}
    
    
    def parseJS(self, dom):
        
        ndom = minidom.parseString(dom.replace('&', '&amp;'))
        # TODO convert back on textNode
        # TODO handle special chars (&pound;, etc)
      
        
        ret = ''
        retAppend = ''
        
        for elements in range(len(ndom.getElementsByTagName('*'))):
            element = ndom.getElementsByTagName('*')[elements]
            
            if element.nodeName != 'makeJSContainer':
                
                # set elemcounter for node type // if not exisits, creates a new one
                if element.nodeName in self.elemcounter:
                    self.elemcounter[element.nodeName] = self.elemcounter[element.nodeName]+1
                else:
                    self.elemcounter[element.nodeName] = 0
                    
                # debug info
                ret+="// DEBUG <" + element.nodeName
                for attr in element.attributes.items():
                    if attr[0] != 'mjs_index':
                        ret+=" "+attr[0]+"='"+attr[1]+"'"
                ret+=">\n"
                    
                # TODO needs more testing on different class names and IDs
                parent = element.parentNode
                elid = element.getAttribute('id')
                elcl = element.getAttribute('class').replace('-','_').replace(' ','__')

                
                element.setAttribute('mjs_index', str(self.elemcounter[element.nodeName]))
                
                
                ret+="var _"+element.nodeName+"_"+elid+"_"+elcl+"_"+element.getAttribute('mjs_index')+" = document.createElement('"+element.nodeName.upper()+"');\n"
                
                
                for child in element.childNodes:
                    if child.nodeValue:
                        ret+="// DEBUG textNode = " + child.nodeValue.strip()+"\n"
                        ret+="_"+element.nodeName+"_"+elid+"_"+elcl+"_"+element.getAttribute('mjs_index')+".appendChild(document.createTextNode('"+child.nodeValue.strip()+"'));\n"
        
                
                # TODO check IE compatibility
                # TODO self.elemcounter[element.nodeName] is wrong if same type of node is the child and the parent
                for attr in element.attributes.items():
                    if attr[0] != 'mjs_index':
                        ret+="_"+element.nodeName+"_"+elid+"_"+elcl+"_"+element.getAttribute('mjs_index')+".setAttribute('"+attr[0]+"', '"+attr[1]+"');\n";
                    
                if parent.nodeName != 'makeJSContainer':
                    pid = parent.getAttribute('id')
                    pcl = parent.getAttribute('class').replace('-','_').replace(' ','__')
                    
                    
                    retAppend+="_"+parent.nodeName+"_"+pid+"_"+pcl+"_"+parent.getAttribute('mjs_index')+".appendChild(_"+element.nodeName+"_"+elid+"_"+elcl+"_"+element.getAttribute('mjs_index')+");\n\n"
                else:
                    retAppend+="document.body.appendChild(_"+element.nodeName+"_"+elid+"_"+elcl+"_"+element.getAttribute('mjs_index')+");\n\n\n"
                
            # TODO iterate attributes, include in js 
                
        return ret+retAppend

js = makeJS()
r = sys.stdin.read().strip()
print js.parseJS('<?xml version="1.0" encoding="utf-8" ?><makeCSSContainer>'+r+'</makeCSSContainer>')

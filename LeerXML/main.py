from xml.dom.minidom import parse, Node

xmltree = parse("LeerXML/note.xml")

for node  in xmltree.getElementsByTagName("pro"):
    for node_hijo in node.childNodes:
        if node_hijo.nodeType==Node.TEXT_NODE:
            print(node_hijo.data)
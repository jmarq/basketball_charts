# my favourite XML library
from xml.etree import ElementTree as et
 
# create an SVG XML element (see the SVG specification for attribute details)
doc = et.Element('svg', width='480', height='360', version='1.1', xmlns='http://www.w3.org/2000/svg')
 
# add a circle (using the SubElement function)
et.SubElement(doc, 'circle', cx='240', cy='180', r='160', fill='rgb(255, 192, 192)')
 
# add text (using append function)
text = et.Element('text', x='240', y='180', fill='white', style='font-family:Sans;font-size:48px;text-anchor:middle;dominant-baseline:top')
text.text = 'pink circle'
doc.append(text)
 
# ElementTree 1.2 doesn't write the SVG file header errata, so do that manually
f = open('sample.svg', 'w')
f.write('<?xml version=\"1.0\" standalone=\"no\"?>\n')
f.write('<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n')
f.write('\"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n')
f.write(et.tostring(doc))
f.close()


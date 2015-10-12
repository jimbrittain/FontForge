import fontforge
"""
Custon Python Scripting for FontForge to force all points to extrema for every 
glyph within the font without notification. Is useful for a face where the 
glyphs have been drawn and then needs to ensure linting.

Unsure whether registerMenuItem is correct as developed and used by the 
File > Execute Script method to allow for alteration on the fly.
"""
def extremaForce():
    font = fontforge.activeFont()
    for glyph in font.glyphs():
        noExtremaErrors = False
        while noExtremaErrors == False:
            errors = glyph.validate(True)
            noExtremaErrors = True
            if e & 0x20 == 0x20:
                noExtremaErrors = False
                glyph.addExtrema('only_good_rm')
            if noExtremaErrors == False:
                glyph.simplify(0,'setstarttoextrema')

fontforge.registerMenuItem(extremaForce,None,None,"Font",None, "SubMenu", "Force Glyphs to Extrema");
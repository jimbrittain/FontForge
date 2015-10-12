import fontforge
"""
Custon Python Scripting for FontForge to move all points to Integral Coordinates
 for every glyph within the font without notification. Is useful for a face 
where the glyphs have been drawn and then needs to ensure linting.

Unsure whether registerMenuItem is correct as developed and used by the 
File > Execute Script method to allow for alteration on the fly.
"""def integralPoints():
    font = fontforge.activeFont()
    for glyph in font.glyphs():
        noRoundErrors = False
        while noRoundErrors == False:
            errors = glyph.validate(True)
            noRoundErrors = True
            if errors & 0x80000 == 0x80000:
                noRoundErrors = False
                glyph.round()
fontforge.registerMenuItem(integralPoints,None,None,"Font", None, "SubMenu", "Force Glyphs to Integral Points");
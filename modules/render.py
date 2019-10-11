def render_html(typ,y,x,height,width):
    coor_h = round(y*height*100,0)
    coor_w = round(x*width*100,0)
    if(typ == "button"):
        return """<button type="button" style ="padding-left:""" +str(coor_w)+ """px,padding-top:""" + str(coor_h) + """px">click Me!</button>"""
        
    elif(typ == "paragraph"):
        return """<p style ="padding-left:""" +str(coor_w)+ """px,padding-top:""" + str(coor_h) + """px">click Me!</p>"""
    # <button type="button" style ="width:20px,height:30px">click Me!</button>

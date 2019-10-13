def render_html(typ,y,x,height,width):
    coor_h = round(y*height*100,0)
    coor_w = round(x*width*100,0)
    if(typ == "button"):
        return """<button type="button" style ="padding-left:""" +str(coor_w)+ """px,padding-top:""" + str(coor_h) + """px">click Me!</button>"""
    elif(typ == "paragraph"):
        return """<p style ="padding-left:""" +str(coor_w)+ """px,padding-top:""" + str(coor_h) + """px">click Me!</p>"""
    elif(typ == "header"):
        return """<header style ="padding-left:""" +str(coor_w)+ """px,padding-top:""" + str(coor_h) + """px">click Me!</header>"""
    elif(typ == "link"):
        return """<a href style ="padding-left:""" +str(coor_w)+ """px,padding-top:""" + str(coor_h) + """px">click Me!</a>"""
    elif(typ == "label"):
        return """<label style ="padding-left:""" +str(coor_w)+ """px,padding-top:""" + str(coor_h) + """px">click Me!</label>"""
    elif(typ == "checkbox"):
        return """<input type = "checkbox" style ="padding-left:""" +str(coor_w)+ """px,padding-top:""" + str(coor_h) + """px">click Me!"""
    elif(typ == "radiobutton"):
        return """<input type = "radio" style ="padding-left:""" +str(coor_w)+ """px,padding-top:""" + str(coor_h) + """px">click Me!"""
    elif(typ == "linebreak"):
        return """<hr style ="padding-left:""" +str(coor_w)+ """px,padding-top:""" + str(coor_h) + """px">"""
    elif(typ == "textinput"):
        return """<input type = "text" style ="padding-left:""" +str(coor_w)+ """px,padding-top:""" + str(coor_h) + """px">"""
    elif(typ == "datepicker"):
        return """<input type = "date" style ="padding-left:""" +str(coor_w)+ """px,padding-top:""" + str(coor_h) + """px">"""
    elif(typ == "slider"):
        return """<input type = "range" min="1" max="100" value="50" class="slider" id="myRange" style ="padding-left:""" +str(coor_w)+ """px,padding-top:""" + str(coor_h) + """px">"""
    elif(typ == "list"):
        return """<ul style ="padding-left:""" +str(coor_w)+ """px,padding-top:""" + str(coor_h) + """px"><li>Check_out</li></ul>"""
    elif(typ == "image"):
        return """<img src= "https://yt3.ggpht.com/a/AGF-l7-VZ8qMe-CQ7CTHbYTNHAp1dB0pDrPx47hzmw=s900-c-k-c0xffffffff-no-rj-mo" alt="Italian Trulli">"""
    elif(typ == "dropdown"):
        return """<select style ="padding-left:""" +str(coor_w)+ """px,padding-top:""" + str(coor_h) + """px"><option>rahul</option><option>harsh</option></select>"""
    
    # <button type="button" style ="width:20px,height:30px">click Me!</button>

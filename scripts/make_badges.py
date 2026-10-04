import math, os
def c(x,y,r): return f"M{x-r} {y}a{r} {r} 0 1 0 {2*r} 0a{r} {r} 0 1 0 {-2*r} 0"
S="M12 3l7 3v5c0 4.5-3 8.2-7 10-4-1.8-7-5.5-7-10V6z"
B=[("awareness-advocate","AWARENESS","#FFC940","M3 10v4h3l8 5V5l-8 5zM18 9a4 4 0 0 1 0 6M7 14.5l1.5 5.5h2.5l-1-5.5"),
("signal-booster","5 POSTS","#FFB020",c(12,12,2)+"M8.2 8.2a5.4 5.4 0 0 0 0 7.6M15.8 8.2a5.4 5.4 0 0 1 0 7.6M5.3 5.3a9.5 9.5 0 0 0 0 13.4M18.7 5.3a9.5 9.5 0 0 1 0 13.4"),
("awareness-ambassador","EVERY WEEK","#FF9A3C","M4 6h16v15H4zM4 10h16M8 3v4M16 3v4M9 15.5l2 2 4-4"),
("first-contribution","FIRST MERGE","#3DDC97",c(6,5.5,2.5)+c(6,18.5,2.5)+c(18,12,2.5)+"M6 8v8M6 8c0 3.5 3 4 9.5 4"),
("security-contributor","25 POINTS","#4EA8FF",S+"M12 7.5v9"),
("security-builder","50 POINTS","#9B8CFF","M12 3l9 5-9 5-9-5zM3 12.5l9 5 9-5M3 16.5l9 5 9-5"),
("security-champion","75 POINTS","#FF8A4C",S+"M12 8l1.2 2.4 2.6.4-1.9 1.8.5 2.6-2.4-1.3-2.4 1.3.5-2.6-1.9-1.8 2.6-.4z"),
("cyber-guardian","100 POINTS","#FF5A6E",S+"M8.5 12l2.5 2.5 4.5-5"),
("community-defender","COMMUNITY","#2EC4B6",c(12,12,9)+"M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"),
("ai-security-pioneer","AI SECURITY","#C77DFF","M7 7h10v10H7zM10 10h4v4h-4zM9.5 3v4M14.5 3v4M9.5 17v4M14.5 17v4M3 9.5h4M3 14.5h4M17 9.5h4M17 14.5h4"),
("api-defender","API SECURITY","#4EA8FF","M8 4c-2 0-3 1-3 3v2.5c0 1-.8 2.5-2 2.5 1.2 0 2 1.5 2 2.5V17c0 2 1 3 3 3M16 4c2 0 3 1 3 3v2.5c0 1 .8 2.5 2 2.5-1.2 0-2 1.5-2 2.5V17c0 2-1 3-3 3M9.5 12h.01M12 12h.01M14.5 12h.01"),
("lab-builder","LABS","#3DDC97","M9 3h6M10 3v6L4.5 19a1.5 1.5 0 0 0 1.3 2h12.4a1.5 1.5 0 0 0 1.3-2L14 9V3M7 15h10"),
("open-source-mentor","MENTOR","#FFC940",c(9,8,3.5)+"M2.5 20c.6-3.5 3.3-5.5 6.5-5.5s5.9 2 6.5 5.5M16 4.7a3.5 3.5 0 0 1 0 6.6M18 14.8c2 .7 3.2 2.5 3.5 5.2"),
("cybersectober-champion","CHAMPION","#FFD76A","M8 4h8v5a4 4 0 0 1-8 0zM8 6H5v1.5a3 3 0 0 0 3 3M16 6h3v1.5a3 3 0 0 1-3 3M12 13v4M9 17h6l.5 4h-7z")]
def hexp(r): return " ".join(f"{160+r*math.cos(math.radians(60*k)):.1f},{160+r*math.sin(math.radians(60*k)):.1f}" for k in range(6))
def arc(t,r,top,fill):
    a=7.8+3; pos=-(len(t)*a-3)/2; o=[]
    for ch in t:
        m=pos+3.9; th=(-90+math.degrees(m/r)) if top else (90-math.degrees(m/r)); rot=th+90 if top else th-90
        x=160+r*math.cos(math.radians(th)); y=160+r*math.sin(math.radians(th))
        if ch!=" ": o.append(f'<text x="{x:.2f}" y="{y:.2f}" transform="rotate({rot:.2f} {x:.2f} {y:.2f})" text-anchor="middle">{ch}</text>')
        pos+=a
    return f'<g font-family="\'IBM Plex Mono\', ui-monospace, Menlo, Consolas, monospace" font-size="13" font-weight="500" fill="{fill}">'+"".join(o)+"</g>"
os.makedirs("badges/svg",exist_ok=True)
for slug,lab,col,d in B:
    name=slug.replace("-"," ").title().replace("Ai ","AI ").replace("Api ","API ").replace("Cybersectober","CyberSecTOBER")
    s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="320" height="320" viewBox="0 0 320 320" role="img" aria-label="{name} badge, CyberSecTOBER 2026"><title>{name} badge, CyberSecTOBER 2026</title>
<polygon points="{hexp(152)}" fill="#141C28" stroke="{col}" stroke-width="6" stroke-linejoin="round"/>
<polygon points="{hexp(134)}" fill="none" stroke="{col}" stroke-opacity="0.35" stroke-width="1.5" stroke-dasharray="2 6" stroke-linecap="round"/>
{arc("CYBERSECTOBER · 2026",92,True,"#9AA4B2")}{arc(lab,102,False,col)}
<g transform="translate(112 106) scale(4)"><path d="{d}" fill="none" stroke="{col}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></g></svg>
'''
    open(f"badges/svg/{slug}.svg","w").write(s)
    try:
        import cairosvg; cairosvg.svg2png(bytestring=s.encode(),write_to=f"badges/{slug}.png",output_width=512,output_height=512)
    except Exception as e: print("PNG skipped:",e)
print("done")

# Builds the GitHub Pages playbook graphics (light theme, wordmark bottom right).
import importlib.util, sys, os
spec = importlib.util.spec_from_file_location("kit", "brinvik/brinvik-infographic-canvas-kit.py")
kit = importlib.util.module_from_spec(spec); spec.loader.exec_module(kit)
Canvas = kit.Canvas
OUT = sys.argv[1]

STR = {
 "da": {
  "steps": ["Ejer og opgaver", "Abonnement og data", "Arbejdsgange", "Oplæring", "Agent på hjemmesiden", "Måling"],
  "weeks": ["Uge 1", "Uge 1", "Uge 2 til 4", "Uge 2 til 4", "Når resten kører", "Uge 6"],
  "hero_title": "Fra første login til målbar effekt",
  "inputs": ["Instruktioner", "Dokumenter", "Godt eksempel"],
  "claude": "Claude-projekt", "draft": "Udkast", "review": "Kontrol",
  "flow_note": "En arbejdsgang i Claude: tre input, ét udkast og altid et menneske i sidste led.",
  "check": ["Ejer udpeget", "Tre opgaver valgt", "Datapolitik skrevet", "Arbejdsgange bygget", "Team oplært", "Tal målt før og efter"],
  "check_title": "Er implementeringen færdig?",
  "check_note": "Mangler der et flueben, er implementeringen ikke færdig.",
  "hero_note": "Et bud på rækkefølgen. I bestemmer selv tempoet.",
 },
 "en": {
  "steps": ["Owner and tasks", "Plan and data", "Workflows", "Training", "Website agent", "Measurement"],
  "weeks": ["Week 1", "Week 1", "Weeks 2 to 4", "Weeks 2 to 4", "Once the rest is running", "Week 6"],
  "hero_title": "From first login to measurable use",
  "inputs": ["Instructions", "Documents", "Good example"],
  "claude": "Claude project", "draft": "Draft", "review": "Review",
  "flow_note": "A Claude workflow: three inputs, one draft and always a person at the end.",
  "check": ["Owner named", "Three tasks chosen", "Data policy written", "Workflows built", "Team trained", "Numbers measured before and after"],
  "check_title": "Is the implementation done?",
  "check_note": "If one item isn't ticked, the implementation isn't done.",
  "hero_note": "A suggested order. Adjust the weeks to your own pace.",
 },
}

def hero(loc, path):
    S = STR[loc]; c = Canvas(1600, "light", "", ""); T = c.T
    c.begin(900); d = c.d; w, h, M = c.w, c.h, c.M
    ft = c.playfair(0.040)
    d.text((M, int(h*0.10)), S["hero_title"], font=ft, fill=T["text"])
    y = int(h*0.50); x0, x1 = M + int(w*0.04), w - M - int(w*0.04)
    d.line((x0, y, x1, y), fill=T["rule"], width=6)
    n = 6; step = (x1 - x0) / (n - 1)
    fl = c.inter(0.0165, medium=True); fw = c.inter(0.0145)
    r = int(w*0.022)
    for i in range(n):
        cx = int(x0 + i*step)
        last = i == n-1
        d.ellipse((cx-r, y-r, cx+r, y+r), fill=T["ox"] if last else T["bg"], outline=T["ox"] if last else T["text"], width=6)
        num = str(i+1); fn = c.playfair(0.022)
        tw = c.measure(num, fn)
        d.text((cx - tw/2, y - c.text_height(num, fn)/2 - int(r*0.25)), num, font=fn, fill=T["bg"] if last else T["text"])
        maxw = int(step*0.92)
        lines = c.wrap(S["steps"][i], fl, maxw)
        ly = y + r + int(h*0.05)
        for ln in lines:
            lw = c.measure(ln, fl); d.text((cx - lw/2, ly), ln, font=fl, fill=T["text"]); ly += int(w*0.0165*1.35)
        wk = S["weeks"][i]; ww = c.measure(wk, fw)
        d.text((cx - ww/2, y - r - int(h*0.09)), wk, font=fw, fill=T["dim"])
    # gold geometry: tick at the end
    note_y = h - int(h*0.040) - int(w*0.022) - int(w*0.015) - c.note_height(S["hero_note"]) - int(h*0.02)
    c.draw_note(S["hero_note"], note_y)
    c.finish(path)

def flow(loc, path):
    S = STR[loc]; c = Canvas(1200, "light", "", ""); T = c.T
    c.begin(675); d = c.d; w, h, M = c.w, c.h, c.M
    fl = c.inter(0.022, medium=True)
    bw, bh = int(w*0.20), int(h*0.13); gap = int(h*0.05)
    top = int(h*0.12); xs = M
    centers = []
    for i, lab in enumerate(S["inputs"]):
        y0 = top + i*(bh+gap)
        d.rounded_rectangle((xs, y0, xs+bw, y0+bh), radius=8, outline=T["text"], width=4)
        # small drawn glyph: lines for instructions, page for docs, star-ish check for example
        gx = xs + int(bw*0.08); gy = y0 + bh//2
        if i == 0:
            for k in range(3): d.line((gx, gy-14+k*14, gx+30, gy-14+k*14), fill=T["rule"], width=4)
        elif i == 1:
            d.rectangle((gx, gy-20, gx+28, gy+20), outline=T["rule"], width=4)
        else:
            d.line((gx, gy, gx+10, gy+12, gx+30, gy-14), fill=T["gold"], width=5)
        lines = c.wrap(lab, fl, bw - int(bw*0.30))
        ty = gy - len(lines)*int(w*0.022*1.3)//2
        for ln in lines:
            d.text((xs+int(bw*0.25), ty), ln, font=fl, fill=T["text"]); ty += int(w*0.022*1.3)
        centers.append((xs+bw, y0+bh//2))
    # Claude block
    cx0 = int(w*0.38); cw = int(w*0.20); cy0 = top + bh//2; ch = 2*(bh+gap)
    d.rounded_rectangle((cx0, cy0, cx0+cw, cy0+ch), radius=8, fill=T["text"])
    fc = c.playfair(0.026); lines = c.wrap(S["claude"], fc, cw-40)
    ty = cy0 + ch//2 - len(lines)*int(w*0.026*1.25)//2
    for ln in lines:
        lw = c.measure(ln, fc); d.text((cx0+cw//2-lw//2, ty), ln, font=fc, fill=T["bg"]); ty += int(w*0.026*1.25)
    for (ex, ey) in centers:
        d.line((ex, ey, cx0, cy0+ch//2), fill=T["rule"], width=4)
    # draft page
    dx0 = int(w*0.64); dw = int(w*0.12); dy0 = cy0 + ch//2 - int(h*0.12)
    d.line((cx0+cw, cy0+ch//2, dx0, cy0+ch//2), fill=T["rule"], width=4)
    d.rectangle((dx0, dy0, dx0+dw, dy0+int(h*0.24)), outline=T["text"], width=4, fill=(255,252,246))
    for k in range(5): d.line((dx0+20, dy0+30+k*28, dx0+dw-20-(k%2)*30, dy0+30+k*28), fill=T["faint"], width=5)
    lw = c.measure(S["draft"], fl); d.text((dx0+dw//2-lw//2, dy0+int(h*0.24)+18), S["draft"], font=fl, fill=T["text"])
    # person
    px = w - M - int(w*0.06); py = cy0 + ch//2
    d.line((dx0+dw, py, px-int(w*0.045), py), fill=T["ox"], width=5)
    d.polygon([(px-int(w*0.045), py-12), (px-int(w*0.045)+18, py), (px-int(w*0.045), py+12)], fill=T["ox"])
    hr = int(w*0.022); d.ellipse((px-hr, py-int(h*0.14)-hr, px+hr, py-int(h*0.14)+hr), outline=T["ox"], width=6)
    d.arc((px-int(w*0.045), py-int(h*0.07), px+int(w*0.045), py+int(h*0.10)), 180, 360, fill=T["ox"], width=6)
    lw = c.measure(S["review"], fl); d.text((px-lw//2, py+int(h*0.06)), S["review"], font=fl, fill=T["ox"])
    ny = h - int(h*0.040) - int(w*0.022) - int(w*0.015) - c.note_height(S["flow_note"]) - int(h*0.01)
    c.draw_note(S["flow_note"], ny)
    c.finish(path)

def checklist(loc, path):
    S = STR[loc]; c = Canvas(1200, "light", "", ""); T = c.T
    c.begin(675); d = c.d; w, h, M = c.w, c.h, c.M
    ft = c.playfair(0.036); d.text((M, int(h*0.08)), S["check_title"], font=ft, fill=T["text"])
    fl = c.inter(0.024, medium=True)
    colw = (w - 2*M)//2; top = int(h*0.27); row = int(h*0.17); box = int(w*0.03)
    for i, item in enumerate(S["check"]):
        col, r = i//3, i%3
        x = M + col*colw; y = top + r*row
        empty = i == 5
        d.rounded_rectangle((x, y, x+box, y+box), radius=4, outline=T["ox"] if empty else T["text"], width=5)
        if not empty:
            d.line((x+box*0.2, y+box*0.55, x+box*0.42, y+box*0.78, x+box*0.82, y+box*0.22), fill=T["text"], width=7)
        lines = c.wrap(item, fl, colw - box - int(w*0.05))
        ty = y + box//2 - len(lines)*int(w*0.024*1.3)//2
        for ln in lines:
            d.text((x+box+int(w*0.02), ty), ln, font=fl, fill=T["ox"] if empty else T["text"]); ty += int(w*0.024*1.3)
    ny = h - int(h*0.040) - int(w*0.022) - int(w*0.015) - c.note_height(S["check_note"]) - int(h*0.01)
    c.draw_note(S["check_note"], ny)
    c.finish(path)

os.makedirs(OUT, exist_ok=True)
hero("da", f"{OUT}/hero.jpg"); hero("en", f"{OUT}/hero-en.jpg")
flow("da", f"{OUT}/steps.jpg"); flow("en", f"{OUT}/steps-en.jpg")
checklist("da", f"{OUT}/checklist.jpg"); checklist("en", f"{OUT}/checklist-en.jpg")

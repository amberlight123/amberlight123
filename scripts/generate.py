"""NixOS Cyber-Rice: deterministic SVG assets, Python standard library only."""
from pathlib import Path
from html import escape
import math

ROOT = Path(__file__).resolve().parents[1]
A = ROOT / 'assets'
A.mkdir(exist_ok=True)
C, E, D, N, B = '#18DCF9', '#0161EA', '#032999', '#02091A', '#000000'
FONT = "'Cascadia Code','DejaVu Sans Mono',Consolas,monospace"

def text(x, y, value, size=24, color=C, opacity=1, extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" opacity="{opacity}" {extra}>{escape(value)}</text>'

def rect(x,y,w,h,fill=N,stroke=D):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}"/>'

def save(name,w,h,body,title):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">NixOS Cyber-Rice · Alberto Davis. Presentación decorativa inspirada en i3 y Polybar.</desc>
<style>text{{font-family:{FONT}}}.cursor{{animation:blink 2.8s step-end 3}}@keyframes blink{{50%{{opacity:0}}}}@media(prefers-reduced-motion:reduce){{.cursor{{animation:none}}}}</style>
<rect width="{w}" height="{h}" fill="{B}"/><g>{body}</g></svg>'''
    (A/name).write_text(svg,encoding='utf-8')

def window(x,y,w,h,label,active=False):
    return rect(x,y,w,h,N,E if active else D)+rect(x,y,w,34,N,E if active else D)+text(x+16,y+23,label,15)+text(x+w-60,y+23,'─ □',15,E)

def panel(name,num,title,lines):
    h=100+len(lines)*43
    body=window(1,1,798,h-2,f'{num} / {title}',True)
    for i,line in enumerate(lines):
        body+=text(28,85+i*43,line,24)
    save(name,800,h,body,title)

body=rect(1,1,1198,83,N,E)+text(20,30,'⟐ amberlight123  /  nix-shell',19)
for i,label in enumerate(['01:ABOUT','02:STACK','03:PROJECTS','04:STATS','05:CONTACT']):
    x=20+i*158
    body+=rect(x,43,148,30,E if i==0 else N,E if i==0 else D)+text(x+9,64,label,17,N if i==0 else C)
body+=text(810,62,'WM: i3 · BAR: polybar · ENV: github',16)+f'<circle cx="1177" cy="25" r="4" fill="{C}"/>'
save('polybar.svg',1200,85,body,'Polybar: ABOUT activo; indicadores decorativos')

def emblem(cx,cy,r):
    s=''
    for rad in [r+28,r+52]:
        s+=f'<circle cx="{cx}" cy="{cy}" r="{rad}" fill="none" stroke="{D}" stroke-dasharray="4 12"/>'
    for i in range(6):
        angle=i*60
        s+=f'<g transform="translate({cx} {cy}) rotate({angle})"><path d="M 14 -8 L {r} -8 L {r+18} 10 L 48 10 L 68 30 L 55 43 L 23 10 Z" fill="{E if i%2 else D}"/><path d="M 32 -8 H {r}" fill="none" stroke="{C}" stroke-width="2"/></g>'
    s+=f'<path d="M {cx-12} {cy} L {cx} {cy-12} L {cx+12} {cy} L {cx} {cy+12} Z" fill="{C}"/>'
    return s

body=window(1,9,734,390,'~/profile / terminal',True)+window(747,9,452,390,'~/identity / geometry')
for y,v in [(83,'$ whoami'),(130,'Alberto Davis'),(173,'Full Stack Developer'),(229,'$ cat about.md'),(268,'Software · UTP · Panamá'),(319,'$ echo $CURRENT_FOCUS'),(357,'Web / datos / interfaces')]:
    body+=text(28,y,v,36 if y==130 else 25,C,0.72 if v.startswith('$') else 1)
body+=f'<rect class="cursor" x="407" y="338" width="12" height="24" fill="{C}"/>'+emblem(972,194,86)
body+=text(818,359,'NIXOS CYBER-RICE',25)+text(822,383,'GEOMETRY / ORIGINAL SYMBOL',15,E)
save('hero.svg',1200,410,body,'Alberto Davis · Full Stack Developer · Software UTP, Panamá')
body=window(1,1,598,388,'~/profile / terminal',True)
for y,v in [(78,'$ whoami'),(124,'Alberto Davis'),(165,'Full Stack Developer'),(222,'$ cat about.md'),(260,'Software · UTP · Panamá'),(318,'$ echo $CURRENT_FOCUS'),(358,'Web / datos / interfaces')]:
    body+=text(25,y,v,34 if y==124 else 24)
save('hero-mobile.svg',600,390,body,'Alberto Davis · Full Stack Developer · presentación móvil')

panel('about.svg','01','about.md',[
    '$ cat ~/profile/about.md',
    'role     = Desarrollo web Full Stack',
    'studies  = Ingeniería en Software / UTP',
    'location = Ciudad de Panamá',
    'focus    = Base de datos → interfaz',
    'interests= Redes · UI/UX · seguridad',
])
panel('stack.svg','02','stack.conf',[
    '[languages]',
    'Python · PHP · JavaScript · TypeScript',
    'HTML · CSS · SQL',
    '[frameworks / tools]',
    'React · Next.js · FastAPI · PySide6',
    'Node.js · Vite · Git · Linux',
    '[data / infrastructure]',
    'MySQL · PostgreSQL · Apache',
    'Azure · Vercel',
])
panel('projects.svg','03','~/projects/',[
    '$ ls --public ~/projects/',
    '├─ lucy-activos-utp/',
    '│  Activos institucionales · React / TS',
    '├─ vozelia_site_personal_project/',
    '│  Gestión VoIP · PHP / MySQL / JS',
    '└─ Sabores-del-Mar/',
    '   Menú y reservas · PHP / MySQL',
])
body=window(1,1,798,358,'04 / github-diagnostics',True)
body+=text(28,82,'$ inspect --public --snapshot',24)+text(28,124,'2026-10-12 / incluye este perfil',22)
for x,value,label in [(28,'06','REPOS PÚBLICOS'),(286,'04','PROYECTOS PROPIOS'),(550,'01','FORK PÚBLICO')]:
    body+=text(x,186,value,46)+text(x,218,label,16)
body+=text(28,263,'Lenguaje principal por proyecto propio:',22)
for i,(label,count) in enumerate([('PHP',2),('HTML',1),('TypeScript',1)]):
    x=28+i*258
    body+=text(x,304,f'{label} · {count}/4',20)
    for j in range(4): body+=rect(x+j*48,322,39,9,E if j<count else N,D)
save('stats.svg',800,360,body,'Corte 2026-10-12: seis repositorios públicos, cuatro proyectos propios, un fork y este perfil; PHP 2, HTML 1, TypeScript 1')
panel('contact.svg','05','network / endpoints',[
    '$ connect --human',
    'github   → amberlight123',
    'linkedin → alberto1davis',
    'email    → albertoantonio.davisc',
    '           @gmail.com',
    'Freelance · colaboración · oportunidades',
])
save('divider.svg',800,46,rect(1,1,798,44,N,D)+text(18,29,'NIXOS CYBER-RICE / AD',17)+text(430,29,'i3 inspired · static session',17),'NixOS Cyber-Rice · sesión visual estática')
print('Generated 9 self-contained SVG assets.')

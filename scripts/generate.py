"""Generate the GitHub profile artwork using Python standard library only."""
from pathlib import Path
from html import escape
import base64
import struct
import textwrap
ROOT=Path(__file__).resolve().parents[1]
A=ROOT/'assets'
A.mkdir(exist_ok=True)
CYAN, BLUE, DEEP, SURFACE, BLACK = '#18DCF9','#0161EA','#032999','#02091A','#000000'
WHITE='#F4F7FB'
MUTED='#C4D0DA'
SOFT_CYAN='#9BEAF5'

def text(x,y,value,size=26,color=WHITE,weight=400,mono=False):
    family='Consolas,monospace' if mono else 'Segoe UI,Arial,sans-serif'
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(value)}</text>'

def rect(x,y,w,h,fill,stroke='none'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}"/>'

def save(name,w,h,body,title,desc=''):
    style='''<style>
.halo{animation:halo 8s ease-in-out infinite}
.glint{animation:glint 12s ease-in-out infinite}
.bars{transform-box:fill-box;transform-origin:left center;animation:reveal 1.4s ease-out both}
@keyframes halo{0%,100%{opacity:.45}50%{opacity:.9}}
@keyframes glint{0%,100%{transform:translateX(0);opacity:.35}50%{transform:translateX(270px);opacity:.85}}
@keyframes reveal{from{transform:scaleX(.05)}to{transform:scaleX(1)}}
@media(prefers-reduced-motion:reduce){.halo,.glint,.bars{animation:none;transform:none;opacity:1}}
</style>'''
    (A/name).write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc or title)}</desc>{style}<rect width="{w}" height="{h}" fill="{BLACK}"/>{body}</svg>''',encoding='utf-8')

def heading(name,number,title,sub):
    body=rect(24,29,4,67,BLUE)+text(46,49,number,16,CYAN,600,True)+text(46,83,title,32,WHITE,650)+text(46,115,sub,18,MUTED)
    save(name,800,148,body,title,sub)

# Black gutters are part of every image, independent of GitHub's theme.
body=text(28,49,'AD',24,CYAN,700)+text(86,48,'NIXOS CYBER-RICE',18,WHITE,600,True)
body+=f'<circle class="halo" cx="760" cy="43" r="4" fill="{CYAN}"/>'
save('polybar.svg',800,70,body,'NixOS Cyber-Rice')
for i,(slug,label) in enumerate([('about','ABOUT'),('skills','SKILLS & TOOLS'),('work','WORK'),('connect','CONNECT')]):
    nav=text(20,36,f'{i+1:02} {label}',16 if slug=='skills' else 18,CYAN if i==0 else MUTED,600,True)
    if i==0: nav+=rect(20,48,136,3,BLUE)
    save(f'nav-{slug}.svg',200,68,nav,label)

def emblem(cx,cy,r):
    s=f'<circle class="halo" cx="{cx}" cy="{cy}" r="{r+30}" fill="none" stroke="{BLUE}" stroke-dasharray="3 12"/>'
    for i in range(6):
        s+=f'<g transform="translate({cx} {cy}) rotate({i*60})"><path d="M 14 -8 L {r} -8 L {r+18} 10 L 48 10 L 68 30 L 55 43 L 23 10 Z" fill="{BLUE if i%2 else DEEP}"/><path d="M 32 -8 H {r}" stroke="{CYAN}" stroke-width="2"/></g>'
    return s

body=rect(24,22,752,345,SURFACE,DEEP)+rect(24,22,752,3,BLUE)
body+=text(52,68,'HELLO, I AM',18,CYAN,600,True)+text(48,131,'Alberto Davis',52,WHITE,700)
body+=text(52,176,'Full Stack Developer',27,SOFT_CYAN,600)+text(52,239,'Thoughtful interfaces.',25)+text(52,276,'Reliable systems.',25)+text(52,329,'WEB  /  DESKTOP  /  DATA',17,MUTED,400,True)
body+=rect(52,199,350,1,DEEP)+f'<rect class="glint" x="52" y="198" width="64" height="2" fill="{CYAN}"/>'
body+=emblem(650,228,66)
save('hero.svg',800,395,body,'Alberto Davis — Full Stack Developer','I build web and desktop applications, from data to interface.')
body=rect(18,18,564,374,SURFACE,DEEP)+rect(18,18,564,3,BLUE)
body+=text(42,69,'HELLO, I AM',23,CYAN,600,True)+text(38,135,'Alberto Davis',55,WHITE,700)+text(42,187,'Full Stack Developer',31,SOFT_CYAN,600)+text(42,258,'Thoughtful interfaces.',29)+text(42,302,'Reliable systems.',29)+text(42,357,'WEB / DESKTOP / DATA',23,MUTED,400,True)
body+=rect(42,213,350,1,DEEP)+f'<rect class="glint" x="42" y="212" width="64" height="2" fill="{CYAN}"/>'
save('hero-mobile.svg',600,410,body,'Alberto Davis — Full Stack Developer')
heading('about.svg','01','A little about me','Practical software. Clear interfaces. Purposeful design.')
heading('stack.svg','02','Skills & Tools','Languages, practical capabilities and the tools I use.')
heading('projects.svg','03','Selected work','From business workflows to networks and data analysis.')
heading('contact.svg','04','Let’s build something useful','Open to freelance projects, collaboration and opportunities.')

languages=[('HTML / CSS',82),('SQL',77),('Python',68),('PHP',66),('JavaScript',48),('TypeScript',48)]
body=text(30,59,'LANGUAGE PROFILE',20,CYAN,600,True)+text(30,93,'Portfolio self-assessment · 0–100',22,MUTED)
for i,(label,score) in enumerate(languages):
    y=147+i*84
    body+=text(30,y,label,28,WHITE,600)+text(704,y,str(score),26,CYAN,600,True)
    body+=rect(30,y+17,726,16,SURFACE)
    body+=f'<g class="bars" style="animation-delay:{i*.12:.2f}s">'
    for j in range(25):
        x=30+j*29.04
        if j*4<score:
            width=min(23,max(0,(score-j*4)/4*23))
            body+=rect(round(x,2),y+17,round(width,2),16,CYAN if j%5==4 else BLUE)
    body+='</g>'+rect(30,y+17,1,16,DEEP)
save('languages.svg',800,650,body,'Language self-assessments: HTML/CSS 82, SQL 77, Python 68, PHP 66, JavaScript 48, TypeScript/Next.js 48 provisional','Source: albdavis.zenreverse.space. Original segmented bars on a black background. These are personal estimates, not repository language shares or objective skill measurements.')

body=text(30,49,'PUBLIC WORK',19,CYAN,600,True)
for x,n,label in [(30,'04','original projects'),(285,'01','practice fork'),(540,'01','profile repository')]:
    body+=text(x,115,n,44,WHITE,650)+text(x,151,label,18,MUTED)
body+=text(30,196,'GitHub snapshot · October 12, 2026',19,MUTED)
save('stats.svg',800,230,body,'GitHub snapshot: four original public projects, one practice fork, one profile repository; October 12, 2026')
body=rect(28,32,744,1,DEEP)+text(28,73,'ALBERTO DAVIS',18,WHITE,600,True)+text(489,73,'NIXOS CYBER-RICE',18,CYAN,400,True)
save('divider.svg',800,110,body,'Alberto Davis — NixOS Cyber-Rice')
save('spacer.svg',800,42,'','Decorative black section separator')

def copy_panel(name,paragraphs):
    body=''
    y=36
    for paragraph in paragraphs:
        for line in textwrap.wrap(paragraph,57):
            body+=text(30,y,line,20 if paragraph.isupper() else 24,CYAN if paragraph.isupper() else WHITE,600 if paragraph.isupper() else 400)
            y+=35
        y+=22
    save(name,800,y+12,body,' '.join(paragraphs))

copy_panel('about-content.svg',[
    'I’m Alberto Davis, a Full Stack Developer. I build web applications with PHP, MySQL, JavaScript and Python, from the database to the interface.',
    'My work spans business websites, booking systems, desktop tools and data analysis. I also explore networking, interface design and cybersecurity fundamentals.',
])
capabilities=[('Applied AI',68),('UI / UX design',65),('Networking',60),('Cybersecurity',60),('Scrum',56),('Linux',43),('Node.js',37)]
body=text(30,59,'CAPABILITY PROFILE',20,CYAN,600,True)+text(30,93,'Portfolio self-assessment · 0–100',22,MUTED)
for i,(label,score) in enumerate(capabilities):
    y=147+i*84
    body+=text(30,y,label,28,WHITE,600)+text(704,y,str(score),26,CYAN,600,True)
    body+=rect(30,y+17,726,16,SURFACE)
    body+=f'<g class="bars" style="animation-delay:{i*.12:.2f}s">'
    for j in range(25):
        if j*4<score:
            width=min(23,max(0,(score-j*4)/4*23))
            body+=rect(round(30+j*29.04,2),y+17,round(width,2),16,CYAN if j%5==4 else BLUE)
    body+='</g>'
save('capabilities.svg',800,734,body,'Portfolio capability self-assessments out of 100: Applied AI 68, UI/UX design 65, networking 60, cybersecurity 60, Scrum 56, Linux 43, Node.js 37.','Original animated chart using existing personal portfolio ratings; no new proficiency values are inferred.')
copy_panel('tools.svg',[
    'DESIGN & PROTOTYPING',
    'Figma · Interface design · Interactive prototypes',
    'AI & DEVELOPMENT ASSISTANCE',
    'Claude · Claude Code · AI with Python',
    'WEB & API DEVELOPMENT',
    'React · Next.js · Node.js · Vite · FastAPI',
    'DESKTOP & DELIVERY',
    'PySide6 · Npcap · Inno Setup',
    'DATA & INFRASTRUCTURE',
    'MySQL · PostgreSQL · Apache · Azure · Vercel',
    'NETWORKS & SYSTEMS',
    'Linux · TCP/IP · Routing · Switching',
    'Security fundamentals · Network automation',
    'WORKFLOW & COMMUNICATION',
    'Scrum · Data analysis · Technical presentations',
])
copy_panel('connect-content.svg',['Have a project in mind? Let’s build something useful together.'])
projects=[
    ('themis','Themis','A web platform for CSV analysis, unusual record detection and visual results.','Next.js · TypeScript · FastAPI · PostgreSQL · Azure'),
    ('sentinel','Sentinel','A desktop application for local network discovery and open-port auditing.','Python · PySide6 · Npcap'),
    ('rochy','Rochy Spa Center','Online bookings, customer accounts and an administration panel for appointment management.','JavaScript · Node.js · PostgreSQL · HTML/CSS'),
    ('sabores','Sabores del Mar','Menus, orders and reservations in one restaurant website.','PHP · MySQL · HTML/CSS'),
    ('vozelia','Vozelia','A personal project exploring VoIP operations and administration. Independent of the company that inspired it.','PHP · MySQL · JavaScript · Apache'),
]
for slug,title,description,stack in projects:
    raw=(A/'screenshots'/f'{slug}.png').read_bytes()
    width,height=struct.unpack('>II',raw[16:24])
    image_h=round(740*height/width)
    body=text(30,54,title,34,WHITE,650)+text(30,89,'VIEW PROJECT ↗',17,CYAN,600,True)
    uri=base64.b64encode(raw).decode('ascii')
    body+=f'<image x="30" y="114" width="740" height="{image_h}" href="data:image/png;base64,{uri}"/>'
    y=114+image_h+42
    for line in textwrap.wrap(description,57):
        body+=text(30,y,line,24)
        y+=35
    y+=12
    for line in textwrap.wrap(stack,65):
        body+=text(30,y,line,20,MUTED)
        y+=30
    body+=rect(30,y+20,740,1,DEEP)
    save(f'project-{slug}.svg',800,y+58,body,f'{title}: {description} {stack}','Original project screenshot from albdavis.zenreverse.space, with an accessible project description.')
for slug,label in [('portfolio','PORTFOLIO & CONTACT ↗'),('linkedin','LINKEDIN ↗'),('github','GITHUB ↗')]:
    save(f'link-{slug}.svg',800,68,rect(30,8,740,46,SURFACE,DEEP)+text(48,39,label,23,CYAN,600),label)
print('Generated self-contained SVG artwork and functional navigation segments.')

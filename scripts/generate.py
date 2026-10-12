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
.scan{stroke-dasharray:42 800;animation:flow 9s linear infinite}
.arrive{animation:arrive 1.2s ease-out both}
.arrow{animation:nudge 3.8s ease-in-out infinite}
@keyframes halo{0%,100%{opacity:.45}50%{opacity:.9}}
@keyframes glint{0%,100%{transform:translateX(0);opacity:.35}50%{transform:translateX(270px);opacity:.85}}
@keyframes reveal{from{transform:scaleX(.05)}to{transform:scaleX(1)}}
@keyframes flow{from{stroke-dashoffset:842}to{stroke-dashoffset:0}}
@keyframes arrive{from{opacity:.65;transform:translateY(5px)}to{opacity:1;transform:translateY(0)}}
@keyframes nudge{0%,100%{transform:translateX(0)}50%{transform:translateX(5px)}}
@media(prefers-reduced-motion:reduce){.halo,.glint,.bars,.scan,.arrive,.arrow{animation:none;transform:none;opacity:1}.scan{display:none}}
</style>'''
    (A/name).write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc or title)}</desc>{style}<rect width="{w}" height="{h}" fill="{BLACK}"/>{body}</svg>''',encoding='utf-8')

def scan(x,y,width,delay=0):
    return f'<path class="scan" d="M {x} {y} h {width}" fill="none" stroke="{CYAN}" stroke-width="2" opacity=".8" style="animation-delay:-{delay}s"/>'

def heading(name,number,title,sub):
    body=rect(24,19,4,55,BLUE)+text(46,45,number,17,CYAN,600,True)+text(94,45,title,30,WHITE,650)+text(46,77,sub,18,MUTED)
    body+=scan(46,94,710)
    save(name,800,104,body,title,sub)

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

body=rect(24,12,752,264,SURFACE,DEEP)+rect(24,12,752,3,BLUE)
body+=text(52,49,'HELLO, I AM',17,CYAN,600,True)+text(48,105,'Alberto Davis',48,WHITE,700)
body+=text(52,146,'Full Stack Developer',27,SOFT_CYAN,600)+text(52,200,'Thoughtful interfaces.',25)+text(52,234,'Reliable systems.',25)
body+=rect(52,166,350,1,DEEP)+f'<rect class="glint" x="52" y="165" width="64" height="2" fill="{CYAN}"/>'
body+=emblem(650,151,58)
save('hero.svg',800,290,body,'Alberto Davis — Full Stack Developer','I build web and desktop applications, from data to interface.')
body=rect(18,12,564,288,SURFACE,DEEP)+rect(18,12,564,3,BLUE)
body+=text(42,49,'HELLO, I AM',21,CYAN,600,True)+text(38,109,'Alberto Davis',52,WHITE,700)+text(42,157,'Full Stack Developer',30,SOFT_CYAN,600)+text(42,222,'Thoughtful interfaces.',28)+text(42,265,'Reliable systems.',28)
body+=rect(42,180,350,1,DEEP)+f'<rect class="glint" x="42" y="179" width="64" height="2" fill="{CYAN}"/>'
save('hero-mobile.svg',600,314,body,'Alberto Davis — Full Stack Developer')
heading('about.svg','01','A little about me','Practical software. Clear interfaces. Purposeful design.')
heading('stack.svg','02','Skills & Tools','Languages, practical capabilities and the tools I use.')
heading('projects.svg','03','Selected work','From business workflows to networks and data analysis.')
heading('contact.svg','04','Let’s build something useful','Open to freelance projects, collaboration and opportunities.')

languages=[('HTML / CSS',82),('SQL',77),('Python',68),('PHP',66),('JavaScript',48),('TypeScript',48)]
def compact_chart(name,title,values,description):
    body=text(30,36,title,20,CYAN,600,True)+text(30,66,'Portfolio self-assessment · 0–100',19,MUTED)
    for i,(label,score) in enumerate(values):
        y=105+i*52
        body+=text(30,y+7,label,25,WHITE,600)+text(720,y+7,str(score),24,CYAN,600,True)
        body+=rect(244,y-8,450,14,SURFACE)+f'<g class="bars" style="animation-delay:{i*.12:.2f}s">'
        for j in range(25):
            if j*4<score:
                width=min(14,max(0,(score-j*4)/4*14))
                body+=rect(244+j*18,y-8,round(width,2),14,CYAN if j%5==4 else BLUE)
        body+='</g>'+scan(244,y-1,round(score*4.5,2),i*.8)
    save(name,800,100+len(values)*52,body,description)
compact_chart('languages.svg','LANGUAGES',languages,'Portfolio language self-assessments: HTML/CSS 82, SQL 77, Python 68, PHP 66, JavaScript 48, TypeScript/Next.js 48 provisional.')

body=text(30,49,'PUBLIC WORK',19,CYAN,600,True)
for x,n,label in [(30,'04','original projects'),(285,'01','practice fork'),(540,'01','profile repository')]:
    body+=text(x,115,n,44,WHITE,650)+text(x,151,label,18,MUTED)
body+=text(30,196,'GitHub snapshot · October 12, 2026',19,MUTED)
body+=rect(30,216,740,1,DEEP)+scan(30,216,740)
save('stats.svg',800,230,body,'GitHub snapshot: four original public projects, one practice fork, one profile repository; October 12, 2026')
body=rect(28,32,744,1,DEEP)+scan(28,32,744)+text(28,73,'ALBERTO DAVIS',18,WHITE,600,True)+text(489,73,'NIXOS CYBER-RICE',18,CYAN,400,True)
save('divider.svg',800,90,body,'Alberto Davis — NixOS Cyber-Rice')
save('spacer.svg',800,42,'','Decorative black section separator')

def copy_panel(name,paragraphs):
    body=''
    y=28
    for index,paragraph in enumerate(paragraphs):
        body+=f'<g class="arrive" style="animation-delay:{min(index*.09,.8):.2f}s">'
        if paragraph.isupper():
            body+=f'<rect class="halo" x="14" y="{y-17}" width="3" height="22" fill="{CYAN}" style="animation-delay:-{index*.5}s"/>'
        for line in textwrap.wrap(paragraph,57):
            body+=text(30,y,line,20 if paragraph.isupper() else 24,CYAN if paragraph.isupper() else WHITE,600 if paragraph.isupper() else 400)
            y+=30
        body+='</g>'
        y+=12
    body+=rect(30,y,740,1,DEEP)+scan(30,y,740)
    save(name,800,y+12,body,' '.join(paragraphs))

copy_panel('about-content.svg',[
    'I’m Alberto Davis, a Full Stack Developer. I build web applications with PHP, MySQL, JavaScript and Python, from the database to the interface.',
    'My work spans business websites, booking systems, desktop tools and data analysis. I also explore networking, interface design and cybersecurity fundamentals.',
])
capabilities=[('Applied AI',68),('UI / UX design',65),('Networking',60),('Cybersecurity',60),('Scrum',56),('Linux',43),('Node.js',37)]
compact_chart('capabilities.svg','CAPABILITIES',capabilities,'Portfolio capability self-assessments: Applied AI 68, UI/UX 65, networking 60, cybersecurity 60, Scrum 56, Linux 43, Node.js 37.')
tool_groups=[
 ('DESIGN & PROTOTYPING','Figma · Interface design · Interactive prototypes'),
 ('AI ASSISTANCE','Claude · Claude Code · AI with Python'),
 ('WEB & APIs','React · Next.js · Node.js · Vite · FastAPI'),
 ('DESKTOP & DELIVERY','PySide6 · Npcap · Inno Setup'),
 ('DATA & INFRASTRUCTURE','MySQL · PostgreSQL · Apache · Azure · Vercel'),
 ('NETWORKS & SYSTEMS','Linux · TCP/IP · Routing · Switching · Security fundamentals · Network automation'),
 ('WORKFLOW & COMMUNICATION','Scrum · Data analysis · Technical presentations'),
]
body=''
for i,(label,tools) in enumerate(tool_groups):
    x=30+(i%2)*390
    y=30+(i//2)*144
    body+=f'<g class="arrive" style="animation-delay:{i*.1}s">'
    body+=text(x,y,label,17,CYAN,600)
    for j,line in enumerate(textwrap.wrap(tools,30)):
        body+=text(x,y+32+j*28,line,22)
    body+=f'<circle class="halo" cx="{x-12}" cy="{y-6}" r="3" fill="{CYAN}" style="animation-delay:-{i}s"/></g>'
body+=scan(30,574,740)
save('tools.svg',800,590,body,'Tools: '+ '; '.join(label+': '+tools for label,tools in tool_groups))
body=''
y=26
for i,(label,tools) in enumerate(tool_groups):
    body+=text(30,y,label,20,CYAN,600)
    y+=30
    body+=f'<g class="arrive" style="animation-delay:{i*.1}s">'
    for line in textwrap.wrap(tools,43):
        body+=text(30,y,line,24)
        y+=30
    body+='</g>'+scan(30,y+2,540,i)
    y+=24
save('tools-mobile.svg',600,y,body,'Tools: '+ '; '.join(label+': '+tools for label,tools in tool_groups))
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
    uri=base64.b64encode(raw).decode('ascii')
    body=text(30,44,title,30,WHITE,650)+text(605,43,'VIEW PROJECT ↗',16,CYAN,600,True)
    body+=f'<image x="30" y="66" width="360" height="224" preserveAspectRatio="xMidYMin meet" href="data:image/png;base64,{uri}"/>'
    y=88
    for line in textwrap.wrap(description,28):
        body+=text(420,y,line,22)
        y+=28
    y+=14
    for line in textwrap.wrap(stack,31):
        body+=text(420,y,line,19,MUTED)
        y+=25
    bottom=max(300,y+12)
    body+=rect(30,bottom,740,1,DEEP)+scan(30,bottom,740)
    save(f'project-{slug}.svg',800,bottom+20,body,f'{title}: {description} {stack}','Original portfolio screenshot and project description.')
    body=text(30,42,title,31,WHITE,650)+text(30,72,'VIEW PROJECT ↗',17,CYAN,600,True)
    body+=f'<image x="30" y="88" width="540" height="220" preserveAspectRatio="xMidYMid meet" href="data:image/png;base64,{uri}"/>'
    y=342
    for line in textwrap.wrap(description,43):
        body+=text(30,y,line,24)
        y+=30
    y+=8
    for line in textwrap.wrap(stack,49):
        body+=text(30,y,line,20,MUTED)
        y+=26
    body+=scan(30,y+8,540)
    save(f'project-{slug}-mobile.svg',600,y+24,body,f'{title}: {description} {stack}','Original portfolio screenshot and project description, mobile layout.')
for slug,label in [('portfolio','PORTFOLIO & CONTACT ↗'),('linkedin','LINKEDIN ↗'),('github','GITHUB ↗')]:
    body=rect(30,8,740,46,SURFACE,DEEP)+text(48,39,label.replace(' ↗',''),23,WHITE,600)
    body+='<g class="arrow">'+text(726,39,'↗',23,CYAN,600)+'</g>'+scan(30,54,740)
    save(f'link-{slug}.svg',800,68,body,label)
print('Generated self-contained SVG artwork and functional navigation segments.')

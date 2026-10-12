# NixOS Cyber-Rice

Identidad visual original para Alberto Davis / amberlight123. Ventanas rectangulares, gaps de 12 px en el hero, bordes de 1 px, tipografía monoespaciada del sistema y fondos oscuros autocontenidos.

## Paleta

| Token | Color | Uso |
| --- | --- | --- |
| Cyan | `#18DCF9` | Texto legible e iluminación localizada |
| Electric | `#0161EA` | Ventana activa y segmentos |
| Deep | `#032999` | Estructura secundaria |
| Surface | `#02091A` | Terminales |
| Background | `#000000` | Fondo |

El texto esencial utiliza cian sobre azul casi negro; el azul eléctrico se reserva a estructura y decoración. El emblema es original: no incorpora el logo oficial de NixOS ni implica afiliación. NixOS, i3 y Polybar describen la inspiración visual, no sistemas instalados ni competencias acreditadas.

## Fuentes del contenido

- [Identidad GitHub](https://github.com/amberlight123).
- [Presentación, formación, idiomas, habilidades y contacto](https://github.com/amberlight123/portafolio/blob/main/index.html).
- [Vozelia: contexto y tecnologías](https://github.com/amberlight123/vozelia_site_personal_project/blob/main/README_CONTEXT.md).
- [Lucy: funciones y alcance](https://github.com/amberlight123/lucy-activos-utp/blob/master/docs/lucy-funciones-objetivos-alcance.md), [dependencias](https://github.com/amberlight123/lucy-activos-utp/blob/master/package.json).
- [Sabores del Mar](https://github.com/amberlight123/Sabores-del-Mar/blob/master/README.md).

Solo se publican datos ya presentes en fuentes públicas. No se publican contenidos de repositorios privados. Se conserva la condición de estudiante indicada en la formación del portafolio, sin convertir su título de portada en un grado obtenido. No se trasladan porcentajes subjetivos de habilidades.

## Diagnósticos

Corte: 2026-10-12, posterior a crear el perfil. Repositorios públicos de `amberlight123`: 6. Se excluyen `amberlight123` (perfil) y `PracticaCompiladorC` (fork) del reparto de lenguajes: Sabores-del-Mar y Vozelia → PHP; portafolio → HTML; Lucy → TypeScript. Se usa el lenguaje principal de cada repositorio informado por GitHub; no volumen de código ni dominio. Sin actividad inventada, cron ni servicios de estadísticas externos.

Actualizar los recuentos en `scripts/generate.py`, esta nota y el README cuando cambien. Verificar con `gh api users/amberlight123/repos --paginate`. Para regenerar recursos: `python scripts/generate.py` (biblioteca estándar; sin dependencias). El script no consulta APIs ni publica cambios.

## Compatibilidad y accesibilidad

SVG autocontenidos sin JavaScript, fuentes remotas, imágenes externas ni `foreignObject`. README con texto, enlaces y tablas nativas como alternativa a los gráficos. Hero móvil mediante `picture`; gráficos fluidos con `viewBox`. Todo el contenido funciona estático. Única animación: cursor discreto durante tres ciclos, desactivado con `prefers-reduced-motion`. Los módulos de barra son decorativos; la navegación funcional está en enlaces Markdown.

## Referencias de diseño

- [Polybar Themes: Hack, Cuts, Shades y Blocks](https://github.com/adi1090x/polybar-themes): separación modular y geometría angular.
- [NixOS Branding](https://github.com/NixOS/branding): referencia geométrica, sin reutilizar sus recursos.
- [Profile Signal Kit](https://github.com/saroo98/profile-signal-kit): jerarquía de recursos SVG locales.
- [SVG README](https://github.com/Wenoxxxx/svg-readme): composición autocontenida y animación opcional.

No se copia código ni se incorporan activos de estas referencias.

import os

files_to_fix = {
    "canonical-tag-generator.html": [
        ('lang="es"', 'lang="en"'),
        ("Generador de Etiquetas Canonical — PageGuides", "Canonical Tag Generator — PageGuides"),
        ("Genera etiquetas canonical perfectas (rel=canonical) para evitar problemas de contenido duplicado y consolidar tu autoridad SEO.", "Generate perfect canonical tags (rel=canonical) to avoid duplicate content issues and consolidate your SEO authority."),
        ("← Volver a Herramientas", "← Back to Tools"),
        ('Consolida la fuerza de tus páginas duplicadas o similares diciéndole a Google cuál es la versión "oficial" que debe rankear.', 'Consolidate the strength of your duplicate or similar pages by telling Google which is the "official" version to rank.'),
        ("Define tu URL Canonical", "Define your Canonical URL"),
        ("Página Principal / Original (URL Absoluta)", "Main / Original Page (Absolute URL)"),
        ("¿Dónde coloco este código?", "Where do I put this code?"),
        ("Copia el código generado y pégalo dentro de la etiqueta <code>&lt;head&gt;</code> de <strong>TODAS las páginas duplicadas</strong> (e idealmente también en la original apuntando a sí misma, es decir, un \"canonical auto-referenciado\").", "Copy the generated code and paste it inside the <code>&lt;head&gt;</code> tag of <strong>ALL duplicate pages</strong> (and ideally also on the original pointing to itself, i.e., a \"self-referencing canonical\")."),
        ("Por ejemplo, si tienes <code>/reloj?color=rojo</code>, su etiqueta canonical debería apuntar a <code>/reloj</code>.", "For example, if you have <code>/watch?color=red</code>, its canonical tag should point to <code>/watch</code>."),
        ("📋 Etiqueta HTML", "📋 HTML Tag"),
        (">Copiar<", ">Copy<"),
        ("Escribe una URL para generar la etiqueta.", "Enter a URL to generate the tag."),
        ("¡Copiado!", "Copied!"),
        ("La URL debe incluir http:// o https://", "URL must include http:// or https://"),
        ("Estás usando HTTP. Si tienes certificado SSL, es altamente recomendable usar HTTPS para la URL canonical.", "You are using HTTP. If you have an SSL certificate, it is highly recommended to use HTTPS for the canonical URL."),
        ("URL absoluta correcta con HTTPS.", "Correct absolute URL with HTTPS."),
        ("La URL usa trailing slash (bien hecho, mantén la consistencia).", "The URL uses a trailing slash (well done, maintain consistency)."),
        ("La URL contiene parámetros (?key=val). Normalmente una Canonical apunta a la URL limpia sin parámetros.", "The URL contains parameters (?key=val). Usually a Canonical points to the clean URL without parameters."),
        ("Estás usando una URL relativa. <strong>Google exige URLs absolutas</strong> completas (incluyendo https://) para las etiquetas canonical.", "You are using a relative URL. <strong>Google requires absolute URLs</strong> (including https://) for canonical tags."),
        ("Ruta de URL incompleta o inválida.", "Incomplete or invalid URL path.")
    ],
    "hreflang-tag-generator.html": [
        ('lang="es"', 'lang="en"'),
        ("Genera etiquetas hreflang válidas para SEO Internacional. Asegúrate de que Google muestre la versión correcta de tu web en cada país y en cada idioma.", "Generate valid hreflang tags for International SEO. Ensure Google shows the correct version of your site in every country and language."),
        ("← Volver a Herramientas", "← Back to Tools"),
        ("Evita problemas de contenido duplicado internacional y entrega a cada usuario la versión de tu web correcta según su idioma y región.", "Avoid international duplicate content issues and deliver the correct version of your site to each user based on their language and region."),
        ("Añade las versiones de tu página", "Add the versions of your page"),
        ("Añadir Idioma / Región", "Add Language / Region"),
        ("Importante", "Important"),
        ("Las etiquetas hreflang deben ser bidireccionales. El código generado debe ir en la sección <code>&lt;head&gt;</code> de <strong>TODAS</strong> las páginas listadas arriba por igual o incrustarse en tu Sitemap XML.", "Hreflang tags must be bidirectional. The generated code must go in the <code>&lt;head&gt;</code> section of <strong>ALL</strong> pages listed above equally, or be embedded in your XML Sitemap."),
        ("📄 Etiquetas HTML", "📄 HTML Tags"),
        (">Copiar Código<", ">Copy Code<"),
        ("Completa los campos para generar etiquetas.", "Fill in the fields to generate tags."),
        ("Completa los campos de URL para generar las etiquetas.", "Fill in the URL fields to generate the tags."),
        ("¡Copiado!", "Copied!"),
        ("Versión / Variante", "Version / Variant"),
        ("Eliminar este idioma", "Remove this language"),
        (">Idioma<", ">Language<"),
        (">Región / País (Opcional)<", ">Region / Country (Optional)<"),
        ("URL Absoluta", "Absolute URL"),

        ("Español", "Spanish"),
        ("Inglés", "English"),
        ("Francés", "French"),
        ("Alemán", "German"),
        ("Italiano", "Italian"),
        ("Portugués", "Portuguese"),
        ("Chino", "Chinese"),
        ("Japonés", "Japanese"),
        ("Ruso", "Russian"),
        ("Árabe", "Arabic"),

        ("Cualquier Región (Genérico)", "Any Region (Generic)"),
        ("España", "Spain"),
        ("México", "Mexico"),
        ("Argentina", "Argentina"),
        ("Colombia", "Colombia"),
        ("Chile", "Chile"),
        ("Perú", "Peru"),
        ("Estados Unidos", "United States"),
        ("Reino Unido", "United Kingdom"),
        ("Canadá", "Canada"),
        ("Australia", "Australia"),
        ("Francia", "France"),
        ("Alemania", "Germany"),
        ("Brasil", "Brazil")
    ],
    "htaccess-redirect-generator.html": [
        ('lang="es"', 'lang="en"'),
        ("Genera reglas de redirección 301, fuerza HTTPS o elimina las codiciadas WWW para tu archivo .htaccess sin romper tu web.", "Generate 301 redirect rules, force HTTPS or remove WWW from your URL for your .htaccess file without breaking your site."),
        ("← Volver a Herramientas", "← Back to Tools"),
        ("Genera reglas de redirección 301 seguras. Forza HTTPS, elimina WWW o redirige páginas individuales con total eficiencia.", "Generate secure 301 redirect rules. Force HTTPS, remove WWW or redirect individual pages with total efficiency."),
        ("Selecciona el tipo de redirección", "Select the type of redirect"),
        ("Redirección 301 Individual", "Individual 301 Redirect"),
        ("Forzar HTTPS (SSL)", "Force HTTPS (SSL)"),
        ("Redirigir WWW a sin-WWW", "Redirect WWW to non-WWW"),
        ("Redirigir sin-WWW a WWW", "Redirect non-WWW to WWW"),
        ("Atención", "Attention"),
        ('Haz una copia de seguridad de tu archivo <code>.htaccess</code> actual antes de aplicar estos cambios. Un pequeño error de sintaxis puede causar un "Error 500" en tu sitio web entero.', "Make a backup of your current <code>.htaccess</code> file before applying these changes. A small syntax error can cause a \"500 Error\" on your entire website."),
        ("📄 Código .htaccess", "📄 .htaccess Code"),
        (">Copiar<", ">Copy<"),
        ("Selecciona una opción para generar el código.", "Select an option to generate the code."),
        ("¡Copiado!", "Copied!"),
        ("URL Original (Ruta relativa)", "Original URL (Relative path)"),
        ("URL de Destino (Absoluta o Relativa)", "Destination URL (Absolute or Relative)"),
        ("Tu Dominio (Sin protocolo ni www)", "Your Domain (Without protocol or www)"),
        ("Redirección 301 de página antigua a nueva", "301 Redirect from old page to new"),
        ("Forzar HTTPS", "Force HTTPS"),
        ("Redirigir WWW a sin-WWW", "Redirect WWW to non-WWW"),
        ("Redirigir sin-WWW a WWW", "Redirect non-WWW to WWW")
    ]
}

for tool, replacements in files_to_fix.items():
    if not os.path.exists(tool):
        continue
    with open(tool, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for es_str, en_str in replacements:
        content = content.replace(es_str, en_str)
        
    with open(tool, 'w', encoding='utf-8') as f:
        f.write(content)

print("Files converted to English!")

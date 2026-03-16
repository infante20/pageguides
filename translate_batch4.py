import os
import re

tools_to_translate = [
    "url-slug-generator.html",
    "html-structure-auditor.html",
    "og-preview.html"
]

langs = ["es", "fr", "hi", "pt"]

def inject_dropdown(html_content, lang_code, trans_dict):
    nav_match = re.search(r'(<nav>.*?</nav>)', html_content, re.DOTALL)
    if not nav_match:
        return html_content

    nav_html = nav_match.group(1)

    lang_labels = {
        'en': '🇺🇸 EN',
        'es': '🇪🇸 ES',
        'fr': '🇫🇷 FR',
        'hi': '🇮🇳 HI',
        'pt': '🇧🇷 PT'
    }

    dropdown_html = f'''
        <div class="lang-selector">
            <button class="lang-btn" aria-haspopup="true" aria-expanded="false">
                {lang_labels.get(lang_code, lang_code.upper())}
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="6 9 12 15 18 9"></polyline>
                </svg>
            </button>
            <div class="lang-dropdown">
                <a href="../" class="lang-option {'active' if lang_code == 'en' else ''}">🇺🇸 English</a>
                <a href="../es/" class="lang-option {'active' if lang_code == 'es' else ''}">🇪🇸 Español</a>
                <a href="../fr/" class="lang-option {'active' if lang_code == 'fr' else ''}">🇫🇷 Français</a>
                <a href="../hi/" class="lang-option {'active' if lang_code == 'hi' else ''}">🇮🇳 हिन्दी</a>
                <a href="../pt/" class="lang-option {'active' if lang_code == 'pt' else ''}">🇧🇷 Português</a>
            </div>
        </div>
'''

    new_nav = f'''<nav>
        <a href="/{lang_code}/" class="logo">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
                <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
                <line x1="12" y1="22.08" x2="12" y2="12"></line>
            </svg>
            Page<span>Guides</span>
        </a>
        <div style="display: flex; align-items: center; gap: 1.5rem;">
            {dropdown_html}
            <a href="/{lang_code}/" class="back-link">
                ← {trans_dict["nav_back"]}
            </a>
        </div>
    </nav>'''

    return html_content.replace(nav_match.group(1), new_nav)

translations = {
    "es": {
        "nav_back": "Volver a Herramientas",
    },
    "fr": {
        "nav_back": "Retour aux outils",
    },
    "hi": {
        "nav_back": "उपकरणों पर वापस जाएं",
    },
    "pt": {
        "nav_back": "Voltar para Ferramentas",
    }
}

tool_translations = {
    "url-slug-generator.html": {
        "es": [
            ("URL Slug Generator — PageGuides", "Generador de Slugs URL — PageGuides"),
            ("Generate SEO-friendly slugs instantly. Convert titles to clean URLs without special characters or spaces.", "Genera slugs amigables para SEO al instante. Convierte títulos en URLs limpias sin caracteres especiales o espacios."),
            ("Remove stop words, eliminate special characters, and generate perfect links to index your content quickly.", "Elimina palabras de parada y caracteres especiales para generar enlaces perfectos y rápidos de indexar."),
            ("URL Slug Generator", "Generador de Slugs URL"),
            ("Slug Configuration", "Configuración de Slug"),
            ("Original title or phrase", "Título original o frase"),
            ("All lowercase", "Todo en minúsculas"),
            ("Remove stop words", "Eliminar palabras cortas (stop words)"),
            ("Add trailing slash (/)", "Añadir barra final (/)"),
            ("Subfolder / Domain (Optional)", "Subcarpeta / Dominio (Opcional)"),
            ("Resulting Slug", "Slug Resultante"),
            ("Your slug will appear here...", "Tu slug aparecerá aquí..."),
            ("Copy", "Copiar"),
            ("Alternatives", "Alternativas"),
            ("Without stop words", "Sin palabras cortas"),
            ("With stop words", "Con palabras cortas"),
            ("Original", "Original"),
            ("Best practices for URL structuring", "Mejores prácticas para organizar URLs"),
            ("Use hyphens (<code>-</code>) to separate words. Google does not interpret underscores (<code>_</code>) in the same way.", "Usa guiones (<code>-</code>) para separar palabras. Google no interpreta los guiones bajos (<code>_</code>) de la misma forma."),
            ("Keep the slug short and concise (max 5-7 descriptive words). Shorter URLs tend to have better CTR.", "Mantén el slug corto y conciso (máx. 5-7 palabras descriptivas). URLs más cortas suelen tener mejor CTR."),
            ("Include the main keyword as far to the left of the URL as possible.", "Incluye la palabra clave principal tan a la izquierda de la URL como sea posible."),
            ("Avoid including IDs, messy parameters, or dates, unless it is a strict news site.", "Evita incluir IDs, parámetros confusos o fechas, a menos que sea un sitio estricto de noticias.")
        ],
        "fr": [
            ("URL Slug Generator — PageGuides", "Générateur de Slugs d'URL — PageGuides"),
            ("Generate SEO-friendly slugs instantly. Convert titles to clean URLs without special characters or spaces.", "Générez instantanément des slugs optimisés pour le SEO. Convertissez les titres en URL propres sans caractères spéciaux ni espaces."),
            ("Remove stop words, eliminate special characters, and generate perfect links to index your content quickly.", "Supprimez les mots vides, éliminez les caractères spéciaux et générez des liens parfaits pour indexer rapidement votre contenu."),
            ("URL Slug Generator", "Générateur de Slugs d'URL"),
            ("Slug Configuration", "Configuration du Slug"),
            ("Original title or phrase", "Titre original ou phrase"),
            ("All lowercase", "Tout en minuscules"),
            ("Remove stop words", "Supprimer les mots vides (stop words)"),
            ("Add trailing slash (/)", "Ajouter une barre oblique finale (/)"),
            ("Subfolder / Domain (Optional)", "Sous-dossier / Domaine (Facultatif)"),
            ("Resulting Slug", "Slug Résultant"),
            ("Your slug will appear here...", "Votre slug apparaîtra ici..."),
            ("Copy", "Copier"),
            ("Alternatives", "Alternatives"),
            ("Without stop words", "Sans mots vides"),
            ("With stop words", "Avec mots vides"),
            ("Original", "Original"),
            ("Best practices for URL structuring", "Meilleures pratiques pour la structuration des URL"),
            ("Use hyphens (<code>-</code>) to separate words. Google does not interpret underscores (<code>_</code>) in the same way.", "Utilisez des tirets (<code>-</code>) pour séparer les mots. Google n'interprète pas les traits de soulignement (<code>_</code>) de la même manière."),
            ("Keep the slug short and concise (max 5-7 descriptive words). Shorter URLs tend to have better CTR.", "Gardez le slug court et concis (max 5-7 mots descriptifs). Les URL plus courtes ont tendance à avoir un meilleur taux de clics (CTR)."),
            ("Include the main keyword as far to the left of the URL as possible.", "Incluez le mot-clé principal aussi loin à gauche de l'URL que possible."),
            ("Avoid including IDs, messy parameters, or dates, unless it is a strict news site.", "Évitez d'inclure des ID, des paramètres désordonnés ou des dates, à moins qu'il ne s'agisse d'un strict site d'actualités.")
        ],
        "hi": [
            ("URL Slug Generator — PageGuides", "URL Slug जनरेटर — PageGuides"),
            ("Generate SEO-friendly slugs instantly. Convert titles to clean URLs without special characters or spaces.", "तुरंत SEO-अनुकूल स्लग जेनरेट करें। शीर्षकों को बिना विशेष वर्णों या रिक्त स्थान के साफ URL में बदलें।"),
            ("Remove stop words, eliminate special characters, and generate perfect links to index your content quickly.", "स्टॉप शब्दों को हटाएं, विशेष वर्णों को समाप्त करें, और जल्दी से अपनी सामग्री को अनुक्रमित करने के लिए सही लिंक उत्पन्न करें।"),
            ("URL Slug Generator", "URL Slug जनरेटर"),
            ("Slug Configuration", "Slug कॉन्फ़िगरेशन"),
            ("Original title or phrase", "मूल शीर्षक या वाक्यांश"),
            ("All lowercase", "सभी छोटे अक्षर"),
            ("Remove stop words", "स्टॉप वर्ण निकालें"),
            ("Add trailing slash (/)", "अंत में स्लैश (/) जोड़ें"),
            ("Subfolder / Domain (Optional)", "सबफ़ोल्डर / डोमेन (वैकल्पिक)"),
            ("Resulting Slug", "परिणामस्वरुप स्लग"),
            ("Your slug will appear here...", "आपका स्लग यहाँ दिखाई देगा..."),
            ("Copy", "कॉपी करें"),
            ("Alternatives", "विकल्प"),
            ("Without stop words", "स्टॉप शब्दों के बिना"),
            ("With stop words", "स्टॉप शब्दों के साथ"),
            ("Original", "असली"),
            ("Best practices for URL structuring", "यूआरएल संरचना के लिए सर्वश्रेष्ठ अभ्यास"),
            ("Use hyphens (<code>-</code>) to separate words. Google does not interpret underscores (<code>_</code>) in the same way.", "शब्दों को अलग करने के लिए हाइफ़न (<code>-</code>) का प्रयोग करें। गूगल अंडरस्कोर (<code>_</code>) को उसी तरह नहीं समझता।"),
            ("Keep the slug short and concise (max 5-7 descriptive words). Shorter URLs tend to have better CTR.", "स्लग को छोटा और संक्षिप्त रखें (अधिकतम 5-7 वर्णनात्मक शब्द)। छोटे URLs की CTR बेहतर होती है।"),
            ("Include the main keyword as far to the left of the URL as possible.", "URL में यथासंभव बाईं ओर मुख्य कीवर्ड शामिल करें।"),
            ("Avoid including IDs, messy parameters, or dates, unless it is a strict news site.", "आईडी, मेसी पैरामीटर, या तारीखों को शामिल करने से बचें, जब तक कि यह एक कठिन समाचार वेबसाइट न हो।")
        ],
        "pt": [
            ("URL Slug Generator — PageGuides", "Gerador de Slugs URL — PageGuides"),
            ("Generate SEO-friendly slugs instantly. Convert titles to clean URLs without special characters or spaces.", "Gere slugs amigáveis para SEO instantaneamente. Converta títulos em URLs limpas sem caracteres especiais ou espaços."),
            ("Remove stop words, eliminate special characters, and generate perfect links to index your content quickly.", "Remova as palavras curtas (stop words) e caracteres especiais para gerar links perfeitos e rápidos de indexar."),
            ("URL Slug Generator", "Gerador de Slugs URL"),
            ("Slug Configuration", "Configuração do Slug"),
            ("Original title or phrase", "Título original ou frase"),
            ("All lowercase", "Tudo em letras minúsculas"),
            ("Remove stop words", "Remover palavras curtas (stop words)"),
            ("Add trailing slash (/)", "Adicionar barra final (/)"),
            ("Subfolder / Domain (Optional)", "Subpasta / Domínio (Opcional)"),
            ("Resulting Slug", "Slug Resultante"),
            ("Your slug will appear here...", "Seu slug aparecerá aqui..."),
            ("Copy", "Copiar"),
            ("Alternatives", "Alternativas"),
            ("Without stop words", "Sem palavras curtas"),
            ("With stop words", "Com palavras curtas"),
            ("Original", "Original"),
            ("Best practices for URL structuring", "Melhores práticas para estruturar URLs"),
            ("Use hyphens (<code>-</code>) to separate words. Google does not interpret underscores (<code>_</code>) in the same way.", "Use hifens (<code>-</code>) para separar palavras. O Google não interpreta subtraços (<code>_</code>) da mesma maneira."),
            ("Keep the slug short and concise (max 5-7 descriptive words). Shorter URLs tend to have better CTR.", "Mantenha o slug curto e conciso (máx 5-7 palavras descritivas). URLs mais curtas tendem a ter um CTR melhor."),
            ("Include the main keyword as far to the left of the URL as possible.", "Inclua a palavra-chave principal o mais à esquerda possível da URL."),
            ("Avoid including IDs, messy parameters, or dates, unless it is a strict news site.", "Evite incluir IDs, parâmetros confusos ou datas, a menos que seja um site estrito de notícias.")
        ]
    },
    "html-structure-auditor.html": {
        "es": [
            ("HTML Structure Auditor — PageGuides", "Auditor de Estructura HTML — PageGuides"),
            ("Validate your H1-H6 heading hierarchy. Ensure your page has a perfect semantic structure for Google.", "Valida tu jerarquía de encabezados H1-H6. Asegúrate de que tu página tenga una estructura semántica perfecta para Google."),
            ("Analyze the heading hierarchy and HTML structure of your page to detect on-page SEO issues instantly.", "Analiza la jerarquía de encabezados y la estructura HTML de tu página para detectar problemas de SEO on-page al instante."),
            ("HTML Structure Auditor", "Auditor de Estructura HTML"),
            ("Paste your HTML code here", "Pega tu código HTML aquí"),
            ("Audit Structure", "Auditar Estructura"),
            ("Hierarchy Schema Detected", "Esquema de Jerarquía Detectado"),
            ("Headings", "Encabezados"),
            ("No heading tags (H1-H6) detected in the provided code.", "No se detectaron etiquetas de encabezado (H1-H6) en el código proporcionado."),
            ("Multiple H1s detected. Google recommends only one per page.", "Múltiples H1 detectados. Google recomienda solo uno por página."),
            ("Level jump detected", "Salto de nivel detectado"),
            ("Maintain sequential hierarchy.", "Mantén una jerarquía secuencial.")
        ],
        "fr": [
            ("HTML Structure Auditor — PageGuides", "Auditeur de Structure HTML — PageGuides"),
            ("Validate your H1-H6 heading hierarchy. Ensure your page has a perfect semantic structure for Google.", "Validez votre hiérarchie de titres H1-H6. Assurez-vous que votre page a une structure sémantique parfaite pour Google."),
            ("Analyze the heading hierarchy and HTML structure of your page to detect on-page SEO issues instantly.", "Analysez la hiérarchie des titres et la structure HTML de votre page pour détecter instantanément les problèmes de SEO on-page."),
            ("HTML Structure Auditor", "Auditeur de Structure HTML"),
            ("Paste your HTML code here", "Collez votre code HTML ici"),
            ("Audit Structure", "Auditer la Structure"),
            ("Hierarchy Schema Detected", "Schéma de Hiérarchie Détecté"),
            ("Headings", "Titres"),
            ("No heading tags (H1-H6) detected in the provided code.", "Aucune balise de titre (H1-H6) n'a été détectée dans le code fourni."),
            ("Multiple H1s detected. Google recommends only one per page.", "Plusieurs H1 détectés. Google n'en recommande qu'un seul par page."),
            ("Level jump detected", "Saut de niveau détecté"),
            ("Maintain sequential hierarchy.", "Maintenez une hiérarchie séquentielle.")
        ],
        "hi": [
            ("HTML Structure Auditor — PageGuides", "HTML संरचना ऑडिटर — PageGuides"),
            ("Validate your H1-H6 heading hierarchy. Ensure your page has a perfect semantic structure for Google.", "अपने H1-H6 हेडिंग पदानुक्रम को मान्य करें। सुनिश्चित करें कि आपके पृष्ठ में Google के लिए एक आदर्श अर्थ संरचना है।"),
            ("Analyze the heading hierarchy and HTML structure of your page to detect on-page SEO issues instantly.", "पेज-ऑन एसईओ मुद्दों का तुरंत पता लगाने के लिए अपने पेज के शीर्षक पदानुक्रम और एचटीएमएल संरचना का विश्लेषण करें।"),
            ("HTML Structure Auditor", "HTML संरचना ऑडिटर"),
            ("Paste your HTML code here", "अपना HTML कोड यहां पेस्ट करें"),
            ("Audit Structure", "ऑडिट संरचना"),
            ("Hierarchy Schema Detected", "पदानुक्रम योजना का पता चला"),
            ("Headings", "हेडिंग"),
            ("No heading tags (H1-H6) detected in the provided code.", "प्रदान किए गए कोड में कोई हेडिंग टैग (H1-H6) का पता नहीं चला।"),
            ("Multiple H1s detected. Google recommends only one per page.", "कई H1 का पता चला। Google प्रति पृष्ठ केवल एक ही अनुशंसा करता है।"),
            ("Level jump detected", "स्तर में कूद का पता चला"),
            ("Maintain sequential hierarchy.", "क्रमिक पदानुक्रम बनाए रखें।")
        ],
        "pt": [
            ("HTML Structure Auditor — PageGuides", "Auditor de Estrutura HTML — PageGuides"),
            ("Validate your H1-H6 heading hierarchy. Ensure your page has a perfect semantic structure for Google.", "Valide sua hierarquia de cabeçalhos H1-H6. Garanta que sua página tenha uma estrutura semântica perfeita para o Google."),
            ("Analyze the heading hierarchy and HTML structure of your page to detect on-page SEO issues instantly.", "Analise a hierarquia de cabeçalhos e a estrutura HTML de sua página para detectar instantaneamente problemas de SEO on-page."),
            ("HTML Structure Auditor", "Auditor de Estrutura HTML"),
            ("Paste your HTML code here", "Cole aqui o seu código HTML"),
            ("Audit Structure", "Auditar Estrutura"),
            ("Hierarchy Schema Detected", "Esquema de Hierarquia Detectado"),
            ("Headings", "Cabeçalhos"),
            ("No heading tags (H1-H6) detected in the provided code.", "Nenhuma tag de cabeçalho (H1-H6) foi detectada no código fornecido."),
            ("Multiple H1s detected. Google recommends only one per page.", "Vários H1s detectados. O Google recomenda apenas um por página."),
            ("Level jump detected", "Salto de nível detectado"),
            ("Maintain sequential hierarchy.", "Mantenha uma hierarquia sequencial.")
        ]
    },
    "og-preview.html": {
        "es": [
            ("Open Graph Preview — PageGuides", "Vista Previa Open Graph — PageGuides"),
            ("Preview how your page will look when shared on Twitter/X, Facebook, and LinkedIn. Generate OG meta tags ready to copy.", "Visualiza cómo se verá tu página al compartirla en Twitter/X, Facebook y LinkedIn. Genera etiquetas meta OG listas para copiar."),
            ("Preview and generate your Open Graph meta tags to dazzle on Twitter/X, Facebook, and LinkedIn.", "Visualiza y genera tus etiquetas meta Open Graph para destacar en Twitter/X, Facebook y LinkedIn."),
            ("Open Graph Preview", "Vista Previa Open Graph"),
            ("OG Title", "Título OG"),
            ("The title they will see when sharing", "El título que verán al compartir"),
            ("OG Description", "Descripción OG"),
            ("Engaging description (max 160 characters)", "Descripción atractiva (máx 160 caracteres)"),
            ("Page URL", "URL de la Página"),
            ("Image URL (1200×630 recommended)", "URL de la Imagen (1200×630 recomendada)"),
            ("Content Type", "Tipo de Contenido"),
            ("Website (website)", "Sitio web (website)"),
            ("Article (article)", "Artículo (article)"),
            ("Product (product)", "Producto (product)"),
            ("Video (video.other)", "Vídeo (video.other)"),
            ("Site Name", "Nombre del Sitio"),
            ("HTML Meta Tags Code", "Código de Meta Etiquetas HTML"),
            ("Copy Code", "Copiar Código")
        ],
        "fr": [
            ("Open Graph Preview — PageGuides", "Aperçu Open Graph — PageGuides"),
            ("Preview how your page will look when shared on Twitter/X, Facebook, and LinkedIn. Generate OG meta tags ready to copy.", "Prévisualisez l'apparence de votre page lorsqu'elle est partagée sur Twitter/X, Facebook et LinkedIn. Générez des balises méta OG prêtes à être copiées."),
            ("Preview and generate your Open Graph meta tags to dazzle on Twitter/X, Facebook, and LinkedIn.", "Prévisualisez et générez vos balises méta Open Graph pour éblouir sur Twitter/X, Facebook et LinkedIn."),
            ("Open Graph Preview", "Aperçu Open Graph"),
            ("OG Title", "Titre OG"),
            ("The title they will see when sharing", "Le titre qu'ils verront en partageant"),
            ("OG Description", "Description OG"),
            ("Engaging description (max 160 characters)", "Description attrayante (max 160 caractères)"),
            ("Page URL", "URL de la Page"),
            ("Image URL (1200×630 recommended)", "URL de l'Image (1200×630 recommandé)"),
            ("Content Type", "Type de Contenu"),
            ("Website (website)", "Site web (website)"),
            ("Article (article)", "Article (article)"),
            ("Product (product)", "Produit (product)"),
            ("Video (video.other)", "Vidéo (video.other)"),
            ("Site Name", "Nom du Site"),
            ("HTML Meta Tags Code", "Code de Balises Méta HTML"),
            ("Copy Code", "Copier le Code")
        ],
        "hi": [
            ("Open Graph Preview — PageGuides", "ओपन ग्राफ पूर्वावलोकन — PageGuides"),
            ("Preview how your page will look when shared on Twitter/X, Facebook, and LinkedIn. Generate OG meta tags ready to copy.", "पूर्वावलोकन करें कि ट्विटर/X, फेसबुक और लिंक्डइन पर साझा किए जाने पर आपका पेज कैसा दिखेगा। कॉपी करने के लिए तैयार OG मेटा टैग उत्पन्न करें।"),
            ("Preview and generate your Open Graph meta tags to dazzle on Twitter/X, Facebook, and LinkedIn.", "ट्विटर/X, फेसबुक और लिंक्डइन पर चकाचौंध करने के लिए अपने ओपन ग्राफ मेटा टैग का पूर्वावलोकन करें और उत्पन्न करें।"),
            ("Open Graph Preview", "ओपन ग्राफ पूर्वावलोकन"),
            ("OG Title", "OG शीर्षक"),
            ("The title they will see when sharing", "साझा करते समय उन्हें जो शीर्षक दिखाई देगा"),
            ("OG Description", "OG विवरण"),
            ("Engaging description (max 160 characters)", "आकर्षक विवरण (अधिकतम 160 वर्ण)"),
            ("Page URL", "पृष्ठ URL"),
            ("Image URL (1200×630 recommended)", "छवि URL (1200×630 की अनुशंसा की जाती है)"),
            ("Content Type", "सामग्री का प्रकार"),
            ("Website (website)", "वेबसाइट (website)"),
            ("Article (article)", "लेख (article)"),
            ("Product (product)", "उत्पाद (product)"),
            ("Video (video.other)", "वीडियो (video.other)"),
            ("Site Name", "साइट का नाम"),
            ("HTML Meta Tags Code", "HTML मेटा टैग कोड"),
            ("Copy Code", "कॉपी कोड")
        ],
        "pt": [
            ("Open Graph Preview — PageGuides", "Visualização Open Graph — PageGuides"),
            ("Preview how your page will look when shared on Twitter/X, Facebook, and LinkedIn. Generate OG meta tags ready to copy.", "Visualize como será a aparência da sua página ao ser compartilhada no Twitter/X, Facebook e LinkedIn. Gere tags meta OG prontas para copiar."),
            ("Preview and generate your Open Graph meta tags to dazzle on Twitter/X, Facebook, and LinkedIn.", "Visualize e gere suas tags meta Open Graph para impressionar no Twitter/X, Facebook e LinkedIn."),
            ("Open Graph Preview", "Visualização Open Graph"),
            ("OG Title", "Título OG"),
            ("The title they will see when sharing", "O título que verão ao compartilhar"),
            ("OG Description", "Descrição OG"),
            ("Engaging description (max 160 characters)", "Descrição envolvente (máx 160 caracteres)"),
            ("Page URL", "URL da Página"),
            ("Image URL (1200×630 recommended)", "URL da Imagem (1200×630 recomendado)"),
            ("Content Type", "Tipo de Conteúdo"),
            ("Website (website)", "Site da Web (website)"),
            ("Article (article)", "Artigo (article)"),
            ("Product (product)", "Produto (product)"),
            ("Video (video.other)", "Vídeo (video.other)"),
            ("Site Name", "Nome do Site"),
            ("HTML Meta Tags Code", "Código de Tags Meta HTML"),
            ("Copy Code", "Copiar Código")
        ]
    }
}

def translate_file(filepath, tool_name):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    for lang in langs:
        lang_html = html
        tr = translations[lang]
        
        # Inject custom Dropdown & Fix Links
        lang_html = inject_dropdown(lang_html, lang, tr)
        lang_html = lang_html.replace('lang="en"', f'lang="{lang}"')

        # Translate strings using tool_translations specific arrays (reverse sorted by length to prevent partial matches replacing things)
        t_strings = tool_translations.get(tool_name, {}).get(lang, [])
        t_strings_sorted = sorted(t_strings, key=lambda x: len(x[0]), reverse=True)
        for en_str, t_str in t_strings_sorted:
            lang_html = lang_html.replace(en_str, t_str)
            
        # Write output file to lang folder
        out_dir = os.path.join(os.path.dirname(filepath), lang)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, tool_name)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(lang_html)

for tool in tools_to_translate:
    translate_file(tool, tool)

print("Successfully generated translations for batch 4")

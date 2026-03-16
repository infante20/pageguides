import os
import re

tools_to_translate = [
    "xml-sitemap-generator.html",
    "robots-generator.html",
    "schema-generator.html"
]

langs = ["es", "fr", "hi", "pt"]

def inject_dropdown(html_content, lang_code, trans_dict):
    nav_match = re.search(r'(<nav>.*?</nav>)', html_content, re.DOTALL)
    if not nav_match:
        return html_content

    nav_html = nav_match.group(1)

    # Dictionary mapping language code to human-readable label and flag
    lang_labels = {
        'en': '🇺🇸 EN',
        'es': '🇪🇸 ES',
        'fr': '🇫🇷 FR',
        'hi': '🇮🇳 HI',
        'pt': '🇧🇷 PT'
    }

    # Generate language selector HTML
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

    # Reconstruct nav
    # The original nav has: logo, then back-link.
    # We want logo, dropdown, back-link.
    logo_regex = r'(<a href="/" class="logo">.*?</a>)'
    
    # Let's completely rewrite the nav content to ensure proper placement
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

# Custom translations for Batch 3
translations = {
    "es": {
        "nav_back": "Volver a Herramientas",
        "lang": "es",
        "footer": "&copy; <span id=\"time\"></span> PageGuides.com — StudioLimb Creative Suite"
    },
    "fr": {
        "nav_back": "Retour aux outils",
        "lang": "fr",
        "footer": "&copy; <span id=\"time\"></span> PageGuides.com — StudioLimb Creative Suite"
    },
    "hi": {
        "nav_back": "उपकरणों पर वापस जाएं",
        "lang": "hi",
        "footer": "&copy; <span id=\"time\"></span> PageGuides.com — StudioLimb Creative Suite"
    },
    "pt": {
        "nav_back": "Voltar para Ferramentas",
        "lang": "pt",
        "footer": "&copy; <span id=\"time\"></span> PageGuides.com — StudioLimb Creative Suite"
    }
}

tool_translations = {
    "xml-sitemap-generator.html": {
        "es": [
            ("XML Sitemap Generator — PageGuides", "Generador de Sitemap XML — PageGuides"),
            ("Generate a valid XML Sitemap for Google quickly. Just paste your URLs and get your sitemap ready to submit to Search Console.", "Genera un Sitemap XML válido para Google rápidamente. Sólo pega tus URLs y obtén tu sitemap listo para enviar a Search Console."),
            ("Convert a list of URLs into a structured XML Sitemap ready to be indexed by search engines.", "Convierte una lista de URLs en un Sitemap XML estructurado listo para ser indexado por los motores de búsqueda."),
            ("XML Sitemap Generator", "Generador de Sitemap XML"),
            ("URLs & Configuration", "URLs y Configuración"),
            ("List of URLs (One per line)", "Lista de URLs (Una por línea)"),
            ("URLs", "URLs"),
            ("Change frequency", "Frecuencia de cambio"),
            ("Do not include", "No incluir"),
            ("Always", "Siempre"),
            ("Hourly", "Cada hora"),
            ("Daily", "Diariamente"),
            ("Weekly", "Semanalmente"),
            ("Monthly", "Mensualmente"),
            ("Yearly", "Anualmente"),
            ("Never", "Nunca"),
            ("Default Priority", "Prioridad por defecto"),
            ("1.0 (Maximum)", "1.0 (Máxima)"),
            ("Include current date (lastmod)", "Incluir fecha actual (lastmod)"),
            ("Generate Sitemap", "Generar Sitemap"),
            ("Download", "Descargar"),
            ("Copy", "Copiar"),
            ("Valid URLs", "URLs válidas"),
            ("Approx. Size", "Tamaño aprox."),
            ("Your XML code will appear here...", "Tu código XML aparecerá aquí...")
        ],
        "fr": [
            ("XML Sitemap Generator — PageGuides", "Générateur de Sitemap XML — PageGuides"),
            ("Generate a valid XML Sitemap for Google quickly. Just paste your URLs and get your sitemap ready to submit to Search Console.", "Générez rapidement un Sitemap XML valide pour Google. Collez simplement vos URL et obtenez votre sitemap prêt à être soumis à la Search Console."),
            ("Convert a list of URLs into a structured XML Sitemap ready to be indexed by search engines.", "Convertissez une liste d'URL en un Sitemap XML structuré prêt à être indexé par les moteurs de recherche."),
            ("XML Sitemap Generator", "Générateur de Sitemap XML"),
            ("URLs & Configuration", "URL et Configuration"),
            ("List of URLs (One per line)", "Liste d'URL (Une par ligne)"),
            ("URLs", "URL"),
            ("Change frequency", "Fréquence de modification"),
            ("Do not include", "Ne pas inclure"),
            ("Always", "Toujours"),
            ("Hourly", "Toutes les heures"),
            ("Daily", "Quotidiennement"),
            ("Weekly", "Hebdomadairement"),
            ("Monthly", "Mensuellement"),
            ("Yearly", "Annuellement"),
            ("Never", "Jamais"),
            ("Default Priority", "Priorité par défaut"),
            ("1.0 (Maximum)", "1.0 (Maximum)"),
            ("Include current date (lastmod)", "Inclure la date actuelle (lastmod)"),
            ("Generate Sitemap", "Générer le Sitemap"),
            ("Download", "Télécharger"),
            ("Copy", "Copier"),
            ("Valid URLs", "URL valides"),
            ("Approx. Size", "Taille approx."),
            ("Your XML code will appear here...", "Votre code XML apparaîtra ici...")
        ],
        "hi": [
            ("XML Sitemap Generator — PageGuides", "XML साइटमैप जेनरेटर — PageGuides"),
            ("Generate a valid XML Sitemap for Google quickly. Just paste your URLs and get your sitemap ready to submit to Search Console.", "Google के लिए जल्दी से एक वैध XML साइटमैप तैयार करें। बस अपने URL पेस्ट करें और अपना साइटमैप खोज कंसोल में सबमिट करने के लिए तैयार प्राप्त करें।"),
            ("Convert a list of URLs into a structured XML Sitemap ready to be indexed by search engines.", "URL की एक सूची को संरचित XML साइटमैप में बदलें जो खोज इंजन द्वारा अनुक्रमित होने के लिए तैयार हो।"),
            ("XML Sitemap Generator", "XML साइटमैप जेनरेटर"),
            ("URLs & Configuration", "URL और कॉन्फ़िगरेशन"),
            ("List of URLs (One per line)", "URL की सूची (प्रति पंक्ति एक)"),
            ("URLs", "URL"),
            ("Change frequency", "परिवर्तन आवृत्ति"),
            ("Do not include", "शामिल न करें"),
            ("Always", "हमेशा"),
            ("Hourly", "प्रति घंटा"),
            ("Daily", "दैनिक"),
            ("Weekly", "साप्ताहिक"),
            ("Monthly", "मासिक"),
            ("Yearly", "वार्षिक"),
            ("Never", "कभी नहीं"),
            ("Default Priority", "डिफ़ॉल्ट प्राथमिकता"),
            ("1.0 (Maximum)", "1.0 (अधिकतम)"),
            ("Include current date (lastmod)", "वर्तमान तिथि शामिल करें (lastmod)"),
            ("Generate Sitemap", "साइटमैप जेनरेट करें"),
            ("Download", "डाउनलोड करें"),
            ("Copy", "कॉपी करें"),
            ("Valid URLs", "वैध URL"),
            ("Approx. Size", "अनुमानित आकार"),
            ("Your XML code will appear here...", "आपका XML कोड यहां दिखाई देगा...")
        ],
        "pt": [
            ("XML Sitemap Generator — PageGuides", "Gerador de Sitemap XML — PageGuides"),
            ("Generate a valid XML Sitemap for Google quickly. Just paste your URLs and get your sitemap ready to submit to Search Console.", "Gere rapidamente um Sitemap XML válido para o Google. Cole seus URLs e tenha seu sitemap pronto para enviar ao Search Console."),
            ("Convert a list of URLs into a structured XML Sitemap ready to be indexed by search engines.", "Converta uma lista de URLs em um Sitemap XML estruturado pronto para ser indexado por mecanismos de busca."),
            ("XML Sitemap Generator", "Gerador de Sitemap XML"),
            ("URLs & Configuration", "URLs e Configuração"),
            ("List of URLs (One per line)", "Lista de URLs (Um por linha)"),
            ("URLs", "URLs"),
            ("Change frequency", "Frequência de alteração"),
            ("Do not include", "Não incluir"),
            ("Always", "Sempre"),
            ("Hourly", "De hora em hora"),
            ("Daily", "Diariamente"),
            ("Weekly", "Semanalmente"),
            ("Monthly", "Mensalmente"),
            ("Yearly", "Anualmente"),
            ("Never", "Nunca"),
            ("Default Priority", "Prioridade Padrão"),
            ("1.0 (Maximum)", "1.0 (Máximo)"),
            ("Include current date (lastmod)", "Incluir data atual (lastmod)"),
            ("Generate Sitemap", "Gerar Sitemap"),
            ("Download", "Baixar"),
            ("Copy", "Copiar"),
            ("Valid URLs", "URLs Válidos"),
            ("Approx. Size", "Tamanho Aprox."),
            ("Your XML code will appear here...", "Seu código XML aparecerá aqui...")
        ]
    },
    "robots-generator.html": {
        "es": [
            ("Robots.txt Generator — PageGuides", "Generador de Robots.txt — PageGuides"),
            ("Generate your robots.txt file visually. Control which pages are indexed by Google, Bing, and other bots.", "Genera tu archivo robots.txt visualmente. Controla qué páginas son indexadas por Google, Bing y otros bots."),
            ("Generate your robots.txt file visually. Control exactly which areas of your site search engines can explore.", "Genera tu archivo robots.txt visualmente. Controla exactamente qué áreas de tu sitio web pueden explorar los motores de búsqueda."),
            ("Robots.txt Generator", "Generador de Robots.txt"),
            ("Bot Configuration", "Configuración del Bot"),
            ("All (*)", "Todos (*)"),
            ("Access Rules", "Reglas de Acceso"),
            ("+ Add", "+ Añadir"),
            ("Allow", "Permitir (Allow)"),
            ("Disallow", "Denegar (Disallow)"),
            ("Sitemap & Options", "Sitemap y Opciones"),
            ("Sitemap XML URL", "URL del Sitemap XML"),
            ("Crawl-delay (seconds, optional)", "Retraso de rastreo (segundos, opcional)"),
            ("generated robots.txt", "robots.txt generado"),
            ("Download", "Descargar"),
            ("Copy", "Copiar")
        ],
        "fr": [
            ("Robots.txt Generator — PageGuides", "Générateur de Robots.txt — PageGuides"),
            ("Generate your robots.txt file visually. Control which pages are indexed by Google, Bing, and other bots.", "Générez visuellement votre fichier robots.txt. Contrôlez quelles pages sont indexées par Google, Bing et d'autres bots."),
            ("Generate your robots.txt file visually. Control exactly which areas of your site search engines can explore.", "Générez visuellement votre fichier robots.txt. Contrôlez exactement quelles zones de votre site les moteurs de recherche peuvent explorer."),
            ("Robots.txt Generator", "Générateur de Robots.txt"),
            ("Bot Configuration", "Configuration du Bot"),
            ("All (*)", "Tous (*)"),
            ("Access Rules", "Règles d'Accès"),
            ("+ Add", "+ Ajouter"),
            ("Allow", "Autoriser (Allow)"),
            ("Disallow", "Interdire (Disallow)"),
            ("Sitemap & Options", "Sitemap et Options"),
            ("Sitemap XML URL", "URL du Sitemap XML"),
            ("Crawl-delay (seconds, optional)", "Délai d'exploration (secondes, facultatif)"),
            ("generated robots.txt", "robots.txt généré"),
            ("Download", "Télécharger"),
            ("Copy", "Copier")
        ],
        "hi": [
            ("Robots.txt Generator — PageGuides", "Robots.txt जेनरेटर — PageGuides"),
            ("Generate your robots.txt file visually. Control which pages are indexed by Google, Bing, and other bots.", "अपने robots.txt फ़ाइल को दृश्य रूप से उत्पन्न करें। नियंत्रण में रखें कि Google, Bing और अन्य बॉट द्वारा कौन-से पृष्ठ अनुक्रमित किए जाते हैं।"),
            ("Generate your robots.txt file visually. Control exactly which areas of your site search engines can explore.", "अपने robots.txt फ़ाइल को दृश्य रूप से उत्पन्न करें। नियंत्रण रखें कि खोज इंजन आपकी साइट के कौन-से क्षेत्रों का पता लगा सकते हैं।"),
            ("Robots.txt Generator", "Robots.txt जेनरेटर"),
            ("Bot Configuration", "बॉट कॉन्फ़िगरेशन"),
            ("All (*)", "सभी (*)"),
            ("Access Rules", "पहुंच नियम"),
            ("+ Add", "+ जोड़ें"),
            ("Allow", "अनुमति दें (Allow)"),
            ("Disallow", "अस्वीकार करें (Disallow)"),
            ("Sitemap & Options", "साइटमैप और विकल्प"),
            ("Sitemap XML URL", "साइटमैप XML URL"),
            ("Crawl-delay (seconds, optional)", "क्रॉल-देरी (सेकंड, वैकल्पिक)"),
            ("generated robots.txt", "उत्पन्न robots.txt"),
            ("Download", "डाउनलोड करें"),
            ("Copy", "कॉपी करें")
        ],
        "pt": [
            ("Robots.txt Generator — PageGuides", "Gerador de Robots.txt — PageGuides"),
            ("Generate your robots.txt file visually. Control which pages are indexed by Google, Bing, and other bots.", "Gere seu arquivo robots.txt visualmente. Controle quais páginas são indexadas pelo Google, Bing e outros bots."),
            ("Generate your robots.txt file visually. Control exactly which areas of your site search engines can explore.", "Gere seu arquivo robots.txt visualmente. Controle exatamente quais áreas do seu site os motores de busca podem explorar."),
            ("Robots.txt Generator", "Gerador de Robots.txt"),
            ("Bot Configuration", "Configuração do Bot"),
            ("All (*)", "Todos (*)"),
            ("Access Rules", "Regras de Acesso"),
            ("+ Add", "+ Adicionar"),
            ("Allow", "Permitir (Allow)"),
            ("Disallow", "Proibir (Disallow)"),
            ("Sitemap & Options", "Sitemap e Opções"),
            ("Sitemap XML URL", "URL do Sitemap XML"),
            ("Crawl-delay (seconds, optional)", "Atraso de rastreamento (segundos, opcional)"),
            ("generated robots.txt", "robots.txt gerado"),
            ("Download", "Baixar"),
            ("Copy", "Copiar")
        ]
    },
    "schema-generator.html": {
        "es": [
            ("JSON-LD Schema Generator — PageGuides", "Generador de Schema JSON-LD — PageGuides"),
            ("Generate professional Schema.org markup (JSON-LD) for FAQs, Articles, and Local Businesses. Improve your visibility and CTR on Google.", "Genera marcado profesional de Schema.org (JSON-LD) para FAQs, Artículos y Negocios Locales. Mejora tu visibilidad y CTR en Google."),
            ("Generate valid structured data ready for Google. Increase your chances of getting Rich Snippets.", "Genera datos estructurados válidos listos para Google. Aumenta tus posibilidades de obtener Fragmentos Enriquecidos."),
            ("JSON-LD Schema Generator", "Generador de Schema JSON-LD"),
            ("Schema Type", "Tipo de Schema"),
            ("Frequently Asked Questions (FAQPage)", "Preguntas Frecuentes (FAQPage)"),
            ("Blog Article (Article)", "Artículo de Blog (Article)"),
            ("Local Business (LocalBusiness)", "Negocio Local (LocalBusiness)"),
            ("Questions and Answers", "Preguntas y Respuestas"),
            ("+ Add Question", "+ Añadir Pregunta"),
            ("Article Data", "Datos del Artículo"),
            ("Headline", "Titular"),
            ("Main Image URL", "URL de Imagen Principal"),
            ("Author / Writer", "Autor / Escritor"),
            ("Publisher (Site Logo URL)", "Editor (URL del Logo del Sitio)"),
            ("Publication Date", "Fecha de Publicación"),
            ("Business Information", "Información del Negocio"),
            ("Business Name", "Nombre del Negocio"),
            ("Image or Photo URL", "URL de Imagen o Foto"),
            ("Phone", "Teléfono"),
            ("Address", "Dirección"),
            ("JSON-LD Code", "Código JSON-LD"),
            ("Copy Code", "Copiar Código")
        ],
        "fr": [
            ("JSON-LD Schema Generator — PageGuides", "Générateur de Schema JSON-LD — PageGuides"),
            ("Generate professional Schema.org markup (JSON-LD) for FAQs, Articles, and Local Businesses. Improve your visibility and CTR on Google.", "Générez un balisage professionnel Schema.org (JSON-LD) pour les FAQ, Articles et Entreprises Locales. Améliorez votre visibilité et CTR sur Google."),
            ("Generate valid structured data ready for Google. Increase your chances of getting Rich Snippets.", "Générez des données structurées valides prêtes pour Google. Augmentez vos chances d'obtenir des Rich Snippets."),
            ("JSON-LD Schema Generator", "Générateur de Schema JSON-LD"),
            ("Schema Type", "Type de Schema"),
            ("Frequently Asked Questions (FAQPage)", "Foire Aux Questions (FAQPage)"),
            ("Blog Article (Article)", "Article de Blog (Article)"),
            ("Local Business (LocalBusiness)", "Entreprise Locale (LocalBusiness)"),
            ("Questions and Answers", "Questions et Réponses"),
            ("+ Add Question", "+ Ajouter une Question"),
            ("Article Data", "Données de l'Article"),
            ("Headline", "Titre"),
            ("Main Image URL", "URL de l'Image Principale"),
            ("Author / Writer", "Auteur / Écrivain"),
            ("Publisher (Site Logo URL)", "Éditeur (URL du Logo du Site)"),
            ("Publication Date", "Date de Publication"),
            ("Business Information", "Informations sur l'Entreprise"),
            ("Business Name", "Nom de l'Entreprise"),
            ("Image or Photo URL", "URL de l'Image ou Photo"),
            ("Phone", "Téléphone"),
            ("Address", "Adresse"),
            ("JSON-LD Code", "Code JSON-LD"),
            ("Copy Code", "Copier le Code")
        ],
        "hi": [
            ("JSON-LD Schema Generator — PageGuides", "JSON-LD Schema जेनरेटर — PageGuides"),
            ("Generate professional Schema.org markup (JSON-LD) for FAQs, Articles, and Local Businesses. Improve your visibility and CTR on Google.", "FAQ, लेखों और स्थानीय व्यवसायों के लिए पेशेवर Schema.org मार्कअप (JSON-LD) उत्पन्न करें। Google पर अपनी दृश्यता और CTR में सुधार करें।"),
            ("Generate valid structured data ready for Google. Increase your chances of getting Rich Snippets.", "Google के लिए तैयार वैध संरचित डेटा उत्पन्न करें। रिच स्निपेट्स प्राप्त करने की अपनी संभावनाओं को बढ़ाएं।"),
            ("JSON-LD Schema Generator", "JSON-LD Schema जेनरेटर"),
            ("Schema Type", "Schema प्रकार"),
            ("Frequently Asked Questions (FAQPage)", "अक्सर पूछे जाने वाले प्रश्न (FAQPage)"),
            ("Blog Article (Article)", "ब्लॉग लेख (Article)"),
            ("Local Business (LocalBusiness)", "स्थानीय व्यापार (LocalBusiness)"),
            ("Questions and Answers", "प्रश्न और उत्तर"),
            ("+ Add Question", "+ प्रश्न जोड़ें"),
            ("Article Data", "लेख डेटा"),
            ("Headline", "शीर्षक"),
            ("Main Image URL", "मुख्य छवि URL"),
            ("Author / Writer", "लेखक / लेखक"),
            ("Publisher (Site Logo URL)", "प्रकाशक (साइट लोगो URL)"),
            ("Publication Date", "प्रकाशन की तिथि"),
            ("Business Information", "व्यावसायिक जानकारी"),
            ("Business Name", "व्यापार का नाम"),
            ("Image or Photo URL", "छवि या फोटो URL"),
            ("Phone", "फ़ोन"),
            ("Address", "पता"),
            ("JSON-LD Code", "JSON-LD कोड"),
            ("Copy Code", "कॉपी कोड")
        ],
        "pt": [
            ("JSON-LD Schema Generator — PageGuides", "Gerador de Schema JSON-LD — PageGuides"),
            ("Generate professional Schema.org markup (JSON-LD) for FAQs, Articles, and Local Businesses. Improve your visibility and CTR on Google.", "Gere marcação profissional Schema.org (JSON-LD) para FAQs, Artigos e Negócios Locais. Melhore sua visibilidade e CTR no Google."),
            ("Generate valid structured data ready for Google. Increase your chances of getting Rich Snippets.", "Gere dados estruturados válidos prontos para o Google. Aumente suas chances de obter Rich Snippets."),
            ("JSON-LD Schema Generator", "Gerador de Schema JSON-LD"),
            ("Schema Type", "Tipo de Schema"),
            ("Frequently Asked Questions (FAQPage)", "Perguntas Frequentes (FAQPage)"),
            ("Blog Article (Article)", "Artigo de Blog (Article)"),
            ("Local Business (LocalBusiness)", "Negócio Local (LocalBusiness)"),
            ("Questions and Answers", "Perguntas e Respostas"),
            ("+ Add Question", "+ Adicionar Pergunta"),
            ("Article Data", "Dados do Artigo"),
            ("Headline", "Título"),
            ("Main Image URL", "URL da Imagem Principal"),
            ("Author / Writer", "Autor / Escritor"),
            ("Publisher (Site Logo URL)", "Editor (URL do Logo do Site)"),
            ("Publication Date", "Data de Publicação"),
            ("Business Information", "Informações do Negócio"),
            ("Business Name", "Nome do Negócio"),
            ("Image or Photo URL", "URL da Imagem ou Foto"),
            ("Phone", "Telefone"),
            ("Address", "Endereço"),
            ("JSON-LD Code", "Código JSON-LD"),
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

        # Translate strings using tool_translations specific arrays
        t_strings = tool_translations.get(tool_name, {}).get(lang, [])
        for en_str, t_str in t_strings:
            lang_html = lang_html.replace(en_str, t_str)
            
        # Write output file to lang folder
        out_dir = os.path.join(os.path.dirname(filepath), lang)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, tool_name)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(lang_html)

for tool in tools_to_translate:
    translate_file(tool, tool)

print("Successfully generated translations for batch 3")

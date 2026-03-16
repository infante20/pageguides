import os

tools = ['keyword-density.html', 'lsi-suggester.html']
base_dir = '/Users/franciscoinfante/Downloads/oneusepage/pageguides.com/'

translations = {
    'es': {
        'lang': 'es',
        'nav_back': '← Volver a Herramientas',
        'keyword-density.html': {
            'title_tag': '<title>Analizador de Densidad de Palabras Clave — PageGuides</title>',
            'desc_tag': 'Analiza la densidad de palabras clave en tu contenido. Detecta sobre-optimización y asegura un uso natural de las palabras clave para SEO.',
            'h1': 'Analizador de Densidad de Palabras Clave',
            'subtitle': 'Analiza la densidad de palabras clave en tu contenido. Detecta la sobre-optimización y asegura un uso orgánico y natural para SEO.',
            'l_content': 'Contenido a analizar',
            'placeholder_content': 'Pega tu artículo, página o fragmento de contenido aquí...',
            'l_target': 'Palabra clave objetivo (opcional)',
            'placeholder_target': 'ej., posicionamiento web, seo técnico...',
            'btn_analyze': 'Analizar Densidad',
            't_words': 'Total de Palabras',
            'u_words': 'Pal. Únicas',
            'k_density': 'Densidad',
            'sec_title': 'Palabras Clave Más Frecuentes',
            'th_keyword': 'Palabra Clave',
            'th_occurrences': 'Apariciones',
            'th_density': 'Densidad',
            'th_relative': 'Frecuencia Relativa',
            'th_status': 'Estado SEO',
            'js_low': 'Baja',
            'js_ideal': 'Ideal',
            'js_high': 'Alta',
            'js_over': 'Sobre-opt.',
            'dropdown': '<span class="lang-flag">🇪🇸</span> ES'
        },
        'lsi-suggester.html': {
            'title_tag': '<title>Sugeridor de Palabras Clave LSI — PageGuides</title>',
            'desc_tag': 'Encuentra términos relacionados semánticamente (LSI) para enriquecer tu contenido y mejorar tu relevancia en buscadores.',
            'h1': 'Sugeridor de Palabras Clave LSI',
            'subtitle': 'Mejora la semántica de tu contenido con términos relacionados. Enriquece tu vocabulario y aumenta tu relevancia en Google.',
            'placeholder_main': 'Palabra clave principal... ej., herramientas SEO',
            'btn_find': 'Encontrar LSI',
            'sec_title': 'Sugerencias LSI Encontradas',
            't_terms': 'Términos',
            'btn_copy': 'Copiar',
            'js_copied': '¡COPIADO!',
            'dropdown': '<span class="lang-flag">🇪🇸</span> ES'
        }
    },
    'fr': {
        'lang': 'fr',
        'nav_back': '← Retour aux Outils',
        'keyword-density.html': {
            'title_tag': '<title>Analyseur de Densité de Mots-Clés — PageGuides</title>',
            'desc_tag': 'Analysez la densité des mots-clés dans votre contenu. Détectez la suroptimisation et assurez une utilisation naturelle pour le SEO.',
            'h1': 'Analyseur de Densité de Mots-Clés',
            'subtitle': 'Analysez la densité des mots-clés dans votre contenu. Détectez la suroptimisation et assurez une utilisation organique et naturelle pour le SEO.',
            'l_content': 'Contenu à analyser',
            'placeholder_content': 'Collez votre article, page ou extrait de contenu ici...',
            'l_target': 'Mot-clé cible (optionnel)',
            'placeholder_target': 'ex., référencement web, seo technique...',
            'btn_analyze': 'Analyser la Densité',
            't_words': 'Total de Mots',
            'u_words': 'Mots Uniques',
            'k_density': 'Densité',
            'sec_title': 'Mots-Clés les Plus Fréquents',
            'th_keyword': 'Mot-Clé',
            'th_occurrences': 'Occurrences',
            'th_density': 'Densité',
            'th_relative': 'Fréquence Relative',
            'th_status': 'Statut SEO',
            'js_low': 'Faible',
            'js_ideal': 'Idéal',
            'js_high': 'Élevée',
            'js_over': 'Sur-opt.',
            'dropdown': '<span class="lang-flag">🇫🇷</span> FR'
        },
        'lsi-suggester.html': {
            'title_tag': '<title>Suggesteur de Mots-Clés LSI — PageGuides</title>',
            'desc_tag': 'Trouvez des termes sémantiquement liés (LSI) pour enrichir votre contenu et améliorer votre pertinence pour les moteurs de recherche.',
            'h1': 'Suggesteur de Mots-Clés LSI',
            'subtitle': 'Améliorez la sémantique de votre contenu avec des termes associés. Enrichissez votre vocabulaire et augmentez votre pertinence sur Google.',
            'placeholder_main': 'Mot-clé principal... ex., outils SEO',
            'btn_find': 'Trouver LSI',
            'sec_title': 'Suggestions LSI Trouvées',
            't_terms': 'Termes',
            'btn_copy': 'Copier',
            'js_copied': 'COPIÉ !',
            'dropdown': '<span class="lang-flag">🇫🇷</span> FR'
        }
    },
    'hi': {
        'lang': 'hi',
        'nav_back': '← टूल पर वापस जाएं',
        'keyword-density.html': {
            'title_tag': '<title>कीवर्ड घनत्व विश्लेषक — PageGuides</title>',
            'desc_tag': 'अपनी सामग्री में कीवर्ड घनत्व का विश्लेषण करें। अत्यधिक अनुकूलन का पता लगाएं और SEO के लिए प्राकृतिक कीवर्ड उपयोग सुनिश्चित करें।',
            'h1': 'कीवर्ड घनत्व विश्लेषक',
            'subtitle': 'अपनी सामग्री में कीवर्ड घनत्व का विश्लेषण करें। अत्यधिक अनुकूलन का पता लगाएं और SEO के लिए जैविक और प्राकृतिक कीवर्ड उपयोग सुनिश्चित करें।',
            'l_content': 'विश्लेषण करने के लिए सामग्री',
            'placeholder_content': 'अपना लेख, पृष्ठ या सामग्री स्निपेट यहां पेस्ट करें...',
            'l_target': 'लक्ष्य कीवर्ड (वैकल्पिक)',
            'placeholder_target': 'उदा., वेब पोजिशनिंग, तकनीकी एसईओ...',
            'btn_analyze': 'घनत्व का विश्लेषण करें',
            't_words': 'कुल शब्द',
            'u_words': 'अद्वितीय शब्द',
            'k_density': 'घनत्व',
            'sec_title': 'शीर्ष लगातार कीवर्ड',
            'th_keyword': 'कीवर्ड',
            'th_occurrences': 'घटनाएँ',
            'th_density': 'घनत्व',
            'th_relative': 'आपेक्षिक आवृत्ति',
            'th_status': 'SEO स्थिति',
            'js_low': 'कम',
            'js_ideal': 'आदर्श',
            'js_high': 'उच्च',
            'js_over': 'अधिक',
            'dropdown': '<span class="lang-flag">🇮🇳</span> HI'
        },
        'lsi-suggester.html': {
            'title_tag': '<title>LSI कीवर्ड सुझावकर्ता — PageGuides</title>',
            'desc_tag': 'अपनी सामग्री को समृद्ध करने और खोज इंजनों के लिए अपनी प्रासंगिकता में सुधार करने के लिए अर्थपूर्ण रूप से संबंधित शब्द (LSI) खोजें।',
            'h1': 'LSI कीवर्ड सुझावकर्ता',
            'subtitle': 'संबंधित शब्दों के साथ अपनी सामग्री के अर्थ विज्ञान में सुधार करें। अपनी शब्दावली को समृद्ध करें और Google पर अपनी प्रासंगिकता बढ़ाएं।',
            'placeholder_main': 'मुख्य कीवर्ड... उदा., SEO टूल',
            'btn_find': 'LSI खोजें',
            'sec_title': 'LSI सुझाव मिले',
            't_terms': 'शर्तें',
            'btn_copy': 'कॉपी',
            'js_copied': 'कॉपी किया गया!',
            'dropdown': '<span class="lang-flag">🇮🇳</span> HI'
        }
    },
    'pt': {
        'lang': 'pt',
        'nav_back': '← Voltar para Ferramentas',
        'keyword-density.html': {
            'title_tag': '<title>Analisador de Densidade de Palavras-chave — PageGuides</title>',
            'desc_tag': 'Analise a densidade de palavras-chave em seu conteúdo. Detecte superotimização e garanta o uso natural de palavras-chave para SEO.',
            'h1': 'Analisador de Densidade de Palavras-chave',
            'subtitle': 'Analise a densidade de palavras-chave em seu conteúdo. Detecte a superotimização e garanta um uso orgânico e natural para o SEO.',
            'l_content': 'Conteúdo para analisar',
            'placeholder_content': 'Cole seu artigo, página ou trecho de conteúdo aqui...',
            'l_target': 'Palavra-chave alvo (opcional)',
            'placeholder_target': 'ex., posicionamento web, seo técnico...',
            'btn_analyze': 'Analisar Densidade',
            't_words': 'Total de Palavras',
            'u_words': 'Pal. Únicas',
            'k_density': 'Densidade',
            'sec_title': 'Palavras-chave Mais Frequentes',
            'th_keyword': 'Palavra-chave',
            'th_occurrences': 'Ocorrências',
            'th_density': 'Densidade',
            'th_relative': 'Frequência Relativa',
            'th_status': 'Status SEO',
            'js_low': 'Baixa',
            'js_ideal': 'Ideal',
            'js_high': 'Alta',
            'js_over': 'Super otim.',
            'dropdown': '<span class="lang-flag">🇧🇷</span> PT'
        },
        'lsi-suggester.html': {
            'title_tag': '<title>Sugestor de Palavras-chave LSI — PageGuides</title>',
            'desc_tag': 'Encontre termos semanticamente relacionados (LSI) para enriquecer seu conteúdo e melhorar sua relevância para mecanismos de busca.',
            'h1': 'Sugestor de Palavras-chave LSI',
            'subtitle': 'Melhore a semântica do seu conteúdo com termos relacionados. Enriqueça seu vocabulário e aumente sua relevância no Google.',
            'placeholder_main': 'Palavra-chave principal... ex., ferramentas SEO',
            'btn_find': 'Encontrar LSI',
            'sec_title': 'Sugestões LSI Encontradas',
            't_terms': 'Termos',
            'btn_copy': 'Copiar',
            'js_copied': 'COPIADO!',
            'dropdown': '<span class="lang-flag">🇧🇷</span> PT'
        }
    }
}

nav_dropdown_html = """        <div class="nav-actions">
            <div class="lang-selector">
                <button class="lang-btn">
                    {BTN_CONTENT}
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                </button>
                <div class="lang-dropdown">
                    <a href="/" class="lang-option"><span class="lang-flag">🇺🇸</span> English</a>
                    {OP_ES}
                    {OP_FR}
                    {OP_PT}
                    {OP_HI}
                </div>
            </div>
        </div>"""

def inject_dropdown(html_content, code, tr, lang_dict):
    # CSS injection
    css = """
        /* LANGUAGE SELECTOR */
        .nav-actions {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .lang-selector {
            position: relative;
        }

        .lang-btn {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: var(--text);
            padding: 0.4rem 0.8rem;
            border-radius: 8px;
            font-size: 0.85rem;
            font-weight: 500;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.2s;
            font-family: inherit;
        }

        .lang-btn:hover {
            background: rgba(255, 255, 255, 0.1);
            border-color: rgba(255, 255, 255, 0.2);
        }

        .lang-dropdown {
            position: absolute;
            top: calc(100% + 0.5rem);
            right: 0;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 0.5rem;
            min-width: 140px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
            opacity: 0;
            visibility: hidden;
            transform: translateY(-10px);
            transition: all 0.2s;
            z-index: 100;
        }

        .lang-selector:hover .lang-dropdown {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }

        .lang-option {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 0.75rem;
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.85rem;
            border-radius: 6px;
            transition: all 0.2s;
            font-weight: 500;
        }

        .lang-option:hover {
            background: rgba(255, 255, 255, 0.05);
            color: var(--text);
        }

        .lang-option.active {
            color: var(--accent);
            background: var(--accent-glow);
        }
        
        .lang-flag {
            font-size: 1rem;
            line-height: 1;
        }
    </style>"""
    html_content = html_content.replace('</style>', css)
    
    dropdown = nav_dropdown_html.replace('{BTN_CONTENT}', tr['dropdown'])
    # active classes
    es = f'<a href="/es/{filename}" class="lang-option active"><span class="lang-flag">🇪🇸</span> Español</a>' if code == 'es' else f'<a href="/es/{filename}" class="lang-option"><span class="lang-flag">🇪🇸</span> Español</a>'
    fr = f'<a href="/fr/{filename}" class="lang-option active"><span class="lang-flag">🇫🇷</span> Français</a>' if code == 'fr' else f'<a href="/fr/{filename}" class="lang-option"><span class="lang-flag">🇫🇷</span> Français</a>'
    pt = f'<a href="/pt/{filename}" class="lang-option active"><span class="lang-flag">🇧🇷</span> Português</a>' if code == 'pt' else f'<a href="/pt/{filename}" class="lang-option"><span class="lang-flag">🇧🇷</span> Português</a>'
    hi = f'<a href="/hi/{filename}" class="lang-option active"><span class="lang-flag">🇮🇳</span> हिन्दी</a>' if code == 'hi' else f'<a href="/hi/{filename}" class="lang-option"><span class="lang-flag">🇮🇳</span> हिन्दी</a>'
    
    dropdown = dropdown.replace('{OP_ES}', es).replace('{OP_FR}', fr).replace('{OP_PT}', pt).replace('{OP_HI}', hi)
    dropdown = dropdown.replace('href="/"', f'href="/{filename}"') # EN link
    
    # replace back-link with dropdown + back-link
    res = html_content.replace(f'← Back to Tools\n        </a>\n    </nav>', f'{lang_dict["nav_back"]}\n        </a>\n{dropdown}\n    </nav>')
    # Fix logo href
    res = res.replace('href="/" class="logo"', f'href="/{code}/" class="logo"')
    return res

for filename in tools:
    with open(f'{base_dir}{filename}', 'r', encoding='utf-8') as f:
        html = f.read()
    
    for code, tr in translations.items():
        t = tr[filename]
        res = html.replace('lang="en"', f'lang="{code}"')
        
        # Inject CSS and HTML for Language Dropdown
        res = inject_dropdown(res, code, t, tr)
        
        if filename == 'keyword-density.html':
            res = res.replace('<title>Keyword Density Analyzer — PageGuides</title>', t['title_tag'])
            res = res.replace('content="Analyze keyword density in your content. Detect over-optimization and ensure natural keyword usage for SEO."', f'content="{t["desc_tag"]}"')
            res = res.replace('<h1>Keyword Density Analyzer</h1>', f'<h1>{t["h1"]}</h1>')
            res = res.replace('<p class="subtitle">Analyze keyword density in your content. Detect over-optimization and ensure organic and natural keyword usage for SEO.</p>', f'<p class="subtitle">{t["subtitle"]}</p>')
            res = res.replace('<label>Content to analyze</label>', f'<label>{t["l_content"]}</label>')
            res = res.replace('placeholder="Paste your article, page, or content snippet here..."', f'placeholder="{t["placeholder_content"]}"')
            res = res.replace('<label>Target keyword (optional)</label>', f'<label>{t["l_target"]}</label>')
            res = res.replace('placeholder="e.g., web positioning, technical seo..."', f'placeholder="{t["placeholder_target"]}"')
            res = res.replace('Analyze Density', t['btn_analyze'])
            res = res.replace('Total Words', t['t_words'])
            res = res.replace('Unique Words', t['u_words'])
            res = res.replace('Keyword Density', t['k_density'])
            res = res.replace('Top Frequent Keywords', t['sec_title'])
            res = res.replace('<th>Keyword</th>', f'<th>{t["th_keyword"]}</th>')
            res = res.replace('<th>Occurrences</th>', f'<th>{t["th_occurrences"]}</th>')
            res = res.replace('<th>Density</th>', f'<th>{t["th_density"]}</th>')
            res = res.replace('<th>Relative Frequency</th>', f'<th>{t["th_relative"]}</th>')
            res = res.replace('<th>SEO Status</th>', f'<th>{t["th_status"]}</th>')
            res = res.replace('Low\'];', f'{t["js_low"]}\'];')
            res = res.replace('Ideal\'];', f'{t["js_ideal"]}\'];')
            res = res.replace('High\'];', f'{t["js_high"]}\'];')
            res = res.replace('Over-opt.\'];', f'{t["js_over"]}\'];')
            
        elif filename == 'lsi-suggester.html':
            res = res.replace('<title>LSI Keyword Suggester — PageGuides</title>', t['title_tag'])
            res = res.replace('content="Find semantically related terms (LSI) to enrich your content and improve your relevance for search engines."', f'content="{t["desc_tag"]}"')
            res = res.replace('<h1>LSI Keyword Suggester</h1>', f'<h1>{t["h1"]}</h1>')
            res = res.replace('<p class="subtitle">Improve the semantics of your content with related terms. Enrich your vocabulary and increase your relevance on Google.</p>', f'<p class="subtitle">{t["subtitle"]}</p>')
            res = res.replace('placeholder="Main keyword... e.g., SEO tools"', f'placeholder="{t["placeholder_main"]}"')
            res = res.replace('>Find LSI<', f'>{t["btn_find"]}<')
            res = res.replace('<h3>LSI Suggestions Found</h3>', f'<h3>{t["sec_title"]}</h3>')
            res = res.replace('0 Terms', f'0 {t["t_terms"]}')
            res = res.replace('Terms`;', f'{t["t_terms"]}`;')
            res = res.replace('>Copy<', f'>{t["btn_copy"]}<')
            res = res.replace('COPIED!', t['js_copied'])

        with open(f'{base_dir}{code}/{filename}', 'w', encoding='utf-8') as f:
            f.write(res)
        
print("Successfully generated translations for batch 1")

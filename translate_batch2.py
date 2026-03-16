import os

tools = ['readability-checker.html', 'meta-tag-optimizer.html']
base_dir = '/Users/franciscoinfante/Downloads/oneusepage/pageguides.com/'

translations = {
    'es': {
        'lang': 'es',
        'nav_back': '← Volver a Herramientas',
        'dropdown': '<span class="lang-flag">🇪🇸</span> ES',
        'readability-checker.html': {
            'title_tag': '<title>Comprobador de Legibilidad — PageGuides</title>',
            'desc_tag': 'Analiza la legibilidad de tu contenido web. Asegura que tu texto sea fácil de entender para tus usuarios y mejora tu SEO.',
            'h1': 'Comprobador de Legibilidad',
            'subtitle': 'Analiza la complejidad de tu texto. El contenido fácil de leer retiene a más usuarios y clasifica mejor en Google.',
            'placeholder_content': 'Pega el contenido que quieres analizar aquí (artículos, posts, fragmentos)...',
            'btn_analyze': 'Analizar Legibilidad',
            'l_score': 'Puntuación de Legibilidad de Flesch',
            'l_grade': 'Calculando...',
            'l_words': 'Palabras',
            'l_sentences': 'Oraciones',
            'l_syllables': 'Sílabas / Palabra',
            'js_grade_easy': 'Fácil (11 años)',
            'js_grade_standard': 'Estándar (Conversacional)',
            'js_grade_fairly': 'Bastante Difícil (Secundaria)',
            'js_grade_difficult': 'Difícil (Académico)',
            'js_grade_very': 'Muy Difícil (Técnico / Legal)'
        },
        'meta-tag-optimizer.html': {
            'title_tag': '<title>Vista Previa SERP y Optimizador de Etiquetas Meta — PageGuides</title>',
            'desc_tag': 'Visualiza cómo se verá tu página en Google. Optimiza tus títulos y meta descripciones para mejorar el CTR.',
            'h1': 'Optimizador de Etiquetas Meta',
            'subtitle': 'Escribe, visualiza y perfecciona tu presencia en los resultados de búsqueda de Google (SERP).',
            'l_title': 'Etiqueta Meta Title',
            'placeholder_title': 'Ej.: Las 10 Mejores Herramientas SEO de 2026',
            'l_url': 'Slug de URL / Dominio',
            'placeholder_url': 'pageguides.com › herramientas-seo',
            'l_desc': 'Etiqueta Meta Description',
            'placeholder_desc': 'Escribe una meta descripción atractiva para mejorar tu CTR...',
            'sec_preview': 'Vista Previa de Google',
            'badge_dark': 'Modo Oscuro Escritorio',
            'serp_brand': 'Sitio web',
            'serp_title': 'Título de la Página',
            'serp_desc': 'Esta es la descripción que aparecerá en los resultados de búsqueda. Asegúrate de que sea relevante, natural y contenga una llamada a la acción atractiva.',
            'tips_h4': 'Consejos Pro de Optimización',
            'tips_li1': 'La longitud ideal del título es entre <strong>50 y 60 caracteres</strong> para evitar que Google lo trunque.',
            'tips_li2': 'Incluye tu palabra clave principal <strong>lo más cerca posible del principio</strong> del título.',
            'tips_li3': 'La meta descripción debe actuar como un <strong>"discurso de promoción" rápido</strong> para atraer clics (CTR).',
            'tips_li4': 'Evita el relleno de palabras clave; escribe para humanos y optimiza para algoritmos.'
        }
    },
    'fr': {
        'lang': 'fr',
        'nav_back': '← Retour aux Outils',
        'dropdown': '<span class="lang-flag">🇫🇷</span> FR',
        'readability-checker.html': {
            'title_tag': '<title>Vérificateur de Lisibilité — PageGuides</title>',
            'desc_tag': 'Analysez la lisibilité de votre contenu web. Assurez-vous que votre texte est facile à comprendre pour vos utilisateurs et améliorez votre SEO.',
            'h1': 'Vérificateur de Lisibilité',
            'subtitle': 'Analysez la complexité de votre texte. Un contenu facile à lire fidélise plus d\'utilisateurs et se classe mieux sur Google.',
            'placeholder_content': 'Collez le contenu que vous souhaitez analyser ici (articles, publications, extraits)...',
            'btn_analyze': 'Analyser la Lisibilité',
            'l_score': 'Score de Lisibilité Flesch',
            'l_grade': 'Calcul en cours...',
            'l_words': 'Mots',
            'l_sentences': 'Phrases',
            'l_syllables': 'Syllabes / Mot',
            'js_grade_easy': 'Facile (11 ans)',
            'js_grade_standard': 'Standard (Conversationnel)',
            'js_grade_fairly': 'Assez Difficile (Lycée)',
            'js_grade_difficult': 'Difficile (Académique)',
            'js_grade_very': 'Très Difficile (Technique / Légal)'
        },
        'meta-tag-optimizer.html': {
            'title_tag': '<title>Aperçu SERP & Optimiseur de Balises Meta — PageGuides</title>',
            'desc_tag': 'Visualisez l\'apparence de votre page sur Google. Optimisez vos titres et méta-descriptions pour améliorer le taux de clic (CTR).',
            'h1': 'Optimiseur de Balises Meta',
            'subtitle': 'Rédigez, visualisez et perfectionnez votre présence dans les résultats de recherche Google (SERP).',
            'l_title': 'Balise Meta Title',
            'placeholder_title': 'Ex. : Les 10 Meilleurs Outils SEO de 2026',
            'l_url': 'Slug de l\'URL / Domaine',
            'placeholder_url': 'pageguides.com › outils-seo',
            'l_desc': 'Balise Meta Description',
            'placeholder_desc': 'Rédigez une méta-description engageante pour améliorer votre CTR...',
            'sec_preview': 'Aperçu Google',
            'badge_dark': 'Mode Sombre Bureau',
            'serp_brand': 'Site web',
            'serp_title': 'Titre de la Page',
            'serp_desc': 'Voici la description qui apparaîtra dans les résultats de recherche. Assurez-vous qu\'elle soit pertinente, naturelle et contienne un appel à l\'action convaincant.',
            'tips_h4': 'Conseils Pro d\'Optimisation',
            'tips_li1': 'La longueur idéale du titre est entre <strong>50 et 60 caractères</strong> pour éviter que Google ne le tronque.',
            'tips_li2': 'Incluez votre mot-clé principal <strong>le plus près possible du début</strong> du titre.',
            'tips_li3': 'La méta-description doit agir comme un <strong>"argument de vente" rapide</strong> pour convaincre les utilisateurs de cliquer (CTR).',
            'tips_li4': 'Évitez l\'accumulation de mots-clés ; écrivez pour les humains et optimisez pour les algorithmes.'
        }
    },
    'hi': {
        'lang': 'hi',
        'nav_back': '← टूल पर वापस जाएं',
        'dropdown': '<span class="lang-flag">🇮🇳</span> HI',
        'readability-checker.html': {
            'title_tag': '<title>पठनीयता चेकर — PageGuides</title>',
            'desc_tag': 'अपनी वेब सामग्री की पठनीयता का विश्लेषण करें। सुनिश्चित करें कि आपका पाठ आपके उपयोगकर्ताओं के लिए समझने में आसान है और आपका एसईओ सुधारता है।',
            'h1': 'पठनीयता चेकर',
            'subtitle': 'अपने पाठ की जटिलता का विश्लेषण करें। आसानी से पढ़ी जाने वाली सामग्री अधिक उपयोगकर्ताओं को आकर्षित करती है और Google पर बेहतर रैंक करती है।',
            'placeholder_content': 'वह सामग्री पेस्ट करें जिसका आप विश्लेषण करना चाहते हैं (लेख, पोस्ट, स्निपेट)...',
            'btn_analyze': 'पठनीयता का विश्लेषण करें',
            'l_score': 'फ्लेश पढ़ने में आसानी स्कोर',
            'l_grade': 'गणना की जा रही है...',
            'l_words': 'शब्द',
            'l_sentences': 'वाक्य',
            'l_syllables': 'अक्षर / शब्द',
            'js_grade_easy': 'आसान (11 वर्ष के बच्चे)',
            'js_grade_standard': 'मानक (बातचीत)',
            'js_grade_fairly': 'काफी कठिन (हाई स्कूल)',
            'js_grade_difficult': 'कठिन (शैक्षणिक)',
            'js_grade_very': 'बहुत कठिन (तकनीकी / कानूनी)'
        },
        'meta-tag-optimizer.html': {
            'title_tag': '<title>SERP पूर्वावलोकन और मेटा टैग अनुकूलक — PageGuides</title>',
            'desc_tag': 'कल्पना करें कि आपका पृष्ठ Google पर कैसा दिखेगा। CTR को बेहतर बनाने के लिए अपने शीर्षक और मेटा विवरण को अनुकूलित करें।',
            'h1': 'मेटा टैग अनुकूलक',
            'subtitle': 'Google खोज परिणामों (SERP) में अपनी उपस्थिति लिखें, कल्पना करें और सुधारें।',
            'l_title': 'मेटा शीर्षक (Title) टैग',
            'placeholder_title': 'उदा.: 2026 के शीर्ष 10 SEO टूल',
            'l_url': 'URL स्लग / डोमेन',
            'placeholder_url': 'pageguides.com › seo-tools',
            'l_desc': 'मेटा विवरण (Description) टैग',
            'placeholder_desc': 'अपने CTR को बेहतर बनाने के लिए एक आकर्षक मेटा विवरण लिखें...',
            'sec_preview': 'Google पूर्वावलोकन',
            'badge_dark': 'डेस्कटॉप डार्क मोड',
            'serp_brand': 'वेबसाइट',
            'serp_title': 'पृष्ठ का शीर्षक',
            'serp_desc': 'यह वह विवरण है जो खोज परिणामों में दिखाई देगा। सुनिश्चित करें कि यह प्रासंगिक, स्वाभाविक है, और इसमें एक आकर्षक कॉल टू एक्शन है।',
            'tips_h4': 'अनुकूलन प्रो टिप्स',
            'tips_li1': 'Google द्वारा काटे जाने से रोकने के लिए आदर्श शीर्षक की लंबाई <strong>50 से 60 वर्णों</strong> के बीच है।',
            'tips_li2': 'शीर्षक की <strong>शुरुआत के जितना संभव हो सके</strong> अपना प्राथमिक कीवर्ड शामिल करें।',
            'tips_li3': 'मेटा विवरण को उपयोगकर्ताओं को क्लिक (CTR) करने के लिए मनाने के लिए <strong>त्वरित "बिक्री पिच"</strong> के रूप में कार्य करना चाहिए।',
            'tips_li4': '"कीवर्ड स्टफिंग" से बचें; इंसानों के लिए लिखें और एल्गोरिदम के लिए अनुकूलन करें।'
        }
    },
    'pt': {
        'lang': 'pt',
        'nav_back': '← Voltar para Ferramentas',
        'dropdown': '<span class="lang-flag">🇧🇷</span> PT',
        'readability-checker.html': {
            'title_tag': '<title>Verificador de Legibilidade — PageGuides</title>',
            'desc_tag': 'Analise a legibilidade do seu conteúdo web. Garanta que seu texto seja fácil de entender para seus usuários e melhore seu SEO.',
            'h1': 'Verificador de Legibilidade',
            'subtitle': 'Analise a complexidade do seu texto. Um conteúdo fácil de ler retém mais usuários e classifica melhor no Google.',
            'placeholder_content': 'Cole o conteúdo que você deseja analisar aqui (artigos, postagens, trechos)...',
            'btn_analyze': 'Analisar Legibilidade',
            'l_score': 'Índice de Facilidade de Leitura Flesch',
            'l_grade': 'Calculando...',
            'l_words': 'Palavras',
            'l_sentences': 'Frases',
            'l_syllables': 'Sílabas / Palavra',
            'js_grade_easy': 'Fácil (11 anos)',
            'js_grade_standard': 'Padrão (Conversacional)',
            'js_grade_fairly': 'Razoavelmente Difícil (Ensino Médio)',
            'js_grade_difficult': 'Difícil (Acadêmico)',
            'js_grade_very': 'Muito Difícil (Técnico / Jurídico)'
        },
        'meta-tag-optimizer.html': {
            'title_tag': '<title>Visualização SERP e Otimizador de Meta Tags — PageGuides</title>',
            'desc_tag': 'Visualize como sua página ficará no Google. Otimize seus títulos e meta descrições para melhorar o CTR.',
            'h1': 'Otimizador de Meta Tags',
            'subtitle': 'Escreva, visualize e aperfeiçoe sua presença nos resultados de pesquisa do Google (SERP).',
            'l_title': 'Meta Tag Title',
            'placeholder_title': 'Ex.: As 10 Melhores Ferramentas SEO de 2026',
            'l_url': 'Slug do URL / Domínio',
            'placeholder_url': 'pageguides.com › ferramentas-seo',
            'l_desc': 'Meta Tag Description',
            'placeholder_desc': 'Escreva uma meta descrição envolvente para melhorar seu CTR...',
            'sec_preview': 'Visualização do Google',
            'badge_dark': 'Modo Escuro Desktop',
            'serp_brand': 'Site',
            'serp_title': 'Título da Página',
            'serp_desc': 'Esta é a descrição que aparecerá nos resultados da pesquisa. Certifique-se de que seja relevante, natural e contenha uma frase de chamariz convincente.',
            'tips_h4': 'Dicas Profissionais de Otimização',
            'tips_li1': 'O comprimento ideal do título é entre <strong>50 e 60 caracteres</strong> para evitar que o Google o corte.',
            'tips_li2': 'Inclua sua palavra-chave principal <strong>o mais perto possível do início</strong> do título.',
            'tips_li3': 'A meta descrição deve atuar como um <strong>"discurso de vendas" rápido</strong> para convencer os usuários a clicar (CTR).',
            'tips_li4': 'Evite o "keyword stuffing"; escreva para humanos e otimize para algoritmos.'
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

def inject_dropdown(html_content, code, lang_dict, filename):
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
    
    dropdown = nav_dropdown_html.replace('{BTN_CONTENT}', lang_dict['dropdown'])
    es = f'<a href="/es/{filename}" class="lang-option active"><span class="lang-flag">🇪🇸</span> Español</a>' if code == 'es' else f'<a href="/es/{filename}" class="lang-option"><span class="lang-flag">🇪🇸</span> Español</a>'
    fr = f'<a href="/fr/{filename}" class="lang-option active"><span class="lang-flag">🇫🇷</span> Français</a>' if code == 'fr' else f'<a href="/fr/{filename}" class="lang-option"><span class="lang-flag">🇫🇷</span> Français</a>'
    pt = f'<a href="/pt/{filename}" class="lang-option active"><span class="lang-flag">🇧🇷</span> Português</a>' if code == 'pt' else f'<a href="/pt/{filename}" class="lang-option"><span class="lang-flag">🇧🇷</span> Português</a>'
    hi = f'<a href="/hi/{filename}" class="lang-option active"><span class="lang-flag">🇮🇳</span> हिन्दी</a>' if code == 'hi' else f'<a href="/hi/{filename}" class="lang-option"><span class="lang-flag">🇮🇳</span> हिन्दी</a>'
    
    dropdown = dropdown.replace('{OP_ES}', es).replace('{OP_FR}', fr).replace('{OP_PT}', pt).replace('{OP_HI}', hi)
    dropdown = dropdown.replace('href="/"', f'href="/{filename}"')
    
    res = html_content.replace('← Back to Tools\n        </a>\n    </nav>', f'{lang_dict["nav_back"]}\n        </a>\n{dropdown}\n    </nav>')
    res = res.replace('href="/" class="logo"', f'href="/{code}/" class="logo"')
    return res

for filename in tools:
    with open(f'{base_dir}{filename}', 'r', encoding='utf-8') as f:
        html = f.read()
    
    for code, lang in translations.items():
        t = lang[filename]
        res = html.replace('lang="en"', f'lang="{code}"')
        res = inject_dropdown(res, code, lang, filename)
        
        if filename == 'readability-checker.html':
            res = res.replace('<title>Readability Checker — PageGuides</title>', t['title_tag'])
            res = res.replace('content="Analyze the readability of your web content. Ensure your text is easy to understand for your users and improves your SEO."', f'content="{t["desc_tag"]}"')
            res = res.replace('<h1>Readability Checker</h1>', f'<h1>{t["h1"]}</h1>')
            res = res.replace('<p class="subtitle">Analyze the complexity of your text. Easy-to-read content retains more users and ranks better on Google.</p>', f'<p class="subtitle">{t["subtitle"]}</p>')
            res = res.replace('placeholder="Paste the content you want to analyze here (articles, posts, snippets)..."', f'placeholder="{t["placeholder_content"]}"')
            res = res.replace('>Analyze Readability<', f'>{t["btn_analyze"]}<')
            res = res.replace('Flesch Reading Ease Score', t['l_score'])
            res = res.replace('>Calculating...<', f'>{t["l_grade"]}<')
            res = res.replace('>Words<', f'>{t["l_words"]}<')
            res = res.replace('>Sentences<', f'>{t["l_sentences"]}<')
            res = res.replace('>Syllables / Word<', f'>{t["l_syllables"]}<')

            res = res.replace('Easy (11-year-olds)', t['js_grade_easy'])
            res = res.replace('Standard (Conversational)', t['js_grade_standard'])
            res = res.replace('Fairly Difficult (High School)', t['js_grade_fairly'])
            res = res.replace('Difficult (Academic)', t['js_grade_difficult'])
            res = res.replace('Very Difficult (Technical / Legal)', t['js_grade_very'])

        elif filename == 'meta-tag-optimizer.html':
            res = res.replace('<title>SERP Preview & Meta Tag Optimizer — PageGuides</title>', t['title_tag'])
            res = res.replace('content="Visualize how your page will look on Google. Optimize your titles and meta descriptions to improve CTR."', f'content="{t["desc_tag"]}"')
            res = res.replace('<h1>Meta Tag Optimizer</h1>', f'<h1>{t["h1"]}</h1>')
            res = res.replace('<p class="subtitle">Write, visualize, and perfect your presence in Google search results (SERP).</p>', f'<p class="subtitle">{t["subtitle"]}</p>')
            
            res = res.replace('>Meta Title Tag<', f'>{t["l_title"]}<')
            res = res.replace('placeholder="E.g.: Top 10 SEO Tools of 2026"', f'placeholder="{t["placeholder_title"]}"')
            
            res = res.replace('>URL Slug / Domain<', f'>{t["l_url"]}<')
            res = res.replace('placeholder="pageguides.com › seo-tools"', f'placeholder="{t["placeholder_url"]}"')
            
            res = res.replace('>Meta Description Tag<', f'>{t["l_desc"]}<')
            res = res.replace('placeholder="Write an engaging meta description to improve your CTR..."', f'placeholder="{t["placeholder_desc"]}"')
            
            res = res.replace('>Google Preview<', f'>{t["sec_preview"]}<')
            res = res.replace('>Desktop Dark Mode<', f'>{t["badge_dark"]}<')
            res = res.replace('>Website<', f'>{t["serp_brand"]}<')
            res = res.replace('>Page Title<', f'>{t["serp_title"]}<')
            res = res.replace('This is the description that will appear in search results. Ensure it is relevant, natural, and contains a compelling call to action.', t['serp_desc'])
            
            res = res.replace('<h4>Optimization Pro Tips</h4>', f'<h4>{t["tips_h4"]}</h4>')
            res = res.replace('The ideal title length is between <strong>50 and 60 characters</strong> to prevent truncation by Google.', t['tips_li1'])
            res = res.replace('Include your primary keyword <strong>as close to the beginning</strong> of the title as possible.', t['tips_li2'])
            res = res.replace('The meta description should act as a <strong>quick "sales pitch"</strong> to convince users to click (CTR).', t['tips_li3'])
            res = res.replace('Avoid "keyword stuffing"; write for humans and optimize for algorithms.', t['tips_li4'])

        with open(f'{base_dir}{code}/{filename}', 'w', encoding='utf-8') as f:
            f.write(res)

print("Successfully generated translations for batch 2")

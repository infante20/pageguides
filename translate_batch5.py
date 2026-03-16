import os
import re

tools_to_translate = [
    "canonical-tag-generator.html",
    "hreflang-tag-generator.html",
    "htaccess-redirect-generator.html"
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
    "es": { "nav_back": "Volver a Herramientas" },
    "fr": { "nav_back": "Retour aux outils" },
    "hi": { "nav_back": "उपकरणों पर वापस जाएं" },
    "pt": { "nav_back": "Voltar para Ferramentas" }
}

tool_translations = {
    "canonical-tag-generator.html": {
        "es": [
            ("Canonical Tag Generator — PageGuides", "Generador de Etiquetas Canonical — PageGuides"),
            ("Generate perfect canonical tags (rel=canonical) to avoid duplicate content issues and consolidate your SEO authority.", "Genera etiquetas canonical perfectas (rel=canonical) para evitar problemas de contenido duplicado y consolidar tu autoridad SEO."),
            ("Consolidate the strength of your duplicate or similar pages by telling Google which is the \"official\" version to rank.", "Consolida la fuerza de tus páginas duplicadas o similares diciéndole a Google cuál es la versión \"oficial\" que debe rankear."),
            ("Define your Canonical URL", "Define tu URL Canonical"),
            ("Main / Original Page (Absolute URL)", "Página Principal / Original (URL Absoluta)"),
            ("Where do I put this code?", "¿Dónde coloco este código?"),
            ("Copy the generated code and paste it inside the <code>&lt;head&gt;</code> tag of <strong>ALL duplicate pages</strong> (and ideally also on the original pointing to itself, i.e., a \"self-referencing canonical\").", "Copia el código generado y pégalo dentro de la etiqueta <code>&lt;head&gt;</code> de <strong>TODAS las páginas duplicadas</strong> (e idealmente también en la original apuntando a sí misma, es decir, un \"canonical auto-referenciado\")."),
            ("For example, if you have <code>/watch?color=red</code>, its canonical tag should point to <code>/watch</code>.", "Por ejemplo, si tienes <code>/reloj?color=rojo</code>, su etiqueta canonical debería apuntar a <code>/reloj</code>."),
            ("📋 HTML Tag", "📋 Etiqueta HTML"),
            ("Enter a URL to generate the tag.", "Escribe una URL para generar la etiqueta."),
            ("URL must include http:// or https://", "La URL debe incluir http:// o https://"),
            ("You are using HTTP. If you have an SSL certificate, it is highly recommended to use HTTPS for the canonical URL.", "Estás usando HTTP. Si tienes certificado SSL, es altamente recomendable usar HTTPS para la URL canonical."),
            ("Correct absolute URL with HTTPS.", "URL absoluta correcta con HTTPS."),
            ("The URL uses a trailing slash (well done, maintain consistency).", "La URL usa trailing slash (bien hecho, mantén la consistencia)."),
            ("The URL contains parameters (?key=val). Usually a Canonical points to the clean URL without parameters.", "La URL contiene parámetros (?key=val). Normalmente una Canonical apunta a la URL limpia sin parámetros."),
            ("You are using a relative URL. <strong>Google requires absolute URLs</strong> (including https://) for canonical tags.", "Estás usando una URL relativa. <strong>Google exige URLs absolutas</strong> completas (incluyendo https://) para las etiquetas canonical."),
            ("Incomplete or invalid URL path.", "Ruta de URL incompleta o inválida.")
        ],
        "fr": [
            ("Canonical Tag Generator — PageGuides", "Générateur de Balises Canonical — PageGuides"),
            ("Generate perfect canonical tags (rel=canonical) to avoid duplicate content issues and consolidate your SEO authority.", "Générez des balises canonical parfaites (rel=canonical) pour éviter les problèmes de contenu dupliqué et consolider votre autorité SEO."),
            ("Consolidate the strength of your duplicate or similar pages by telling Google which is the \"official\" version to rank.", "Consolidez la force de vos pages dupliquées ou similaires en indiquant à Google quelle est la version « officielle » à classer."),
            ("Define your Canonical URL", "Définissez votre URL Canonical"),
            ("Main / Original Page (Absolute URL)", "Page Principale / Originale (URL Absolue)"),
            ("Where do I put this code?", "Où dois-je mettre ce code ?"),
            ("Copy the generated code and paste it inside the <code>&lt;head&gt;</code> tag of <strong>ALL duplicate pages</strong> (and ideally also on the original pointing to itself, i.e., a \"self-referencing canonical\").", "Copiez le code généré et collez-le dans la balise <code>&lt;head&gt;</code> de <strong>TOUTES les pages dupliquées</strong> (et idéalement aussi sur l'originale pointant vers elle-même, c'est-à-dire une « adresse canonique auto-référencée »)."),
            ("For example, if you have <code>/watch?color=red</code>, its canonical tag should point to <code>/watch</code>.", "Par exemple, si vous avez <code>/montre?couleur=rouge</code>, sa balise canonical doit pointer vers <code>/montre</code>."),
            ("📋 HTML Tag", "📋 Balise HTML"),
            ("Enter a URL to generate the tag.", "Entrez une URL pour générer la balise."),
            ("URL must include http:// or https://", "L'URL doit inclure http:// ou https://"),
            ("You are using HTTP. If you have an SSL certificate, it is highly recommended to use HTTPS for the canonical URL.", "Vous utilisez HTTP. Si vous disposez d'un certificat SSL, il est fortement recommandé d'utiliser HTTPS pour l'URL canonique."),
            ("Correct absolute URL with HTTPS.", "URL absolue correcte avec HTTPS."),
            ("The URL uses a trailing slash (well done, maintain consistency).", "L'URL utilise une barre oblique finale (bien joué, maintenez la cohérence)."),
            ("The URL contains parameters (?key=val). Usually a Canonical points to the clean URL without parameters.", "L'URL contient des paramètres (?key=val). Généralement, une Canonical pointe vers l'URL propre sans paramètres."),
            ("You are using a relative URL. <strong>Google requires absolute URLs</strong> (including https://) for canonical tags.", "Vous utilisez une URL relative. <strong>Google exige des URL absolues</strong> (y compris https://) pour les balises canoniques."),
            ("Incomplete or invalid URL path.", "Chemin d'URL incomplet ou invalide.")
        ],
        "hi": [
            ("Canonical Tag Generator — PageGuides", "कैनोनिकल टैग जनरेटर — PageGuides"),
            ("Generate perfect canonical tags (rel=canonical) to avoid duplicate content issues and consolidate your SEO authority.", "डुप्लिकेट सामग्री की समस्याओं से बचने और अपने एसईओ अधिकार को मजबूत करने के लिए सही कैनोनिकल टैग (rel=canonical) उत्पन्न करें।"),
            ("Consolidate the strength of your duplicate or similar pages by telling Google which is the \"official\" version to rank.", "Google को यह बताकर अपने डुप्लिकेट या समान पृष्ठों की ताकत समेकित करें कि रैंक करने के लिए कौन सा \"आधिकारिक\" संस्करण है।"),
            ("Define your Canonical URL", "अपना कैनोनिकल URL परिभाषित करें"),
            ("Main / Original Page (Absolute URL)", "मुख्य / मूल पृष्ठ (पूर्ण URL)"),
            ("Where do I put this code?", "मैं यह कोड कहाँ रखूँ?"),
            ("Copy the generated code and paste it inside the <code>&lt;head&gt;</code> tag of <strong>ALL duplicate pages</strong> (and ideally also on the original pointing to itself, i.e., a \"self-referencing canonical\").", "जेनरेट किए गए कोड को कॉपी करें और इसे <strong>सभी डुप्लिकेट पेजों</strong> के <code>&lt;head&gt;</code> टैग के अंदर पेस्ट करें (और आदर्श रूप से मूल पृष्ठ में भी जो खुद की ओर इशारा करता हो)।"),
            ("For example, if you have <code>/watch?color=red</code>, its canonical tag should point to <code>/watch</code>.", "उदाहरण के लिए, यदि आपके पास <code>/घड़ी?रंग=लाल</code> है, तो इसका कैनोनिकल टैग <code>/घड़ी</code> को इंगित करना चाहिए।"),
            ("📋 HTML Tag", "📋 HTML टैग"),
            ("Enter a URL to generate the tag.", "टैग जनरेट करने के लिए एक URL दर्ज करें।"),
            ("URL must include http:// or https://", "URL में http:// या https:// शामिल होना चाहिए"),
            ("You are using HTTP. If you have an SSL certificate, it is highly recommended to use HTTPS for the canonical URL.", "आप HTTP का उपयोग कर रहे हैं। यदि आपके पास एसएसएल प्रमाणपत्र है, तो कैनोनिकल यूआरएल के लिए HTTPS का उपयोग करने की अत्यधिक अनुशंसा की जाती है।"),
            ("Correct absolute URL with HTTPS.", "HTTPS के साथ सही पूर्ण URL।"),
            ("The URL uses a trailing slash (well done, maintain consistency).", "URL एक ट्रेलिंग स्लैश का उपयोग करता है (शाबाश, स्थिरता बनाए रखें)।"),
            ("The URL contains parameters (?key=val). Usually a Canonical points to the clean URL without parameters.", "URL में पैरामीटर (?key=val) शामिल हैं। आमतौर पर एक कैनोनिकल बिना मापदंडों के साफ यूआरएल की ओर इशारा करता है।"),
            ("You are using a relative URL. <strong>Google requires absolute URLs</strong> (including https://) for canonical tags.", "आप एक सापेक्ष URL का उपयोग कर रहे हैं। <strong>Google को कैनोनिकल टैग के लिए पूर्ण URL (https:// सहित) की आवश्यकता है</strong>।"),
            ("Incomplete or invalid URL path.", "अपूर्ण या अमान्य URL पथ।")
        ],
        "pt": [
            ("Canonical Tag Generator — PageGuides", "Gerador de Tags Canonical — PageGuides"),
            ("Generate perfect canonical tags (rel=canonical) to avoid duplicate content issues and consolidate your SEO authority.", "Gere tags canonical perfeitas (rel=canonical) para evitar problemas de conteúdo duplicado e consolidar sua autoridade SEO."),
            ("Consolidate the strength of your duplicate or similar pages by telling Google which is the \"official\" version to rank.", "Consolide a força de suas páginas duplicadas ou semelhantes dizendo ao Google qual é a versão \"oficial\" a ser classificada."),
            ("Define your Canonical URL", "Defina sua URL Canonical"),
            ("Main / Original Page (Absolute URL)", "Página Principal / Original (URL Absoluta)"),
            ("Where do I put this code?", "Onde coloco esse código?"),
            ("Copy the generated code and paste it inside the <code>&lt;head&gt;</code> tag of <strong>ALL duplicate pages</strong> (and ideally also on the original pointing to itself, i.e., a \"self-referencing canonical\").", "Copie o código gerado e cole-o dentro da tag <code>&lt;head&gt;</code> de <strong>TODAS as páginas duplicadas</strong> (e idealmente também na original apontando para si mesma, ou seja, uma \"canonical auto-referenciada\")."),
            ("For example, if you have <code>/watch?color=red</code>, its canonical tag should point to <code>/watch</code>.", "Por exemplo, se você tem <code>/relogio?cor=vermelho</code>, sua tag canonical deve apontar para <code>/relogio</code>."),
            ("📋 HTML Tag", "📋 Tag HTML"),
            ("Enter a URL to generate the tag.", "Insira uma URL para gerar a tag."),
            ("URL must include http:// or https://", "A URL deve incluir http:// ou https://"),
            ("You are using HTTP. If you have an SSL certificate, it is highly recommended to use HTTPS for the canonical URL.", "Você está usando HTTP. Se você possui um certificado SSL, é altamente recomendável usar HTTPS para a URL canonical."),
            ("Correct absolute URL with HTTPS.", "URL absoluta correta com HTTPS."),
            ("The URL uses a trailing slash (well done, maintain consistency).", "A URL usa uma barra final (muito bem, mantenha a consistência)."),
            ("The URL contains parameters (?key=val). Usually a Canonical points to the clean URL without parameters.", "A URL contém parâmetros (?key=val). Geralmente, uma Canonical aponta para a URL limpa sem parâmetros."),
            ("You are using a relative URL. <strong>Google requires absolute URLs</strong> (including https://) for canonical tags.", "Você está usando uma URL relativa. <strong>O Google exige URLs absolutas</strong> completas (incluindo https://) para tags canonical."),
            ("Incomplete or invalid URL path.", "Caminho de URL incompleto ou inválido.")
        ]
    },
    "hreflang-tag-generator.html": {
        "es": [
            ("Hreflang Tag Generator — PageGuides", "Generador de Etiquetas Hreflang — PageGuides"),
            ("Generate valid hreflang tags for International SEO. Ensure Google shows the correct version of your site in every country and language.", "Genera etiquetas hreflang válidas para SEO Internacional. Asegúrate de que Google muestre la versión correcta de tu web en cada país y en cada idioma."),
            ("Avoid international duplicate content issues and deliver the correct version of your site to each user based on their language and region.", "Evita problemas de contenido duplicado internacional y entrega a cada usuario la versión de tu web correcta según su idioma y región."),
            ("Add the versions of your page", "Añade las versiones de tu página"),
            ("Add Language / Region", "Añadir Idioma / Región"),
            ("Important", "Importante"),
            ("Hreflang tags must be bidirectional. The generated code must go in the <code>&lt;head&gt;</code> section of <strong>ALL</strong> pages listed above equally, or be embedded in your XML Sitemap.", "Las etiquetas hreflang deben ser bidireccionales. El código generado debe ir en la sección <code>&lt;head&gt;</code> de <strong>TODAS</strong> las páginas listadas arriba por igual o incrustarse en tu Sitemap XML."),
            ("📄 HTML Tags", "📄 Etiquetas HTML"),
            ("Fill in the fields to generate tags.", "Completa los campos para generar etiquetas."),
            ("Fill in the URL fields to generate the tags.", "Completa los campos de URL para generar las etiquetas."),
            ("Version / Variant", "Versión / Variante"),
            ("Remove this language", "Eliminar este idioma"),
            (">Language<", ">Idioma<"),
            (">Region / Country (Optional)<", ">Región / País (Opcional)<"),
            ("Absolute URL", "URL Absoluta"),
            ("Spanish", "Español"),
            ("English", "Inglés"),
            ("French", "Francés"),
            ("German", "Alemán"),
            ("Italian", "Italiano"),
            ("Portuguese", "Portugués"),
            ("Chinese", "Chino"),
            ("Japanese", "Japonés"),
            ("Russian", "Ruso"),
            ("Arabic", "Árabe"),
            ("Any Region (Generic)", "Cualquier Región (Genérico)"),
            ("Spain", "España"),
            ("Mexico", "México"),
            ("Argentina", "Argentina"),
            ("Colombia", "Colombia"),
            ("Chile", "Chile"),
            ("Peru", "Perú"),
            ("United States", "Estados Unidos"),
            ("United Kingdom", "Reino Unido"),
            ("Canada", "Canadá"),
            ("Australia", "Australia"),
            ("France", "Francia"),
            ("Germany", "Alemania"),
            ("Brazil", "Brasil")
        ],
        "fr": [
            ("Hreflang Tag Generator — PageGuides", "Générateur de Balises Hreflang — PageGuides"),
            ("Generate valid hreflang tags for International SEO. Ensure Google shows the correct version of your site in every country and language.", "Générez des balises hreflang valides pour le SEO international. Assurez-vous que Google affiche la bonne version de votre site dans chaque pays et langue."),
            ("Avoid international duplicate content issues and deliver the correct version of your site to each user based on their language and region.", "Évitez les problèmes de contenu dupliqué international et offrez la bonne version de votre site à chaque utilisateur en fonction de sa langue et de sa région."),
            ("Add the versions of your page", "Ajouter les versions de votre page"),
            ("Add Language / Region", "Ajouter une Langue / Région"),
            ("Important", "Important"),
            ("Hreflang tags must be bidirectional. The generated code must go in the <code>&lt;head&gt;</code> section of <strong>ALL</strong> pages listed above equally, or be embedded in your XML Sitemap.", "Les balises hreflang doivent être bidirectionnelles. Le code généré doit aller dans la section <code>&lt;head&gt;</code> de <strong>TOUTES</strong> les pages listées ci-dessus de manière égale, ou être intégré dans votre plan de site XML."),
            ("📄 HTML Tags", "📄 Balises HTML"),
            ("Fill in the fields to generate tags.", "Remplissez les champs pour générer les balises."),
            ("Fill in the URL fields to generate the tags.", "Remplissez les champs d'URL pour générer les balises."),
            ("Version / Variant", "Version / Variante"),
            ("Remove this language", "Supprimer cette langue"),
            (">Language<", ">Langue<"),
            (">Region / Country (Optional)<", ">Région / Pays (Facultatif)<"),
            ("Absolute URL", "URL Absolue"),
            ("Spanish", "Espagnol"),
            ("English", "Anglais"),
            ("French", "Français"),
            ("German", "Allemand"),
            ("Italian", "Italien"),
            ("Portuguese", "Portugais"),
            ("Chinese", "Chinois"),
            ("Japanese", "Japonais"),
            ("Russian", "Russe"),
            ("Arabic", "Arabe"),
            ("Any Region (Generic)", "Toute Région (Générique)"),
            ("Spain", "Espagne"),
            ("Mexico", "Mexique"),
            ("Argentina", "Argentine"),
            ("Colombia", "Colombie"),
            ("Chile", "Chili"),
            ("Peru", "Pérou"),
            ("United States", "États-Unis"),
            ("United Kingdom", "Royaume-Uni"),
            ("Canada", "Canada"),
            ("Australia", "Australie"),
            ("France", "France"),
            ("Germany", "Allemagne"),
            ("Brazil", "Brésil")
        ],
        "hi": [
            ("Hreflang Tag Generator — PageGuides", "Hreflang टैग जनरेटर — PageGuides"),
            ("Generate valid hreflang tags for International SEO. Ensure Google shows the correct version of your site in every country and language.", "अंतर्राष्ट्रीय SEO के लिए मान्य hreflang टैग जनरेट करें। सुनिश्चित करें कि Google हर देश और भाषा में आपकी साइट का सही संस्करण दिखाता है।"),
            ("Avoid international duplicate content issues and deliver the correct version of your site to each user based on their language and region.", "अंतर्राष्ट्रीय डुप्लिकेट सामग्री के मुद्दों से बचें और प्रत्येक उपयोगकर्ता को उनकी भाषा और क्षेत्र के आधार पर अपनी साइट का सही संस्करण वितरित करें।"),
            ("Add the versions of your page", "अपने पेज के संस्करण जोड़ें"),
            ("Add Language / Region", "भाषा / क्षेत्र जोड़ें"),
            ("Important", "महत्वपूर्ण"),
            ("Hreflang tags must be bidirectional. The generated code must go in the <code>&lt;head&gt;</code> section of <strong>ALL</strong> pages listed above equally, or be embedded in your XML Sitemap.", "Hreflang टैग द्विदिशी होने चाहिए। जनरेट किया गया कोड समान रूप से ऊपर सूचीबद्ध <strong>सभी</strong> पृष्ठों के <code>&lt;head&gt;</code> अनुभाग में जाना चाहिए, या आपके XML साइटमैप में एम्बेड होना चाहिए।"),
            ("📄 HTML Tags", "📄 HTML टैग"),
            ("Fill in the fields to generate tags.", "टैग जेनरेट करने के लिए फ़ील्ड भरें।"),
            ("Fill in the URL fields to generate the tags.", "टैग जेनरेट करने के लिए URL फ़ील्ड भरें।"),
            ("Version / Variant", "संस्करण / प्रकार"),
            ("Remove this language", "इस भाषा को हटाएँ"),
            (">Language<", ">भाषा<"),
            (">Region / Country (Optional)<", ">क्षेत्र / देश (वैकल्पिक)<"),
            ("Absolute URL", "पूर्ण URL"),
            ("Spanish", "स्पैनिश"),
            ("English", "अंग्रेज़ी"),
            ("French", "फ़्रेंच"),
            ("German", "जर्मन"),
            ("Italian", "इतालवी"),
            ("Portuguese", "पुर्तगाली"),
            ("Chinese", "चीनी"),
            ("Japanese", "जापानी"),
            ("Russian", "रूसी"),
            ("Arabic", "अरबी"),
            ("Any Region (Generic)", "कोई भी क्षेत्र (सामान्य)"),
            ("Spain", "स्पेन"),
            ("Mexico", "मेक्सिको"),
            ("Argentina", "अर्जेंटीना"),
            ("Colombia", "कोलम्बिया"),
            ("Chile", "चिली"),
            ("Peru", "पेरू"),
            ("United States", "संयुक्त राज्य अमेरिका"),
            ("United Kingdom", "यूनाइटेड किंगडम"),
            ("Canada", "कनाडा"),
            ("Australia", "ऑस्ट्रेलिया"),
            ("France", "फ़्रांस"),
            ("Germany", "जर्मनी"),
            ("Brazil", "ब्राज़ील")
        ],
        "pt": [
            ("Hreflang Tag Generator — PageGuides", "Gerador de Tags Hreflang — PageGuides"),
            ("Generate valid hreflang tags for International SEO. Ensure Google shows the correct version of your site in every country and language.", "Gere tags hreflang válidas para SEO Internacional. Garanta que o Google mostre a versão correta do seu site em cada país e idioma."),
            ("Avoid international duplicate content issues and deliver the correct version of your site to each user based on their language and region.", "Evite problemas de conteúdo duplicado internacional e forneça a versão correta do seu site a cada usuário com base no idioma e região deles."),
            ("Add the versions of your page", "Adicione as versões da sua página"),
            ("Add Language / Region", "Adicionar Idioma / Região"),
            ("Important", "Importante"),
            ("Hreflang tags must be bidirectional. The generated code must go in the <code>&lt;head&gt;</code> section of <strong>ALL</strong> pages listed above equally, or be embedded in your XML Sitemap.", "As tags Hreflang devem ser bidirecionais. O código gerado deve ir na seção <code>&lt;head&gt;</code> de <strong>TODAS</strong> as páginas listadas acima igualmente, ou ser incorporado no seu Sitemap XML."),
            ("📄 HTML Tags", "📄 Tags HTML"),
            ("Fill in the fields to generate tags.", "Preencha os campos para gerar tags."),
            ("Fill in the URL fields to generate the tags.", "Preencha os campos de URL para gerar as tags."),
            ("Version / Variant", "Versão / Variante"),
            ("Remove this language", "Remover este idioma"),
            (">Language<", ">Idioma<"),
            (">Region / Country (Optional)<", ">Região / País (Opcional)<"),
            ("Absolute URL", "URL Absoluta"),
            ("Spanish", "Espanhol"),
            ("English", "Inglês"),
            ("French", "Francês"),
            ("German", "Alemão"),
            ("Italian", "Italiano"),
            ("Portuguese", "Português"),
            ("Chinese", "Chinês"),
            ("Japanese", "Japonês"),
            ("Russian", "Russo"),
            ("Arabic", "Árabe"),
            ("Any Region (Generic)", "Qualquer Região (Genérico)"),
            ("Spain", "Espanha"),
            ("Mexico", "México"),
            ("Argentina", "Argentina"),
            ("Colombia", "Colômbia"),
            ("Chile", "Chile"),
            ("Peru", "Peru"),
            ("United States", "Estados Unidos"),
            ("United Kingdom", "Reino Unido"),
            ("Canada", "Canadá"),
            ("Australia", "Austrália"),
            ("France", "França"),
            ("Germany", "Alemanha"),
            ("Brazil", "Brasil")
        ]
    },
    "htaccess-redirect-generator.html": {
        "es": [
            (".htaccess Redirect Generator — PageGuides", "Generador de Redirecciones .htaccess — PageGuides"),
            ("Generate 301 redirect rules, force HTTPS or remove WWW from your URL for your .htaccess file without breaking your site.", "Genera reglas de redirección 301, fuerza HTTPS o elimina las codiciadas WWW para tu archivo .htaccess sin romper tu web."),
            ("Generate secure 301 redirect rules. Force HTTPS, remove WWW or redirect individual pages with total efficiency.", "Genera reglas de redirección 301 seguras. Forza HTTPS, elimina WWW o redirige páginas individuales con total eficiencia."),
            ("Select the type of redirect", "Selecciona el tipo de redirección"),
            ("Individual 301 Redirect", "Redirección 301 Individual"),
            ("Force HTTPS (SSL)", "Forzar HTTPS (SSL)"),
            ("Redirect WWW to non-WWW", "Redirigir WWW a sin-WWW"),
            ("Redirect non-WWW to WWW", "Redirigir sin-WWW a WWW"),
            ("Attention", "Atención"),
            ("Make a backup of your current <code>.htaccess</code> file before applying these changes. A small syntax error can cause a \"500 Error\" on your entire website.", 'Haz una copia de seguridad de tu archivo <code>.htaccess</code> actual antes de aplicar estos cambios. Un pequeño error de sintaxis puede causar un "Error 500" en tu sitio web entero.'),
            ("📄 .htaccess Code", "📄 Código .htaccess"),
            ("Select an option to generate the code.", "Selecciona una opción para generar el código."),
            ("Original URL (Relative path)", "URL Original (Ruta relativa)"),
            ("Destination URL (Absolute or Relative)", "URL de Destino (Absoluta o Relativa)"),
            ("Your Domain (Without protocol or www)", "Tu Dominio (Sin protocolo ni www)"),
            ("301 Redirect from old page to new", "Redirección 301 de página antigua a nueva"),
            ("Force HTTPS", "Forzar HTTPS")
        ],
        "fr": [
            (".htaccess Redirect Generator — PageGuides", "Générateur de Redirections .htaccess — PageGuides"),
            ("Generate 301 redirect rules, force HTTPS or remove WWW from your URL for your .htaccess file without breaking your site.", "Générez des règles de redirection 301, forcez HTTPS ou supprimez les WWW pour votre fichier .htaccess sans casser votre site."),
            ("Generate secure 301 redirect rules. Force HTTPS, remove WWW or redirect individual pages with total efficiency.", "Générez des règles de redirection 301 sécurisées. Forcez HTTPS, supprimez les WWW ou redirigez des pages individuelles avec une efficacité totale."),
            ("Select the type of redirect", "Sélectionnez le type de redirection"),
            ("Individual 301 Redirect", "Redirection 301 Individuelle"),
            ("Force HTTPS (SSL)", "Forcer HTTPS (SSL)"),
            ("Redirect WWW to non-WWW", "Rediriger WWW vers sans WWW"),
            ("Redirect non-WWW to WWW", "Rediriger sans WWW vers WWW"),
            ("Attention", "Attention"),
            ("Make a backup of your current <code>.htaccess</code> file before applying these changes. A small syntax error can cause a \"500 Error\" on your entire website.", "Faites une sauvegarde de votre fichier <code>.htaccess</code> actuel avant d'appliquer ces modifications. Une petite erreur de syntaxe peut provoquer une \"Erreur 500\" sur l'ensemble de votre site web."),
            ("📄 .htaccess Code", "📄 Code .htaccess"),
            ("Select an option to generate the code.", "Sélectionnez une option pour générer le code."),
            ("Original URL (Relative path)", "URL Originale (Chemin relatif)"),
            ("Destination URL (Absolute or Relative)", "URL de Destination (Absolue ou Relative)"),
            ("Your Domain (Without protocol or www)", "Votre Domaine (Sans protocole ni www)"),
            ("301 Redirect from old page to new", "Redirection 301 de l'ancienne page vers la nouvelle"),
            ("Force HTTPS", "Forcer HTTPS")
        ],
        "hi": [
            (".htaccess Redirect Generator — PageGuides", ".htaccess रीडायरेक्ट जनरेटर — PageGuides"),
            ("Generate 301 redirect rules, force HTTPS or remove WWW from your URL for your .htaccess file without breaking your site.", "अपनी साइट को तोड़े बिना अपनी .htaccess फ़ाइल के लिए 301 रीडायरेक्ट नियम तैयार करें, HTTPS को बाध्य करें या WWW को हटा दें।"),
            ("Generate secure 301 redirect rules. Force HTTPS, remove WWW or redirect individual pages with total efficiency.", "सुरक्षित 301 रीडायरेक्ट नियम तैयार करें। HTTPS को बाध्य करें, WWW हटाएं या पूर्ण दक्षता के साथ व्यक्तिगत पृष्ठों को रीडायरेक्ट करें।"),
            ("Select the type of redirect", "रीडायरेक्ट का प्रकार चुनें"),
            ("Individual 301 Redirect", "व्यक्तिगत 301 रीडायरेक्ट"),
            ("Force HTTPS (SSL)", "HTTPS (SSL) बाध्य करें"),
            ("Redirect WWW to non-WWW", "WWW को गैर-WWW में रीडायरेक्ट करें"),
            ("Redirect non-WWW to WWW", "गैर-WWW को WWW में रीडायरेक्ट करें"),
            ("Attention", "ध्यान दें"),
            ("Make a backup of your current <code>.htaccess</code> file before applying these changes. A small syntax error can cause a \"500 Error\" on your entire website.", "इन परिवर्तनों को लागू करने से पहले अपनी वर्तमान <code>.htaccess</code> फ़ाइल का बैकअप लें। एक छोटी सिंटैक्स त्रुटि आपकी पूरी वेबसाइट पर \"500 त्रुटि\" का कारण बन सकती है।"),
            ("📄 .htaccess Code", "📄 .htaccess कोड"),
            ("Select an option to generate the code.", "कोड जनरेट करने के लिए विकल्प चुनें।"),
            ("Original URL (Relative path)", "मूल URL (सापेक्ष पथ)"),
            ("Destination URL (Absolute or Relative)", "गंतव्य URL (पूर्ण या सापेक्ष)"),
            ("Your Domain (Without protocol or www)", "आपका डोमेन (प्रोटोकॉल या www के बिना)"),
            ("301 Redirect from old page to new", "पुराने पेज से नए पेज पर 301 रीडायरेक्ट"),
            ("Force HTTPS", "HTTPS बाध्य करें")
        ],
        "pt": [
            (".htaccess Redirect Generator — PageGuides", "Gerador de Redirecionamentos .htaccess — PageGuides"),
            ("Generate 301 redirect rules, force HTTPS or remove WWW from your URL for your .htaccess file without breaking your site.", "Gere regras de redirecionamento 301, force HTTPS ou remova o WWW da URL para o seu arquivo .htaccess sem quebrar o seu site."),
            ("Generate secure 301 redirect rules. Force HTTPS, remove WWW or redirect individual pages with total efficiency.", "Gere regras de redirecionamento 301 seguras. Força HTTPS, remove o WWW ou redireciona páginas individuais com total eficiência."),
            ("Select the type of redirect", "Selecione o tipo de redirecionamento"),
            ("Individual 301 Redirect", "Redirecionamento 301 Individual"),
            ("Force HTTPS (SSL)", "Forçar HTTPS (SSL)"),
            ("Redirect WWW to non-WWW", "Redirecionar WWW para sem WWW"),
            ("Redirect non-WWW to WWW", "Redirecionar sem WWW para WWW"),
            ("Attention", "Atenção"),
            ("Make a backup of your current <code>.htaccess</code> file before applying these changes. A small syntax error can cause a \"500 Error\" on your entire website.", "Faça um backup do seu arquivo <code>.htaccess</code> atual antes de aplicar estas mudanças. Um pequeno erro de sintaxe pode causar um \"Erro 500\" em todo o seu site."),
            ("📄 .htaccess Code", "📄 Código .htaccess"),
            ("Select an option to generate the code.", "Selecione uma opção para gerar o código."),
            ("Original URL (Relative path)", "URL Original (Caminho relativo)"),
            ("Destination URL (Absolute or Relative)", "URL de Destino (Absoluta ou Relativa)"),
            ("Your Domain (Without protocol or www)", "Seu Domínio (Sem protocolo ou www)"),
            ("301 Redirect from old page to new", "Redirecionamento 301 da página antiga para a nova"),
            ("Force HTTPS", "Forçar HTTPS")
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

print("Successfully generated translations for batch 5")

import os
import glob
import re

base_dir = '/Users/franciscoinfante/Downloads/oneusepage/pageguides.com'

# List all HTML files in base_dir and its immediate subdirectories
all_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.html'):
            all_files.append(os.path.join(root, f))

# The languages we support
lang_codes = ['es', 'fr', 'pt', 'hi']

for filepath in all_files:
    # get relative path from base_dir
    rel_path = os.path.relpath(filepath, base_dir)
    filename = os.path.basename(rel_path)
    
    # Check if this file is in the root or a subdirectory
    parts = os.path.split(rel_path)
    
    is_root = (len(parts) == 1 or parts[0] == '')
    
    current_lang = 'en'
    if not is_root:
        # The parent folder should be one of our language codes
        current_lang = parts[0]
        if current_lang not in lang_codes:
            # Maybe some other subfolder, skip or assume root behavior
            is_root = True
            current_lang = 'en'

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the dropdown block using regex
    pattern = r'(?s)(<div class="lang-dropdown">.*?</div>)'
    match = re.search(pattern, html)
    if not match:
        continue
    
    old_dropdown = match.group(1)
    
    # generate new dropdown
    # For a file in ROOT:
    # English: href="filename"
    # es: href="es/filename"
    
    # For a file in es:
    # English: href="../filename"
    # es: href="filename"
    # fr: href="../fr/filename"
    
    def get_link(target_lang, fname):
        if target_lang == 'en':
            return f'../{fname}' if not is_root else f'{fname}'
        else:
            if is_root:
                return f'{target_lang}/{fname}'
            else:
                if current_lang == target_lang:
                    return f'{fname}'
                else:
                    return f'../{target_lang}/{fname}'

    # We also need to keep the "active" class correct
    en_class = 'lang-option active' if current_lang == 'en' else 'lang-option'
    es_class = 'lang-option active' if current_lang == 'es' else 'lang-option'
    fr_class = 'lang-option active' if current_lang == 'fr' else 'lang-option'
    pt_class = 'lang-option active' if current_lang == 'pt' else 'lang-option'
    hi_class = 'lang-option active' if current_lang == 'hi' else 'lang-option'

    # Ensure index.html doesn't look weird if we use relative paths
    # We will just plug the filename.
    fn = filename
    if fn == 'index.html': fn = 'index.html'

    new_dropdown = f'''<div class="lang-dropdown">
                    <a href="{get_link('en', fn)}" class="{en_class}"><span class="lang-flag">🇺🇸</span> English</a>
                    <a href="{get_link('es', fn)}" class="{es_class}"><span class="lang-flag">🇪🇸</span> Español</a>
                    <a href="{get_link('fr', fn)}" class="{fr_class}"><span class="lang-flag">🇫🇷</span> Français</a>
                    <a href="{get_link('pt', fn)}" class="{pt_class}"><span class="lang-flag">🇧🇷</span> Português</a>
                    <a href="{get_link('hi', fn)}" class="{hi_class}"><span class="lang-flag">🇮🇳</span> हिन्दी</a>
                </div>'''

    new_html = html.replace(old_dropdown, new_dropdown)
    
    # Additionally, let's fix the logo link so you can always go back to the correct language home
    # The logo uses `<a href="/" class="logo">` or `<a href="/es/" class="logo">`
    
    logo_pattern = r'(?s)(<a class="logo"[^>]*>|<a href="[^"]*" class="logo"[^>]*>)'
    
    # the existing uses `<a href="/" class="logo">` etc.
    # We can replace href="..." class="logo" with the right relative path to index
    if is_root:
        logo_href = 'index.html'
    else:
        logo_href = 'index.html'
        
    def replace_logo_href(m):
        full_tag = m.group(1)
        # replace the href inside the full tag
        return re.sub(r'href="[^"]*"', f'href="{logo_href}"', full_tag)

    new_html = re.sub(logo_pattern, replace_logo_href, new_html)

    # Some of the python scripts might have replaced it with just href="/es/" class="logo"
    # Wait, the logo link from a subfolder tool should go back to the subfolder index.
    # Therefore, its href should be `index.html` because tool and index are in the same folder.
    # For a root tool, it should be `index.html`.
    # Let's ensure this is accurate.

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)

print("Finished fixing relative links.")
